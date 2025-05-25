'''When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.'''


class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def info(self):
        print(f'Name is {self.name} and id is {self.id}')


x = employee("Vernnit", 2131)
y = employee("Chad", 3232)
x.info()


class employee2(employee):

    # def __init__(self , name2  , id2):
    #     self.name2=name2
    #     self.id2=id2
    def info2(self):
        print(f'Second name is {self.name} and second id is {self.id}')


# looks for __init__ in employee2 , does not find it there then checks in employee , if not there inbuilt.object
a = employee2("tony", 2121)
# print(help(employee2))   #to check how this chain is working.
a.info()
a.info2()


class snemployee(employee):
    def __init__(self, name, id, pro_lang, employees=None):
        super().__init__(name, id)  # Self argument is automatically passed.
        # employee.__init__(self, name, id)    #all arguments should be mentioned as in the class, we want them to handle.
        self.pro_lang = pro_lang

        if employees is None:
            # mutable datatype should'nt be passed as argument.
            self.employees = []
        else:
            self.employees = employees

    def info3(self):
        print(f'programming language is {self.pro_lang}')
        for emp in self.employees:
            print(f' employee under senior employee {emp.name}')


sn1 = snemployee('harry', 2121, 'python', [x, y])
sn1.info()
sn1.info3()
