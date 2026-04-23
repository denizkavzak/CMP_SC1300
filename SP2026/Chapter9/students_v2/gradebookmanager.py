# import sys
# sys.path.append("/C:/MU/CMP_SC1300/Code/Chapter9/students_simple/gradebook")

from gradebook import GradeBook
from student import Student

gradebook = GradeBook()

student1 = Student("Deniz", "Kavzak", Student.GRADUATE, 4.0)
print("ID:", student1.getID())
student2 = Student("Jack", "Black", Student.SENIOR, 3.5)
print("ID:", student2.getID())
student3 = Student("Emma", "Ufuktepe", Student.SOPHMORE, 3.0)
print("ID:", student3.getID())
student4 = Student("Britton", "Ufuktepe", Student.SOPHMORE, 3.2)
print("ID:", student4.getID())

print(student1.isSameYear(student2))
print(student3.isSameYear(student4))

studentAlias = student1
print((studentAlias == student1))

print((studentAlias == 1))

gradebook.addStudent(student1)
gradebook.addStudent(student2)
print("Student count:", gradebook.getStudentCount())
gradebook.addStudent(student3)

gradebook.printGradebook()

print("Student count:", gradebook.getStudentCount())

gradebook.removeStudent(2)

gradebook.printGradebook()

print("Student count:", gradebook.getStudentCount())

gradebook.addStudent(student4)

gradebook.printGradebook()

print("Student count:", gradebook.getStudentCount())

