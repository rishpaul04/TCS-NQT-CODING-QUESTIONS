def smallestSubsequence(s):
    last_occurence={}
    for i in range(len(s)):
        last_occurence[s[i]]=i
    stack=[]
    seen=set()

    for i in range(len(s)):
        char=s[i]
        if char in seen:
            continue
        while stack and stack[-1] > char and last_occurence[stack[-1]]>i:
            removed_char=stack.pop()
            seen.remove(removed_char)
        stack.append(char)
        seen.add(char)
    return "".join(stack)
s=input()
print(smallestSubsequence(s))
