# Problem Statement: First and Last Occurrence of X/
# Given a sorted array of integers of size $N$ and a target value $X$, perform the following:
# Find the first occurrence of $X$ in the array.
# Find the last occurrence of $X$ in the array.
# Calculate the difference between the last and first occurrence (i.e., last_index - first_index).
# Condition: If the target element $X$ is not present in the array, print -1.
# Requirement: The solution must be implemented using Binary Search to ensure $O(\log N)$ time complexity.

def binary_search(arr,n,x,find_first):
    low=0
    high=n-1
    result=-1
    while low<=high:
        mid=(low+high)//2
        result=mid
        if arr[mid]==x:
            if find_first:
                high=mid-1
            else:
                low=mid+1
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return result
n=int(input())
arr=list(map(int,input().strip().split()))
x=int(input())
first_index=binary_search(arr,n,x,True)
last_index=binary_search(arr,n,x,False)
if first_index==-1 or last_index==-1:
    print(-1)
else:
    print(last_index-first_index)