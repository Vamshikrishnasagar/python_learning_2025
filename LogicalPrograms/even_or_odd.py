while True:
    user_number = int(input("Enter a number: "))

    if user_number <= 0:
        print("Invalid input! Enter a valid number: ")
    else:
        if user_number % 2 == 0:
            print(f"{user_number} is an even number!")
        else:
            print(f"{user_number} is an odd number!")
        break


# Using Ternary Operator
num = int(input("Enter a valid number other than zero: "))
result = (
    "Invalid number"
    if num < 0
    else f"{num} is an even number"
    if num % 2 == 0
    else f"{num} is an odd number"
)

print(result)