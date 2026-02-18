#check if array is sorted or not
#if it is sorted it should have to return true ,otherwise false
def is_sorted(arr):
    n = len(arr)

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True
if __name__=="__main__":
    print(is_sorted([1,2,3,4]))
    print(is_sorted([1,2,6,4]))
