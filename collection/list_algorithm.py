
           #PROGRAM - 1
#program to find repeated numbers                  #logic
arr=[5,2,5,3,2]                             # 2   2   3   5    5   #after sorting
arr.sort()                                  # 0   1   2   3    4(position)
duplicate_list=[]                           #first current=2,next=2 then check:2==2  continue....util the loop stop
for i in range(0,len(arr),-1):#(start from 0,stop- length of athe arr,decrement by 1)
   current=arr[i]
   next=arr[i+1]
   if current==next:
      if current not in duplicate_list:
         duplicate_list.append(current)
print(duplicate_list)


       #PROGRAM - 2
#find least +ve missing integer
        #LOGIC
#1.sort first ,move curr into first posi and nxt into nxt of curr
#2.nxt-curr!=1(if the difference is not 1 the value is missing)
#3.then print curr+1
arr=[1,2,3,5,6]
#    c n
arr.sort()
for i in range(0,len(arr)-1):
   current=arr[i]
   next=arr[i+1]
   if next-current!=1:
      print(current+1,"is missing")
      break
               # or( check whether first digit is missing or not)
arr=[1,2,3,5,6]
arr.sort()
if arr[0]!=1:
   print("1 is missing")
else:
 for i in range(0,len(arr)-1):
   current=arr[i]
   next=arr[i+1]
   if next-current!=1:
      print(current+1,"is missing")
      break

                #PROGRAM - 3
   
   #two pair sum(vimp)

list=[2,3,4,5]                                          #logic
sum=8                                            # 2  3  4   5
lower_limit=0                                    # low       upper
upper_limt=len(list)-1                             #1.low<upper(2<5)
while(lower_limit<upper_limt):                     #2.currentsum=low+upp(2+5=7)
                                                   #3.condition(cases)
   current_sum=list[lower_limit]+list[upper_limt]   #a.currentsum==sum(7==8)
   if(current_sum==sum):#case1                      #b.currentsum<sum(7<8)->low+1 or upper+1
      print(list[lower_limit],list[upper_limt])                             #2+1=3 or 5+1=6
      break
   elif(current_sum<sum):#case2
      lower_limit+=1
   else:
     upper_limt-=1 
#bruspot-to minimise the complicity(time compli o()t, space compl o()s) 
#question -find common digits in lists
list1=[10,11,12,13,16]                      #logic (with using membership operator)
list2=[12,13,14,20,21]                #1.list1 first element check with all elements in list2
out=[]                                #2.continue ....util find the common elements
for n in list1:
   if n in list2:
      print(n)
           
           #OR

list1=[10,11,12,13,16]                           #logic(using case)
                                          #list1-10(p1),11,12..    list2-12(p2),13,14...
list2=[12,13,14,20,21]                           #1.p1,p2=0
list1.sort()                                     #2.loop for both the list:
list2.sort()                                     #3.if list1[p1]==list2[p2] (case1)(if the first element of both list is same)
p1,p2=0,0   # (starting with 0 posi)             #4.iflst[p1]<lst2[p2],p+1 or p2+1(if the list2 element is lessthan list2 )
while(p1<len(list1) and p2 <len(list2)):
 if list1[p1]==list2[p2]:                        
  print("common",list[p2])
  p2+=1
 elif list1[p1]<list2[p2]:            
    p1+=1                                
 else:
    p2+=1

   #user input

index=int(input("enter the lenght of list:")) #input the lenght
list=[]
for i in range(index):
   element=int(input("enter the elements:>")) #input the elemenets
   list.append(element) #add the elements to list
print(list)
