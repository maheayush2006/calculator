print("CALCULATOR")
print("Enter first number")
a = int(input())
print("Enter second number")
b = int(input())
print("Which tast do you want to perform?")
print("add!\nsubtraction!\nmultiplication!\ndivision!\nremainder!")
c = input()
if c == "add":
    print(a + b)
elif c == "subtraction":
    if a > b:
        print(a - b)
    elif b > a:
        print(b - a)
    elif a == b:
        print("0")
elif c == "multiplication":
    print(a * b)
elif c == "division":
    print(a/b)
elif c == "remainder":
    print(a%b)
else:
    print("invalid instruction!!!!!123")