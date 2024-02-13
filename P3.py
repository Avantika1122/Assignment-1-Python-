# write a python programme to accept student number, name and marks in 3 subjects.Calculate total and average. Print the student result based on the below conditions.
#if avg>=75 result is distinction
#if avg>=60 result is First class
#if avg>=50 result is Second class
#if avg>=35 result is  Third class
#otherwise result is Fail


class Student:
    marks = []
    def getData(self, rn, name, m1, m2, m3):
        Student.rn = rn
        Student.name = name
        Student.marks.append(m1)
        Student.marks.append(m2)
        Student.marks.append(m3)
        
    def displayData(self):
        print ("Roll Number is: ", Student.rn)
        print ("Name is: ", Student.name)
        #print ("Marks in subject 1: ", Student.marks[0])
        #print ("Marks in subject 2: ", Student.marks[1])
        #print ("Marks in subject 3: ", Student.marks[2])
        print ("Marks are: ", Student.marks)
        print ("Total Marks are: ", self.total())
        print ("Average Marks are: ", self.average())
        
    def total(self):
        return (Student.marks[0] + Student.marks[1] +Student.marks[2])
    
    def average(self):
        return ((Student.marks[0] + Student.marks[1] +Student.marks[2])/3)
    
r = int (input("Enter the roll number: "))
name = input("Enter the name: ")
m1 = int (input("Enter the marks in the first subject: "))
m2 = int (input("Enter the marks in the second subject: "))
m3 = int (input("Enter the marks in the third subject: "))

s1 = Student()
s1.getData(r, name, m1, m2, m3)
s1.displayData()

if average >= 75:
    Result = 'Distinction'
else:
    if average >= 60 :
        Result = 'First Class'
    else:
        if average >=50:
            Result = 'Second Class'
        else:
            if average >= 35:
                Result = 'Third Class'
            else:
                Result = 'Fail'
