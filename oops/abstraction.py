#details hide (implementation details hide)
#binding of data-encapsulation
#abstract class contain only declaraction  not definition,the class inherit from abstract will define
#first import abstract class-abc.py

#syntax:
#from abc importABC, abstractmethod:   (import from abc)
#class parent(ABC):    (eppo parent is a abstract class)

        # @abstractmethod
        #   declare method

#class child(parent): (inherit class)
       #  method defition   

#obj creation


from abc import ABC,abstractmethod #(abstract base class ,abstractmethod)
class Bike(ABC):

    @abstractmethod #decorater(compel)
    def start(self):
        pass

    @abstractmethod
    def accelarate(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Hunter(Bike):

        def start(self):
            print("starting")

        def accelarate(self):
            print("accelarate")

        def stop(self):
            print("stop")


obj=Hunter()
obj.start()
obj.accelarate()



#program-bank
from abc import ABC,abstractmethod #(abstract base class ,abstractmethod)
class Bank(ABC):

    @abstractmethod #decorater(compel)
    def fund_tranfer(self):
        pass

    @abstractmethod
    def balance(self):
        pass

    @abstractmethod
    def translaction_history(self):
        pass

class gpay(Bank):

        def fund_tranfer(self):
            print("fund_tranfer")

        def balance(self):
            print("balance")

        def translaction_history(self):
            print("translaction_history")

        def reward(self):
            print("reward") #we can define amethod on inherit class without creating declaraction in abstract classny 

        


obj=gpay()
obj.fund_tranfer()
obj.balance()
obj.reward()




        


        