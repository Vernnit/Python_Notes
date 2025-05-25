# Importing in Python is the process of loading code from a Python module into the current script. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.

import math 
print(math.sqrt(25))    #after importing you can access the variables and fn by using a dot notation

# You can also import specific functions or variables from a module using the from keyword.
from math import sqrt , pi    #no need of dot notation then.
print(sqrt(144)*pi)

# It's also possible to import all functions and variables from a module using the * wildcard. However, this is generally not recommended as it can lead to confusion and make it harder to understand where specific functions and variables are coming from.
from math import *      #no need of using a dot notation.

# You can rename your imported module using as keyword 
# to contract long module names of sometimes make more descriptive.

import math as m 
print(m.sqrt(169))
print(dir(m))            #This will output a list of all the names defined in the math module, including functions like sqrt and pi, as well as other variables and constants.

import Dummyfile as df 
df.welcome()
print(df.shimla)