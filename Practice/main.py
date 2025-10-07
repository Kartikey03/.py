def count_numbers_with_repeated_digits():
    """
    Count numbers from 4000 to 4999 (inclusive) that have at least one repeated digit.
    """
    count = 0
    
    # Iterate through all numbers from 4000 to 4999
    for num in range(4000, 5000):
        # Convert number to string to easily access digits
        num_str = str(num)
        
        # Check if there are repeated digits
        # If the length of the set of digits is less than the length of the string,
        # it means there are repeated digits
        if len(set(num_str)) < len(num_str):
            count += 1
    
    return count

def count_numbers_without_repeated_digits():
    """
    Alternative approach: Count numbers WITHOUT repeated digits,
    then subtract from total to get numbers WITH repeated digits.
    """
    count_without_repeat = 0
    
    # For numbers from 4000 to 4999
    for num in range(4000, 5000):
        num_str = str(num)
        
        # Check if all digits are unique
        if len(set(num_str)) == len(num_str):
            count_without_repeat += 1
    
    total_numbers = 1000  # From 4000 to 4999 inclusive
    count_with_repeat = total_numbers - count_without_repeat
    
    return count_with_repeat, count_without_repeat

def mathematical_approach():
    """
    Mathematical approach to solve the problem.
    
    For 4-digit numbers starting with 4 (4abc where a, b, c are digits 0-9):
    - Total numbers: 1000 (from 4000 to 4999)
    - Numbers without repeated digits: 
      * First digit is fixed as 4
      * Second digit can be any of 9 digits (0-9 except 4): 9 choices
      * Third digit can be any of 8 remaining digits: 8 choices  
      * Fourth digit can be any of 7 remaining digits: 7 choices
      * Total without repetition: 1 × 9 × 8 × 7 = 504
    - Numbers with at least one repeated digit: 1000 - 504 = 496
    """
    total_numbers = 1000
    
    # Calculate numbers without repeated digits
    # First digit is 4 (fixed)
    # Second digit: 9 choices (0,1,2,3,5,6,7,8,9)
    # Third digit: 8 choices (remaining after first two)
    # Fourth digit: 7 choices (remaining after first three)
    numbers_without_repeat = 1 * 9 * 8 * 7
    
    numbers_with_repeat = total_numbers - numbers_without_repeat
    
    return numbers_with_repeat, numbers_without_repeat

# Test all approaches
if __name__ == "__main__":
    print("Method 1 - Direct counting:")
    result1 = count_numbers_with_repeated_digits()
    print(f"Numbers with at least one repeated digit: {result1}")
    
    print("\nMethod 2 - Counting complement:")
    result2_with_repeat, result2_without_repeat = count_numbers_without_repeated_digits()
    print(f"Numbers without repeated digits: {result2_without_repeat}")
    print(f"Numbers with at least one repeated digit: {result2_with_repeat}")
    
    print("\nMethod 3 - Mathematical approach:")
    result3_with_repeat, result3_without_repeat = mathematical_approach()
    print(f"Numbers without repeated digits: {result3_without_repeat}")
    print(f"Numbers with at least one repeated digit: {result3_with_repeat}")
    
    print(f"\nAll methods give the same result: {result1 == result2_with_repeat == result3_with_repeat}")
    
    # Show some examples of numbers with repeated digits
    print("\nFirst 10 numbers with repeated digits in the range:")
    count = 0
    for num in range(4000, 5000):
        if len(set(str(num))) < len(str(num)):
            print(num, end=" ")
            count += 1
            if count == 10:
                break
    print()