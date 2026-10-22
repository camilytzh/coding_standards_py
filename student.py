"""Student Grade Management System - Section A (Python)."""


class Student:
    """Stores the grades of a student and calculates the results."""

    def __init__(self, student_id, name):
        """Create a student. The ID and the name can't be empty."""
        if student_id == "" or name == "":
            raise ValueError("the student ID and name can't be empty")
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.average = 0
        self.letter = "F"
        self.is_passed = False
        self.honor = False

    def add_grade(self, grade):
        """Add a grade if it is a number between 0 and 100."""
        if not isinstance(grade, (int, float)):
            print("Error: the grade", grade, "is not a number")
        elif grade < 0 or grade > 100:
            print("Error: the grade", grade, "must be between 0 and 100")
        else:
            self.grades.append(grade)

    def calc_average(self):
        """Calculate the average of the grades."""
        if len(self.grades) == 0:
            self.average = 0
        else:
            total = 0
            for grade in self.grades:
                total += grade
            self.average = total / len(self.grades)
        return self.average

    def calc_letter(self):
        """Convert the average into a letter grade."""
        average = self.calc_average()
        if average >= 90:
            self.letter = "A"
        elif average >= 80:
            self.letter = "B"
        elif average >= 70:
            self.letter = "C"
        elif average >= 60:
            self.letter = "D"
        else:
            self.letter = "F"
        return self.letter

    def check_passed(self):
        """Mark the student as passed if the average is 60 or more."""
        self.is_passed = self.calc_average() >= 60
        return self.is_passed

    def check_honor(self):
        """Mark the student for the honor roll if the average is 90+."""
        self.honor = self.calc_average() >= 90
        return self.honor

    def delete_grade(self, index):
        """Delete the grade at the given index."""
        if index < 0 or index >= len(self.grades):
            print("Error: there is no grade at index", index)
        else:
            del self.grades[index]

    def delete_grade_by_value(self, value):
        """Delete the first grade that has the given value."""
        if value in self.grades:
            self.grades.remove(value)
        else:
            print("Error: the grade", value, "was not found")

    def report(self):
        """Print the summary report of the student."""
        self.calc_letter()
        self.check_passed()
        self.check_honor()
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Grades count:", len(self.grades))
        print("Average:", round(self.average, 2))
        print("Letter grade:", self.letter)
        print("Status:", "Passed" if self.is_passed else "Failed")
        print("Honor roll:", "Yes" if self.honor else "No")


def start_run():
    """Test the program with valid and invalid data."""
    try:
        Student("x", "")
    except ValueError as error:
        print("Error:", error)

    student = Student("S001", "Maria Lopez")
    student.add_grade(100)
    student.add_grade("Fifty")
    student.add_grade(85)
    student.add_grade(120)
    student.add_grade(72.5)
    student.delete_grade(5)
    student.delete_grade_by_value(50)
    student.delete_grade_by_value(72.5)
    student.report()


if __name__ == "__main__":
    start_run()
