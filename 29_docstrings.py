# Python doc strings are the string literals that appear right after the definition of a function, method, class, or module.

def addition(a,b):
    # print(addition) if we insert this doc string is Obtained NONE type.
    ''' This is a doc string not a comment'''
    add=a+b
    return(add)
print(addition(2,1))
# can be accessed by .__doc__ attribute.
print(addition.__doc__)

# comments are totally ignored by python and  are descriptions that help programmers better understand the intent and functionality of the program , whereas doc strings are not they can be obtained by using the doc attribute and they are used to document our code.



# PEP 8
# PEP 8 is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.

# PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.

# The Zen of Python
# Long time Pythoneer Tim Peters succinctly channels the BDFL’s guiding principles for Python’s design into 20 aphorisms, only 19 of which have been written down.

# easter egg -- write import this in repl.