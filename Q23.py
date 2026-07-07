def check_valid_string(s):
    # Count the number of '*' and '#' in the string
    star_count = s.count('*')
    hash_count = s.count('#')
    
    # Subtracting hash_count from star_count perfectly handles all 3 conditions:
    # 1. If * > #, it returns a positive number.
    # 2. If # > *, it returns a negative number.
    # 3. If * == #, it returns 0.
    result = star_count - hash_count
    
    return result


if __name__ == "__main__":
    # Take string input from the user
    s = input()
    
    # Print the calculated result
    print(check_valid_string(s))