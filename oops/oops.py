           #object  oriented programming(vimp)
#1.class=collection of objt,blueprint of objt(design or plan)-attributes,methods
#2.object-(class vache entaane create cheyte athane objt)realworld entity
#eg :class Botle:
    #color (attri)
    #cap 

    #def fill()
    #def open() (methods)  self.attribute=attribute-class inte attrib aananne katan aane or attri create,current ojt point cheyyan

   #refrence=classname() (objt create)



#program1

class Employee:  #class
    id:int #(employee id=data type)
    name:str
    gender:str          #attributes
    department:str
    salary:int

    def create(self,id,name,gender,dpt,slry): #method1-create
        self.id=id  #self is used for getting attributes
        self.name=name
        self.gender=gender
        self.department=dpt
        self.salary=slry

    def get(self):#methode2-display
        print(self.id,self.name,self.gender,self.department,self.salary)

emp1=Employee() #1st obj creation (copy of class)
emp1.create(1,"hana","female","py",20000)

emp2=Employee()#2nd obj creration
emp2.create(2,"kaavu","female","py",2000)

emp1.get() #display obj1












