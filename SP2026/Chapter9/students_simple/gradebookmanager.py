# import sys
# sys.path.append("/C:/MU/CMP_SC1300/Code/Chapter9/students_simple/gradebook")

##
# This is a Gradebook manager class
# This class handles the records of
# students, prepares and updates 
# the gradebook
#

from gradebook import GradeBook
from student import Student

gradebook = GradeBook()

student1 = Student(1, "Deniz", "Kavzak", "Grad", 4.0)
student2 = Student(2, "Jack", "Black", "senior", 3.5)
student3 = Student(3, "Emma", "Ufuktepe", "sophmore", 3.0)

gradebook.addStudent(student1)
gradebook.addStudent(student2)
print("Student count:", gradebook.getStudentCount())
gradebook.addStudent(student3)

gradebook.printGradebook()

print("Student count:", gradebook.getStudentCount())

gradebook.removeStudent(3)

gradebook.printGradebook()

print("Student count:", gradebook.getStudentCount())

