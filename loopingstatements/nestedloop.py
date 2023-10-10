#nested loop=more than one loop on a program
#-> row ,| col



# print row and column 
#  #  #
#  #  #
#  #  #

# for row in range(1,4): #parent loop 1
#    for col in range(1,4):#child loop 2
#       print("#",end="\t") #/t is used for get tab space 
# print()



# 1  1  1
# 2  2  2
# 3  3  3

# for row in range(1,4):
#    for col in range(1,4):  
#       print(row,end="\t") # in this case we print row bcoz in row the values are same as row number ,but in the case of col values are incremented so difficult to print.
# print()





#  
#   #       #if row value is 1 = col number is also 1
#   #  #

# for row in range(1,4):
#    for col in range(row): #row count equal to col number
#       print("#",end="\t")
# print()


#1 
#1   2
#1   2   3


for row in range(1,4):
   for col in range(row):
       print(col+1,end="\t") #in this case col value is same and +1 is used bcoz it start zero
   print()


#print the following,if even print #
#1 
#1  #
#1  #   3
#1  #   3  #
#1  #   3  #  5
#1  #   3  #  5  #

for row in range(1,7):
    for col in range(row): 
        result=col+1
        if (result %2==0):
            print("#",end="\t")
        else:
            print(result,end="\t")
    print()


#  #  #  #
#  #  #
#  #
#

for row in range(4,0,-1):
    for col in range(row):
        print("#",end="\t")  
    print()

#                         
#           *               space=6
#         *   *              sp=5
#       *   *   *            sp=4
#     *   *   *   *          sp=3
#   *  *    *   *   *        sp=2
# *  *   *   *   *    *      sp=1


for row in range(1,7):
    for space in range(7-row,1,-1): #for space using help to know the space b/w each star,star=7-row,stop=1,and space decrement from 6 to 1
        print(end=" ")
    for star in range(row):#star value=row number
        print("*",end=" ")
    print()


#hollow full pyramid



#           *
#         *   *
#       *       *      (on left side :row number+col no total=7) 
#      *          *    (right side: col- row= 5)  
#    *              *
# *   *   *   *   *   *(11,6)=5(-)
 # (6,1)=7(+)


for row in range(1,7):
    if row==6 or row+col==7 or col-row==5:
     print("*",end=" ")
print()
          
