class ExportStudentsAttendance:
    student_details_structure = ["Name", "Surname", "ID", "Attendance"]

    @staticmethod
    def csv(path, list):
        student_details_structure = ExportStudentsAttendance.student_details_structure

        file = open(path, "a")

        lines = []

        for student_details in list:
            line = []

            if (
                    not all(student_detail_key in student_details_structure for student_detail_key in student_details) or
                    len(student_details) != len(student_details_structure)
            ):
                raise Exception(f"list should contain dict with only keys: {",".join(student_details_structure)}")

            for student_detail_key in student_details:
                line.append(student_details[student_detail_key])

            line = ";".join(line)

            lines.append(line)

        file.writelines(lines)

    @staticmethod
    def txt(path, list):
        student_details_structure = ExportStudentsAttendance.student_details_structure

        file = open(path, "a")

        lines = []

        for student_details in list:
            line = []

            if (
                    not all(student_detail_key in student_details_structure for student_detail_key in student_details) or
                    len(student_details) != len(student_details_structure)
            ):
                raise Exception(f"list should contain dict with only keys: {",".join(student_details_structure)}")


            for student_detail_key in student_details:
                line.append(student_details[student_detail_key])

                if student_detail_key == "Surname":
                    line.append(" - ")
                else:
                    line.append(" ")

            line.pop()

            line = "".join(line)

            lines.append(line)

        file.writelines(lines)