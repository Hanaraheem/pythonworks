

#   #METHODS
set={10,20,3,6,10}
# 1.add-for adding (position is not predictable)
set.add(40)
print(set)
#2.union- all elements of two set added in one set
# st1={10,20,11,12}
# st2={20,21,11,30,40}
# union_set=st1.union(st2)
# print(union_set)
#3.intersection-common of two set
# st1={10,20,11,12}
# st2={20,21,11,30,40}
# inter_set=st1.intersection(st2)
# print(inter_set)
#4.difference-set1 il  ninne set2 elements remove
# st1={10,20,11,12}
# st2={20,21,11,30,40}
# diff_set=st1.difference(st2)
# print(inter_set)
#5.remove-setil nine elements remove cheyyan (error return,if the value is not exist)
# st1.remove(20)
# print(st1)
#6.dicard- specify remove set ( no error return,if the value is not exist)
# st1.discard(20)
# print(st1)
#7.pop-random element remove
# st1.pop()
# print(st1)
#8.symmetric differerence-common elements remove from the both a and b
st1={4,5,2,8}         #a u b-a n b
str2={2,8,6,7}
sym_diff=st1.symmetric_difference(str2)  
print(sym_diff)

  
#convert list  into set and find the sachin followings


all_users=["sachin","rahul","rohit","koli","dravid","laxman","ganguly"]
sachin_following=["rahul","ganguly","dravid"]
sachin_su=set(all_users).difference(set(sachin_following))
sachin_su.remove("sachin")
print(sachin_su)
