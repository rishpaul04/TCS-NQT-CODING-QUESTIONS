# You are given an integer array nums.
# Your task is to find a contiguous subarray (containing at least one number) within the array that has the largest product, and return that product.

# Understanding the Challenge

# Unlike the "Maximum Sum Subarray" problem, where you can simply reset the sum to zero if it becomes negative,
#  this problem is trickier because of negative numbers:

# A large negative number, when multiplied by another negative number, can become a large positive number.

# Therefore, you must track both the maximum and minimum product at every step, 
# because the current minimum could become the maximum if you multiply it by a negative number later.

def max_product_subarray(nums):
    if not nums:
        return 0
    
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]

        if num < 0:
            max_product, min_product = min_product, max_product

        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)

        result = max(result, max_product)

    return result
nums = list(map(int, input().split()))
result = max_product_subarray(nums)
print(result)
    