# Implementation of binary search algorithm!!

# We will prove that binary search is faster than naive search!

# naive search: scan entire list and ask if its equal to the target
# if yes, return the index
# if no, then return -1
def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
        
    if high < low:
        return -1
    
    
    midpoint = (len(l)) // 2
    
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, low, midpoint-1)
    else:
        # target > l[midpoint]
        return binary_search(l[midpoint], midpoint+1, high)
    
if __name__ == '__main__':
    l = [1, 3, 10, 12]
    target = 3
    print(naive_search(l, target))
    print(binary_search(l, target))