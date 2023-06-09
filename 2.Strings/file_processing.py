'''File processing code
'''
# # Find number of lines in file
FILE_NAME = input("Enter name of file for counting number of lines: ")
try:
    XFILE = open(FILE_NAME)
except:
    print(f'file {FILE_NAME} cannot be found')
    quit()

LINE_COUNT = 0

for lines in XFILE:
    LINE_COUNT += 1

print("\n")
print(f'total number of lines in {FILE_NAME} is {LINE_COUNT}')

# Reading the *whole* file
print("\n")
FILE_NAME = input("Enter name of file for counting total number of characters: ")
try:
    OPEN_FILE = open(FILE_NAME)
except:
    print(f'file {FILE_NAME} cannot be found')
    quit()

READ_FILE = OPEN_FILE.read()
TOTAL_CHAR = len(READ_FILE)
print("\n")
print(f'Total number of characters in {FILE_NAME} is {TOTAL_CHAR}')

# Searching through file
print("\n")
FILE_NAME = input("Enter name of file for searching special lines: ")
try:
    OPEN_FILE = open(FILE_NAME)
except:
    print(f'file {FILE_NAME} cannot be found')
    quit()

for LINE in OPEN_FILE:
    LINE = LINE.rstrip()
    if LINE.startswith('From'):
        print(LINE)

