def count_frequencies(arr):
    frequency_map={}
    for num in arr:
        frequency_map[num]=frequency_map.get(num,0)+1
    return frequency_map
elements=list(map(int,input().split()))
frequencies=count_frequencies(elements)
print(frequencies)