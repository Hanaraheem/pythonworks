#more than one form
#method overriding, overloading


         #method overiding
#inheritance must
#parent inte method override cheyyum childil
#signature same as parent
#parent inte chela method mati child new method edum

class Car:
    def start(self):
        print("key start")

    def break_type(self):
        print("sudden")

    def transmission(self):
        print("manuel")

class Waganor(Car):
    pass#(same as car inte method)

class swift(Car):
    def break_type(self): # method over riding
        print("disc type") #car inte breakil ninnum different ane swift inte so override cheyyum
                            #sudden maati disc aakkum
obj=swift()
obj.start()
obj.break_type()
obj.transmission()


#method overloading
#same method name ,but different parameter
#only one class
#not used in python

class calculator:
    def add(self,n1,n2):
        print(n1+n2)
    def add(self,n1,n2,n3):
        print(n1+n2+n3)
obj=calculator()
obj.add(10,20,30)
