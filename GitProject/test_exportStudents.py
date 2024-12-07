import unittest
from datetime import datetime

import pytest
import addStudent
import exportStudents
import importStudents
from GitProject.addStudent import ModifyStudents
from GitProject.exportStudents import ExportStudents
from GitProject.main import path2
from GitProject.student_class import Student
from attendance import Attendance

def Mock_modify_student(path,path1,students,id,inputname,inputsurname):
    for student in students:
        if student.id == id:
            student.name = inputname
            student.surname = inputsurname
            ExportStudents.csv(path, students)
            ExportStudents.txt(path2, students)
            return
    print("Student not found.")
def Mock_delete_student(path, path2, students, id):
    student_id = id
    for student in students:
        if student.id == student_id:
            students.remove(student)
            ExportStudents.csv(path, students)
            ExportStudents.txt(path2, students)
            return
class Test:
    def test_importStudentsCSV(self):
        #given
        path = "lists/student_list.csv"
        #when
        got = importStudents.ImportStudents.csv(path,[])
        #then
        assert type(got) == list
        assert type(got[0]) == Student
    def test_importStudentsTXT(self):
        #given
        path = "lists/student_list.txt"
        #when
        got = importStudents.ImportStudents.txt(path, [])
        #then
        assert type(got) == list
        assert type(got[0]) == Student
    def test_exportStudentsCSV(self):
        #given
        save_path = "test_files/test_exportedCSV.csv"
        content_path = "lists/student_list.csv"
        student_list = importStudents.ImportStudents.csv(content_path,[])
        w = open(content_path,"r")
        want = w.read()
        #when
        exportStudents.ExportStudents.csv(save_path, student_list)
        g = open(save_path, "r")
        got = g.read()
        #then
        assert got == want

    def test_exportStudentsTXT(self):
        # given
        save_path = "test_files/test_exportedTXT.txt"
        content_path = "lists/student_list.txt"
        student_list = importStudents.ImportStudents.txt(content_path,[])
        w = open(content_path,"r")
        want = w.read()
        # when
        exportStudents.ExportStudents.txt(save_path, student_list)
        g = open(save_path, "r")
        got = g.read()
        # then
        assert got == want
    def test_modify_student(self):
        #given
        path = "test_files/test_add_student_and_export.csv"
        path1 = "test_add_student_and_export.txt"
        Andrzej = Student("Andrzej", "Hasiok", "HAGIE93LC", "-")
        Grzegorz = Student("Grzegorz", "Bonk", "761HSO405", "-")
        Krzysztof = Student("Krzysztof", "Loczek", "76131H405", "-")
        list_of_Students = [Andrzej, Grzegorz, Krzysztof]
        want = "Skoczek"
        #when
        Mock_modify_student(path, path1, list_of_Students, "76131H405", "Krzysztof", "Skoczek")
        got = Krzysztof.surname
        #then
        assert got == want
    def test_delete_student(self):
        #given
        path = "test_files/test_delete_student.csv"
        path1 = "test_files/test_delete_student.txt"
        wanted_state = "test_files/delete_student.csv"
        w = open(wanted_state,"r")
        want = w.read()
        Damian = Student("Damian", "Pyrcz", "123456789", "-")
        Marcel = Student("Marcel", "Ras", "987654321", "-")
        Leon = Student("Leon", "Sadlo", "AHR73J89G", "present")
        Mikolaj = Student("Mikolaj", "Sulkowski", "UW36BK90J", "absent")
        Lukasz = Student("Lukasz", "Radecki", "HS3N96N0O", "-")
        student_list = [Damian, Marcel, Leon, Mikolaj, Lukasz]
        #when
        Mock_delete_student(path, path1, student_list, "123456789")
        g = open(path, "r")
        got = g.read()
        #then
        assert got == want


if __name__ == '__main__':
    unittest.main()