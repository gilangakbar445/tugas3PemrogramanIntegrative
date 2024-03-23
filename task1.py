total = 0

with open('indata.txt', 'r') as file:
    for baris in file:
        total += int(baris)

print("{:,.2f}".format(total))