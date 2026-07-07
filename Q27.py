import heapq
def find_k_best_selling(sales,k):
    sales_count={}
    for product in sales:
        if product in sales_count:
            sales_count[product]+=1
        else:
            sales_count[product]=1
    # Use a heap to find the k products with the highest sales
    min_heap=[]
    for product,count in sales_count.items():
        heapq.heappush(min_heap,(count,product))
        if len(min_heap)>k:
            heapq.heappop(min_heap)
    return min_heap[0][1]
if __name__ == "__main__":
    # Example input: 
    # Line 1: K (e.g., 2)
    # Line 2: Product stream (e.g., laptop phone laptop watch phone laptop)
    
    k = int(input())
    sales_stream = input().split()
    
    result = find_k_best_selling(sales_stream, k)
    print(result)