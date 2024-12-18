from GitProject.exportStudents import ExportStudents
from GitProject.student_class import Student

class ModifyStudents:
    # method to add student to list and export it to csv and txt files, files are deleted after operation and new list overwrite file
    @staticmethod
    def add_student_and_export(path, path2, students):
        name = input("Enter student's name: ")
        surname = input("Enter student's surname: ")
        student_id = input("Enter student's ID: ")
        attendance = input("Enter student's attendance: ")
        students.append(Student(name, surname, student_id, attendance))
        ExportStudents.csv(path, students)
        ExportStudents.txt(path2, students)

    @staticmethod
    def modify_student(path, path2, students):
        student_id = input("Enter student's ID to modify: ")
        for student in students:
            if student.id == student_id:
                name = input("Enter new student's name: ")
                surname = input("Enter new student's surname: ")
                student.name = name
                student.surname = surname
                ExportStudents.csv(path, students)
                ExportStudents.txt(path2, students)
                return
        print("Student not found.")

    @staticmethod
    def delete_student(path, path2, students):
          student_id = input("Enter student's ID to delete: ")
          for student in students:
              if student.id == student_id:
                  students.remove(student)
                  ExportStudents.csv(path, students)
                  ExportStudents.txt(path2, students)
                  return
          print("Student not found.")







