import csv
import datetime
import os

def filling_data(Name, Age, Profession, Address, City, Zipcode):
    file_name = f"WithOpenCSV{datetime.date.today()}.csv"
    file_exists = os.path.exists(file_name)

    with open(file_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if not file_exists:
            writer.writerow(["Name","Age","Profession","Address","City","Zipcode"])

        writer.writerow([Name,Age,Profession,Address,City,Zipcode])

filling_data(
    Name=input("Enter your name: "),
    Age=input("Enter your age: "),
    Profession=input("Enter your profession: "),
    Address=input("Enter your address: "),
    City=input("Enter your city: "),
    Zipcode=input("Enter your zipcode: "),
)
