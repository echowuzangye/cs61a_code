# 1.1 What is a linked list? Why do we consider it a naturally recursive structure?
# A common representation of a sequence constructed from nested pairs is called a linked list。
# Linked lists have recursive structure: the rest of a linked list is a linked list or 'empty'.
class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
            return 'Link({0}{1})'.format(repr(self.first), rest_str)
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
            return string + str(self.first) + '>'

# 1.3
def has_cycle(link):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    """
    # collect_list = [link]
    # while not link == Link.empty:
    #     collect_list.append(link.first)
    #     link = link.rest
    #     if link.rest in collect_list:
    #         return True
    # return False
    s = link
    while not link == Link.empty:
        if link.rest == s:
            return True
        else:
            link = link.rest
    return False

# 1.4
def seq_in_link(link, sub_link):
    """
    >>> lnk1 = Link(1, Link(2, Link(3, Link(4))))
    >>> lnk2 = Link(1, Link(3))
    >>> lnk3 = Link(4, Link(3, Link(2, Link(1))))
    >>> seq_in_link(lnk1, lnk2)
    True
    >>> seq_in_link(lnk1, lnk3)
    False
    """
    # first_link = []
    # while link != Link.empty:
    #     first_link.append(link.first)
    #     link = link.rest
    #
    # while sub_link != Link.empty:
    #     if sub_link.first in first_link:
    #         index = first_link.index(sub_link.first)
    #         first_link = first_link[index:]
    #         sub_link = sub_link.rest
    #     else:
    #         return False
    # return True
#  this method is too complicated!
    while link != Link.empty and sub_link != Link.empty:
        if sub_link.first == link.first:
            sub_link = sub_link.rest
        link = link.rest

    if sub_link == Link.empty:
        return True
    else:
        return False


# 2.1 What is the relationship between a class and an ADT?
#  An ADT is an abstract data structure with associated operations.
# A class is a programming construct associated with object oriented programming.
# Often a class will implement an ADT, but they are conceptually different.


# 2.2 What is the definition of a Class? What is the definition of an Instance?
# A class serves as a template for all objects whose type is that class.
# Every object is an instance of some particular class.

# 2.3 What is a Class Attribute? What is an Instance Attribute?
# class: a template for creating objects
# instance: a single object created from a class
# instance attribute: a property of an object, specific to an instance
# class attribute: a property of an object, shared by all instances of a class
# method: an action (function) that all instances of a class may perform

# 2.4
class Foo():
    x = 'bam'

    def __init__(self, x):
        self.x = x

    def baz(self):
        return self.x


class Bar(Foo):
    x = 'boom'

    def __init__(self, x):
        Foo.__init__(self, 'er' + x)

    def baz(self):
        return Bar.x + Foo.baz(self)

foo = Foo('boo')
# Foo.x ---> bam
# foo.x ---> boo
# print(foo.baz()) --- >boo
# print(Foo.baz()) ---> error
# print(Foo.baz(foo))  --->boo
bar = Bar('ang')
# print(Bar.x) --->boom
# print(bar.x) ---->erang
# print(bar.baz()) --->boomerang

# 2.5 What Would Python Display?

class Student:
    def __init__(self, subjects):
        self.current_units = 16
        self.subjects_to_take = subjects
        self.subjects_learned = {}
        self.partner = None

    def learn(self, subject, units):
        print('I just learned about ' + subject)
        self.subjects_learned[subject] = units
        self.current_units -= units

    def make_friends(self):
        if len(self.subjects_to_take) > 3:
            print('Whoa! I need more help!')
            self.partner = Student(self.subjects_to_take[1:])
        else:
            print("I'm on my own now!")
            self.partner = None

    def take_course(self):
        course = self.subjects_to_take.pop()
        self.learn(course, 4)
        if self.partner:
            print('I need to switch this up!')
            self.partner = self.partner.partner
            if not self.partner:
                print('I have failed to make a friend :(')


# tim = Student(['Chem1A', 'Bio1B', 'CS61A', 'CS70', 'CogSci1'])
# tim.make_friends()
# # 'Whoa! I need more help!'
# print(tim.subjects_to_take)
# # ['Chem1A', 'Bio1B', 'CS61A', 'CS70', 'CogSci1']
# tim.partner.make_friends()
# # 'Whoa! I need more help!'
# tim.take_course()
# # I just learned about CogSci1
# # 'I need to switch this up!'
# tim.partner.take_course()
# # I just learned about CogSci1
# tim.take_course()
# # I just learned about CS70
# # I need to switch this up!
# # I have failed to make a friend :('
# tim.make_friends()
# # I'm on my own now!

# 2.6
    """
    >>>cat = Cat('Tuna')
    >>>kitten = kitten('Fish', cat)
    >>>cat.meow()
    meow, Tuna is hungry
    >>>kitten.meow()
    i'm baby, Fish is hungry
    I want mama Tuna
    >>>cat.eat()
    meow
    >>>cat.meow()
    meow, my name is Tuna
    >>>kitten.eat()
    i'm baby
    >>>kitten.meow()
    meow, my name is Fish
    I want mama Tuna
    """
class Cat():
    noise = 'meow'
    def __init__(self, name):
        self.name = name
        self.hungry = True

    def meow(self):
        if self.hungry:
            print(self.noise + ',' + self.name + ' is hungry')
        else:
            print(self.noise + ', my name is ' + self.name)

    def eat(self):
        print(self.noise)
        self.hungry = False


class Kitten(Cat):
    noise = "I'm baby"
    def __init__(self, name, mother):
        Cat.__init__(self, name)
        self.mother = mother

    def meow(self):
        Cat.meow(self)
        print('I want mama '+ self.mother.name)




