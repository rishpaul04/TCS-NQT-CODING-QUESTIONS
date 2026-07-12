def max_sub_sum(arr):
   max_sum=float('-inf')  # Initialize to negative infinity to handle negative numbers
   current_sum=0
   for num in arr:
      current_sum+=num
      if current_sum>max_sum:
         max_sum=current_sum
      if current_sum<0:
         current_sum=0
   return max_sum
arr=list(map(int,input().split()))
result=max_sub_sum(arr)
print(result)