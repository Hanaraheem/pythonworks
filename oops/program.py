

#abstraction

class Person:
    def __init__(self):
        self.name="kaavu"

    def bio(self):
        self.adr="abc"
        self.course="xys"
obj=Person()
print(obj.name)
             #or
class Student:
    def __init__(self,name,job):
        
        self.name=name
        self.job=job
    def get_student(self):
        print("my name is",self.name,"and my job is", self.job)
obj=Student("kaavu","watchwomen")
obj.get_student()
obj1=Student("hana","doctor")
obj1.get_student()

 #or
class  Book:
    def __init__(self):
         self.id=int(input("enter the id"))
         self.title=(input("enter the title"))
         self.author=(input("enter the author"))
         self.price=int(input("enter the price"))
    def get_author(self):
        print(self.author)
    def get_title(self):
        print(self.title)
    def get_author(self):
        self.price=int(input("enter the price"))
    def set_title(self):
        self.title=int(input("enter the price"))
b1=Book()
b1.get_author()
b1.get_title()
 
 ########
class  Mobile:
    def mob(self):
        print("oneplus")
    def car(self):
        print("bnw")
    def bike(self):
        print("ktm")
class Child(Mobile):
    def bike(self):
        print("pulse")
obj=Child()
obj.mob()
obj.car()
obj.bike()