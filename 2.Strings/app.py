x = "Wingardium Laviosa"
z = "Lavitating Spell"

# Print string in Vertical
for y in x:
    print(y)
    
# Slice string
x = x[13:31]
print("Slicing the string: ", x)

# String Concatenation
w = x + ' is a ' + z
print(w)

print("\n")
# String Comparison
x = input("Enter the name of your House: ")
x = x.lower()
y = "Slytherin"

if x == y:
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

