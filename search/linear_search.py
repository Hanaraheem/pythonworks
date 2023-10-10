                   #linear search
# complicity is high

text=[1,2,16,5]
         #cu
element=16 #searching element
i=0 #start from 0th position
stop=len(text) #stop end of the txt
is_fount=False #set fount=false
while(i<stop): #start<stop
    current_value=text[i] # the value start from one 
    if current_value==element: # check current==16
     is_fount=True
    break  #stop searching
    i+=1 #to incre
print(is_fount)   

