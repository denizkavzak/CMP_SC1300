from student import Student

# ID, name, lastname, year = "FRESHMAN", gpa = 0.0
student1 = Student(1, "Deniz", "Kavzak", Student.GRADUATE, 4.0)
student1.printStudent()

student2 = Student(1, "Emma", "Ufuktepe")
student2.printStudent()

student3 = Student(gpa = 3.5, name = "Britton", lastname= "Ufuktepe", ID = 5, year = Student.SENIOR)
student3.printStudent()
