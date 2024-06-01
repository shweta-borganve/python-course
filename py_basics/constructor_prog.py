class Student:
    def __init__(self,fullname):
        self.name = fullname
        print("adding new student in Database")

S1 = Student("karan")
print(S1.name)
S2 = Student("arjun")
print(S2.name)