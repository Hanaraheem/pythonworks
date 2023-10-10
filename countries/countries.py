from json import load #json file ne convert cheyyan,loads-string ne covert cheyyan
path="C:\\Users\\HP\\OneDrive\\Desktop\\luminar_python\\countries\\countries.json"
with open(path,encoding="UTF-8") as f:
    countries=load(f)

#lenght
print(len(countries))
#1.names of count
countries_name=[c.get("name")for c in countries]
print(countries_name)

#2.capital of china
china=[c.get("capital")for c in countries if c.get("name")=="China"]
print(china)
 
 #3.print region
regions={c.get("region")for c in countries} #to remove duplicate we use{}
print(regions)
#4.print india borders
borders=[c.get("borders")for c in countries if c.get("name")=="India"][0] #remove one list
print(borders)

# #check alpha 3 code match then print name
# fullname_country=[c.get("name")for c in countries if c.get("alpha3Code") in borders ]
# print(fullname_country)

#print indepent country
independ=[c.get("name")for  c in countries if c.get("independent")==True]
print(independ)
#print currency name of india
currency=[c.get ("currencies") for c in countries if c.get("name")=="India"][0][0]
print(currency.get("name"))

#print country without currency

data=[c.get("name")for c in countries if ("currencies") not in c]
print(data)

#print currency countires and also max count
country_curr=[c for c in countries if "currencies" in c] #to find only currency countires
currencies=[c.get("currencies")[0].get("symbol")for c in country_curr]
                      #to remove [] from curren
wc={}
for c in currencies:
    if c in wc:
        wc[c]+=1
    else:
        wc[c]=1

print(wc)
print(max((v,k) for k,v in wc.items()))






