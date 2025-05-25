# The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression

# The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements.

# It is important to note that the Walrus Operator should be used sparingly as it can make code less readable if overused.
a=[1,2,3,4,5]
while (n:=len(a)) > 0:
    print(a.pop())


# The biggest advantage of the walrus operator is to make writing codes easier. In the past, you had to collect each user input into a distinct variable before passing it to the for loop to check its value or apply a condition.


# foods=list()
#  while True:
#   food = input("What food do you like?: ")
#   if food == "quit":
#       break
#   foods.append(food)

foods=list()
while ((food:=input('type your favorite food '))!='quit'):
    foods.append(food)
print(foods)                                      #    Why printing True?