
print("Welcome to the program: 'Identify the smallest and largset number in the given range'\n")
my_list = (input("Enter numbers seperated by blank spaces, and then hit enter: "))

# Process the input, split the list of strings, and then convert the elements into integer

my_list = my_list.split()
my_list = list(map(int, my_list))
print(my_list)
print("\n")

SMALLEST_NUMBER = None
LARGEST_NUMBER = None

# Definite loop nested with conditional statements

for item in my_list:
    if SMALLEST_NUMBER is None:
        SMALLEST_NUMBER = item
    elif item < SMALLEST_NUMBER:
        SMALLEST_NUMBER = item
          
for item in my_list:
    if LARGEST_NUMBER is None:
        LARGEST_NUMBER = item
    elif item > LARGEST_NUMBER:
        LARGEST_NUMBER = item

# Print results

print("Smallest number is: ", SMALLEST_NUMBER)

print("Largest number is: ", LARGEST_NUMBER)