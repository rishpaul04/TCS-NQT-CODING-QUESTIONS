n = int(input("Enter a number: "))
total_sum = 0  # Initialize a variable to keep track of the sum

for i in range(1, n + 1):
    c = 0  # Reset the counter for each 'i'
    for j in range(1, i + 1):  # Start at 1 so a prime is divided exactly 2 times
        if i % j == 0:
            c = c + 1
            
    if c == 2:  # If it was divisible by exactly 1 and itself, it's prime
        total_sum = total_sum + i  # Add the prime number to the total sum
        
# Print the final sum after the loops finish
print("Sum of prime numbers:", total_sum)


n = int(input("Enter a number: "))

# Primes start at 2
for i in range(2, n + 1):
    is_prime = True
    
    # We only need to check divisibility up to the square root of 'i'
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break  # Stop checking as soon as we find a divisor
            
    if is_prime:
        print(i)