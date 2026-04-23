class Counter:
    
    def __init__(self):
        self._studentCount = 0
        
    def enterClass(self):
        self._studentCount = self._studentCount + 1
        
    def enterClassMultipleStudents(self, numberOfStudent):
        self._studentCount = self._studentCount + numberOfStudent
    
    def exitClassMultipleStudents(self, numberOfStudents):
        self._studentCount = self._studentCount - numberOfStudents
        
    def exitClass(self):
        self._studentCount = self._studentCount - 1
        
    def getStudentCount(self):    
        return self._studentCount
    
    def reset(self):
        self._studentCount = 0
        
    def _helper(self):
        return 0