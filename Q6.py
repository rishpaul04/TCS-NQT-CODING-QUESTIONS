# Problem Statement: Longest Quick-Order Streak
# A restaurant has $N$ food items, where each element in the array arr[] denotes the preparation time of a food item in minutes.
# A threshold value $T$ is given.An item is considered a "Quick-Order Item" if its preparation_time <= T.
# Your task is to find the longest continuous streak of "Quick-Order Items".
# Rules:If multiple streaks have the same maximum length, you must choose the first occurring streak.
# Print:The first value of the longest streak.The number of quick-order items in that streak (length).
# The last index (0-based) of that streak.
# Input Format:
# First line: An integer $N$ — the number of food items.
# Second line: $N$ space-separated integers representing the preparation times.
# Third line: An integer $T$ — the threshold value.
# Output Format:
# Print three space-separated values:[first_value_of_streak] [streak_length] [last_index]

n=int(input())
arr=list(map(int,input().strip().split()))
t=int(input())
current_length=0
max_length=0
start_index=0
for i in range(n):
    if arr[i]<=t:
        current_length+=1
        if current_length==1:
            start_index=i
        if current_length>max_length:
            max_length=current_length
            first_value=arr[start_index]
            last_index=i
    else:
        current_length=0
if max_length>0:
    print(f"{first_value} {max_length} {last_index}")





