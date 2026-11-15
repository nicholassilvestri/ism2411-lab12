# ISM2411 Lab 12- Read a Sales CSV, Write a Cleaned Report
# Name: Nicholas Silvestri
#
# Reflection 1:
# Python makes it easier to automate tasks that would otherwise be tedious and time-consuming, calculate totals, and clean data. Excel is useful for visually viewing data, creating charts, and making quick changes manually.
#
# Reflection 2:
# A business could use an append-mode log to record every customer order. Append mode is useful because it preserves previous entries and adds new records without deleting existing logs.

import csv
from datetime import datetime

#---Exercise 1: Setup---
filename="data/sales.csv"

#---Exercise 2: Read and print raw rows---
with open(filename, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#---Exercise 3: Skip the header---

with open(filename, "r", newline="") as file:
    reader= csv.reader(file)

    header=next(reader)
    print("Header:", header)

    for row in reader:
        print(row)

#---Exercise 4: Compute totals---

total_revenue=0
original_count=0

with open(filename, "r", newline="") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        product=row[0]
        price=float(row[1])
        quantity=int(row[2])

        total=price*quantity
        total_revenue+=total
        original_count+=1

        print(
            f"{product}: {quantity} units"
            f"* ${price:.2f} = ${total:.2f}"
        )
print(f"Total Revenue: ${total_revenue:.2f}")

#---Exercise 5: Filter and write---
written_count=0

with open(filename, "r", newline="") as infile:
    reader=csv.reader(infile)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer=csv.writer(outfile)
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            product=row[0]
            price=float(row[1])
            quantity=int(row[2])

            total=price*quantity

            if total>100:
                writer.writerow([product, price, quantity, f"{total:.2f}"])
                written_count+=1
print(f"Original rows: {original_count}, Written rows: {written_count}")

#---Exercise 6: DictReader---

dict_total=0

with open(filename, "r", newline="") as file:
    reader=csv.DictReader(file)
    for row in reader:
        product=row["product"]
        price=float(row["price"])
        quantity=int(row["quantity"])

        total=price*quantity
        dict_total+=total

        print(f"{product}: ${total:.2f}")
print(f"DictReader Total Revenue: ${dict_total:.2f}")

# csv.reader uses column indexes while DictReader uses column names.
# reader is useful for simple CSV files, while DictReader is easier to understand when working with named columns.

#---Exercise 7: Sales summary by product---

summary={}

with open(filename, "r", newline="") as file:
    reader=csv.DictReader(file)
    for row in reader:
        product=row["product"]
        price=float(row["price"])
        quantity=int(row["quantity"])

        total=price*quantity

        if product in summary:
            summary[product]+=total
        else:
            summary[product]=total
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

#---Exercise 8: Append Mode Log---

timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as logfile:
    logfile.write(f"{timestamp} - Total Revenue: ${total_revenue:.2f}\n")

print("Run log updated successfully.")