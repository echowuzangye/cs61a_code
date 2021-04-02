""" Lab 07: Generators, Linked Lists, and Trees """


# Linked Lists

def link_to_list(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    # iterative solution
    # if link == Link.empty:
    #     return []
    # else:
    #     base = []
    #     while link.rest != link.empty:
    #         base.append(link.first)
    #         link = link.rest
    #     base.append(link.first)
    #     return base

#     recursive solution
    if link == Link.empty:
        return []
    else:
        return [link.first] + link_to_list(link.rest)

# Trees

def cumulative_mul(t):
    """Mutates t so that each node's label becomes the product of all labels in
    the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_mul(t)
    >>> t
    Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return
    else:
        for branch in t.branches:
            cumulative_mul(branch)
        s = 1
        for item in t.branches:
            s = s * item.label
        t.label = t.label * s




# Link List Class
class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
# Tree ADT

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)
    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    link_list = []
    while link != Link.empty:
        link_list.append(link)
        link = link.rest
        if link in link_list:
            return True
    return False

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"



def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    def helper(m, reverse):
        if m.is_leaf():
            return
        else:
            new_label = [branch.label for branch in m.branches][::-1]
            for i in range(len(m.branches)):
                helper(m.branches[i], not reverse)
                if reverse:
                    m.branches[i].label = new_label[i]
    return helper(t, True)





"""Q1 WWPD: Linked Lists """
# link = Link(1000)
# link.first   1000
# link.rest is Link.empty True
# link = Link(1000, 2000) Error
# link = Link(1000, Link()) TypeError: __init__() missing 1 required positional argument: 'first'

# link = Link(1, Link(2, Link(3)))
# link.first
# 1

# link.rest.first
# 2

# link.rest.rest.rest is Link.empty
# True

# link.first = 9001
# link.first
# 9001

# link.rest = link.rest.rest
# print(link.rest.first)
# 3

# * link = Link(1)
# link.rest = link
# link.rest.rest.rest.rest.first
# 1

# link = Link(2, Link(3, Link(4)))
# link2 = Link(1, link)
# # link2.first
# # 1
# link2.rest.first
# 2

# link = Link(5, Link(6, Link(7)))
# link
# Link(5, Link(6, Link(7))) # Look at the __repr__ method of Link
#
#
# print(link)          # Look at the __str__ method of Link
# <5 6 7>