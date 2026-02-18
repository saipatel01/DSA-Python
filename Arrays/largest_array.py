
def largest(arr):
    n = arr[0]   #  first element, not whole list
        
    for i in range(1, len(arr)):
         if arr[i] > n:
            n = arr[i]
                
    return n
if __name__=="__main__":
    arr = list(map(int, input("Enter numbers: ").split()))
    result = largest(arr)
    print(result)   