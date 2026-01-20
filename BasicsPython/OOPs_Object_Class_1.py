class Employee:
    def __init__(self, name, empid, project, location, package):
        self.emp_name = name
        self.emp_id = empid
        self.project = project
        self.location = location
        self.package = package

    def greeting(self):
        print(" Welcome to TCS ".center(60, "-"))
        result = (f"Hi {self.emp_name}!\nPlease find your details below:\n"
                  f"Emp_Id: {self.emp_id}\n"
                  f"Project: {self.project}\n"
                  f"Location: {self.location}\n"
                  f"Package: {self.package}\n")

        return result

emp1 = Employee("Sagar", "215621", "CyberSecurity", "Hyderabad", 23)
print(emp1.greeting())

# emp2 = Employee(
#     input("Enter Employee Name: "),
#     input("Enter Employee ID: "),
#     input("Enter Project Name: "),
#     input("Enter Location: "),
#     input("Enter Package: "),
# )
# print(emp2.greeting())




# -------------------------------------------------------------------
class APICallCounter:
    def __init__(self, count=0):
        self.count = count

    def hit(self):
        self.count += 1
        return self.count
api_counter = APICallCounter()

api_counter.hit()
api_counter.hit()
api_counter.hit()
api_counter.hit()
print(api_counter.count)   # 4


# -------------------------------------------------------------------
def calling():
    api_called = 0

    def api_call():
        nonlocal api_called
        api_called += 1
        return api_called

    return api_call

f = calling()
f()
f()
f()
print(f())