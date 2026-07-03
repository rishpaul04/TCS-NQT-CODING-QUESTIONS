# Problem Statement: Maximum Subarray Sum
# Given an array of integers, your task is to find the contiguous subarray (containing at least one number) 
# which has the largest sum and return that sum along with the elements of the subarray itself.
# This problem is a classic application of Kadane’s Algorithm, which allows you to find the maximum sum in a single pass ($O(N)$ time complexity).

# Using Kandane's Algorithm, we can efficiently find the maximum subarray sum. The algorithm works by iterating through the array while keeping track of the current subarray sum and the maximum sum found so far. 
# If the current subarray sum becomes negative, we reset it to zero, as starting a new subarray would yield a higher sum.

def max_subarray_sum(arr):
    max_sum=float('-inf')
    current_sum=0
    start=0
    end=0
    s=0
    for i in range(len(arr)):
        current_sum+=arr[i]
        max_sum=max(max_sum,current_sum)
        start=s
        end=i


        if current_sum<0:
            current_sum=0
            s=i+1
    return max_sum,arr[start:end+1]
