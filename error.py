#Error Handling
while True:
    try:
        user_input = input("Enter a number:")
        number = int(user_input)
        print("You entered:", number)
        break # Exit loop if conversion succeeds
    except ValueError:
        print("Invalid input. Please enter a number.")
        