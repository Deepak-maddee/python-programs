#2d list consisting of collections
np = ((1,2,3),
    (4,5,6),
    (7,8,9),
    ("*",0,"#"))

for row in np:
    for num in row:
        print(num,end = " ")
    print()
