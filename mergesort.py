"Paris"
def mergesort(l):
    if len(l) < 2:
        return l 
    
    mid = len(l)//2
    a = l[:mid]
    b = l[mid:]

    mergesort(a)
    mergesort(b)
    merge(a,b,l)
    return l 

def merge(a,b,l):
    i = 0
    j = 0
    while i < len(a) and i < len(b):
        if a[i] < b[j]:
            l[i+j] = a[i]
            i+=1
        else:
            l[i+j] = b[j]
            j+=1
    l[i+j:] = a[i:]+b[j:]




