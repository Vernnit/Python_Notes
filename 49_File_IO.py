# Python provides several ways to manipulate files. Today, we will discuss how to handle files in Python.

# Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.
try: 
    open("vernnit.txt", "x")
except FileExistsError:
    pass

# f=open('vernnit.txt' , 'w')
# z='hello world'
# b = f.write(z)
# print(b)
# f.close()

f=open('vernnit.txt' ,'a' )
b=f.write('Happy Holi')
print(b)
f.close()

f = open("vernnit.txt" , "rt") #t is text and it is default
a=f.read()
print(a) 
f.close()


# You need not to close a file if you use with statement

with open("vernnit.txt" , "a") as f:
    f.write("hey i am inside with")
    
    
#     There are various modes in which we can open files.

# read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter. r+ for both reading and writing.

# write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

# create (x): This mode creates a file and gives an error if the file already exists.

# text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

# binary (b): used to handle binary files (images, pdf(s), etc).