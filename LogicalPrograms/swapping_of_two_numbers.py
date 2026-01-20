a = 10
b = 20

print(f"Method: 01\nBefore Swapping: a={a}; b={b}")
a, b = b, a
print(f"After Swapping:  a={a}; b={b}\n-----------------------------------------------------")


a = 10
b = 20
print(f"Method: 02\nBefore Swapping: a={a}; b={b}")
temp = a
a = b
b = temp

print(f"After Swapping:  a={a}; b={b}\n-----------------------------------------------------")



a = 10
b = 20
print(f"Method: 03\nBefore Swapping: a={a}; b={b}")
a = a + b
b = a - b
a = a - b

print(f"After Swapping:  a={a}; b={b}\n-----------------------------------------------------")

