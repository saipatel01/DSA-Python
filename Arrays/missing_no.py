# xor method using
#


def missing_number(arr):
    n = len(arr)

    xor_all = 0
    xor_arr = 0

    # XOR of all numbers from 0 to n
    for i in range(n + 1):
        xor_all ^= i

    # XOR of all elements in the array
    for num in arr:
        xor_arr ^= num

    # Missing number
    return xor_all ^ xor_arr

if __name__ == "__main__":
    arr = [3, 0, 1]
    print("Missing number:", missing_number(arr))