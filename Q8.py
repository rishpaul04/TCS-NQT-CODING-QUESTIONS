# Problem Statement: Box Grouping ( Sliding Window Approach)
# You are given $N$ boxes, each with a specific weight, and a maximum total weight $W$ allowed for each group. 
# You must form groups of boxes in the given order.
# Rules:
# Add boxes one by one into the current group.
# The total weight of any group cannot exceed $W$.
# If adding the next box exceeds $W$, you must stop immediately (do not form any more groups).
# You cannot skip any box.Your Tasks:Count the number of complete groups formed.
# Count the total number of boxes used before the process stopped.
# Input Format:
# First line: Two space-separated integers $N$ and $W$.
# Second line: $N$ space-separated integers representing the weights of the boxes.
# Read N and W


n, w = map(int, input().split())
weights = list(map(int, input().split()))

complete_groups = 0
boxes_used = 0
current_group_weight = 0

for weight in weights:
    # Rule 3: If a single box exceeds W, stop immediately
    if weight > w:
        break
    
    # Check if adding the box keeps us within the limit W
    if current_group_weight + weight <= w:
        current_group_weight += weight
        boxes_used += 1
    else:
        # Window "slides": The previous group is complete
        complete_groups += 1
        # Start the new group with the current box
        current_group_weight = weight
        boxes_used += 1

# If there is a group currently being filled, it counts as a complete group
if current_group_weight > 0:
    complete_groups += 1

print(f"{complete_groups} {boxes_used}")
