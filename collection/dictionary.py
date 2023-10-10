#key:values pairs
#{}
#very imp


mobile={"name":"vivoA5","brand":"vivo","price":15000,"color":"black","offer":100}
print(mobile["name"])
print(mobile["price"])

#1.adding any values into mobile(updatable)
mobile["display"]="led"
print(mobile)
#2.checking if the value is present or not in mobile
if "offer" in mobile:
    print("present")
else:
    print("not present")
#3.if the offer is present add 50 to it ,else 10

if "offer" in mobile:
    mobile["offer"]+=50
else:
    mobile["offer"]=50
print(mobile)


#find the order count
orders=["vegmeals","fishmeals","meatmeals","hv","bb","fishmeals"]
order_count={} #empty diction
for item in orders: #items in order
    if item in order_count: #items in orders into order_count
        order_count[item]+=1#if the items is repeat add 1 to it
    else:
       order_count[item]=1#not repeat gave 1
print(order_count) 

#find the count of enquery
enquery=["java","testing","java","full stack","python","python","mearn"]
enquery_count={}
for item in enquery:
    if item in enquery_count:
        enquery_count[item]+=1
    else:
        enquery_count[item]=1
print(enquery_count)

#character count from text
text="carrot"
wc_count={}
for ch in text: #ch is used for take each letters separately
    if ch in wc_count:
       wc_count[ch]+=1
    else:
        wc_count[ch]=1
print(wc_count) 

#word count
text="hello hai hello hai"
words=text.split(" ") #used for spliting the words
wc={}
for w in words: #w is used foe taking words separatly
        if w in wc:
            wc[w]+=1
        else:
           wc[w]=1
print(wc)

#dictonaryil ninne key edukkan []use cheyyanam
#eg: person=["name","age"]
 #print(person["name"])
#searching mechanism fast

#find the first recrussive character(first repeating character)
text="ABACB"
wc={} #empy dicti
for ch in text: #ch in text
    if ch in wc: #ch add to wc,reapeat the until find the recrussive
        print(ch,"is the recrussive character")
        break #if the first character is recrussive stop
    else:
        wc[ch]=1 #add  1 to ch into wc


    