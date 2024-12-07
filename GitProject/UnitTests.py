from importStudents import ImportStudents
from GitProject.student_class import Student
from importStudents import ImportStudents
from addStudent import ModifyStudents
from exportStudents import ExportStudents

Damian = Student("Damian","Pyrcz","123456789","-")
Marcel = Student("Marcel","Ras","987654321","-")
Leon = Student("Leon","Sadlo","AHR73J89G","present")
Mikolaj = Student("Mikolaj","Sulkowski","UW36BK90J","absent")
Lukasz = Student("Lukasz","Radecki","HS3N96N0O","-")

student_list = [Damian, Marcel, Leon, Mikolaj, Lukasz]

path = "test_files/delete_student.csv"
path1 = "delete_student.txt"

ModifyStudents.delete_student(path,path1,student_list)


