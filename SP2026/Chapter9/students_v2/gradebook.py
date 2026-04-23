from student import Student

##
## 
#  This module defines the GradeBook class.
#

## A simulated GradeBook entity
#
class GradeBook :
   ## Constructs a cash register with cleared item count and total.
   #
   def __init__(self) :
      self._gradebook = {}
      self._studentCount = 0
      
   ## Implementing add function to add a student object
   #  to the dictionary gradebook
   #  @param student object
   #
   def addStudent(self, student) :
      self._gradebook[student.getID()] = student
      self._studentCount += 1
      
   ## Implementing remove function to remove a student object
   #  by its ID
   #  @param student ID
   #
   def removeStudent(self, ID) :
      self._gradebook.pop(ID)
      self._studentCount -= 1      

   ## Implementing getter function for a student object
   #  from the dictionary gradebook
   #  @param student ID
   #  @return student object
   #
   def getStudent(self, ID) :
      return self._gradebook[ID]

   ## Implementing add function to clear the dictionary
   #  @param student object
   #
   def clearGradebook(self) :
      self._gradebook.clear()

   ## Implementing print function to print all students in the dictionary
   #
   def printGradebook(self) :
      for studentID in self._gradebook:
         student = self._gradebook[studentID]
         student.printStudent()         

   ## Gets student count
   #  @return student count
   #
   def getStudentCount(self) :
      return self._studentCount