; Lab 14: Final Review

(define (compose-all funcs)
    (define (helper num)
      (if (null? funcs) num
      ((compose-all (cdr funcs)) ((car funcs) num))
      ))
    helper
)