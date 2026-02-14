# using slicing  
def rotate_left(arr, d):#fun raasthunnam
    if not arr:      # Handle empty array okkavela empty array aithe error raakunda undaniki 
        return arr

    n = len(arr) # arr okka length value ni store cheskuntadhi
    d = d % n        # Handle d > n
    return arr[d:] + arr[:d] #d: anedhi aa pos nunchi migitha arr varku and :d anedhi starting nunchi pos varku 


if __name__ == "__main__": #Run the code below only if this file is executed directly.
    arr = list(map(int, input("Enter array elements: ").split())) # first input istham ex 1 2 3 4 5 ani enter chesa
    #split() idhi striings ni list of strings la covert chesthadhi
    #map anedhi strings ni list laga channge chesthadhi


    d = int(input("Enter number of left rotations: "))
 
    result = rotate_left(arr, d)
    print("Rotated Array:", result)
