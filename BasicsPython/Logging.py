import logging
import os
import datetime


Location = r'D:\PythonProjects\Python_Learning_Youtube_2025\BasicsPython\Logging'
os.makedirs(Location, exist_ok=True)
FileGenDate = datetime.datetime.now().strftime("%d%b%y")
FileName = os.path.join(Location, f'Demo_log_{FileGenDate}.logs')

logging.basicConfig(
    level= logging.DEBUG,
    filemode='a',
    filename=FileName,
    format= '%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

def Addtion(a, b):
    logging.info(a+b)

Addtion(a= int(input("Enter a number: ")),
        b= int(input("Enter a number: ")))