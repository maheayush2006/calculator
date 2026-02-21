numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))

operation = input("Choose operation (+, -, *, /): ")

result = numbers[0]

for num in numbers[1:]:
    if operation == "+":
        result += num
    elif operation == "-":
        result -= num
    elif operation == "*":
        result *= num
    elif operation == "/":
        if num == 0:
            print("Error: Division by zero")
            exit()
        result /= num
    else:
        print("Invalid operation")
        exit()

print("Result:", result)