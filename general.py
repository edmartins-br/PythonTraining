#! /usr/bin/python3

#Fiibonacci
a,b = 0, 1
for i in range(0, 10):
    print(a)
    a, b = b, a + b

# ----------------------------------------------------------------

# FIBONACCI GENERATOR
def fib(num):
    a,b = 0, 1
    for i in range(0, num):
        yield "{}: {}".format(i+1, a)
        a, b = b, a + b

for item in fib(10):
    print (item)

# ----------------------------------------------------------------

# LISTAS SÃO IMUTAVEIS E TUPLAS SÃO MUTÁVEIS
my_list = [1,2,3,4,5,6,7,8,9,10]

squares = [num*num for num in my_list]
print (squares)

# ---------------------- OOP ------------------------------------------

class Person(object):
    def _init_(self, name):
        self.name = name

    def reveal_identity(self):
        print("My name is {}".format(self.name))

class SuperHero(Person):
    def _init_(self, name, hero_name):
        super(SuperHero, self)._init_(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print("...And I am {}".format(self.hero_name))

# corey = Person('Corey')
# corey.reveal_identity()

wade = SuperHero('Wade Wilson', 'Deadpool')
wade.reveal_identity()


# ----------------------------------------------------------------

class employee:

    def _init_(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.email = self.firstName + "." + self.lastName + "@outlook.com"
    
    def giveRaise(self, salary):
        self.salary = salary

class developer(employee):
    
    def _init_(self, firstName, lastName, salary, programming_languages):
        super()._init_(firstName, lastName, salary)
        self.prog_langs = programming_languages

    def addLanguage(self, lang):
        self.prog_langs += [lang]

employee1 = employee("Jon", "Montana", 100000)
print(employee1.salary)

employee1.giveRaise(100000)
print(employee1.salary)

dev1 = developer("Joe", "Montana", 100000, ["Python", "C"])
print(dev1.salary)

dev1.giveRaise(125000)
print(dev1.salary)

dev1.addLanguage("Java")
print(dev1.prog_langs)

# ----------------------------------------------------------------

# STRING FORMATING
name = "Eduardo"
age = 33

string = "Hi, my name is %s and I am %i years old" % (name, age) # similar to printf in C language
print(string) 

string2 = "Hi, my name is {} and I am {} years old" .format(name, age)
print(string2)

string3 = f"Hello, {name}"
print(string3)

string4 = f"1 + 1 is {1 + 1}"
print(string4)

# ----------------------------------------------------------------

# DATA STRUCTURE

# STaCK
stack = []
stack.append(1)
stack.append(2)

pop_elem = stack.pop()

print(stack, pop_elem)

queue = []
queue.append(1)
queue.append(2)

pop_elem = queue.pop(0)
print(queue, pop_elem)

# SET
set1 = set([1,2,3,4,5,6])
set2 = set([2,4,3,1,8,7,9,2])

print(set1 & set2)

# DICTIONARY
ages = dict()

ages["bob"] = 22
ages["emily"] = 20

for key, value in ages.items():
    # print(ages)
    print(key, value)

# LIST COMPREHENSION

lst = [1,2,3,4,5,6,7]

even_lst = [x for x in lst if x % 2 == 0]
print(even_lst)

square_lst = [x ** 2 for x in lst]
print(square_lst)

# PYTHON STANDARD LIBRARIES

from collections import defaultdict

exam_grades = [("Bob", 43), ("Joe", 98), ("Eduardo", 89), ("Mark", 90), ("Tiff", 44), ("Jan", 56)]
student_grades = defaultdict(list)

for name, grade in exam_grades:
    student_grades[name].append(grade)

print(student_grades)
print(student_grades["Eduardo"])

from collections import Counter

numbers = [1,2,3,4,5,6,7,8,3,5,7,8,3,2, 8, 8, 8, 8, 8]
counts = Counter(numbers)

print(counts)

top2 = counts.most_common(2)
print(top2)
# ex: [(8, 7), (3, 3)] - Numero 8 ocorreu 7 vezes e o número 3 ocorreu 3 vezes

class Carro:
    def _init_(self, marca, preco, cor):
        self.marca = marca
        self.preco = preco
        self.cor = cor
    
    def mostraMarca(self):
        print('A marca do carro é {}'.format(self.marca))
    
    def mostraPreco(self):
        print('O preço do carro é R${}'.format(self.preco))

    def mostraCor(self):
        print('A cor do carro é {}'.format(self.cor))

meuCarro = Carro('Volks', 45000, 'Prata')

meuCarro.mostraMarca()
meuCarro.mostraPreco()
meuCarro.mostraCor()