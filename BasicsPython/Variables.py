# Variables = Name of the memory location which is used to hold the values/objects
# Datatype = Specifies the type of data that a variable can hold
# Identifier = A name of a programing element is technically called as Identifier
import keyword
from keyword import iskeyword

variable = 10
print(variable)
print(type(variable))
print(id(variable))
print("--"*30)

variable = 102.4252
print(variable)
print(type(variable))
print(id(variable))
print("--"*30)

variable = "Vamshi"
print(variable)
print(type(variable))
print(id(variable))
print("--"*30)

variable = [10,2,4,2,5]
print(variable)
print(type(variable))
print(id(variable))
print("--"*30)

variable = (2,2,246,46,3,25)
print(variable)
print(type(variable))
print(id(variable))
print("--"*30)

variable = {1,2,3,4,5,1,1,2,4}
print(variable)
print(type(variable))
print(id(variable))
print("--"*30)

variable = {"Key1": "Value1",
            "Key2": "Value2",
            "Key3": "Value3",}
print(variable)
print(type(variable))
print(id(variable))
print("--"*30)

keyword_list = keyword.kwlist
print(keyword_list)
print(keyword.iskeyword("None"))
print(keyword.iskeyword("12"))

# Start with a letter or underscore
# Use only letters, numbers, underscores
# No numbers at the beginning
# No spaces
# Case-sensitive = A programming language is case-sensitive if it treats uppercase and lowercase letters as different.
# No keywords
# Use meaningful names