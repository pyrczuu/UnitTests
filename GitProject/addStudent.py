from exportStudentsAttendance import ExportStudentsAttendance


class ModifyStudents:
    @staticmethod
    def add_student(students):
        name = input("Enter student's name: ")
        surname = input("Enter student's surname: ")
        student_id = input("Enter student's ID: ")
        students.append({"Name": name, "Surname": surname, "ID": student_id, "Attendance": None})
        ExportStudentsAttendance.txt("lists/student_list.txt", students)
        ExportStudentsAttendance.csv("lists/student_list.csv", students)

