number= int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
operation = input("Enter an operation (+, -, *, /): ")
if operation == "+":
    result = number + number2
elif operation == "-":
    result = number - number2
elif operation == "*":
    result = number * number2
elif operation == "/":
    result = number / number2
else:
    print("Invalid operation")
    result = None
if result is not None:
    print(f"The result of {number} {operation} {number2} is: {result}")