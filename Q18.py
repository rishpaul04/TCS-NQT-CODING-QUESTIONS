# Problem Rules Extracted:Even index characters: Move forward by 2 positions (e.g., A $\rightarrow$ C).
# Odd index characters: Move backward by 1 position (e.g., C $\rightarrow$ B).
# Special Wrap-around Cases:
# Z $\rightarrow$ B (forward 2 wraps past A)z $\rightarrow$ bA $\rightarrow$ Z (backward 1 wraps to Z)a $\rightarrow$ z0 $\rightarrow$ 9 (backward 1 wraps to 9)
# Error Handling: If the string contains a space, print "Error" and stop execution.

def solve(s):
    if not s:
        return
    if " " in s:
        return "Error"
    result = []
    for i in range(len(s)):
        if i % 2 == 0:  # Even index
            if s[i] == 'Z':
                result.append('B')
            elif s[i] == 'z':
                result.append('b')
            else:
                result.append(chr(ord(s[i]) + 2))
        else:
            if s[i] == 'A':
                result.append('Z')
            elif s[i] == 'a':
                result.append('z')
            elif s[i] == '0':
                result.append('9')
            else:
                result.append(chr(ord(s[i]) - 1))
    return ''.join(result)
s=input().strip()
output=solve(s)
if output=="Error":
    print("Error")
else:
    print(output)
