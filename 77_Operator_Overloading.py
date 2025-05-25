'''Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types. This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes, just as you would for built-in data types like int, float, and str.'''

# You can overload an operator in Python by defining special methods in your class

# It's important to note that operator overloading is not limited to the built-in operators, you can overload any user-defined operator as well.f;


class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.x}i + {self.y}j + {self.z}k'

    def __add__(self, other):
        # return f'{self.x + other.x}i + {self.y + other.y}j + {self.z + other.z}k'
        return vector((self.x + other.x), (self.y + other.y), (self.z + other.z))


v1 = vector(1, 2, 3)
v2 = vector(3, 2, 1)
print(v1)
print(v2)
# it returns type vector instead of using string in dunder str as it just returns the value but it is vector class object.
print(type(v1))

print(v1+v2)
print(type(v1+v2))  # returns string if we use f-string in return statement
# returns the vector class if we use vector class.
