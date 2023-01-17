print("Enter a sentence of your choice")
mystr = input()
print(mystr)
print("4th character in string is ",mystr[3])
print(mystr[0:10]) #here 0 is including and 10 is excluding so add 1 more wherever needed.
print(mystr[0:10:3]) #here 0 is including and 10 is excluding so add 1 more wherever needed.
print(len(mystr))
print(mystr[::-1])
print(mystr.isalpha())#too many functions like this are present
print(mystr.endswith(" Jha"))#endswith is case senstive
print(mystr.count("n"))#case senstive
print(mystr.find(" is")) #gives the first occurance co-ordinate

