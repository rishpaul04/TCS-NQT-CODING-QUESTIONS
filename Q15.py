# Problem Statement: Odd Ticket Price Analysis
# You are given an array of size N representing the prices of movie tickets.
# Your task is to analyze the ticket prices to find specific information regarding the odd-priced tickets.

# You need to:

# Identify: Find all ticket prices in the array that are odd.

# Compute:

# The sum of all odd ticket prices.

# The count of all odd ticket prices.

# The average of all odd ticket prices.

# Input Format:

# First line: An integer N (representing the number of tickets).

# Second line: N integers (representing the individual ticket prices).

n=int(input())
prices=list(map(int,input().split()))
sum_odd=0
count_odd=0
for price in prices:
    if price%2==1:
        sum_odd+=price
        count_odd+=1
if count_odd>0:
    average_odd=sum_odd/count_odd
    print(f"Sum of odd ticket prices: {sum_odd}")
    print(f"Count of odd ticket prices: {count_odd}")
    print(f"Average of odd ticket prices: {average_odd:.2f}")