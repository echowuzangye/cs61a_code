test = {'name': 'q1',
 'points': 10,
 'suites': [{'cases': [{'code': '>>> order(Tree(1, [Tree(2, [Tree(3, '
                                '[Tree(4)])])]))               # The only '
                                'valid plucking order.\n'
                                '[4, 3, 2, 1]\n'
                                '\n'
                                '>>> order(Tree(1, [Tree(2), Tree(3)])) in '
                                '[[2, 3, 1], [3, 2, 1]]  # There are 2 valid '
                                'orders.\n'
                                'True\n'
                                '\n'
                                '>>> o = order(Tree(1, [Tree(2, [Tree(3)]), '
                                'Tree(4, [Tree(5)])]))  # There are many valid '
                                'orders,\n'
                                '\n'
                                '>>> o.index(5) < '
                                'o.index(4)                                       '
                                '# but all have 5 before 4,\n'
                                'True\n'
                                '\n'
                                '>>> o.index(3) < '
                                'o.index(2)                                       '
                                '# and 3 before 2,\n'
                                'True\n'
                                '\n'
                                '>>> '
                                'o[4:]                                                         '
                                '# and 1 at the end.\n'
                                '[1]\n'
                                '\n'
                                '>>> order(Tree(7, [Tree(4, [Tree(6)]), '
                                'Tree(5)])) in [[6, 5, 4, 7], [5, 6, 4, 7], '
                                '[6, 4, 5, 7]]\n'
                                'True\n'}],
             'scored': True,
             'setup': 'from q1 import *',
             'type': 'doctest'},
            {'cases': [{'code': '>>> b0 = Tree(2, [Tree(3, [Tree(4), '
                                'Tree(5)])])\n'
                                '\n'
                                '>>> b1 = Tree(6, [Tree(7), Tree(8, '
                                '[Tree(9)])])\n'
                                '\n'
                                '>>> t = Tree(1, [b0, b1])\n'
                                '\n'
                                '>>> pluck(t)(9)(8)(7)(6)(5)(4)(3)(2)(1)\n'
                                "'success!'\n"
                                '\n'
                                '>>> pluck(t)(5)(9)(4)(7)(3)(8)(6)(2)(1)\n'
                                "'success!'\n"
                                '\n'
                                '>>> pluck(t)(2)\n'
                                "'Hey, not valid!'\n"
                                '\n'
                                '>>> pluck(t)(5)(9)(7)(6)\n'
                                "'Hey, not valid!'\n"
                                '\n'
                                '>>> pluck(b0)(5)(2)\n'
                                "'Hey, not valid!'\n"
                                '\n'
                                '>>> pluck(b0)(4)(5)(3)(2)\n'
                                "'success!'\n"}],
             'scored': True,
             'setup': 'from q1 import *',
             'type': 'doctest'}]}