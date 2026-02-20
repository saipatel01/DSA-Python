#i emo unique value ni ediki povalo cheppaniki
#j emo scan cheyyaniki

def remove_duplicates(arr):
    if not arr:
        return 0

    i = 0  # position of last unique element

    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1

if __name__ == "__main__":
    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(arr)

    print("Number of unique elements:", k)
    print("Array after removing duplicates:", arr[:k])