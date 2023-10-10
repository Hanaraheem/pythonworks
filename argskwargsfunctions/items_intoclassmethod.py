
#items ne class ,methods aakki maatanam
#return cheyyundel matram print kodutaal matee,allel nirbandamilla


class Hotel:
    items=[
    {"id":100,"name":"cb","price":160},
    {"id":101,"name":"veg","price":140},
    {"id":102,"name":"poratto","price":70},
    {"id":103,"name":"shake","price":460},
    {"id":104,"name":"chicken","price":10},
    {"id":105,"name":"ghee","price":150},
]


    def create(self,*args,**kwargs):
       self.items.append(kwargs)  #create method
       return f"{kwargs} created"

   
    def retrieve(self,id=None,*args,**kwargs):  #retrieve method
         obj=[i for i in self.items if i.get("id")==id][0]
         return obj
    
    def destroy(self,id=None,*args,**kwargs):  #destroy method
         obj=[i for i in self.items if i.get("id")==id][0]
         self.items.remove(obj)
         return f"{obj} has been removed"
    
    def update(self,id=None,*args,**kwargs):  #update method
         obj=self.retrieve(id=id)
         obj.update(kwargs)
         return f"{obj} has been updated"
    

obj=Hotel()
#  print(obj.create(id=106,name="noodles",price=180))
# print(obj.retrieve(id=101))
# print(obj.destroy(id=102))
print(obj.update(id=102,name="GHEE ROAST"))