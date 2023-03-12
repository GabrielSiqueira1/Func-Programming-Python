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
        H = head(L)
        T = tail(L)
        return [H] + ll2py(T)

def size(L):
    if not L:
        return 0
    else:
        return 1 + size(tail(L))

def sorted(L):
    if not L:
        return True
    elif not tail(L):
        return True
    else:
        H0 = head(L)
        T0 = head(tail(L))
        if H0 <= T0:
            return sorted(tail(L))
        else:
            return False
        
def sum(L):
    if not L:
        return 0
    if not tail(L):
        return head(L)
    else:
        return head(L) + sum(tail(L))

def split(L):
    if not L:
        return (None, None)
    if not tail(L):
        return (L, None)
    else:
        H0 = head(L)
        H1 = head(tail(L))
        (T0, T1) = split(tail(tail(L)))
        return ((H0, T0),(H1, T1))

def merge(L0, L1):
    if not L0:
        return L1
    if not L1:
        return L0
    else:
        H0 = head(L0)
        T0 = tail(L0)
        H1 = head(L1)
        T1 = tail(L1)
        if H0 < H1:
            return(H0, merge(T0, L1))
        else:
            return(H1, merge(L0, T1))

def mSort(L):
    if not L:
        return None
    if not tail(L):
        return L
    else:
        (L0, L1) = split(L)
        return merge(mSort(L0), mSort(L1))

def max(L):
    if not L:
        return None
    if not tail(L):
        return L
    else:
        H = head(L)
        T = tail(L)
        if H > head(T):
            return max(merge(py2ll([H]), tail(T)))
        else:
            return max(T)

def get(L, N):
    if not L:
        return None
    if not tail(L) or N == 0:
        return head(L)
    else:
        N -= 1
        return get(tail(L), N)
