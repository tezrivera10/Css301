class person:
     def _init_(self, name, age):
        self.name = name
        self.age = age

     def myfunc(self):
        print ("Hello my name is Raul" + self.name)

p1 = person("Raul", 21)
p1.myfunc()
