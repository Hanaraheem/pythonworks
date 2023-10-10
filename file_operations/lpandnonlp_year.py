f_read=open("C:\\Users\\HP\Desktop\\luminar_python\\file_operations\\years.txt","r")
lp_write=open("C:\\Users\\HP\\Desktop\\luminar_python\\file_operations\\leap_year.txt","w")
# for y in range(1800,2024):
#  if (y%400==0)or(y%100!=0)and(y%4==0): 
#    fw.write(str(y)+"\n")

         #or
for year in f_read:
  year=int(year)
  if (year%100==0)and (year%400==0):
    lp_write.write(str(year)+"\n")
  elif(year%100!=0)and(year%4==0):
    lp_write.write(str(year)+"\n")