def longest_subarray_with_sumk(arr,target):
    prefix_map={0:-1}
    current_sum=0
    max_length=0
    for i in range(len(arr)):
        current_sum+=arr[i]
        if (current_sum-target) in prefix_map:
            start_index=prefix_map[current_sum-target]+1
            current_length=i-start_index+1
            max_length=max(max_length,current_length)
        if current_sum not in prefix_map:
         prefix_map[current_sum] = i
    
    return max_length

arr=list(map(int,input().split()))
target=int(input())
print(longest_subarray_with_sumk(arr,target))
            
        











