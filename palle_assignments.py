#assignment 1 - to read a number from keyboard and give the order of the days of the week

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

