import os
if not os.path.exists("D:/direc"):
    os.mkdir("D:/direc")
if not os.path.exists("D:/direc/Data"):
    os.mkdir("D:/direc/Data")
print(os.getcwd())
os.chdir("D:/direc/Data")
print(os.getcwd())

os.mkdir("hello")

