class Student:
    FRESHMAN = 1 # class variable
    SOPHMORE = 2
    JUNIOR = 3
    SENIOR = 4
    GRADUATE = 5
    
    def __init__(self, ID, name, lastname, year = FRESHMAN, gpa = 0.0):
        self._ID = ID
        self._name = name
        self._lastname = lastname
        self._year = year
        self._gpa = gpa
        
    def printStudent(self):
        print(self._ID, self._name, self._lastname, self._year, self._gpa)

    def updateGPA(self, newGPA):
        self._gpa = newGPA
       
    def getID(self):
        return self._ID
    
    def getName(self):
        return self._name
    
    def getLastName(self):
        return self._lastname
    
    def getYear(self):
        return self._year
    
    def getGPA(self):
        return self._gpa