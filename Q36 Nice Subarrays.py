def count_nice_subarrays(arr,k):
    current_sum=0
    prefix_map={0:1}
    c=0
    for num in arr:
        if num%2==0:
            current_sum+=0
        else:
            current_sum+=1
        if (current_sum-k) in prefix_map:
            c=c+prefix_map[current_sum-k]
        prefix_map[current_sum]=prefix_map.get(current_sum,0)+1
    return c
arr=list(map(int,input().split()))
k=int(input())
print(count_nice_subarrays(arr,k))
        
        




