#it is an keyword 
#child il ninne parent inte sadhanaghal vaaghan vendi,parent ine mention or point cheyyan vendi -self() 
# parent ne child kodukkunnu
class Parent:
    properties=["bike","car"]

    def get_properties(self):
      return self.properties


class Child(Parent):
   
   def get_properties(self): #over ride
    self.p=super().get_properties() #parent inte proper varaan vendi super() keyword use
    self.p.append("phone") #parent inte kuude child int phn add cheytu
    return self.p

obj=Child()
print(obj.get_properties())

######## sir program
class Mobile:
   def __init__(self,*args,**kwargs): #constructor,*args,kwargs
      self.name=kwargs.get("name")

      self.brand=kwargs.get("brand")
      self.diplay=kwargs.get("display")

   def display_details(self):
      print(self.name,self.brand,self.display)


class Mobilevarient(Mobile):#child
   price:int
   color:str

   def __init__(self,*args,**kwargs):
      self.price=kwargs.pop("price") #remove
      self.color=kwargs.pop("color")
      print(self.price,self.color)
      super().__init__(kwargs)
   def display(self):
      super(self).display_details()
      print(self.price,self.color)

mv=Mobilevarient(name="milli",brand="mi",display="amoled",price=12000,color="grey")



