# Problem Statement: Vendor Entry ManagementA society maintains a list of registered vendors who are allowed to enter the premises. 
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