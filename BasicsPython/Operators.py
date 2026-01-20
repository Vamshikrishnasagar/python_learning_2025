# Operator = A special symbol that tells the interpreter to perform an operation on operands
# Arithmetic → + - * / % ** //
# Assignment → = += -= *= /= %= **= //=
# Comparison → == != > < >= <=
# Logical → and or not
# Bitwise → & | ^ ~ << >>
# Membership → in, not in
# Identity → is, is not


a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)   # 3.3333 → Division
print(a % b)   # 1   → Modulus (remainder)
print(a ** b)  # 1000 → Exponentiation (10^3)
print(a // b)  # 3   → Floor Division


print("--"*40)
x = 5     # Assignment
x += 3    # x = x + 3 → 8
x -= 2    # x = x - 2 → 6
x *= 2    # x = x * 2 → 12
x /= 3    # x = x / 3 → 4.0
x %= 3    # x = x % 3 → 1.0
x **= 2   # x = x ** 2 → 1.0
x //= 1   # x = x // 1 → 1.0
print(x)
print("--"*40)


a = 10
b = 20
print(a == b)  # False → equal to
print(a != b)  # True  → not equal to
print(a > b)   # False → greater than
print(a < b)   # True  → less than
print(a >= 10) # True  → greater than or equal to
print(b <= 20) # True  → less than or equal to
print("--"*40)

x = True
y = False
print(x and y)  # False → both must be True
print(x or y)   # True  → at least one True
print(not x)    # False → reverse the value
print(not y)
print("--"*40)

a = 5  # 0101 in binary
b = 3  # 0011 in binary

print(a & b)   # 1 → 0101 & 0011 = 0001
print(a | b)   # 7 → 0101 | 0011 = 0111
print(a ^ b)   # 6 → 0101 ^ 0011 = 0110
print(~a)      # -6 → bitwise NOT (two's complement)
print(a << 1)  # 10 → left shift
print(a >> 1)  # 2  → right shift
print("--"*40)


fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)
print("mango" not in fruits)
print("--"*40)

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is b)     # False → different objects in memory
print(a is c)     # True  → same object
print(a is not b) # True  → different objects


