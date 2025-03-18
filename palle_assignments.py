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

#print only numbers which are divisible by 4 and 7 from 50 to 100
u = 50
while u <= 100:
    if u % 4 == 0 and u % 7 == 0:
        print(u, end = ' ')
    u += 1
print()

for n in range(50,101):
    if n % 4 == 0 and n % 7 == 0:
        print(n, end = " ")

l = [10,20,31,41,50,61,71,80,91,100]
i = 0
while i < len(l):
    print(l[i], end = " ")
    i+=1

# Declare a tuple from 10 to 21 (inclusive)
my_tuple = tuple(range(10, 22))

# Print odd and even elements
even_elements = tuple(x for x in my_tuple if x % 2 == 0)
odd_elements = tuple(x for x in my_tuple if x % 2 != 0)

print("Even elements:", even_elements)
print("Odd elements:", odd_elements)

# Print odd and even index elements
even_index_elements = tuple(my_tuple[i] for i in range(len(my_tuple)) if i % 2 == 0)
odd_index_elements = tuple(my_tuple[i] for i in range(len(my_tuple)) if i % 2 != 0)

print("Even index elements:", even_index_elements)
print("Odd index elements:", odd_index_elements)

# Print count of even and odd elements
even_count = len(even_elements)
odd_count = len(odd_elements)

print("Count of even elements:", even_count)
print("Count of odd elements:", odd_count)

# Print sum of even and odd elements
even_sum = sum(even_elements)
odd_sum = sum(odd_elements)

print("Sum of even elements:", even_sum)
print("Sum of odd elements:", odd_sum)

# Print even index odd elements and odd index even elements
even_index_odd_elements = tuple(my_tuple[i] for i in range(len(my_tuple)) if i % 2 == 0 and my_tuple[i] % 2 != 0)
odd_index_even_elements = tuple(my_tuple[i] for i in range(len(my_tuple)) if i % 2 != 0 and my_tuple[i] % 2 == 0)

print("Even index odd elements:", even_index_odd_elements)
print("Odd index even elements:", odd_index_even_elements)

# Print sum of odd index even elements and count of even index odd elements
sum_odd_index_even = sum(odd_index_even_elements)
count_even_index_odd = len(even_index_odd_elements)

print("Sum of odd index even elements:", sum_odd_index_even)
print("Count of even index odd elements:", count_even_index_odd)



institute = "Palle Technologies"

# Print only vowels
vowels = "aeiouAEIOU"
vowel_chars = ""
for char in institute:
    if char in vowels:
        vowel_chars += char
print("Vowels:", vowel_chars)

# Print only consonants
consonant_chars = ""
for char in institute:
    if char.isalpha() and char not in vowels:
        consonant_chars += char
print("Consonants:", consonant_chars)

# Print all characters in reverse using while loop
reversed_chars = ""
index = len(institute) - 1
while index >= 0:
    reversed_chars += institute[index]
    index -= 1
print("Reversed:", reversed_chars)

# Print character if it is 'l' else print '@'
modified_chars = ""
for char in institute:
    if char == 'l' or char == 'L':
        modified_chars += char
    else:
        modified_chars += '@'
print("Modified:", modified_chars)

"""

elements = [10,11,12,13,15,14,16,18,17,19,20]
for x in elements :
    print(x,end=" ")
    x=x+1

