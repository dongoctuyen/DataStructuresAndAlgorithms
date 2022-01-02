"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
    1 <= k <= nums.length <= 10**4
    -10**4 <= nums[i] <= 10**4
"""
from Algorithms.Core.Application.QuickSelect import quick_select


def findKthLargest(nums: list[int], k: int) -> int:
    length = len(nums)
    k_index = length - k
    quick_select(1, length - 1, k_index, nums)
    return nums[k_index]

if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(findKthLargest(nums, k))
