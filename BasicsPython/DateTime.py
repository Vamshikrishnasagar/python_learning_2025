import datetime

current_date = datetime.datetime.today().date()
print(current_date)
print(type(current_date))
current_time = datetime.datetime.today().time()
print(current_time)
curren_tt = datetime.datetime.today().now()
print(curren_tt)

formating = current_date.strftime("%y_%b_%d")
print(formating)
print(type(formating))