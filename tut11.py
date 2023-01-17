#sets

s=set()
print(type(s))
set_from_list = set([1,23,432,123,234])
print(set_from_list)
print(type(set_from_list))
l=[1,3,2,45]
s_from_list=set(l)
print(s_from_list)
s.add(1)
s.add(4)
s.add("hello")
s.remove(4)
s1=s.union({1,2,3})
s2=s.intersection({1,2,3,4})
print(s,s1,s2)
#this set function can be used to complete all the functions of the SET THEORY which we read in school.
