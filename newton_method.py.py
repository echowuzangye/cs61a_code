def approx_eq(x, y, tolerance=1e-15):
    return abs(x-y) < tolerance

def improve(update, close, guess=1, max_update=100):
    k = 0
    while not close(guess) and k < max_update:
        guess = update(guess)
        k += 1
        return guess
    
 def newton_update(f,df):
     def update(x):
         return x - f(x)/df(x)
     return update

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)



# find square root of any number a

def square_root(a):
    def f(x):
        return x*x - a
    def df(x):
        return 2*x
    return find_zero(f, df)

