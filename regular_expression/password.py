        #password valid
#atleast one upper          (evide eghilum)
#atleast 1 special char
#minimum of 8 char

#(positivelook)"?=.evideghilum undayaal matee"
#*-atleast
#.-forntil

from re import*
password="Password@123"
rule="(?=.*[A-Z])(?=.*[\W])(?=.*[\d]).{8,}"
matcher=fullmatch(rule,password)
print("invalid" if matcher==None else "valid")