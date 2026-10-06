from dataclasses import dataclass

@dataclass
class Student:
    name: str
    student_id: str
    course: str
    marks: float

    def result(self):
        return "Pass" if self.marks >= 40 else "Fail"

student = Student("Samrat Arjani", "25BCON1602", "B.Tech CSE", 78)

print("Student Details")
print("----------------")
print("Name:", student.name)
print("Student ID:", student.student_id)
print("Course:", student.course)
print("Marks:", student.marks)
print("Result:", student.result())
