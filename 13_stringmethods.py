# strings are immutable. they cannot be changed or converted. 
# strings can be modified and a new string is obtained by applying operations but they do not change the existing string or convert it.

str1="!!!hey , I AM VERnnit !!?!"
print(str1.upper())
print(str1.lower()) #new string.


# strip removes white spaces before and after the string.
# rstrip removes the trailing characters but not the leading ones.

print(str1.strip())     #if char is specified then there shouldn't be any spaces to remove leading or trailing.
print(str1.rstrip("!")) #trailing characters only and if char is specified there shouldn't be trailing space or anything.

# replace replaces all occurrences of string with a new one.
print(str1.replace("!", "$"))

# split method splits the string at specified instance and returns the string as a list.
print(str1.split())



# The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

str2="hey , I AM am am tHe Only One"
print(str2.capitalize()) 


# The center() method aligns the string to the center as per the parameters given by the user.also you can assign a character to fill the spaces.  value given - the length = spaces given total before and after the string. i.e here total of 27 spaces will be given adding before and after.
print(str2.center(50,"."))


# count method counts the number of times a value has occurred.
print(str2.count("am"))


# The startswith() method checks if the string starts with a given value. If yes then return True, else return False.
# The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
print(str2.endswith("One"))

# We can even also check for a value in-between the string by providing start and end index positions.

print(str2.endswith("AM", 7 , 9))
print(str2.endswith("AM", 7 , 10))

# The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

# The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

print(str2.index("am"))
# print(str2.index("on")) #gives value error


# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

# The isalpha() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.


# The islower()/isupper() method returns True if all the characters in the string are lower/upper case, else it returns False.

# The isspace() method returns True only and only if the string contains white spaces, else returns False.

# The istitle() returns True only if the first letter of each word of the string is capitalized, else it returns False.



# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
str3="hey THERE i Am vernNit \n"
print(str3.isprintable()) #returns false

# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

print(str3.swapcase())

# The title() method capitalizes first letter of each word within the string  and  rest to small letters.

print(str3.title())
