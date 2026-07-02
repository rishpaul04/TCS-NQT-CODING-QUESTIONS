# Problem Statement: Vendor Entry Management
# A society maintains a list of registered vendors who are allowed to enter the premises. 
# You are given a list of registered vendor IDs and a sequence of gate operations to process.
# Operations: ENTRY X: * If vendor $X$ is registered, allow entry and add them to the "active vendors" list.
# If $X$ is not registered, count this as a "blocked attempt."
# CHECK X: Count this as a check request.
# EXIT X: Remove vendor $X$ from the active vendors list if they are currently present.
# At the End, Print:Total Active Vendors: The current number of vendors inside the premises.
# Total Blocked Attempts: The total number of failed entry requests.
# Total Checked Requests: The total number of check requests made.

# Input FormatFirst line: Integer $N$ (number of registered vendors).
# Second line: $N$ space-separated vendor IDs.
# Third line: Integer $M$ (number of operations).
# Next $M$ lines: The gate operations (e.g., ENTRY V1, CHECK V2, EXIT V1).
# Output Format:
# Active Vendors: X
# Blocked: Y
# Checked: Z

n=int(input())
vendor_id=set(input().strip().split())
m=int(input())
active_vendors=set()
blocked_attempts=0
checked_requests=0
for _ in range(m):
    operation=input().strip().split()
    op_type=operation[0]
    vendor=operation[1]
    if op_type=="ENTRY":
        if vendor in vendor_id:
            active_vendors.add(vendor)
        else:
            blocked_attempts+=1
    elif op_type=="CHECK":
        checked_requests+=1
    elif op_type=="EXIT":
        active_vendors.discard(vendor)
print(f"Active Vendors: {len(active_vendors)}")
print(f"Blocked: {blocked_attempts}")
print(f"Checked: {checked_requests}")
