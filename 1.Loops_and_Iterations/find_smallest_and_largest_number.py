
print("Welcome to the program: 'Identify the smallest and largset number in the given range'\n")
my_list = (input("Enter numbers seperated by blank spaces, and then hit enter: "))

my_list = my_list.split()
my_list = list(map(int, my_list))
print(my_list)
print("\n")

smallest_number = None
largest_number = None

for item in my_list:
    if smallest_number is None:
        smallest_number = item
    elif item < smallest_number:
        smallest_number = item
        
for item in my_list:
    if largest_number is None:
        largest_number = item
    elif item > largest_number:
        largest_number = item


print("Smallest number is: ", smallest_number)
print("Largest number is: ", largest_number)  