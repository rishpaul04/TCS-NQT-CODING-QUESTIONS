# Problem Statement: Prime & Digit Sum Multiplication
# You are given two integers, $m$ and $n$. 
# Your task is to perform the following operations:
# Find the $m$-th prime number. (e.g., if $m=1$, the prime is 2; if $m=3$, the prime is 5).
# Compute the digit sum of $n$ repeatedly until it becomes a single digit (this is also known as the digital root).
# Multiply the $m$-th prime number by the resulting single-digit sum.
# Print the final result.

def get_nth_prime(m):
    count=0
    num=2
    while True:
        is_prime=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            count+=1
            if count==m:
                return num
        num+=1
m=int(input())
n=int(input())
if n==0:
    digit_sum=0
if n%9==0:
    digit_sum=9
else:
    digit_sum=n%9
print(get_nth_prime(m)*digit_sum)

