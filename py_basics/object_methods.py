class Student:
    def __init__(self,fullname):
        self.name = fullname
    def hello(self):
        print("hello",self.name)
student = Student("shweta")
student.hello()