print("Welcome to the program for calculating sum of the numbers in user provided list.\n")
x = (input("Enter the number for addition: "))
x = x.split()
print("\n")
print("Your List is =", x)
print("\n")

COUNT = 0
TOTAL_SUM = 0

for item in x:
    COUNT = COUNT + 1
    TOTAL_SUM = TOTAL_SUM + int(item)

print("Total sum of provided numbers in list is:",TOTAL_SUM)
print("Average of the provided numbers in list is:", TOTAL_SUM / COUNT )
