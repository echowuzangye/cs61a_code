**** 3.1 Call expressions ****
scm> (define a (+ 1 2))
scm> a
3

scm> (define b (+ (* 3 3) (* 4 4)))
scm> (+ a b)
28

scm> (= (modulo 10 3) (quotient 5 3))
#t

scm> (even? (+ (- (* 5 4) 3) 2))
#f

**** 4.1 Special forms ****

scm> (if (or #t (/ 1 0)) 1 (/ 1 0))
1

scm> (if (> 4 3) (+ 1 2 3 4) (+ 3 4 (* 3 2)))
10

scm> ((if (< 4 3) + -) 4 100)
-96

scm> (if 0 1 2)
1

**** lambda and defining functions ****
4.1 Write a function that returns the factorial of a number.

(define (factorial x)
    (if (= x 1) 1
        (* x (factorial (- x 1))))
)

4.2 Write a function that returns the nth Fibonacci number.

(define (fib n)
    (cond
       ((= n 0) 0)
       ((= n 1) 1)
       (else (+ (fib (- n 1)) (fib (- n 2))))
    )
)

**** pairs and lists ****
5.1 Write a function which takes two lists and concatenates them.
Notice that simply calling (cons a b) would not work because it will create a
deep list. Do not call the builtin procedure append, which does the same thing as
my-append.
(define (my-append a b)
    (cond
        ((null? a) b)
        ((null? b) a)
        (else (cons (car a) (my-append (cdr a) b)))
    )
)
