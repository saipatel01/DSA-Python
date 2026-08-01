def maxSubArray(nums):
    curr_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        if curr_sum < 0:
            curr_sum = nums[i]
        else:
            curr_sum += nums[i]

        max_sum = max(max_sum, curr_sum)

    return max_sum


# Driver Code
nums = list(map(int, input("Enter array elements: ").split()))

answer = maxSubArray(nums)

print("Maximum Subarray Sum:", answer)