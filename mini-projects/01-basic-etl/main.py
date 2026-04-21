# to avoid file not found issue
# import os
# base_path = os.path.dirname(__file__)
# file_path = os.path.join(base_path, "orders.csv")

# ETL code
import csv

data = []

# CSV = rows of text
with open("./mini-projects/01-basic-etl/orders.csv", "r") as file:
    reader = csv.DictReader(file) # DictReader -> turns CSV rows into Python dictionaries using headers as keys
    for row in reader:
        row["amount"] = int(row["amount"])
        data.append(row)

print(data)

# simple transform
total = sum(row["amount"] for row in data)
print("Total sales:", total)
