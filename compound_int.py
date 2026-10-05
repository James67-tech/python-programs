# Program that helps user claculate the Compound Interest. It does not accepts empty values.

principle = 0
while True:
  principle = float(input("Enter the principle amount: "))
  if principle <= 0:
    print("Principle amount cannot be less than or equal to zero. Please enter a valid amount.")
  else:
    break

time = 0
while True:
    time = float(input("Enter the time in years: "))
    if time <0:
        print("Time cannot be less than zero. Please enter a valid time.")
    else:
        break

rate = 0
while True:
    rate = float(input("Enter the rate of Interest: "))
    if rate < 0:
        print("Rate of Interest cannot be less than zero. Please enter a valid rate.")
    else:
        break
    
total = principle * pow((1 + rate / 100), time)
print(f"Total amount after {time} years is with rate of interest at {rate} is : {total:,.2f}")