def subarray_with_sum_map(arr, target):
    # Dictionary stores {prefix_sum: index}
    # We initialize it with 0: -1 to catch subarrays starting at index 0
    prefix_map = {0: -1} 
    current_sum = 0
    
    for i, num in enumerate(arr):
        current_sum += num
        
        # If (current_sum - target) exists in our map, we found a valid subarray!
        if (current_sum - target) in prefix_map:
            start_index = prefix_map[current_sum - target] + 1
            return arr[start_index : i+1]
            
        # Store the current prefix sum and its index
        prefix_map[current_sum] = i
        
    return []

arr = list(map(int, input("Enter array: ").split()))
target = int(input("Enter target: "))
print(subarray_with_sum_map(arr, target))