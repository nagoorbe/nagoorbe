#override of __str__ method
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student(Name={self.name}, Marks={self.marks})"
    
s1 = Student("Rahul", 85)
print(s1)
