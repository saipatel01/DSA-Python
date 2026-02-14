def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_left(arr, d):
    if not arr:   # handle empty list
        return arr

    n = len(arr)
    d = d % n

    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    reverse(arr, 0, n - 1)

    return arr


if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    d = int(input("Enter number of rotations: "))

    result = rotate_left(arr, d)

    print("Rotated Array:", result)
