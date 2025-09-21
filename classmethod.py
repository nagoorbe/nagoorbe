class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name   
print(Student.school)        
Student.change_school("XYZ School")
print(Student.school)       
