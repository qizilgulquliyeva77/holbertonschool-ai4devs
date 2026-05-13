def calculate_average(numbers):
    """
    Calculates the arithmetic mean of a list of numbers.
    Fixes applied: sum initialization and empty list check.
    """
    if not isinstance(numbers, list) or len(numbers) == 0:
        print("Warning: Input list is empty or invalid.")
        return 0
    
    # Fixed: total_sum starts at 0 to avoid off-by-one errors
    total_sum = 0 
    for num in numbers:
        total_sum += num
        
    result = total_sum / len(numbers)
    print(f"Calculated average: {result}")
    return result

# Simple test execution
calculate_average([10, 20, 30])
