#child inherit from parent
#syntax=class child(parent):


class Parent:
    phone="vivoY20"
    bike="passionpro"
    def mobile(self):
        print(self.phone)
    def vehicle(self):
        print(self.bike)

class Child(Parent):
     pass
obj=Child()
obj.mobile()


       #multiple inheritance
#syntax:class child(class1,class2)
class P1:

    def m1(self):
        print("inside the class p1 m1 method")

class P2:
    def m2(self):
        print("inside tge class p2 m2 method")

class Child(P2,P1): #only work m2 and m1 we gave p2 and p1 are inheritant by child
    def m3(self):
        print("inside the child m3 method")


obj=Child()
obj.m3()
obj.m2()
obj.m1()

####################################
class P1:

    def m1(self):
        print("inside the class p1 m1 method")

class P2:
    def m1(self):
        print("inside tge class p2 m2 method")

class Child(P2,P1): 
    def m3(self):
        print("inside the child m3 method")

obj=Child()
obj.m1()
