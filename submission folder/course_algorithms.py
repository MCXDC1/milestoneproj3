#Mia
def insertion(L: list):
    """Insertion sort used for sorting by id, name, or date"""
    n = len(L)
    for i in range(n):
        j = n - i - 1
        while j < n - 1 and L[j] > L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]
            j += 1

#Mia
def bubble(L: list):
    """Bubble sort used for sorting by id, name, or date"""

    n = len(L)

    for i in range(n-1):
        swapped = False
        for j in range(n-1- i):
            if L[j] > L[j+1]:
                L[j+1], L[j] = L[j], L[j+1]
                swapped = True
        if swapped == False:
            break

#Paris 

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
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            l[i+j] = a[i]
            i+=1
        else:
            l[i+j] = b[j]
            j+=1
    l[i+j:] = a[i:]+b[j:]

#Paris

def partition(l, i ,j): #i = first.  j = last
    pivot = j
    j = pivot - 1

    while i <= j:
        while l[i] <= l[pivot]: #moves the i counter
            i+=1
            while i < j and j >= l[pivot]:  #moves the j counter
                j-=1
            if i < j:
                l[i], l[j] = l[j],l[i] #swaps the wrong values
            if j < l[pivot]:
                l[pivot], l[j] = l[j],l[pivot] #swaps the values and makes sure the pivot is correct

def quicksort(l, left, right):
    pivot = partition(l, left, right)
    quicksort(l, left, pivot)
    quicksort(l, pivot+1, right)