"""
A dictionary in Python is an unordered collection of key-value pairs.
Keys are unique.
Values can be anything (duplicate values are allowed).
Dictionaries are mutable → you can change, add, or remove items.
Think of it like a real-life dictionary: you look up a word (key) and get its meaning (value).
"""

student = {
    "Name": "Sagar",
    "Age": 25,
    "Subjects": ["Telugu", "Hindi", "English", "Maths", "Science"],
    "Passed": True,
    25: 450
}
for i, j in student.items():
    if i == "Subjects":
        print(j)
        continue
    print(f"{i}: {j}")

print(student["Subjects"][4])
print(student.get("Subjects", []))
print(type(student["Subjects"]))
print(type(student["Name"]))
student["Add"] = False
print(student)
student.pop("Subjects")
print(student)
print(student.keys())
print(student.values())
print(student.items())
student.clear()
print(student)

