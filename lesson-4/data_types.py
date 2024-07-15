import math 
# String data type

# Literal assignment
first = 'Dave'
last = 'Gray'
print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# Constructor function
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concatenation
fullname = first + ' ' + last
print(fullname)
fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = """
Hey, how are you?                    

I was just checking in.        
                          All good?

"""
print(multiline)

# Escaping special characters
# \t is a tab
# \n is a new line
#\' helps with the apostrophe
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title()) # Prints a capital for each word
print(multiline.replace("good", "ok")) # Replaces a word
print(multiline)

print(len(multiline)) # See the length of multiline - each character
multiline += "                                 " # Adding to the end
multiline = "                                     " + multiline # Adding space to the beginning
print(len(multiline)) # See characters after adding to multiline
print(len(multiline.strip())) # Removes white space - prints the output unless you put it inside len()
print(len(multiline.lstrip())) # Removes white space left side
print(len(multiline.rstrip())) # Removes white space right side
print("")


# Build a menu
title = "menu".upper()
print(title.center(20, "=")) # center menu word and use the 20 for characters to fill out the rest of the space
print("Coffee".ljust(16, ".") + "$1".rjust(4)) #ljust() = left justify. rjust() = right justify. numbers = characters in length
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))
print("")

# String index values
print(first[1]) # Prints the string index from first name = returns 'a' as expected
print(first[-1]) # Prints the string index from first name = returns 'e' as expected
print(first[1:-1])
print(first[1:]) # Prints the string index from first name = start at first, end at last

#Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

#Numeric data types
#integer
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(gpa, float))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag) # imaginary number value

# built-in functions for numbers
print(abs(gpa)) # absolute value
print(abs(gpa * -1))
print(round(gpa)) # rounds to nearest integer
print(round(gpa, 1)) # rounds to nearest decimal place which is specified

print(math.pi)
print(math.sqrt(64)) # square root
print(math.ceil(gpa)) # ceiling of gpa value
print(math.floor(gpa)) # floor of gpa value

# casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

#Error if you attempt to cast incorrect data
# zip_value = int("New York") # "invalid literal"