import csv
import os
import datetime

Main_Folder_Location = r'D:\PythonProjects\Python_Learning_Youtube_2025\BasicsPython\CsvData'
os.makedirs(Main_Folder_Location, exist_ok=True)

Sub_Folder_Location = os.path.join(Main_Folder_Location, 'Sub_Folder')
os.makedirs(Sub_Folder_Location, exist_ok=True)

FileGenData = datetime.datetime.now().strftime("%Y%m%d")
FileName = os.path.join(Sub_Folder_Location, f'FirstCSVFile{FileGenData}.csv')


Headers = ['Date', 'Time', 'EmployeeID', 'EmployeeName']

# Check if file already exists
file_exists = os.path.isfile(FileName)

with open(FileName, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write header only if file is new
    if not file_exists:
        writer.writerow(Headers)

    writer.writerow([
        datetime.date.today(),
        datetime.datetime.now(),
        '278454',
        'Vamshi'
    ])
