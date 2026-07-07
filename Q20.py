def assign_ranks(arr):
    unique_numbers=set(arr)
    sorted_arr=sorted(unique_numbers,reverse=True)

    rank={}
    current_rank=1
    for num in sorted_arr:
        rank[num]=current_rank
        current_rank+=1
    result=[]
    for num in arr:
        result.append(rank[num])
    return result
if __name__=="__main__":
    arr=list(map(int,input().split()))
    answer=assign_ranks(arr)
    print(*answer)