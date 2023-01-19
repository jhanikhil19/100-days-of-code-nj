# f = open("nik.txt","w")
# f.write("Nik you are doing great. Keep it up\n")
# f.close()
#
# f = open("nik.txt","a")
# a=f.write("Good luck")
# print(a)
# f.close()
#
# f= open("nik.txt","rt")
# #print(f.readline())
# print(f.readlines())
# f.close()

f=open("nik.txt","r+")
print(f.read())
f.write("\nThank you")
print(f.read())