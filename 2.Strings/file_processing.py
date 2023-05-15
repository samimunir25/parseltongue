FILE_NAME = input("Enter name of file for processing: ")
XFILE = open(FILE_NAME)

LINE_COUNT = 0

for lines in XFILE:
    LINE_COUNT += 1

print("\n")
print(f'total number of lines in', FILE_NAME , 'is :', LINE_COUNT)