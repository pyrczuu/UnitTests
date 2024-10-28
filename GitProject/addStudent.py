from exportStudents import ExportStudents


class ModifyStudents:
    @staticmethod
    def add_student_and_export(path, path2, students):
        name = input("Enter student's name: ")
        surname = input("Enter student's surname: ")
        student_id = input("Enter student's ID: ")
        students.append({"Name": name, "Surname": surname, "ID": student_id})
        ExportStudents.csv(path, students)
        ExportStudents.txt(path2, students)