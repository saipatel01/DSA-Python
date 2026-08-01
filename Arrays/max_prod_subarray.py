def maxProduct(nums):
    max_product = nums[0]
    min_product = nums[0]
    answer = nums[0]

    for i in range(1, len(nums)):

        # If current number is negative, swap
        if nums[i] < 0:
            max_product, min_product = min_product, max_product

        # Update maximum product
        max_product = max(nums[i], max_product * nums[i])

        # Update minimum product
        min_product = min(nums[i], min_product * nums[i])

        # Update overall answer
        answer = max(answer, max_product)

    return answer

nums = list(map(int, input("Enter array elements: ").split()))

result = maxProduct(nums)

print("Maximum Product Subarray:", result)