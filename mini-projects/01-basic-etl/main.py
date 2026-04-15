# to avoid file not found issue
import os
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "orders.csv")

# ETL code
import csv

data = []

with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["amount"] = int(row["amount"])
        data.append(row)

# simple transform
total = sum(row["amount"] for row in data)
print("Total sales:", total)
