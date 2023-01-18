#forloops
list1=["a","b","c","d"]
# i=0
# for i in len(list1):
#     print(list1[i])
#     i++;
# for item in list1:
#     print(item)
# for key in list1:
#     print(key)
# for i in list1:
#     print(i)

tup1=("a","b","c","d")
for i in tup1:
    print(i)

list2= [["a",1],["b",4],["c",23],["d",12]]
for i,j in list2:
    print(i,j)
for i in list2:
    print(i)

dict1=dict(list2)
for item in dict1.items():
    print(item)
for item in dict1:
    print(item)
#QUIZ
list3=["ana",1,34,645,234,11,"home"]
for item in list3:
    if (type(item)==int):
        print(item)
for item in list3:
    if str(item).isnumeric() and item>6:
        print(item)




