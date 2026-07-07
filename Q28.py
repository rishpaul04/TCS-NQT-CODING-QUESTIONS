import heapq
def find_min_and_max(arr):
    # find smallest 
    min_heap=arr.copy()
    heapq.heapify(min_heap)
    smallest=heapq.heappop(min_heap)
    # find largest 
    negative_heap=[]
    for num in arr:
        heapq.heappush(negative_heap,-num)
    largest=-heapq.heappop(negative_heap)
    return smallest,largest
if __name__=="__main__":
    arr=list(map(int,input().split()))
    smallest,largest=find_min_and_max(arr)
    print(smallest,largest)
