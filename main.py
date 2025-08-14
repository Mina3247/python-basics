# setting of dev tools and intro to python
# print ("hello world")

# getting started with programming
# m=10
# print(m)

# data types in python
# a=4
# b=4
# print (a+b)
# c="4"
# d="4" 
# print (c+d)
# print (type(a))
# print (type (c))
# weight_in_kg=60.5
# print(weight_in_kg)
# print(type(weight_in_kg))

# is_married=True
# print(is_married)
# print(type(is_married))

# birth_year=input("enter your birthyear")
# birth_year= int(birth_year)
# current_year=2025
# age=current_year-birth_year
# print(age)

# python operators I
# age1=34
# age2=65
# age3=5
# sum=age1+age2+age3
# average= sum/3
# average=int(average)
# print("Average:",average)


# print("welcome to the ATM")
# amount=input("enter an amount (in multiples of 100) to withdraw: ")
# amount=int(amount)
# note_1000=amount//1000
# print("1000 note count: ",note_1000)
# remainder1=amount%1000
# note_500=remainder1//500
# print("500 note count:  ",note_500)
# remainder2=remainder1%500
# note_200=remainder2//200
# print("200 note count: ",note_200)
# remainder3=remainder2%100
# note_100=remainder3//100
# print("100 note count: ",note_100)


# print("enter a,ount of marks (out of 100)in the below 4 subjects")
# science=int(input("science: "))
# math=int(input("math: "))
# english=int(input("english: "))
# history=int(input("history"))

# total_marks=science+math+english+history
# percentage=(total_marks/400)*100
# print("percentage:",percentage,end="%\n")

#conditional statements
# first_number=int(input("Enter first integer"))
# second_number=int(input("Enter second integer"))
# if first_number > second_number :
#     print(first_number,"is larger")
# elif second_number > first_number:
#     print(second_number,"is larger")
# else:
#     print("they are equal")

# cost_price=int(input("Enter the cost price of an apple"))
# selling_price=int(input("enter the selling price of an apple"))
# profit=selling_price - cost_price
# if profit > 0 :
#     print("you made a profit of:$",profit)
# elif profit<0 :
#     print("you have a loss of:$",(-profit))
# else:
#     print(" you have made neither a profit or loss")


# number=int(input("enter a number to check whether it is odd or even: "))
# if number %2 ==1 :
#     print("your number is odd")
# else:
#     print("your number is even")


# a=-9
# b=20
# result=a>b
# print(result)

# x=-9
# y=20
# z=20
# if z>0 or y>0 or x>0 :
#     print("at least 1 number is positive")
# else: 
#     print("all numbers are negative or zero")

#python operators II
# body_temperature=37
# if body_temperature!=37:
#     print("abnormal body temperature detected")


# height_in_cm=float(input("enter your height in cm: "))
# weight_in_kg=float(input("enter your weight in kg: "))
# height_in_meters=height_in_cm/100
# BMI=weight_in_kg/(height_in_meters**2)
# BMI=round(BMI,1)
# print(BMI)
# if BMI<18.5:
#     print("you are underweight")
# elif BMI<=24.9:
#     print("you are healthy weight")
# elif BMI<=29.9:
#     print("you are overweight")
# elif BMI<=39.9:
#     print("you are obese")
# else:
#     print("you are severly obese")