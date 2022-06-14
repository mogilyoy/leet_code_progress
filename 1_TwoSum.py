""" The first variant was like"""
# class Solution:
#     def twoSum(self, nums, target):
#         for i in nums:
#             fst = self.bin_search(i, nums)
#             scd = self.bin_search(target - i, nums)
#             if fst != scd != -1:
#                 return [fst, scd]
#             elif fst == scd:
#                 scd = self.bin_search(target - i, nums[scd:]) + 1
#                 return [fst, scd]
#             else: 
#                 return '??'
        
#     def bin_search(self, number, lst):
#         left = 0
#         right = len(lst) - 1
#         pos = len(lst) // 2
#         while lst[pos] != number and left < right:
#             if lst[pos] > number:
#                 right = pos - 1
#             else: 
#                 left = pos + 1
#             pos = (left + right) // 2
#         return -1 if left > right else pos
"""But it doesnt work when we have a list of the same numbers, for example: when we want to find '3' in the '[3, 3]' array it would return 1, cause default value of 'pos' here is 1"""


"""So I came up with using hash map"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {value: i for i, value in enumerate(nums)}
        for i in range(len(nums)):
            fst = nums[i]
            scd = target - fst
            if fst + scd == target and data[fst] != data[scd]:
                try:
                    return [data[fst], data[scd]]
                except KeyError:
                    i += 1
                    if i>1000:
                        break

'''So it doesnt work( Will return later'''


