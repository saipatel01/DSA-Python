'''Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false'''

def is_monotonic(arr):
    n=len(arr)
    inc = True
    dec = True
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            inc = False
        elif arr[i]<arr[i+1]:
            dec=False
    return inc or dec

if __name__ == "__main__":
    print(is_monotonic([1,2,2,3]))
    print(is_monotonic([6,5,4,4]))
    print(is_monotonic([1,3,2]))
 

