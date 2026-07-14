def max_integer(n):
    nums=[0]*(n+1)
    nums[0]=0
    nums[1]=1
    for i in range(2,n+1):
        if i%2==0:
            nums[i]=nums[i//2]
        else:
            nums[i]=nums[i//2]+nums[i//2+1]
    return max(nums)
n=int(input())
print(max_integer(n))