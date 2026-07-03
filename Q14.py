# Problem Statement: Minimum Adjacent Swaps to Transform Array
# You are given two arrays, s and x, of size n, containing the same elements (possibly in a different order). Your task is to find the minimum number of adjacent swaps required to transform array s into array x. 
# If it is not possible to transform s into x (i.e., the arrays contain different elements or different frequencies of elements), return -1.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0  # Return array and 0 swaps for base case
    
    mid = len(arr) // 2
    left_half, left_swaps = merge_sort(arr[:mid])
    right_half, right_swaps = merge_sort(arr[mid:])
    
    # Get the merged result and the swaps found during this specific merge
    merged_result, merge_swaps = merge_and_count(left_half, right_half)
    
    return merged_result, (left_swaps + right_swaps + merge_swaps)

def merge_and_count(left_half, right_half):
    i = j = 0
    result = []
    swaps = 0
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            # The "jump": right element is smaller, so it jumps over 
            # all remaining elements in the left half
            result.append(right_half[j])
            swaps += (len(left_half) - i)
            j += 1
            
    result.extend(left_half[i:])
    result.extend(right_half[j:])
    return result, swaps