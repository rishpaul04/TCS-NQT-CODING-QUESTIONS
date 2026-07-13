# 3. The Optimal $O(N)$ Trick: 
# "Contribution"Instead of building the subarrays, we ask a different question:
#  "How many different subarrays does a specific number appear in?"
# If we know a number appears in exactly 4 different subarrays, its total "contribution" to the final answer is simply number * 4. 
# We just calculate this for every number in the array and add them up.The FormulaFor an element at index i in an array of length n:Start points: 
# How many choices do we have for the start of a subarray that includes arr[i]? 
# We can start at any index from 0 up to i. That gives us (i + 1) choices.
# End points: How many choices do we have for the end of a subarray that includes arr[i]?
#  We can end at any index from i up to the end of the array (n - 1). 
# That gives us (n - i) choices.
# If we multiply the choices together, we get the total number of subarrays containing that element:Occurrences = (i + 1) * (n - i)

def sum_of_all_subarrays(arr):
    s=0
    for i in range(0,len(arr)):
        contributions=(i+1)*(len(arr)-i)
        s+=arr[i]*contributions
    return s
arr=list(map(int,input().split()))
print(sum_of_all_subarrays(arr))