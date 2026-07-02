# Question 1: Find Top K Frequent Scores
# Problem Statement:Given an array of match scores and an integer K, 
# find the scores with the highest frequencies.Requirement: Print the scores arranged in decreasing order of frequency.
# Constraint: Return only the first K scores.Tie-breaking Rule: If two scores have the same frequency, the score that appears first in the array should come first.
# Input Format:First line contains the array elements separated by commas.Second line contains integer K.

scores=list(map(int,input().strip().split(',')))
k=int(input())
frequency={}
for num in scores:
    frequency[num]=frequency.get(num,0)+1
unique_scores=[]
for num in scores:
    if num not in unique_scores:
        unique_scores.append(num)
unique_scores.sort(key=lambda x:frequency[x],reverse=True)
for i in range(min(k,len(unique_scores))):
    print(unique_scores[i])

