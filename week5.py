#total = 0
#for i in range(5):
#    print(i)
#    total = total + i
#print("total is : ",total)



#for i in range(1,20,2):
#    print(i)



#number = 10
#while (number > 0):
#    print(number)
#    number = number - 1



#import random

#guesses_taken = 0

#hidden = random.randint(1,20)

#guesses_taken = int(input("Enter your guess : "))
#while True:
#    if guesses_taken < 5:




#s = "python rocks"
#for ch in s:
#    print("hello")


def factorial(n):
    if n == 0:
        return 1
    return n* factorial(n-1)
try:
    while True:
        user_input = input("Enter the value : ")
        n = int(user_input)
        print ("Factorial is : ", factorial(n))
    
except ValueError as e:
    print("Error")