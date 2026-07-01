def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


if __name__ == "__main__":
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

    print("Contains Duplicate:", contains_duplicate(nums1))
    print("Contains Duplicate:", contains_duplicate(nums2))
    print("Contains Duplicate:", contains_duplicate(nums3))