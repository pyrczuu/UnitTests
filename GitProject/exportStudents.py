

class ExportStudents:
    @staticmethod
    def csv(path_to_save: str, student_list: list):
        file = open(path_to_save, "w")
        for student in student_list:
            file.write(f"{student.name};{student.surname};{student.id}\n")
        file.close()

    @staticmethod
    def txt(path_to_save: str, student_list: list):
        file = open(path_to_save, "w")
        for student in student_list:
            file.write(f"{student.name} {student.surname} - {student.id}\n")
        file.close()
