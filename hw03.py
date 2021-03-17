HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

def num_sevens(x):
    """Returns the number of times 7 appears as a digit of x.

    >>> num_sevens(3)
    0
    >>> num_sevens(7)
    1
    >>> num_sevens(7777777)
    7
    >>> num_sevens(2637)
    1
    >>> num_sevens(76370)
    2
    >>> num_sevens(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_sevens',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if x//10 > 0:
        if x % 10 == 7:
            return num_sevens(x//10) + 1
        else:
            return num_sevens(x//10)
    else:
        if x == 7:
            return 1
        else:
            return 0

# print(num_sevens(12345))


def pingpong(n):
    """Return the nth element of the ping-pong sequence.
    cannot use any assignment statements!!!

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 8:
        return n
    else:
        return pingpong(n-1) + direction(n)


def direction(x):
    if x < 7:
        return 1
    elif (x-1) % 7 == 0 or num_sevens(x-1) != 0:
        return direction(x-1)*(-1)
    else:
        return direction(x-1)


""" Solution from website"""
    # def helper(result, i, step):
    #     if i == n:
    #         return result
    #     elif i % 8 == 0 or num_eights(i) > 0:
    #         return helper(result - step, i + 1, -step)
    #     else:
    #         return helper(result + step, i + 1, step)
    # return helper(1, 1, 1)

# print(pingpong(72))


def count_change(total):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    """1. use the biggest coin
    2. use the second biggest coin
    3. x is the remainder """

    def helper(x, n):
        if x == 0:
            return 1
        elif x < 0:
            return 0
        elif n == 0:
            return 1
        elif n < 0:
            return 0
        else:
            return helper(x-2**n, n) + helper(x, n-1)
    #     use 2**n or use 2**(n-1)
    return helper(total, max_2(total))


def max_2(x, n=0):
    if x <= 0:
        return 0
    else:
        if x > 2**n:
            return max_2(x, n+1)
        elif x == 2**n:
            return n
        else:
            return n-1


# print(count_change(20))

def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    else:
        def helper(x, a):
            if x//10 == 0:
                return a
            elif x % 10 == x//10%10 or x%10-x//10%10 == 1:
                return helper(x//10, a)
            else:
                return helper(x//10, a+(x%10-x//10%10-1))
        return helper(n, 0)

"""Alternative solution"""
# if n < 10:
#         return 0
#     last, rest = n % 10, n // 10
#     return max(last - rest % 10 - 1, 0) + missing_digits(rest)
print(missing_digits(11223344))



###################
# Extra Questions #
###################

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    if n == 1:
        print_move(start, end)
    else:
        middle = 2
        """middle = 6-start-end"""
        move_stack(n - 1, start, middle)
        print_move(start, end)
        move_stack(n - 1, middle, end)

# ?why if I replace other with 2 doesn't work - end will change as you call a new move_stack'
# move_stack(3, 1, 3)

"""The strategy used in Towers of Hanoi is to move all but the bottom disc 
to the second peg, then moving the bottom disc to the third peg, then moving 
all but the second disc from the second to the third peg."""


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

     >>> make_anonymous_factorial()(5)
     120
     >>> from construct_check import check
     >>> # ban any assignments or recursion
     >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
     True
     """
    return (lambda f: f(f))(lambda f: lambda x: 1 if x == 1 else x * f(f)(x - 1))


"""use def method"""
# def make_anonymous_factorial():
#     def factorial(n):
#         if n == 1:
#             return 1
#         else:
#             return factorial(n-1)*n
#     return factorial

print(make_anonymous_factorial()(1))
