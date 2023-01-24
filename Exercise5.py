# Health Management System
# 3 clients
# Total 6 files
# write a function that when executed with as file name
# logs diet and exercise with time stamp
# one function to enter all the data
# one function to retrieve all the date
# f.write("\n"+a+"\t"+b)

#For reading whole file.
# f = open("nik.txt","rt")
# for line  in f:
#     print(line)
# f.close()


def getdate():
    import datetime
    return datetime.datetime.now()
date_time=str(getdate())

def enter_data_diet(num_1):
    food =input("enter what you ate ? ")
    if (num_1==1):
        with open("Hulk_diet.txt","a+") as f:
            f.write("\n["+date_time+"\t"+food)


    elif (num_1 == 2):
        with open("Thor_diet.txt","a+") as f:
            f.write("\n["+date_time+"\t"+food)

    elif (num_1 == 3):
        with open("Loki_diet.txt","a+") as f:
            f.write("\n["+date_time+"\t"+food)
    else:
        print("WRONG CLIENT NUMBER")
        # return null


def enter_data_exercise(num_2):
    exercise = input("enter what you exercised ? ")
    if (num_2 == 1):
        with open("Hulk_exercise.txt","a+") as f:
            f.write("\n["+date_time+"\t"+exercise)

    elif (num_2 == 2):
        with open("Thor_exercise.txt","a+") as f:
            f.write("\n["+date_time+"\t"+exercise)

    elif (num_2 == 3):
        with open("Loki_exercise.txt","a+") as f:
            f.write("\n["+date_time+"\t"+exercise)

    else:
        print("WRONG CLIENT NUMBER")
        # return null

def retrieve_data(num_3):
    if (num_3 == 1):
        with open("Hulk_diet.txt","rt") as f:
            for line in f:
                print(line)
        with open("Hulk_exercise.txt","rt") as f:
            for line in f:
                print(line)
    elif (num_3 == 2):
        with open("Thor_diet.txt","rt") as f:
            for line in f:
                print(line)
        with open("Thor_exercise.txt","rt") as f:
            for line in f:
                print(line)
    elif (num_3 == 3):
        with open("Loki_diet.txt","rt") as f:
            for line in f:
                print(line)
        with open("Loki_exercise.txt","rt") as f:
            for line in f:
                print(line)
    else:
        print("WRONG CLIENT NUMBER")
        # return null

def main1():
    print("Enter the client name for which you want to enter data")
    print("Enter 1 for Hulk 2 for Thor 3 for Loki")
    client_num = int(input())

    print("Enter 1 for Logging DIET Data in the file")
    print("Enter 2 for Logging EXERCISE Data in the file")
    print("Enter 3 for Looking at Data Stored")
    action_num = int(input())

    if (action_num==1):
        enter_data_diet(client_num)
    elif (action_num==2):
        enter_data_exercise(client_num)
    elif (action_num==3):
        retrieve_data(client_num)
    else:
        print("Enter proper request")

    choice=input("Want to continue Y for YES and any other key to exit")
    if(choice in ["Y","y"]):
        main1()
    else:
        print("----- THANK YOU FOR USING NIK's HEALTH MANAGEMENT SYSTEM------")


main1()
