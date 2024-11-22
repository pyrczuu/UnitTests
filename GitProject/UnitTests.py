import pytest
import os
from GitProject.importStudents import ImportStudents
from exportStudents import ExportStudents
# Mocks to keep functionality but get rid of all useless prints and inputs
class MockModifyStudents:
    @staticmethod
    def add_student(students, student_name, student_surname, student_id):
        students.append({"Name" : student_name, "Surname" : student_surname, "ID" : student_id})
    @staticmethod
    def modify_student(students, student_id, new_name, new_surname):
        for student in students:
            if student["ID"] == student_id:
                student["Name"] = new_name
                student["Surname"] = new_surname
class MockAttendance:
    @staticmethod
    def check_attendance_for_all(date, students):
        presence = {}
        if date not in presence:
            presence[date] = {}
        for student in students:
            student_name = f"{student['Name']} {student['Surname']}"
            presence[date][student_name] = "1"
        return presence
    @staticmethod
    def clear_attendance(presence, date):
        if date in presence:
            del presence[date]
        return presence
# actual tests
class Test:
    @staticmethod
    def test_export_csv():
        #given
        path = "test_student_export.csv"
        students = [
            {"Name" : "George", "Surname" : "Droid", "ID" : "53SAF4"},
            {"Name" : "Niguel", "Surname" : "Link", "ID" : "G456AA"}
        ]
        with open(path, "w") as f:
            pass
        want = """George;Droid;53SAF4\nNiguel;Link;G456AA"""
        #when
        ExportStudents.csv(path, students)
        with open(path, "r") as f:
            got = f.read().strip()
        #then
        assert got == want
        os.remove(path)
    @staticmethod
    def test_import_csv():
        #given
        path = "test_student_import.csv"
        student_detail_structure = ["Name", "Surname", "ID"]
        file_content = """Theodore;Duck;7347\nQuandale;Dingle;0932"""
        with open(path, "w") as file:
            file.write(file_content)
        want = [{"Name" : "Theodore", "Surname" : "Duck", "ID" : "7347"}, {"Name" : "Quandale", "Surname" : "Dingle", "ID" : "0932"}]
        #when
        got = ImportStudents.csv(path, student_detail_structure)
        #then
        assert got == want
    @staticmethod
    def test_add_student():
        #given
        students = []
        want = [{"Name" : "Krzysztof", "Surname" : "Kasztan", "ID" : "99999"}]
        #when
        MockModifyStudents.add_student(students, "Krzysztof", "Kasztan", "99999")
        #then
        assert want == students
    @staticmethod
    def test_modify_student():
        #given
        students = [{"Name" : "Grzegorz", "Surname" : "Bęździełko", "ID" : "11111"},
                    {"Name" : "Paul", "Surname" : "Free", "ID" : "22222"}]
        want = [{"Name" : "Paul", "Surname" : "Slow", "ID" : "11111"},
                    {"Name" : "Paul", "Surname" : "Free", "ID" : "22222"}]
        #when
        MockModifyStudents.modify_student(students, "11111", "Paul", "Slow")
        #then
        assert want == students
    @staticmethod
    def test_check_attendance_for_all():
        #given
        date = "2024-11-22"
        students = [
            {"Name" : "Kamil", "Surname" : "Labuda"},
            {"Name" : "Poncjusz", "Surname" : "Piłat"}
        ]
        want = {"2024-11-22":{"Kamil Labuda":"1", "Poncjusz Piłat":"1"}}
        #when
        got = MockAttendance.check_attendance_for_all(date, students)
        #then
        assert want == got
    @staticmethod
    def test_clear_attendance():
        #given
        want = {}
        presence = {"2024-11-22":{"Kamil Labuda":"1", "Poncjusz Piłat":"1"}}
        date = "2024-11-22"
        #when
        got = MockAttendance.clear_attendance(presence, date)
        #then
        assert got == want
