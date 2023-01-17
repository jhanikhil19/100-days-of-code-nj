#Faulty calculator
#create a calculator which can do all the operations correctly apart from the following ones:
#45*3=555, 56+9=77,56/6=4
#your program should take operator and two numbers as input and then show result.


Opr = input("Enter Operator")
num1= int(input("Enter Number1"))
num2=int(input("Enter Number2"))
if Opr=="*":
    if num1==num2:
        result=num1*num2
        print(num1, Opr, num2, "=", result)
    elif num1 in [45,3]:
        if num2 in [45,3]:
            print(num1,Opr,num2,"=555")
    else:
        result=num1*num2
        print(num1, Opr, num2, "=", result)
elif Opr=="+":
    if num1==num2:
        result=num1+num2
        print(num1, Opr, num2, "=", result)
    elif num1 in [59,7]:
        if num2 in [59,7]:
            print(num1,Opr,num2,"=77")
    else:
        result=num1+num2
        print(num1, Opr, num2, "=", result)

elif Opr=="/":
    if num1==num2:
        result=num1/num2
        print(num1, Opr, num2, "=", result)
    elif num1==56:
        if num2==6:
            print(num1,Opr,num2,"=4")
    else:
        result=num1/num2
        print(num1, Opr, num2, "=", result)
elif Opr=="-":
    result=num1-num2
    print(num1, Opr, num2, "=", result)

else:
    print("Enter correct Operators")

#print(num1,Opr,num2,"=",result)