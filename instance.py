class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Instance Method
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Rahul", 85)
s1.display()   
