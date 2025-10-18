class Student:
    def __init__(self, name, usn, age, dob, subject):
        self.name = name
        self.usn = usn
        self.age = age
        self.dob = dob
        self.subject = subject
def display_details(self):
        print("Student Details:")
        print(f"Name     : {self.name}")
        print(f"USN      : {self.usn}")
        print(f"Age      : {self.age}")
        print(f"DOB      : {self.dob}")
        print(f"Subject  : {self.subject}")
student1 = Student("basamma.p.m", "01fe24bca265", 19, "14/11/2006", "devops")
student1.display_details()
