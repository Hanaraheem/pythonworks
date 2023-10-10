bikes=[
    {"cc":150,"id":100,"name":"duke","price":200000,"brand":"ktm"},
    {"cc":150,"id":101,"name":"xpulse","price":200000,"brand":"ktm"},
    {"cc":150,"id":102,"name":"hunder","price":220000,"brand":"hero"},
    {"id":103,"name":"metor","price":240000,"brand":"her"},
    {"id":104,"name":"activa","price":100000,"brand":"honda"},
    {"id":105,"name":"access","price":200000,"brand":"suzuki"},
]
#total number of bikes 
print(len(bikes))
#print all bikes name
for b in bikes:
    print(b.get("name"))
#print hero brand
for b in bikes:
    if b.get("brand")=="hero":
        print(b.get("name"))
#print bike name available under 150000
for b in bikes:
    if b.get("price")<=150000:
     print(b.get("name"),b.get("brand"))
#print 150 cc b ike names
for b in bikes:
   if b.get("cc")==150:
      print(b.get("name"))



               #program-2



items=[
    {"id":1,"name":"sugar","price":40,"avl_qty":10},
    {"id":2,"name":"milk","price":28,"avl_qty":40},
    {"id":3,"name":"teapowder","price":230,"avl_qty":100},
    {"id":4,"name":"tomatto","price":120,"avl_qty":5},
    {"id":5,"name":"potatto","price":45,"avl_qty":70},
    {"id":6,"name":"carrot","price":80,"avl_qty":0},
    {"id":7,"name":"oreo","price":45,"avl_qty":0},
    {"id":8,"name":"hideandseek","price":50,"avl_qty":50}
]


# print total number of products
print("total number of products:")
print(len(items))
# print all product names
print("all products name:")
for i in items:
   print(i.get("name"))
     
# print all in stock product names
print("stock product names:")
for i in items:
        if i.get("avl_qty")>0:
         print(i.get("name"))

   
# print product names avaialble under rs 50
print("product names avaialble under rs 50:")
for i in items:
    if i.get("price")<50:
        print(i.get("name"))
  

# print all product names avilable in range of 20 to 50
print("product names avilable in range of 20 to 50:")
for i in items:
    if i.get("price") in range(20,51):
        print(i.get("name"))
  


#costly price
costly_price=max(items,key=lambda d:d.get("price"))
print(costly_price)
least_price=min(items,key=lambda d:d.get("price"))
print(least_price)
