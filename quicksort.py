#stable / in place sort version
"Paris"

def partition(l, i ,j): #i = first.  j = last
    if len(l) <= 1:
        return l #base case
    pivot = j - 1
    j = pivot - 1

    while i < j:
        while l[i] < l[pivot]: #moves the i counter
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
