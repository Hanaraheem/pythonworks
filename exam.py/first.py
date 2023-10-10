# # program1
# list=[
#     [1803,1809,1805],
#     [1909,1911,1805],
#     [2000,2004,2005],
#     [2011,2012,2013]
# ]
# for e in list:
#  if (list%e==400 and list%e==100):
#       print(e)
#  elif (list%e==4 and list%e!=100):
#      print(e)





#program-2


# txt="ABABC"
# non_re="C"
# count=0
# for ch in txt:
#     if ch in non_re:
#         count+=1
#         break
#     else:
#         count=1
#         print(non_re)
#         break



# program=3
txt="ABCDABCDAB"
from re import*
pattern="AB"
count=0

for ch in txt:
    if ch in pattern:
        count+=1
    else:
        count=1
print(count)
 


#program-4

# class Books:
#     id:int
#     name:str
#     price:int

# def create(self,id,name,price):
#     self.id=id
#     self.name=name
#     self.price=price

# obj=Books()
# obj.create(100,"python",350)
# obj.create(101,"java",450)
# obj.create(102,"Django", 1300)







        


