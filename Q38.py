n = "1321"
d = "1"
ans = []

for i in range(len(n)):
    if n[i] == d:
        t = n[0:i] + n[(i+1):]
        ans.append(int(t))
        
print(str(max(ans)))