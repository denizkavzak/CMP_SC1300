from counter import Counter

counter1 = Counter() # calling the constructor creating a new object

print("Count initial:", counter1.getStudentCount())
#print("Count initial using instance variable:", counter1._studentCount)

counter1.enterClass()
print("Count:", counter1.getStudentCount())

counter1.enterClass()
counter1.enterClass()
print("Count:", counter1.getStudentCount())

counter1.exitClass()
print("Count:", counter1.getStudentCount())

counter1.reset()
print("Count after reset:", counter1.getStudentCount())

counter1.enterClassMultipleStudents(5)
print("Count after 5 people entered:", counter1.getStudentCount())

counter1.exitClassMultipleStudents(2)
print("Count after 2 people left:", counter1.getStudentCount())