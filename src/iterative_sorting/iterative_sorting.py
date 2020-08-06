# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # TO-DO: find next smallest element
    # (hint, can do in 3 loc)
    # Your code here
    # Check every element to the right, find smallest_index
    # element at cur_index with smallest_index
    for ii in range(0, len(arr) - 1):
        cur_index = ii
        smallest_index = cur_index
        for jj in range(ii+1, len(arr)):
            if arr[smallest_index] > arr[jj]:
                smallest_index = jj
        arr[ii], arr[smallest_index] = arr[smallest_index], arr[ii]

        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # Loop through indexes 0 - ???
    for ii in range(len(arr)-1):
        # last ii element already in place:
        for jj in range(0, len(arr)-ii-1):
            if arr[jj] > arr[jj+1]:
                arr[jj], arr[jj+1] = arr[jj+1], arr[jj]
        # we are done if a loop results in no swaps

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
