# 1.1
class Student:
    students = 0 # this is a class attribute

    def __init__(self, name, ta):
        self.name = name # this is an instance attribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        ta.add_student(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1


# snape = Professor("Snape")
# harry = Student("Harry", snape)
# # There are now 1 students
# harry.visit_office_hours(snape)
# # Thanks, Snape
# harry.visit_office_hours(Professor("Hagrid"))
# # Thanks, Hagrid
# harry.understanding
# #  2
# [name for name in snape.students]
# # [harry]
# x = Student("Hermione", Professor("McGonagall")).name
# # There are now 2 students
# x
# # Hermione
# [name for name in snape.students]
# # [harry]

# 1.2
class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Server:
    """Each Server has an instance attribute clients, which
    is a dictionary that associates client names with
    client objects.
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        self.clients[email.recipient_name].receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them
        to the clients instance attribute.
        """
        self.clients[client_name] = client


class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).
    """
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name
        self.server.register_client(self, self.name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)


    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        self.inbox.append(email)

# 2.1
class Pet():
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)


class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')


class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives

    def talk(self):
        """ Print out a cat's greeting.
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name + ' says meow!')

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False. If this is called after lives has reached zero, print out
        that the cat has no more lives to lose.
        """
        if not self.is_alive:
            print('The cat has no more lives to lose!')
        else:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False

# 2.2
class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""
    # def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
    #     this is not necessary. Cat class has exactly the same init method.
    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        Cat.talk(self)
        Cat.talk(self)

# 2.3 WWPD
class A:
    def f(self):
        return 2
    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)

class B(A):
    def f(self):
        return 4

# x, y = A(), B()
# x.f() ---- 2
# B.f(self) ---- 4
# x.g(x, 1) --- 4
# >>> y.g(x, 2) --- 8

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

# 3.1
def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if lnk.rest is Link.empty:
        return lnk.first
    else:
        return lnk.first + sum_nums(lnk.rest)

a = Link(1, Link(6, Link(7)))

#3.2

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """

    s = 1
    for i in range(len(lst_of_lnks)):
        s *= lst_of_lnks[i].first
    for i in range(len(lst_of_lnks)):
        if lst_of_lnks[i].rest is Link.empty:
            return Link(s)
    return Link(s, multiply_lnks([item.rest for item in lst_of_lnks]))


# 3.3
def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    StopIteration
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link is not Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest

    def filter_no_iter(link, f):
        """
        >>> link = Link(1, Link(2, Link(3)))
        >>> list(filter_no_iter(link, lambda x: x % 2 != 0))
        [1, 3]
        """

        if link is Link.empty:
            return
        elif f(link.first):
            yield link.first
        yield from filter_no_iter(link.rest, f)

# 1. Midterm Review Snax
def feed(snax, x, y):
    """
    >>> feed([1, 1, 1], 2, 2) # The two robots both refill once at the beginning
    2
    >>> feed([1, 2, 2], 2, 2) # Only one robot refills to feed the middle student
    3
    >>> feed([1, 1, 1, 2, 2], 2, 2)
    4
    >>> feed([3, 2, 1, 3, 2, 1, 1, 2, 3], 3, 3)
    6
    """
    def helper(lst, p, q):
        if p<0 or q<0:
            return float('inf')
            # infinitely large value
        elif not lst:
            return 0
        elif len(lst) == 1:
            return not(p>=lst[0] or q>=lst[0]) #true equals 1 and false quals 0
        else:
            a = helper(lst[1:-1], p-lst[0], q-lst[-1])  #no one refills
            b = 2 + helper(lst[1:-1], x-lst[0], y - lst[-1]) #both refill
            c = 1 + helper(lst[1:-1], x-lst[0], q-lst[-1]) # only a refills
            d = 1 + helper(lst[1:-1], p-lst[0], y-lst[-1]) # only b refills
            return min(a, b, c, d)
    return helper(snax, 0, 0)