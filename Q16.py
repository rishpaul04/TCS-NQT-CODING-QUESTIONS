# Question

# There are N passengers who need to travel.

# A car can carry 4 passengers and produces X units of pollution.

# A van can carry 100 passengers and produces Y units of pollution.

# You may use any number of cars and vans.

# Output Format
# Print the minimum pollution for each test case.

t=int(input())
for _ in range(t):
    n,x,y=map(int,input().split())
    cars_needed=(n+3)//4  # Calculate the number of cars needed (ceil division)
    vans_needed=(n+99)//100  # Calculate the number of vans needed (ceil division)
    
    # Calculate pollution for using only cars and only vans
    pollution_cars=cars_needed*x
    pollution_vans=vans_needed*y
    mix=(n//100)*y+((n%100+3)//4)*x
    
    # Print the minimum pollution
    print(min(pollution_cars,pollution_vans,mix))