#in write
#syntax:variable name=open(path\\write.txt,w)

fw=open("C:\\Users\\HP\\Desktop\\luminar_python\\file_operations\\write.txt","w")
fw.write("babu")
    #years
fw=open("C:\\Users\\HP\\Desktop\\luminar_python\\file_operations\\years.txt","w")
for y in range(1800,2025):
    fw.write(str(y)+"\n")#only take string so use str


#write leapyears into leapyear.txt l_lw  (w)
lp_write=open("C:\\Users\\HP\\Desktop\\luminar_python\\file_operations\\leap_year.txt","w")
# for y in range(1800,2024):
#  if (y%400==0)or(y%100!=0)and(y%4==0): 
#    fw.write(str(y)+"\n")




   
#write nonleapyear into nonleap.txt nl_w  (w)

fw=open("C:\\Users\\HP\\Desktop\\luminar_python\\file_operations\\nonleapyears.txt","w")
for y in range(1800,2024):
 if (y%100==0)and(y%4!=0)or(y%400!=0): 
   fw.write(str(y)+"\n")
   
    