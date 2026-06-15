class Solution:
    def twoSum(self, nums, target):
        mp = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in mp:
                return [mp[complement], i]

            mp[num] = i

        return [-1, -1]


# Driver Code
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    sol = Solution()
    result = sol.twoSum(nums, target)

    print("Indices:", result)