import re
class Student:
    name_pattern = r"^[A-Z][a-z]+$"
    surname_pattern = r"^[A-Z][a-z]+$"                     #may need changes for max length
    id_pattern = r"[A-Z0-9]{9}"
    def __init__(self, name, surname, id: str, attendence):
        if re.fullmatch(Student.name_pattern, name):
            self.name = name
        else:
            raise ValueError("Incorrect name")                #english alphabet only
        if re.fullmatch(Student.surname_pattern, surname):
            self.surname = surname
        else:
            raise ValueError("Incorrect surname")             #english alphabet only
     #   if re.fullmatch(Student.id_pattern, id):
        self.id = id
     #   else: raise ValueError("Incorrect ID")                     #id needs to be in "" or ''
        self.attendence = attendence
