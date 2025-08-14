# setting of dev tools and intro to python
# no acp for this lesson


# getting started with programming


# Raj="23/04/2010"
# Mina="2/01/2012"
# tobi="04/02/2013"
# carlos="02/12/2014"
# selvana="02/02/2008"
# print(Raj)
# print(Mina)
# print(tobi)
# print(carlos)
# print(selvana)


# data types in python
# question- get 2 integers from the user and print their sum
# integer1=input("enter an integer")
# integer2=input("enter another integer")
# integer1=int(integer1)
# integer2=int(integer2)
# sum=integer1+integer2
# print(sum)



# python operatorsI
# question- get 2 integers from the user and ask him which operation they want to perform(addition,subtraction,multiplication,division)

# integer1=int(input("enter an integer"))
# integer2=int(input("enter another integer"))
# operation=input("what operation do you want to perform")
# if operation == "division":
#     print(integer1 / integer2)
# elif operation == "multiplication":
#     print(integer1 * integer2)
# elif operation == "addition":
#     print(integer1 + integer2)
# elif operation == "subtraction":
#     print(integer1 - integer2)
# else:
#     print("wrong operation")

# conditional statements
#question- create a simple login system. Ask the user for a username and password, and check if they match stored values. if they match, print login is sucsessful, otherwise print user name or password id incorrect.

# username=input("enter a username")
# if username == "mina.2067":
#     input("enter password")
# password=int(input("enter a password"))
# if password == 789:
#     print("welcome")
# else:
#     print("incorrect username or password")


username=input("enter a username")
password=input("enter a password")
correct_username= "mina.2067"
correct_password="123"
if username == correct_username and password== "123":
    print("welcome")
else:
    print("incorrect username or password")