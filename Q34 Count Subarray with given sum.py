def subarray_sum(arr,target):
    prefix_arr={0:1} # Map stores {prefix_sum: count_of_occyrrences}
    current_sum=0
    c=0
    for num in arr:
        current_sum=current_sum+num
        if (current_sum-target) in prefix_arr:
            c+=prefix_arr[current_sum-target]
        prefix_arr[current_sum]=prefix_arr.get(current_sum,0)+1
    return c

arr=list(map(int,input().split()))
target=int(input())
print(subarray_sum(arr,target))



