f = open("nik.txt") #open(filename.txt) returns a file pointer
content = f.read()
print(content)
f.close()

f = open("nik.txt","rt") #open(filename.txt) returns a file pointer // IMPT: rb read binary rt - read text
content = f.read(10)
print(content)
content = f.read(10)
print(content)
f.close()

f = open("nik.txt","rt")
for line  in f:
    print(line)
f.close()

f=open("nik.txt","rt")
print(f.readline(10))
print(f.readline(3))
print(f.readline(2))
print(f.readline())
print(f.readline())

f=open("nik.txt","rt")
print(f.readlines()) #comment this line to see magic of same output from the code beneath
list3 = f.readlines() #makes the output of whole lines in go in list
print(list3)
