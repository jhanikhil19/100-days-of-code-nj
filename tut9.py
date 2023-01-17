#Pyton List
equipment=["iphone","monitor","ipad","pencil","air pods",64]
print(equipment)
print(equipment[2])
print(equipment[-2])
nums=[1,3,2,4,5,6]
print(nums[::-4])
print(nums)
print(nums[3])
print(nums[-1])
nums.sort()
print(nums)
nums.reverse()
print(nums)
print(nums[:6:2])
print(max(nums))

num2=[]
num2.append(1)
num2.append(4)
num2.append(6)
print(num2)
num2.insert(0,55) #it should name num2 as [55,1,4,6]
print(num2)
num2.pop()#removes the last element
num2.pop(0)#removes the item at 0
print(num2)
num3=[23,432,12,43,11,66,643]
print(num3)
num3[1]=69 #replaces num3[1] with the number I suggested
print(num3)
#List is mutable - can change elements from between as well.
#String and tuples are immutable
tp=(33,42,12) #tuple
print(tp)
print(tp[1])
print(tp[::-1])
# tp[1]=99 # not possible in tuples as it is immutable
# print(tp)
