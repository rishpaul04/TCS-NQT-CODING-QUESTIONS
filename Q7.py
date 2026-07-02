# Problem Statement:
# Nth Smallest and Nth Largest RankYou are provided with a predefined set of 10 ranks arranged in ascending order: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.
# Your Task:Take an integer $N$ as input.If $N$ is outside the range of 1 to 10, print: Invalid Input.
# If $N$ is within the range, perform the following:
# Find the $N$-th smallest rank.F
# ind the $N$-th largest rank.
# Print both values.
# (Note: Based on the provided list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], the $N$-th smallest rank is simply $N$, and the $N$-th largest rank is $11 - N$.)

# Input Format:
# A single integer $N$.

n = int(input())
if n < 1 or n > 10:
    print("Invalid Input")
else:
    nth_smallest = n
    nth_largest = 11 - n
    print(f"{nth_smallest} {nth_largest}")