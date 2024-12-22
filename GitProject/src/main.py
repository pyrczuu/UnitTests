from addStudent import ModifyStudents
from exportStudents import ExportStudents
from importStudents import ImportStudents
from attendance import Attendance

running = True
while running:
    print(21*" ", "MENU")
    print(50*"-")
    print("[1] - add student")
    print("[2] - modify student")
    print("[3] - delete student")
    print("[4] - check attendance")
    print("[5] - display student list")
    print("[6] - quit")
    chosen = input()
    match chosen:
        case "1":
            students = []
            print("Inserted data will be exported, please type in file names for: ")       #TODO:  needs to be more user friendly and handle exceptions
            path1 = "lists/" + input("CSV: ")
            path2 = "lists/" + input("TXT: ")
            ModifyStudents.add_student_and_export(path1, path2, students)
        case "2":
            students = []
            print("Inserted data will be exported, please type in file names for: ")
            path1 = "lists/" + input("CSV: ")
            path2 = "lists/" + input("TXT: ")
            ModifyStudents.modify_student(path1, path2, students)
        case "3":
            students = []
            print("Inserted data will be exported, please type in file names for: ")
            path1 = "lists/" + input("CSV: ")
            path2 = "lists/" + input("TXT: ")
            ModifyStudents.delete_student(path1, path2, students)
        case "4":
            students = []
            path = input("Where is your list stored? ")
            if path.endswith(".csv"):
                students = ImportStudents.csv(path, students)
            elif path.endswith(".txt"):
                students = ImportStudents.txt(path, students)
            else:
                print("Wrong input")
            students = Attendance.check_attendance(students)
            if path.endswith(".csv"):
                ExportStudents.csv(path, students)
            elif path.endswith(".txt"):
                ExportStudents.txt(path, students)
        case "5":
            students = []
            path = input("Where is your list stored? ")
            if path.endswith(".csv"):
                students = ImportStudents.csv(path,students)
            elif path.endswith(".txt"):
                students = ImportStudents.txt(path, students)
            else:
                print("Wrong input")
            for student in students:
                print(f"{student.name} {student.surname} {student.id} {student.attendence}")
        case "6":
            running = False
