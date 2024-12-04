import re
class Student:
    name_pattern = r"^[A-Z][a-z]+$"
    surname_pattern = r"^[A-Z][a-z]+$"                     #may need changes for max length
 #   id_pattern = r"[A-Z0-9]{9}"
    attendence_pattern = r"^(present|absent|-)$"           #can only be 'present' or 'absent'
    def __init__(self, name, surname, id: str, attendence):
        if re.fullmatch(Student.name_pattern, name):
            self.name = name
        else: raise ValueError("Incorrect name")                #english alphabet only
        if re.fullmatch(Student.surname_pattern, surname):
            self.surname = surname
        else: raise ValueError("Incorrect surname")             #english alphabet only
      #  if re.fullmatch(Student.id_pattern, id):
        self.id = id
     #   else: raise ValueError("Incorrect ID")                     #id needs to be in "" or ''
        if re.fullmatch(Student.attendence_pattern, attendence):
            self.attendence = attendence
        else: raise ValueError("Incorrect attendence")
    # @staticmethod
    # def add_data(student: "Student", *args: "Student"):   #can add one or more student
    #     student_list = []
    #     student_list.append(student)
    #     for arg in args:
    #         student_list.append(arg)
    # @staticmethod
    # def display_data(student_list):
    #     for student in student_list:
    #         print(student.name, student.surname, student.id, student.attendence)