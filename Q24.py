# merge two arrays into one array
def merge_arrays(arr1, arr2):
    n=len(arr1)
    m=len(arr2)
    result=[]
    i=0
    j=m-1
    while i<n and j>=0:
        if arr1[i]<arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j-=1
    while i<n:
        result.append(arr1[i])
        i+=1
    while j>=0:
        result.append(arr2[j])
        j-=1
    return result
if __name__=="__main__":
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    answer=merge_arrays(arr1,arr2)
    print(*answer)
