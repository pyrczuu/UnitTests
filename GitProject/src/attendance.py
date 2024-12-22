from GitProject.src.student_class import Student


class Attendance:
    @staticmethod
    def check_attendance(students : list[Student]) -> list[Student]:
        for student in students:
            student.attendence = input(f"Attendance for {student.name} {student.surname} {student.id}: ")
        return students