menu = {"popcorn" : 150,
    "soda" : 100,
    "samosa" : 50,
    "chips" : 60,
    "burgers" : 75,
    "pizza" : 100}

cart = []
total = 0

print("----------MENU----------")
for key,value in menu.items():
    print(f"{key:10} : ${value:.2f}")

print("------------------------")

while True:
    food = input("Enter the item you wish to buy and eat: ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)


for food in cart:
    total+=menu.get(food)
    print(food,end = " ")

print()
print("----------YOUR ORDER----------")
print(f"Total is: {total:.2f}")
