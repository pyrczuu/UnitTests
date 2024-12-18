import unittest
from GitProject import importStudents
from GitProject.exportStudents import ExportStudents
from GitProject.importStudents import ImportStudents
from GitProject.student_class import Student

def Mock_modify_student(path,path1,students,id,inputname,inputsurname):
    for student in students:
        if student.id == id:
            student.name = inputname
            student.surname = inputsurname
            ExportStudents.csv(path, students)
            ExportStudents.txt(path1, students)
            return
    print("Student not found.")
def Mock_add_student_and_export(path, path2, students, inputname, inputsurname, inputid, inputattendance):
    students.append(Student(inputname, inputsurname, inputid, inputattendance))
    ExportStudents.csv(path, students)
    ExportStudents.txt(path2, students)

class Test:
    def test_importStudentsCSV(self):
        #given
        path = "GitProject/lists/student_list.csv"
        #when
        got = ImportStudents.csv(path,[])
        #then
        assert isinstance(got, list)
        assert isinstance((got[0]),Student)
    def test_importStudentsTXT(self):
        #given
        path = "GitProject/lists/student_list.txt"
        #when
        got = ImportStudents.txt(path, [])
        #then
        assert isinstance(got, list)
        assert isinstance((got[0]),Student)
    def test_exportStudentsCSV(self):
        #given
        save_path = "test_exportedCSV.csv"
        content_path = "GitProject/lists/student_list.csv"
        student_list = ImportStudents.csv(content_path,[])
        w = open(content_path,"r")
        want = w.read()
        #when
        ExportStudents.csv(save_path, student_list)
        g = open(save_path, "r")
        got = g.read()
        #then
        assert got == want

    def test_exportStudentsTXT(self):
        # given
        save_path = "test_exportedTXT.txt"
        content_path = "GitProject/lists/student_list.txt"
        student_list = importStudents.ImportStudents.txt(content_path,[])
        w = open(content_path,"r")
        want = w.read()
        # when
        ExportStudents.txt(save_path, student_list)
        g = open(save_path, "r")
        got = g.read()
        # then
        assert got == want
    def test_modify_student(self):
        #given
        path = "test_add_student_and_export.csv"
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
    def test_add_student_and_export(self):
        #given
        path = "test_add_student_and_export.csv"
        path1 = "test_add_student_and_export.txt"
        students = []
        name = "Damian"
        surname = "Pyrcz"
        id = "TEST54321"
        attendence = "present"

        #when
        Mock_add_student_and_export(path, path1, students, name, surname, id, attendence)
        got = ImportStudents.csv(path, students)
        #then
        assert isinstance(got, list)
        assert isinstance((got[0]),Student)
        assert got[0].name == name
        assert got[0].surname == surname
        assert got[0].id == id
        assert got[0].attendence == attendence

if __name__ == '__main__':
    unittest.main()
