def head(L):
    return L[0]
 
def tail(L):
    return L[1]

def py2ll(L):
    if not L:
        return None
    else:
        return (L[0], py2ll(L[1:]))

def ll2py(L):
    if not L:
        return []
    else:
        return [head(L)] + ll2py(tail(L))

def fact(N):
    if N > 1:
        return N * fact(N-1)
    else:
        return 1

def prime(a):
     return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

def mapL(L, f):
    if not L:
        return None
    else:
        return (f(head(L)), mapL(tail(L), f))

def factAll(L):
    if not L:
        return None
    else:
        return (fact(head(L)), factAll(tail(L)))

def strAll(L):
    if not L:
        return None
    else:
        return (str(head(L)), strAll(tail(L)))

def incAll(L):
    if not L:
        return None
    else:
        return (head(L)+1, incAll(tail(L)))

def sqrAll(L):
    if not L:
        return None
    else:
        return (head(L)**2 , sqrAll(tail(L)))

def isPrimeAll(L):
    if not L:
        return None
    else:
        return (prime(head(L)), isPrimeAll(tail(L)))

def incAllN(L, N):
    return mapL(L, lambda x: x+N)

def filterL(L, f):
    if not L:
        return None
    else:
        T = filterL(tail(L), f)
        H = head(L)
        return (H, T) if f(H) else T

def filterOdd(L):
    # TODO
    return None

def filterPositive(L):
    # TODO
    return None

def filterGtN(L, N):
    # TODO
    return None

def filterPrimes(L):
    # TODO
    return None
