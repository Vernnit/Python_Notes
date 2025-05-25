# Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class. accessed via classname.variable_name.


# Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to store information that is specific to each instance of the class.

class Subject:
    branch='Engineering physics'          #class variable 
    def __init__(self , one , two):
        self.one=one   
        self.two=two                      #instance variable
    def info(self):
        print(f' {self.one} , {self.two} , {self.branch}')

a=Subject('quantum' , 'nuclear')
b=Subject('Maths', 'DS Algos')
a.info()
b.info()

a.branch='Physics and Photonic Science'   #prints for instance always at first and then looks for class variable.
a.info()

Subject.branch='ECE'                      #changes for the whole class but not for a particular instance if mentioned modifications .       
a.info()
b.info()

c=Subject('a' , 'b')
c.info()
