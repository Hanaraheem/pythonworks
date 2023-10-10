#operators

#arithmetic    +(addition),-(sub),*(multiplication),%(modulars),/(division),//(floor division)-remove all pointed values ,**(exponential)
#logical      
#assignment
#relational
#bitwise
#membership operators
#//(floor division)-remove all pointed after values
#eg:2.7=2 ,10//5=2




n1=10
n2=20
print("sum=",n1+n2)
print("difference=",n1-n2)
print("multiplication=",n1*n2)
print("division=",n1/n2)
print("modulas=",n1%n2)  #reminder
print("expo=",n1**n2)    #n1 rise to n2
print("floor=",n1//n2)   #point values remove,only gave interger values


#assign1:find out the selling price of a product if offer in percentage and items current orice is given.
#for eg:if current_price=89
     #dis_percentage=5%
     #selling_price=?

cu=89
dis=5
discount=cu*dis/100
sp=cu-discount
print("current_price is",cu)
print("discount is",discount)
print("selling_price is",sp)



#assign2:convert degree celcious to fahrenheit
#input:45 %celcious
#output:113 Fahrenheit

celsius=45
fahrenheit=(celsius * 1.8) + 32
print("fahrenheit is",fahrenheit)


#assignment 3 (find offer in percentage)

actual_price=140
selling_price=135
discount=actual_price-selling_price
print(discount)
offer_inperc=(discount/actual_price)*100
print(offer_inperc)



#assignment 3 (find bmi)

#BMI body mass index
#bmi=(weight in kg)/height in meter square
weight_kg=72
height_cm=165
#cm=>meter  meter=cm/100
height_m=height_cm/100
print(height_m)
bmi=(weight_kg)/height_m**2
print(bmi)

                    #ASSIGNMENT

#1.volume

vol_litre=4
vol_milliliter=vol_litre*1000
print(vol_milliliter)

#2.pressure

pres_pascal=1
pres_bar=pres_pascal/100000
print(pres_bar)


#3.speed

speed_mtr_per_sec=5
speed_kilometer_per_hr=speed_mtr_per_sec*3.6
print(speed_kilometer_per_hr)


#4.mass

mass_kg=7
mass_gm=mass_kg*1000
print(mass_gm)


