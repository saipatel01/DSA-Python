from typing import List

def reverseString(s: List[str]) -> None:
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Input
s = ["h", "e", "l", "l", "o"]

print("Original array:", s)

# Reverse in-place
reverseString(s)

print("Reversed array:", s)