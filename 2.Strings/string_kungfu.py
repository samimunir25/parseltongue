# Print string in Vertical
'''convert string into vertical
'''
x = input("Write a word, and I will magicly turn into vertical: ")
for y in x:
    print(y)

print("\n")
# Slice string
x = input('Enter a few word sentence: ')
print("Original Text: ", x)
x = x[2:11]
print("Slicing the string: ", x)

print("\n")
# String Concatenation
x = input("Enter first string: ")
y = input("Enter second string: ")
print("First String: ", x)
print("Second String: ", y)
z = x + y
print("Concated String: ", z)

print("\n")
# String Comparison
x = input("Enter the name of your House: ")
x = x.lower()
Y = "Slytherin"

if x == Y:
    print("Your belong to the purest of houses")
else:
    print("Better be, Gryfindor")

print("\n")
# String Libraries
x = input("Enter a sentence in a mix of upper and lower case: ")
print("\n")
y = x.lower()
print("All in lower case:", y)
z = x.upper()
print("All in upper case:", z)

# Search and Replce
print("\n")
x = input("Write a sentence, and all the letter 'a' will be replaced by '=)': ")
y = x.replace('a', '=)')
print(y)

# Stripping Whitespace
print("\n")
x = input('Write a sentence with emtpy spaces in begining and in end: ')
print('Original Sentence: ', x)
x = x.strip()
print('After stripping whitespace: ', x)

# Prefixes
print("\n")
x = input("Boolean response, to the sentence if it starts with word 'Please': ")
y = x.startswith("Please")
print(y)

print("\n")
# Parsing and Extracting
print("Find the website domain from given string.\n")
DATA = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
print(DATA, "\n")
AA = DATA.find("@")
BB = DATA.find(' ', AA)
CC = DATA[AA+1 : BB]
print("Website domain is: ", CC)
