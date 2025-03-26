principle = 0
rate = 0
time = 0
while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle amount should be greater than 0")

while rate <= 0:
    rate = float(input("Enter the rate: "))
    if rate <= 0:
        print("Rate should be greater than 0")

while time <= 0:
    time = float(input("Enter the time: "))
    if time <= 0:
        print("Time should be greater than 0")

ci = principle * (pow((1+rate/100), time))
print("Compound interest is: ", ci)

    
