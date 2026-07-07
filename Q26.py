def timeConversion(s):
    # 1. Slice the string to extract the important parts
    period = s[-2:]          # The last two characters: "AM" or "PM"
    hour = s[:2]             # The first two characters: "07", "12", etc.
    minutes_secs = s[2:-2]   # Everything in the middle: ":05:45"
    
    # --- Apply the 4 Rules of Military Time ---
    
    # Rule 1: 12 AM becomes 00
    if period == "AM" and hour == "12":
        return "00" + minutes_secs
        
    # Rule 2: Any other AM time stays exactly the same
    elif period == "AM":
        return hour + minutes_secs
        
    # Rule 3: 12 PM stays 12
    elif period == "PM" and hour == "12":
        return hour + minutes_secs
        
    # Rule 4: Any other PM time adds 12 to the hour (e.g., 01 PM -> 13)
    else:
        new_hour = str(int(hour) + 12)
        return new_hour + minutes_secs

# --- TCS NQT Standard Input Handling ---
if __name__ == "__main__":
    # Example input: "07:05:45PM"
    time_input = input().strip() 
    
    # Print the converted string
    print(timeConversion(time_input))