#total = 0
#for i in range(5):
#    print(i)
#    total = total + i
#print("total is : ",total)





#for i in range(1,20,2):
#    print(i)



#try:
#    stars = int(input("Enter the number of stars you want : "))
#    for i in range(stars):
#        print("*" , end = " ")
#except ValueError as e :
#    print("Please use integer values")





#import random

#double = 0

#for i in range (100):
#    dies_1 = random.randint(1,6)
#    dies_2 = random.randint(1,6)
#    print(dies_1 , end= " ")
#    print(dies_2 , end= " ")
#    print()

 #   if dies_1 == dies_2:
 #       double += 1
#print(f"Out of 100 you rolled {double} doubles.")





import random
number = random.randint(1,20)
attemps_allows = 5
user_attemps = 0

try:
    while user_attemps < attemps_allows:
        guess = int(input("Enter the number between 1 to 20 : "))

        if guess > 20 or guess < 1 :
            print("Please enter number between 1 to 20")

        elif guess == number:
            print("number : " , number)
            print("Guess number : " , guess)
            print("Congratulations you guessed the correct number")
            break
        else:
            if guess < number:
                print("Try a higher number")
            else:
                print("Try a lower number")

            user_attemps += 1
        if user_attemps == attemps_allows:
            print("You have reached maximum attempts . Please try again later")
except ValueError as e :
    print("Error")