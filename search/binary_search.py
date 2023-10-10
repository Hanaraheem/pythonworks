        #binary search
 #complicity less
 #sorted order
 #mid find         0     1        2           3     4
#                 10    12       14          16     18                       
 #logic          low             mid               upp
 #low=0                low (if left side)   low(eghot varanm,rightside nokkumbool)
 #upp=len(lst)-1
 #loop:
 #mid=(low+upp)//2
 #case1
 #if element==lst[mid] 
 #found
 #case2
 #elif element>lst[mid] (searching element on the right side of mid)
#low=mid+1
#case3
#elif element<lst[mid](left side)
#upp=mid-1

#program
lst=[12,3,4,15,16,18]
lst.sort()
element=3
low=0
upp=len(lst)-1
is_found=False
while(low<=upp):
    mid=(low+upp)//2

    if element==lst[mid]:
     is_found=True
     break
    elif element<lst[mid]:
      upp=mid-1
    elif element>lst[mid]:
     low=mid+1
print(is_found)

    
