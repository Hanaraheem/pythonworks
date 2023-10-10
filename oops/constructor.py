#initializing instance variable
#constructor name-__init__
#instead of creating we can easly use constructor so we can gave value on obj directly

class Book:
    book_name:str
    price:int
    author:str
    pages:int

    def __init__(self,book_name,price,author,pages): #constructor
        self.book_name=book_name
        self.price=price
        self.author=author
        self.pages=pages
    def get(self):
        print(self.book_name,self.price)

obj=Book("it",300,"charks",202)
print(obj.book_name)
  

        #__str__method -for return string value
        #it is from object parent class


class Book:
    book_name:str
    price:int
    author:str
    pages:int

    def __init__(self,book_name,price,author,pages): #constructor
        self.book_name=book_name
        self.price=price
        self.author=author
        self.pages=pages
    def get(self):
        print(self.book_name,self.price)

    def __str__(self):
      return self.book_name


obj=Book("it",300,"charks",202)
print(obj)#obj inte name pettanne venameghil str method 





