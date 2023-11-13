import datetime

def calculate_tip (cost):
   tip = cost * 10/100
   return tip

def calculate_final_bill (tip , cost):
  final_bill = tip + cost
  return final_bill

def get_date_and_time():
   current_date = datetime.datetime.now().date()
   current_time = datetime.datetime.now().time()
   return current_date , current_time

try:
    def main():
     while True:
        current_date , current_time = get_date_and_time()
        cost = float(input("Enter the cost : "))
        tip = calculate_tip(cost)

        final_bill =  calculate_final_bill(tip , cost)
        print("Final bill is : " , final_bill)
        print("Date : " , current_date)
        print("Time : " , current_time)
        print("Thank you come again....")
        break
    main()

except ValueError as e :
   print("error")