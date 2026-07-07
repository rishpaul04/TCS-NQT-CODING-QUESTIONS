# 1. The "Move Zeros" / Empty Packets Problem  Problem Statement: A chocolate factory packs chocolates in an array. The empty packets are represented by 0. You need to move all the empty packets (0s) to the end of the array while keeping the order of the other chocolates the same.  Input: 4 5 0 1 9 0 5 0Output: 4 5 1 9 5 0 0 0Easy Python Code:


def move_zeros(arr):
    result=[]
    zero_count=0
    for num in arr:
        if num!=0:
            result.append(num)
        else:
            zero_count+=1
    result.extend([0]*zero_count)
    return result
if __name__=="__main__":
    arr=list(map(int,input().split()))
    answer=move_zeros(arr)
    print(*answer)