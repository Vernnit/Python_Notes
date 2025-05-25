# In Python, the seek() and tell() functions are used to work with file objects and their positions within a file. These functions are part of the built-in io module, which provides a consistent interface for reading and writing to various file-like objects, such as files, pipes, and in-memory buffers.

# The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position. For example:


# To change the file object’s position, use f.seek(offset, whence) -- whence value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. DEFAULT 0.

with open('workfile.txt' , 'r+') as f:
    f.write('Hello There')
    print(f.tell())
    print(f.read())
    f.seek(0,2)    #files without 'b' allow seeks from beginning not a -ve seek.  
    print(f.tell())
    print(f.read(3)) #does not prints anything 
    f.seek (1,0)
    print(f.read(3))
    print(f.read(-1)) #entire content is being read when argument is omitted or -ve.
    
#f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.
    
#  if you want to truncate the file to a specific size, you can use the truncate function.  
# f.write('sjxjsjx')
# f.truncate(3)     would give 3 characters only on reading .
    
with open('workfile2.txt' , 'rb+') as f:
    f.write(b'123456789abcdef') 
    print(f.tell())  
    a=f.read(1)
    
    print(type(a))
    print(a)       #prints an empty binary string if the end of file has been reached 
    f.seek(0)
    print(f.read(5))
    
    # f.seek(-3,0)   #invalid argument as reference point  is beginning and nothing is before that.
    f.seek(-3, 2)    #3rd value before the end. i.e. 13th byte.
    print(f.read(1))
    print(f.read())
    print(f.read(-1)) #entire content is being read  with -ve argument.
    c=f.tell()     #at the end
    print(c)
    f.seek(c)
    print(f.read(2))
    # seek to a saved value 
