print("Welcome to the program for calculating sum of the numbers in user provided list.\n")
x = (input("Enter the number for addition: "))
x = x.split()
print("\n")
print("Your List is =", x)
print("\n")

count = 0
total_sum = 0

for item in x:
    count = count + 1
    total_sum = total_sum + int(item)

print("Total sum of provided numbers in list is:",total_sum)
print("Average of the provided numbers in list is:", total_sum / count )