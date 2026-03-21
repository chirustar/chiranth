import csv
import os

FILE_NAME = "employees.csv"

def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["id", "name", "age", "department"])

def read_data():
    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def write_data(data):
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "age", "department"])
        writer.writeheader()
        writer.writerows(data)

def append_data(emp):
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([emp['id'], emp['name'], emp['age'], emp['department']])