import os
if not os.path.exists("Data"):
    os.mkdir("Data")
for i in range (100):
    if not os.path.exists(f"Data/Day{i+1}"):
        os.mkdir(f"Data/Day{i+1}")  
    if not os.path.exists(f"Data/Week{i+1}"):
     os.rename(f"Data/Day{i+1}" , f"Data/Week{i+1}")

a=os.listdir("Data")
print(a)

for i in a:
    print(i)
print(type(a))

print(os.getcwd())
os.chdir("/STUDY/Python Resources")
print(os.getcwd())

for i in range(10):
    os.mkdir(f"Dayta{i+1}")   #will implement in new directory.