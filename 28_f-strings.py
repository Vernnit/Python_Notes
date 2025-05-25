# When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.

string="Hi my name is {1} and i am from {0}."
a="vernnit"
b="India"
print(string.format(a,b))
c='lolo'
d='locolo'                        
string=f"hello my name is {c} and i am from {d} and this is how we can show this {{e}}"
print(string)

price=21.098758585
print(f"print to only two decimal places {price:.2f}")

print(f"{2*30}")   



# It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String Interpolation 