#this is  a program that define the even & odd numbers in python

x = int(input("what is your number"))
# attemp the user to give u a number and then determine whether it's a even or odd
if x == 2:
    print("this number is 2")
if x % 2 == 0:
# if the x value divided by 2 and the reminder is 0 that means it's a even number
    print ("this number is even")
if x % 2 != 0:
#if the x value divided by 2 and the reminder is not equal to 0 then this is an odd number
    print("this number is odd")