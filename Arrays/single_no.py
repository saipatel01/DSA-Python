def single_number(arr):
    result = 0
    for num in arr:
        result ^= num
    return result


if __name__ == "__main__":
    arr = [4, 1, 2, 1, 2]
    answer = single_number(arr)
    print("Single number is:", answer)