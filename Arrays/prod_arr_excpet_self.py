def productExceptSelf(nums):

    n = len(nums)
    answer = [1] * n
    prefix = 1

    for i in range(n):

        # Store product of all elements to the LEFT of i
        answer[i] = prefix

        # Include current element for next iteration
        prefix *= nums[i]

    # At this point:
    # nums   = [1,2,3,4]
    # answer = [1,1,2,6]

    suffix = 1

    for i in range(n - 1, -1, -1):

        # Multiply current answer (left product)
        # with right side product
        answer[i] *= suffix

        # Include current element for next iteration
        suffix *= nums[i]

    return answer


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))