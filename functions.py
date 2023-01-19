#functions

a=12
b=23
c=sum((a,b))
print(c)

def function1():
    print("Welcome to function 1")

def function2(a,b):
    """This is just to calculate the average"""
    avg = (a+b)/2
    #print("avg is",avg)
    return avg

function1()
function2(3,2)
v=function2(3,2)
print(v)
print(function2.__doc__)

