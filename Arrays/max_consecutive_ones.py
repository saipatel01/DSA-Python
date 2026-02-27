def max_consecutive_ones(arr):
    current = 0
    maximum = 0

    for num in arr:
        if num == 1:
            current += 1
            maximum = max(maximum, current)
        else:
            current = 0

    return maximum


if __name__ == "__main__":
    arr = [1, 1, 0, 1, 1, 1]
    result = max_consecutive_ones(arr)
    print("Maximum consecutive ones:", result)