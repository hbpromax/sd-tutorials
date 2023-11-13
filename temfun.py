import datetime

def celsius_to_fahrenheit(celsius):
    fahrenhiet = (celsius * 9/5) + 32
    return fahrenhiet

def fahrenhiet_to_celsius(fahrenhiet):
    celsius = (fahrenhiet - 32) * 5/9
    return celsius

current_date = datetime.datetime.now().date()
current_time = datetime.datetime.now().time()

try:
    def main():
        while True:
            print( """ ....Hello Welcome to the temperature convering software....

                  ...Please press 1 or 2 or 3 to continue...
                  
                        1. Celsius to Fahrenhiet.
                        2. Fahrenheit to Celsius.
                        3. Exit.
                """)
            choise = int(input("Enter your choice (1/2/3) : "))

            if choise == 1 :
                celsius = float(input("Enter the temperature in celcius : "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(str(celsius)+ " C" + " " + "is equal to " + ": " + str(fahrenheit) + " F" )
                print("Date : ", current_date)
                print("Time : ", current_time)
                break

            elif choise == 2:
                fahrenheit = float(input("Enter the temperature in fahrenheit : "))
                celsius = fahrenhiet_to_celsius(fahrenheit)
                print(str(fahrenheit)+ " F" + " " + "is equal to " + ": " + str(celsius) + " C" )
                print("Date : ", current_date)
                print("Time : ", current_time)
                break

            elif choise == 3:
                print("Come again")
                print("Date is : ", current_date)
                print("Time is : ", current_time)
                break

            else:
                print("Please enter 1 or 2 or 3")
    main()

except ValueError as e :
     print("Error")
                         


