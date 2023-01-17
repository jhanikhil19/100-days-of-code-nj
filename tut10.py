#dictonary : it is nothing but key value pairs
d1={}
print(type(d1)) #Dictionary
d2=()
print(type(d2)) #Tuple
d3=[]
print(type(d3)) #List

d4={"Nikhil":"India","Alya":"Turkey","Freddie":"Egypt","Mark":"Germany","Rashida":{"Food":"Chicken","Dress":"Sexy dress","friends":"global"}}
print(d4["Alya"])
print(d4["Rashida"]["Food"])
#print(d4["Rashida"]["food"])#checking case sensitive --- its case senstive
d4["deep"]="Rajasthan"
print(d4)
print(d4["deep"])
del d4["Freddie"]
print(d4)
d3 = d4.copy()
print(d3)
print(d4.get("Nikhil"))
d4.update({"Akhil":"India"})
print(d4)
print(d4.keys())
print(d4.items())