
def printing():
    print("--"*30)

def login(username, password):
    printing()
    if username == "admin" and password == "1123":
        return "login success"
    else:
        return "login failed"


result = login("admin", "1123")
print(result)




# 1. Positional Arguments:
def testing(a, b, c):
    printing()
    print("Positional Arguments:")
    print(f"a: {a}, b: {b}, c: {c}")

a = 10
b= 20
c = 30
testing(a, b, c)
testing(b, c, a)


# 2. Keyword Arguments:
def testing1(a, b, c):
    printing()
    print("Keyword Arguments:")
    print(f"a: {a}, b: {b}, c: {c}")
a = 100
b = 200
c = 300
testing1(a=93204, b= 12453, c= 41412)


# 3. Default Arguments:
def testing3(a, b=10):
    printing()
    print("Default Arguments:")
    print(f"{a*b}")

a = 10
b = 5
testing3(a)
testing3(a,b)


# 4. Variable Arguments:
def testing4(*k):
    printing()
    for i in range(len(k)):
        if i == len(k) - 1:
            print(k[i], end=".")
        else:
            print(k[i], end=",")
    print()



testing4(1,2,3,4)
testing4(1,2)
testing4(23,123,124,124,42,4, "asfs",24,32,"2352iis", 65)






# def calculation():
#     while True:
#         num1  = int(input("Enter 1st number: "))
#         num2 = int(input("Enter 2nd number: "))
#         user_input = input("Select any option for the given options: "
#                            "\n1. Add"
#                            "\n2. Subtract"
#                            "\n3. Multiply"
#                            "\n4. Divide\n")[0]
#
#         if user_input == "1":
#             return num1 + num2
#         elif user_input == "2":
#             return num1 - num2
#         elif user_input == "3":
#             return num1 * num2
#         elif user_input == "4":
#             return num1 / num2
#         else:
#             var = input("Invalid input. Do you want to try again? YES or NO: ").lower()[0]
#             if var != "y":
#                 break
#
#
#
#
# result = calculation()
# print(result)