def pushZerosToEnd(arr):
    # Pointer to track the position
    # for next non-zero element
    j = 0
    
    for i in range(len(arr)):
        
        # If the current element is non-zero
        if arr[i] != 0:
            
            # Swap the current element with
            # the 0 at index 'count'
            arr[j], arr[i] = arr[i], arr[j]
            
            # Move 'count' pointer to the next position
            j += 1

if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)
    for num in arr:
        print(num, end=" ")