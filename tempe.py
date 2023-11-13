import datetime
date = datetime.datetime.now().date()
time = datetime.datetime.now().time()
try:
    choice = int(input( """
    Welcome to temperature converter
    pick a number,
            1. Press 1 to convert celsius to fahrenheit(C ---> F).
            2. Press 2 to convert fahrenhiet to celsius(F ---> C).
            3. Press 3 to Exit.
    :  """)
    )

       
    while True:

        if choice == 1:
            celsius = float(input("Enter the value celsius : "))
            conversion_1 = celsius*9/5 + 32 
            print(str(celsius) + " " + "C" + " " + "The conversion of the celsius in fahrenhiet is : ", str(conversion_1),"F" )
            print("Date : ",date)
            print("Time : ",time)
            break

        elif choice == 2:
            fahrenhiet = float(input("Enter the value fahrenhiet : "))
            conversion_2 = fahrenhiet - 32 *5/9
            print(str(fahrenhiet) + " " + "F" + " " + "The conversion of the fahrenhiet in celsius : " , str(conversion_2),"C")
            print("Date : ",date)
            print("Time : ",time)
            break
        elif choice == 3:
            print("Come again...")
            break

        else:
            print("Please choose the numbers 1 or 2 for the conversion //or 3 for exit.")
            break
            
except ValueError as e :
    print("Please choose between (1/2/3) ")
    print("Date : ",date)
    print("Time : ",time)