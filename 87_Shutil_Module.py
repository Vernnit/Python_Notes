# Shutil is a Python module that provides a higher level interface for working with file and directories. The name "shutil" is short for shell utility. It provides a convenient and efficient way to automate tasks that are commonly performed on files and directories

import shutil
shutil.copy('87_Shutil_Module.py' , '88_90_Exercises.py')

# shutil.copy(src, dst):           This function copies the file located at src to a new location specified by dst. If the destination location already exists, the original file will be overwritten.

# shutil.copy2(src, dst):         This function is similar to shutil.copy, but it also preserves more metadata about the original file, such as the timestamp.


# shutil.copytree(src , dst):     This copies the whole directory or folder .If the destination location already exists, the original directory will be merged with it.

# shutil.move(src, dst):          This function moves the file located at src to a new location specified by dst. This function is equivalent to renaming a file in most cases.

# shutil.rmtree('dir') :          For deleting a folder or a directory. 

# os.remove("file.file") for removing a file.