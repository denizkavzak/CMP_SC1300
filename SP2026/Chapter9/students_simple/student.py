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
   ## Constructs a student with given ID, name, lastname, year and gpa
   #
   def __init__(self, ID = 0, name = "", lastname ="", year = "", gpa = 0.0) :
      self._ID = ID
      self._name = name
      self._lastname = lastname
      self._year = year
      self._gpa = gpa
      self_lettergrades = []
      
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
   def addLetterGrade(self) :
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

   ## Prints a student object
   #
   def printStudent(self) :
      print(self.getID(), self.getName(), self.getLastName(), self.getYear(), self.getGPA())
      
      

