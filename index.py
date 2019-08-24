# My first Python
students = []

class Student:
    schoolName = "Sacred Heart"
    def __init__(self, pname, pid):
        self.name = pname
        self.id = pid

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

""" Added the attribute 'course' on the fly """
for student in students:
    student.course = "BCA"
    print(student)

s1 = HighSchoolStudent("Anil", 1005)
s1.course = "MCA"
print(s1.getSchoolName())
print(s1)
students.append(s1)

for student in students:
    print("%s has roll number %s, is enrolled in the course %s" % (student.name, student.id, student.course))

func = lambda p: "\n%s has roll number %s, is enrolled in the course %s" % (p.name, p.id, p.course)

result = map(func, students)

print(*result)