# The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.

# The readlines() method reads all the lines of the file and returns them as a LIST OF STRINGS.
f=open("fileIO.txt" , "r")
a=f.readline()
b=f.readlines()     #returns a list of strings of each line.
print(a)
print(b)
f.close()

with open("fileIO.txt" ,"r" ) as f:
    i=0
    while True:
        i=i+1
        a=f.readline()
        print(a)
        if not a:
          break
        m1=a.split(",")[0]
        m2=a.split(",")[1]
        m3=a.split(",")[2]
        print(f"marks in english for student{i} is {m1}")
        print(f"marks in maths for student{i} is {m2}")
        print(f"marks in science for student{i} is {m3}")

    m=a.split(",")      #List with  each line as an item. we split it ina new list with one line as one and only item. Then we separate by comma to get a new list with all items of one line as separate one. That is why we got INDEX OUT OF RANGE ERROR IN M2.
    
    print(m)
    
    
    
# The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.

# Keep in mind that the writelines() method does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately:
    
with open("fileIO2.txt" , "w") as f:
    files=("hello" , "hi", "there\n" , "1,2,3,4\n" , "5,6,7,8\n"  )  # string given as a tuple . 
    f.writelines(files)
    
    values=['good' , 'truth' , 'love']  #for writing values in new line using loop.
    for value in values:
        f.write(value +'\n')