# Problem Statement: Prime Matrix Validation
# You are given integers $m$ and $n$, followed by $m \times n$ elements representing a matrix. 
# Your task is to determine if every row in the matrix contains at least one prime number.
# Conditions for "Wrong Input":If m <= 0 or n =a 0.
# If any element is negative.
# If the total number of provided elements is less than $m \times n$.
# Output Rules:Print "Valid" if all rows contain at least one prime number.
# Print "Not Valid" if at least one row does not contain any prime number.
# Print "Wrong Input" if any of the above conditions are violated.
# Input Format
# First line: Two space-separated integers, $m$ and $n$, representing the number of rows and columns, respectively.
# Second line: $m \times n$ space-separated integers representing the matrix elements. 
# (These may be provided on one or multiple lines depending on the test case, so reading all integers in a stream is recommended).
# Output Format:The program must output exactly one of the following strings:"Valid" "Not Valid" "Wrong Input"

def is_prime(num):
    if num <= 1: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

# Read m and n
line1 = input().split()
if not line1: exit()
m, n = map(int, line1)

if m <= 0 or n <= 0:
    print("Wrong Input")
    exit()

# Read elements
matrix = list(map(int, input().split()))

# Validation: Count and Negatives
if len(matrix) < m * n or any(x < 0 for x in matrix):
    print("Wrong Input")
    exit()

# Row-by-row validation
all_rows_valid = True
for i in range(m):
    # Slice the row from the flat list
    row = matrix[i*n : (i+1)*n]
    
    # Check if this SPECIFIC row has a prime
    if not any(is_prime(x) for x in row):
        all_rows_valid = False
        break

if all_rows_valid:
    print("Valid")
else:
    print("Not Valid")