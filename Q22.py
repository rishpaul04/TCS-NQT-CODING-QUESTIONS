def sort_pairs():
    n=int(input())
    pairs=[]
    for _ in range(n):
        a,b=map(int,input().split())
        pairs.append((a,b))
    pairs.sort()
    print(pairs)
if __name__=="__main__":
    sort_pairs()

