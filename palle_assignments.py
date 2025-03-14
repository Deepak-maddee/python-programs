#assignment 1 - to read a number from keyboard and give the order of the days of the week
"""
_ = int(input("Enter a number to know the respective order of the days of the week in between 1-7: "))

if _ == 1:
    print("Monday")
elif _ == 2:
    print("Tuesday")
elif _ == 3:
    print("Wednesday")
elif _ == 4:
    print("Thursday")
elif _ == 5:
    print("Friday")
elif _ == 6:
    print("Saturday")
elif _ == 7:
    print("Sunday")
else:
    print("No week")


#assignment 2 - read any two numbers from input and choose the highest number

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if n1>n2:
    print(f"{n1} is greater than {n2}")
else:
    print(f"{n2} is greater than {n1}")


#assignment 3 - 5 multiple

n = int(input("enter a number: "))
if n % 5 == 0:
    print("Good")
else:
    print("Bad")


#assignment 4 - divisible by 2 and 5
n = int(input("enter a number: "))
if n % 2 == 0 and n % 5 == 0:
    print("divisible")
else:
    print("not divisible")


#assignment 4 - read weather from keyboard
w = int(input("Enter the temperature in Celcius: "))
if 0 < w <= 15 :
    print("today is very cold")
elif 15 < w <= 35 :
    print("today is simple weather")
elif 35 < w <= 45 :
    print("today is very hot")
else:
    print("Cannot live for this temperature")


# today's assignment -3 problems
#1st problem
n = 1
while n <= 100:
    print(n,end = " ")
    n += 2

#2nd problem
n = 100
while n >= 5:
    print(n)
    n -= 5
print()

#3rd problem
n = -100
while n <= -1:
    print(n)
    n += 1
print()

#4th problem
n=2
while n<=100:
    print(n," ")
    n+=2
print(n)

#print only the 5 divisibles from 1 to 100
for n in range(1,101):
    if n % 5 == 0:
        print(n, end = " ")

u = 1
while u <=100:
    if u%5==0:
        print(u,end = " ")
        u+=1
"""
#print only numbers which are divisible by 4 and 7 from 50 to 100
for n in range(50,101):
    if n % 4 == 0 and n % 7 == 0:
        print(n, end = " ")

u = 50
while u <= 100:
    if u % 4 == 0 and u % 7 == 0:
        print(u, eend = ' ')
        u += 1
