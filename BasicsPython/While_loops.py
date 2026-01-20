
user_input = int(input("Enter a number: "))
i = 1

while i <= 20:
    print(user_input, "*", i, "=", user_input*i)
    i += 1
    if i > 10:
        break

print("--"*60)
city = input("Enter a city: ")
x = 0
while x < len(city):
    print(city[x])
    x += 1


while True:
    name = input("Enter a name: ")
    age = int(input("Enter a age: "))

    if age >= 18:
        print("You are old enough to vote!")
    else:
        print("You are old enough to vote!")

    choice = input("Enter a choice (YES or NO): ")
    if choice.lower()[0] != "y":
        print("Thanks for using my program!!!")
        break