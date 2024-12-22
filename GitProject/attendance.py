from operator import attrgetter

from GitProject.student_class import Student
from GitProject.importStudents import ImportStudents

class Attendance:
    @staticmethod
    def check_attendance(students : list[Student]) -> list[Student]:
        for student in students:
            student.attendence = input(f"Attendance for {student.name} {student.surname} {student.id}: ")
        return students