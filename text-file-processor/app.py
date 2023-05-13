intro = "This program find if there is \"World\" mentioned in the provided text file"
print(intro)
proceed = "Type \'YES\' to proceed: "
user_input = input(proceed)

user_input = user_input.upper()

if user_input == "YES":
    xfile = input("Enter file name with extension: ")
    try:
        xfile = open(xfile)
    except:
        print("File cannot be opened:", xfile)
        quit()

    for x in xfile:
        x = x.rstrip()
        if "World!" in x:
            print(x)