# My first Python
students = []

class Student:
    schoolName = "Sacred Heart"
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return "Student " + self.name + "-" + str(self.id)

    def getNameCapitalize(self):
        return self.name.capitalize()

    def getSchoolName(self):
        return self.schoolName

class HighSchoolStudent(Student):
    schoolName = "Sacred Heart High"
    def getSchoolName(self):
        return self.schoolName
        


s1 = Student("Prem", 1001)
students.append(s1)
s1 = Student("Neha", 1002)
students.append(s1)
s1 = Student("Arun", 1003)
students.append(s1)
s1 = Student("Gopi", 1004)
students.append(s1)

for student in students:
    print(student)

s1 = HighSchoolStudent("Anil", 1005)
print(s1.getSchoolName())



