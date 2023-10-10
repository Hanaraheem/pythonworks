items=[
    {"id":100,"name":"cb","price":160},
    {"id":101,"name":"veg","price":140},
    {"id":102,"name":"poratto","price":70},
    {"id":103,"name":"shake","price":460},
    {"id":104,"name":"chicken","price":10},
    {"id":105,"name":"ghee","price":150},
]

#1.kwargs={"id":100,"name":"bb","price":160}, #add this to the items

def add_item(*args,**kwargs):#args evide nirbandamilla
    items.append(kwargs)

add_item(id=106,name="bb",price=180)
print (items)


#2.take one item 
def retrieve_items(id=None,*args,**kwargs): # oru specific aayite obj mele operation cheyyumbool idil none use cheyyum
    objt=[i for i in items if i.get("id")==id]  #the operation like:retrive,delete,update
    print(objt)

retrieve_items(id=102)

#3.delete one item
def destroy_item(id=None,*args,**kwargs):
    objt=[i for i in items if i.get("id")==id][0]
    items.remove(objt)

destroy_item(id=102)
print(items)

# #update employee with data

# employee={"id":10,"name":"vijay","salary":3400,"dept":"hr"}
# data={"salary":2500,"dept":"it"}

# employee.update(data) #for updation
# print(employee)

#4.update
def update_item(id=None,*args,**kwargs):
    objt=[i for i in items if i.get("id")==id][0]
    objt.update(kwargs)

update_item(id=105,name="ghee roast")
print(retrieve_items(id=105))