                      #list_comprehension

#it help for minimise the steps into one
lst=[4,5,6,7,8]
# square=[]               in this form many spets are used
# for i in lst:
#     square.append(1**2)
    #instead of using many steps we use list comprehension
    #syntax   a=[return    loop    condition]
square=[i**2 for i in lst ]  #without condition
print(square)

 #with condition

even=[i for i in lst if i%2==0 ]
print(even)

odd=[i for i in lst if i%2!=0 ]
print(odd)

greater=[i for i in lst if i>=5]
print(greater)

#1900-2023
years=[y for y in range(1900,2023)]
print(years)
#print the century yr
years=[y for y in years if y%100==0]
print(years)
#print non century yrs
years=[y for y in range(1900,2023)]
years=[y for y in years if y%100!=0]
print(years)


#prgram-1
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



# print all product names(using list_comprehension)
all_names=[i.get("name" )for i in items]
print(all_names)
# print all in stock product names

stock=[i.get("name") for i in items if i.get("avl_qty")>0]
print(stock)
   
# print product names avaialble under rs 50

prd=[i.get("name") for i in items if i.get("price")<50]
print(prd)

# print all product names avilable in range of 20 to 50

prd=[i.get("name") for i in items if i.get("price") in range(20,51) ]
print(prd)
 #print the orea price
oreo=[i.get("price") for i in items if i.get("name")=="oreo"]
print(oreo)

#update price
oreo_data=[i for i in items if i.get("name")=="oreo"][0] #to remove list(bracket) we gave the position
oreo_data["price"]=90 #update the price
print(items)

#costly price
costly_price=max(items,key=lambda d:d.get("price"))
print(costly_price)
least_price=min(items,key=lambda d:d.get("price"))
print(least_price)
