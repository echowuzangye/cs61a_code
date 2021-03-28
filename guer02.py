# Tree ADT
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

def is_min_heap(t):
    """

    >>> t1 = tree(1, [tree(6), tree(5, [tree(7)]), tree(3, [tree(9), tree(4)])])
    >>> is_min_heap(t1)
    True
    >>> t12 = tree(1, [tree(6), tree(5, [tree(7)]), tree(3, [tree(9), tree(2)]) ] )
    >>> is_min_heap(t12)
    False
    """
    for branch in branches(t):
        if label(branch) < label(t) or not is_min_heap(branch):
            return False
    return True


def largest_product_path(tree):
    """
    >>> largest_product_path(None)
    0
    >>> largest_product_path(tree(3))
    3
    >>> t = tree(3, [tree(7, [tree(2)]), tree(8, [tree(1)]), tree(4)])
    >>> largest_product_path(t)
    42
    """
    if not is_tree(tree):
        return 0
    elif is_leaf(tree):
        return label(tree)
    else:
        return max([label(tree)*largest_product_path(branch) for branch in branches(tree)])

def max_tree(t):
    """
    >>> max_tree(tree(1, [tree(5, [tree(7)]),tree(3,[tree(9),tree(4)]),tree(6)]))
    tree(9, [tree(7, [tree(7)]),tree(9,[tree(9),tree(4)]),tree(6)])
    """
    if is_leaf(t):
        return tree(label(t))
    else:
        new_branches = [max_tree(branch) for branch in branches(t)]
        new_label = max([label(t)] + [label(branch) for branch in new_branches])
        return tree(new_label, new_branches)


def level_order(tree):
    base = [label(tree)]
    stack = [branch for branch in branches(tree)]
    # print(1, stack)
    while len(stack) > 0:
        t = stack.pop(0)
        # print(2, t)
        base.append(label(t))
        # print(3, base)
        if not is_leaf(t):
            stack.extend([branch for branch in branches(t)])
            # print(4, stack)
    return base


t = tree(1, [tree(5, [tree(7)]),tree(3,[tree(9),tree(4, [tree(5)])]),tree(6)])
# print(level_order(t))

def all_paths(t):
    if is_leaf(t):
        return [[label(t)]]
    else:
        path = []
        for branch in branches(t):
            for item in all_paths(branch):
                path.append([label(t)]+item)
        return path


# print(all_paths(t))

def make_max_finder():
    """
    >>> m = make_max_finder()
    >>> m([5, 6, 7])
    7
    >>> m([1, 2, 3])
    7
    >>> m([9])
    9
    >>> m2 = make_max_finder()
    >>> m2([1])
    1
    """
    max_n =0

    def helper(list_in):
        nonlocal max_n
        max_n = max(max(list_in), max_n)
        return max_n
    return helper

# m = make_max_finder()
# print(m([5, 6, 7]))
# print(m([1, 2, 3]))

"""
5.1 
- An iterator is an object that provides sequential access to values, one by one.
Any value that can produce iterators is called an iterable value. In Python, an 
- iterable value is anything that can be passed to the built-in iter function. 
Iterables include sequence values such as strings and tuples, as well as other 
containers such as sets and dictionaries. Iterators are also iterables, because 
they can be passed to the iter function.

- A generator is an iterator returned by a special class of function called a generator 
function. Generator functions are distinguished from regular functions in that rather 
than containing return statements in their body, they use yield statement to return 
elements of a series.
"""

def generate_constant(x):
    """A generator function that repeats the same value x forever.
    >>> area = generate_constant(51)
    >>> next(area)
    51
    >>> next(area)
    51
    >>> sum([next(area) for _ in range(100)])
    5100
    """
    while True:
        yield x

def black_hole(seq, trap):
    """A generator that yields items in SEQ until one of them matches TRAP, in which case that
    value should be repeatedly yielded forever.
    >>> trapped = black_hole([1, 2, 3], 2)
    >>> [next(trapped) for _ in range(6)]
    [1, 2, 2, 2, 2, 2]
    >>> list(black_hole(range(5), 7))
    [0, 1, 2, 3, 4]
    """
    for item in seq:
        if item != trap:
            yield item
        while True:
            yield trap


def gen_inf(lst):
    """
    >>> t = gen_inf([3, 4, 5])
    >>> next(t)
    3
    >>> next(t)
    4
    >>> next(t)
    5
    >>> next(t)
    3
    >>> next(t)
    4
    """
    while True:
        yield from lst


def naturals():
    i = 1
    while True:
        yield i
        i += 1


def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even))
    [0 , 2 , 4]
    >>> all_odd = (2*y-1 for y in range (5))
    >>> list(filter(all_odd, is_even))
    []
    >>> s = filter(naturals(), is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for item in iterable:
        if fn(item):
            yield item


def tree_sequence(t):
    """
    >>> t = tree(1, [tree(2, [tree(5)]), tree(3, [tree(4)])])
    >>> print(list(tree_sequence(t)))
    [1, 2, 5, 3, 4]
    """
    yield label(t)
    for branch in branches(t):
        yield from tree_sequence(branch)

def make_digit_getter(n):
    """ Returns a function that returns the next digit in n
    each time it is called, and the total value of all the integers
    once all the digits have been returned.
    >>> year = 8102
    >>> get_year_digit = make_digit_getter(year)
    >>> for _ in range(4):
    ...     print(get_year_digit())
    2
    0
    1
    8
    >>> get_year_digit()
    11
    """
    s = 0
    def helper():
        nonlocal s, n
        while n > 0:
            s += n % 10
            x = n % 10
            n = n//10
            return x
        return s
    return helper