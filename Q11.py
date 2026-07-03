# Problem Statement: Speed CalculationYou are given a distance (in kilometers) and a time (in minutes). 
# Your task is to calculate the speed in km/h based on the provided inputs and constraints.
# Requirements:Convert time: Convert the given time from minutes into hours (since 60 minutes = 1 hour, time in hours = $\text{Time in minutes} / 60$).
# Calculate Speed: Use the formula:$$\text{Speed} = \frac{\text{Distance}}{\text{Time (in hours)}}$$
# Constraint: The time must be in the range of 1 to 60 minutes (inclusive).
# Error Handling: If the time is outside the range of 1 to 60 minutes, the program must print: "Error".

distance,time=map(int,input().split())

hours=time/60
if time<1 or time>60:
    print("Error")
else:
    speed=distance/hours
    print(int(speed))   