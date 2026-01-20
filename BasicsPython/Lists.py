"""
List: A list is a collection of different data types stored in a single variable.
Mutable – Data can be changed (insert, update, delete).
Accepts duplicate values and maintains order.
"""

ls = [23, 43, 3252.532, "Sagar", "krishna", None, True, False, (34+55j), "krishna", "Sagar", "krishna"]
print(ls)
print(type(ls))
print(len(ls))
ls[3] = "Reddy"
print(ls)
print(ls[2:7])
ls.insert(3, "Good")
print(ls)


rev_list = []
for item in ls:
    rev_list.insert(0, item)


item_to_remove = "krishna"
new_list = []
for item in rev_list:
    if item != item_to_remove:
        new_list.append(item)

new_list.clear()
print(new_list)

new_list = [190.2, 124.21, 232, "tcs", "infos"]
print(new_list)

clean_list = new_list.copy()
print(clean_list)
new_list.insert(2, "CAT")
print(new_list)
print("clean_list:", clean_list)