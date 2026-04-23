##
## 
#  This module defines the Student class.
#

# If we want to make the class immutable
### from dataclasses import dataclass
### @dataclass(frozen=True)

## A simulated Student entity that will be used in a gradebook
#
class Student :
   FRESHMAN = 1
   SOPHMORE = 2
   JUNIOR = 3
   SENIOR = 4
   GRADUATE = 5
   
   _lastAssignedID = 0
   
   ## ID of a student is automatically assigned using class variable 
   # so it is not a parameter in the constructor anymore
   ## Constructs a student with given ID, name, lastname, year and gpa
   #
   def __init__(self, name = "", lastname ="", year = "", gpa = 0.0) :
      self._ID = Student._lastAssignedID + 1
      self._name = name
      self._lastname = lastname
      self._year = year
      self._gpa = gpa
      self._lettergrades = []
      Student._lastAssignedID = Student._lastAssignedID + 1
      
   def __eq__(self, anotherStudent):
      if not isinstance(anotherStudent, Student):
         print("Passed parameter is not a Student object")
         return False 
      
      if self._ID == anotherStudent.getID():
         return True   
      else:
         return False
      
   ## Implementing update function for gpa
   #  @param gpa, new gpa value
   #
   def updateGPA(self, gpa) :
      self._gpa = gpa

   ## Implementing update function for gpa
   #  @param gpa, new gpa value
   #
   def updateYear(self, year) :
      self._year = year
      
   ## Implementing add grade function for the lettergrades list
   #  @param grade, new grade to be added
   #
   def addLetterGrade(self, grade) :
      self._lettergrades.append(grade)      

   ## Implementing get grades function for the lettergrades list
   #  @return lettergrades list
   #
   def getLetterGrades(self) :
      return self._lettergrades

   ## Gets ID value
   #  @return ID
   #
   def getID(self) :
      return self._ID
      
   ## Gets current gpa value
   #  @return gpa
   #
   def getGPA(self) :
      return self._gpa
      
   ## Gets name
   #  @return name of the student
   #
   def getName(self) :
      return self._name

   ## Gets lastname
   #  @return lastname of the student
   #
   def getLastName(self) :
      return self._lastname

   ## Gets year
   #  @return year of the student
   #
   def getYear(self) :
      return self._year
   
   def _convertYear(self, yearNo):
      if yearNo == 1:
         return "FRESHMAN"
      elif yearNo == 2:
         return "SOPHMORE"
      elif yearNo == 3:
         return "JUNIOR"
      elif yearNo == 4:
         return "SENIOR"
      elif yearNo == 5:
         return "GRADUATE"

   ## Prints a student object
   #
   def printStudent(self) :
      print(self.getID(), self.getName(), self.getLastName(), self._convertYear(self.getYear()), self.getGPA())
      
   ## Checks if the student object is at the 
   # same year as another Student object that is passed
   # @param another Student object   
   # @return returns True if same year, False if not
   #
   def isSameYear(self, anotherStudent):
      if self._year == anotherStudent.getYear():
         return True
      else:
         return False
      

