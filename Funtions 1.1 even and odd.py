#a program to print the odd and even numbers by the function method
def odd_or_even(x):  #first we define our method
    if (x % 2 == 0): #second we find the moda for even numbers by 0 as a reminder
        print ("this is even") #use if condition to print the even numbers
    else: #anyvalue wouldn't return a 0 as reminder will be an even number
        print ("this is odd") #print the number is even 
odd_or_even(5)