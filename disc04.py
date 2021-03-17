"""1.1 You want to go up a
fight of stairs that has n steps.
You can either take 1 or 2 steps each
time. How many different ways can you go up this
fight of stairs? Write a function count_stair_ways
that solves this problem. Assume n is positive."""


def count_stair_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)


# print(count_stair_ways(3))
"""
Consider a special version of the count_stairways problem, where instead
of taking 1 or 2 steps, we are able to take up to and including k steps at
a time.
Write a function count_k that figures out the number of paths for this sce-
nario. Assume n and k are positive."""


def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif k == 1:
        return 1
    else:
        sum_1 = 0
        for i in range(1, k+1):
            sum_1 += count_k(n-i, k)
        return sum_1

# print(count_k(3, 2))


# a = [1, 5, 4, [2, 3], 3]
# print(a[0], a[-1])
# print(len(a))
# print(2 in a)
# print(a[3][0])


def even_weighted(s):
    """Write a function that takes a list s and returns a new list that keeps only
    the even-indexed elements of s and multiplies them by their corresponding
    index."""
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[i]*i for i in range(len(s)) if i % 2 == 0]


x = [1, 2, 3, 4, 5, 6]
print(even_weighted(x))


def max_product(s):
    """
    Write a function that takes in a list and returns the maximum product that
    can be formed using nonconsecutive elements of the list. The input list will
    contain only numbers greater than or equal to 1.
    """
    """
    Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """

    if not s:
        return 1
    elif len(s) == 1:
        return s
    else:
        return max(max_product(s[1:]), max_product(s[2:]*s[0]))

"""A hole number is a number in which every other digit dips below the digits immediately adjacent to it.
For example, the number 968 would be considered a hole number because the number 6 is smaller than
both of its surrounding digits. Assume that we only pass in numbers that have an odd number of digits.
Define the following function so that it properly identifies hole numbers."""


def check_hole_number(n):
    """
    >>> check_hole_number(123)
    False
    >>> check_hole_number(3241968)
    True
    >>> check_hole_number(3245968)
    False
    """
    if n < 10:
        return True
    # else:
    #         n1 = n%10
    #         n2 = n//10%10
    #         n3 = n//100%10
    #         if n2<n1 and n2<n3:
    #             print(n//100)
    #             return check_hole_number(n//100)
    #         else:
    #             return False
    return check_hole_number(n//100) if (n//10%10<n%10 and n//10%10 < n//100%10) else False

# return ((n // 10) % 10) < (n % 10) and ((n // 10) % 10) < ((n // 100) % 10) and check_hole_number(n // 100)


# print(check_hole_number(3243958))
"""Define the following function so that it properly identifies mountain numbers. A mountain number is a
number that either
i. has digits that strictly decrease from right to left OR strictly increase from right to left
ii. has digits that increase from right to left up to some point in the middle of the number (not necessarily
the exact middle digit). After reaching the maximum digit, the digits to the left of the maximum
digit should strictly decrease."""
def check_mountain_number(n):
    """
    >>> check_mountain_number(103)
    False
    >>> check_mountain_number(153)
    True
    >>> check_mountain_number(123456)
    True
    >>> check_mountain_number(2345986)
    True
    """
    def helper(x, step):
        if x == 0:
            return True
        if x//10%10 > x%10 and x//10%10 > x//100%10:
            return helper(x//10, step=-1)
        elif (step == 1 and x//10%10 < x%10) or (step ==-1 and x//10%10 < x//100%10):
            return False
        return helper(x//10, step)
    return helper(n, 1)

# def helper(x, is_increasing):
# if x // 10 == 0:
# return True
# if is_increasing and (x % 10) < ((x // 10) % 10):
# 2
# return helper(x // 10, is_increasing)
# return (x % 10) > ((x // 10) % 10) and helper(x // 10, False)
# return helper(n, True)
print(check_mountain_number(103))