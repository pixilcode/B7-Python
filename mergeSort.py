import time

def merge(a,b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

def mergesort(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = int(len(x)/2)
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a,b)

print(mergesort([5, 11, 7, 3, 5, 4, 7, 11, 4, 9]));
print(mergesort([9, 0, 11, 10, 5, 8, -7, 6, 8, 7, 5]));
