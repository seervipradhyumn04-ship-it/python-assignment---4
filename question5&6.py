class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "F"

s1 = Student("Rahul", 92)
s2 = Student("Priya", 78)

print(s1.name, "Grade:", s1.grade())
print(s2.name, "Grade:", s2.grade())
