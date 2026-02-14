#using slicing
def rotate_right(arr, k):
    if not arr:      # Handle empty array
        return arr

    n = len(arr)
    k = k % n        # Handle k > n
    return arr[n-k:] + arr[:n-k]


# -------- MAIN --------
if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    k = int(input("Enter number of right rotations: "))

    result = rotate_right(arr, k)
    print("Rotated Array:", result)
