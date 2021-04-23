**1 Tail Recursion**
;For the following procedures, determine whether or not they are tail recursive. If
they are not, write why not and rewrite the function to be tail recursive on the
right.

; Multiplies x by y
(define (mult x y)
    (if (= 0 y)
    0
    (+ x (mult x (- y 1)))))
  * not; more computation is required - "+ x"

(define (mult x y)
    (define (helper x y mul-result)
        (if (= 0 y) mul-result
            (helper x (- y 1) (+ x mul-result))))
    (helper x y 0)
)

; Always evaluates to true
; assume n is positive
(define (true1 n)
    (if (= n 0)
    #t
    (and #t (true1 (- n 1)))))
* yes

; Always evaluates to true
; assume n is positive
(define (true2 n)
    (if (= n 0)
    #t
    (or (true2 (- n 1)) #f)))
* not, because true2 will not be the last one to be evaluated

; Returns true if x is in lst
(define (contains lst x)
    (cond
        ((null? lst) #f)
        ((equal? (car lst) x) #t)
        ((contains (cdr lst) x) #t)
        (else #f)))
* not; contains is not the final sub-expression.
(define (contains lst x)
    (cond
        ((null? lst) #f)
        ((equal? (car lst) x) #t)
        (else (contains (cdr lst) x))))

;1.2 Tail recursively implement sum-satisfied-k which, given an input list lst, a pred-
icate procedure f which takes in one argument, and an integer k, will return the
sum of the first k elements that satisfy f. If there are not k such elements, return
0."""
; Doctests
scm> (define lst `(1 2 3 4 5 6))
scm> (sum-satisfied-k lst even? 2) ; 2 + 4
6
scm> (sum-satisfied-k lst (lambda (x) (= 0 (modulo x 3))) 10)
0
scm> (sum-satisfied-k lst (lambda (x) #t) 0)
0
(define (sum-satisfied-k lst f k)
    (define (helper lst k result)
        (cond ((= k 0) result)
               ((null? lst) 0)
            ((f (car lst)) (helper (cdr lst) (- k 1) (+ result (car lst))))
            (else (helper (cdr lst) k result))))
    (helper lst k 0)
)

;1.3 Tail-recursively implement remove-range which, given one input list lst, and two
non-negative integers i and j, returns a new list containing the elements of lst except
the ones from index i to index j. You may assume j > i, and j is less than the length
of the list. (Hint: you may want to use the built-in append function)

; Doctests
scm> (append '(1 2) '(3 4) '(5 6))
(1 2 3 4 5 6)
scm> (remove-range '(0 1 2 3 4) 1 3)
(0 4)

(define (remove-range lst i j)
    (define (helper lst k new_lst)
        (cond
          ((> k j) (append new_lst lst))
          ((< k i) (helper (cdr lst) (+ k 1) (append new_lst (list (car lst)))))
          (else (helper (cdr lst) (+ k 1) new_lst))))
    (helper lst 0 nil)
)

**2 Interpreter**
;2.1 Determine the number of calls to scheme eval and the number of calls to scheme apply
for the following expressions. Use the visualizer at code.cs61a.org if you're not
sure how an expression is evaluated.
> (+ 1 2)
3
4 eval; 1 apply
> (if 1 (+ 2 3) (/ 1 0))
5
6 eval; 1 apply

> (or #f (and (+ 1 2) 'apple) (- 5 2))
apple
8 eval; 1 apply

> (define (add x y) (+ x y))
add
> (add (- 5 3) (or 0 2))
2

**2 Macros**
;3.1 What will Scheme display? If you think it errors, write Error
> (define-macro (doierror) (/ 1 0))
doierror

> (doierror)
error

> (define x 5)
x

>(define-macro (evaller y) (list (list 'lambda '(x) 'x) y))
evaller

> (evaller 2)
((lambda (x) x) y)
(define-macro (evaller y) ((list 'lambda '(x) 'x) y))
2

;3.2 Consider a new special form, when, that has the following structure:
(when <condition> <expr1> <expr2> <expr3> ... )
If the condition is not false (a truthy expression), all the subsequent operands are
evaluated in order and the value of the last expression is returned. Otherwise, the
entire when expression evaluates to okay.

scm> (when (= 1 0)(/1 0) 'error)
okay
scm> (when (= 1 1) (print 6) (print 1) 'a)
6
1
a

;Create this new special form using a macro. Recall that putting a dot before the
last formal parameter allows you to pass any number of arguments to a procedure,
a list of which will be bound to the parameter, similar to (*args) in Python.

; implement when without using quasiquotes
(define-macro (when condition . exprs)
(list 'if condition (cons 'begin exprs) ''okay))

; implement when using quasiquotes
(define-macro (when condition . exprs)
`(if ,condition ,(cons 'begin exprs) 'okay)
