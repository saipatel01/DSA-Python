#using sum formula method
#sum of first n natural no's


def missing_number(arr):
    n = len(arr)
    
    # Expected sum of numbers from 0 to n
    expected_sum = n * (n + 1) // 2
    
    # Actual sum of array elements
    actual_sum = sum(arr)
    
    # Missing number
    return expected_sum - actual_sum

if __name__ == "__main__":
    arr = [3, 0, 1]
    print("Missing number:", missing_number(arr))