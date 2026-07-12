def build_prefix_sum(arr):
    prefix_arr=[0]*(len(arr))
    prefix_arr[0]=arr[0]
    for i in range(1,len(arr)):
        prefix_arr[i]=prefix_arr[i-1]+arr[i]
    return prefix_arr
arr=list(map(int,input().split()))
prefix_sum=build_prefix_sum(arr)
print(prefix_sum)

def build_prefix_sum(arr):
    # Array is length N + 1, starting with a 0
    prefix_arr = [0] * (len(arr) + 1)
    
    # Loop matches the original array length exactly
    for i in range(len(arr)):
        prefix_arr[i+1] = prefix_arr[i] + arr[i]
        
    return prefix_arr

arr = list(map(int, input("Enter numbers: ").split()))
prefix_sum = build_prefix_sum(arr)
print(prefix_sum)