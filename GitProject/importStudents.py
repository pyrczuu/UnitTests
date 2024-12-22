
from GitProject.student_class import Student


class ImportStudents:
    @staticmethod
    def csv(path: str, students: list) -> list:
        file = open(path, "r")
        for line in file:
            person = line.strip().split(";")
            students.append(Student(person[0], person[1], person[2], "-"))
        file.close()
        return students

    @staticmethod
    def txt(path: str, students: list) -> list:
        file = open(path, "r")
        for line in file:
            person = line.strip().split(";")
            students.append(Student(person[0], person[1], person[2], "-"))
        file.close()
        return students

