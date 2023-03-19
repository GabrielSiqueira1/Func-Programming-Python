import sys
from functools import reduce

import todo

def test(case, args):
    if case == 0:
        print(list(todo.firstChars(args)))
    elif case == 1:
        print(todo.sum([int(e) for e in args]))
    elif case == 2:
        print(todo.avg([int(e) for e in args]))
    elif case == 3:
        print(todo.maxString(args))
    elif case == 4:
        D = todo.buildLenFreq(args)
        F = lambda acc, b: acc + " " + str(b) + ": " + str(D[b])
        S = reduce(F, sorted(D.keys()), "")
        print(S)
    elif case == 5:
        D = todo.countFirsts(args)
        F = lambda acc, b: acc + " " + b + ": " + str(D[b])
        S = reduce(F, sorted(D.keys()), "")
        print(S)
    elif case == 6:
        print(todo.mostCommonFirstChar(args))
    else:
        print('Invalid option', case)

for line in sys.stdin:
    inps = line.split(" ")
    case = int(inps[0])
    args = inps[1:]
    test(case, args)
