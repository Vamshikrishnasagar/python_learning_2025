"""String: Group of text,
Immutable:- Data can't be changed
Ordered Values and Accepts Duplicates"""

name = "sandolla vamshikrishna sagar  "
print(name)
print(type(name))
print(f"length: {len(name)}")
print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.title())
print(name.endswith("sagar"))
print(name.startswith("sandolla"))
print(name.find("r"))
print(name.center(50,"-"))
print(name.count("a", 10, 24))
print(name.replace("sagar", "vamshikrishna"))
print(name.split("vamshikrishna"))

namee = "     ;.;..;;;4551sandolla vamshikrishna sagar  "
cleaned = namee.strip()
print(cleaned)
cleaned = namee.strip(" ;./4551")
print(cleaned)
print(name[2])
print(name[10:20])
print(name[10:20:2])
print(name[::-1])

print(name)
revers_str = ""
for ch in name:
    revers_str = ch + revers_str
print(revers_str)


# x = 100
# print(f"x = {x}")
# print(type(x))
# x = str(x)
# print(x)
# print(type(x))

