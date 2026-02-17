class Student:    #class define
    schoolname ="nanjil"  #class variable

    def __init__(self,name,age):    #init called as constructors
        print("student object created")
        self.name=name     #instance variables
        self.age= age
    def display(self):
        print(self.name,self.age,Student.schoolname)

student1=Student ("sweety",12)
student1.display()

