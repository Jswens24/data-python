from doctest import OutputChecker


open_file = open("CupcakeInvoices.csv")

# for line in open_file:
#     print(line)

# for line in open_file:
#     line = line.strip()
#     values = line.split(",")
#     print(values[2])

# for line in open_file:
#     line = line.strip()
#     values = line.split(",")
#     total_price = int(values[3]) + float(values[4])
#     print(total_price)

total = 0

for line in open_file:
    line = line.strip()
    values = line.split(",")
    total = int(values[3]) + float(values[4]) + total
    
print(total)

open_file.close()

