class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res

# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums = sorted(nums)
#         list_ = []
#         if len(nums)<3 or nums[0]>0:
#             return list_
#         for i in range(len(nums) - 2):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             j = i + 1
#             k = len(nums) - 1
#             while j < k:
#                 if nums[j] + nums[k] == -nums[i]:
#                     list_.append([nums[i], nums[j], nums[k]])
#                     while j < k-1 and nums[k-1]==nums[k]:
#                         k -=1
#                     while j+1 < k and nums[j+1]==nums[j]:
#                         j +=1
#                     j +=1
#                     k -=1
#                 elif nums[j] + nums[k] > -nums[i]:
#                     k-=1
#                 else:
#                     j+=1
#         return list_


    # def threeSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     all_list = self.get_all_list(nums)
    #     result = [[l[0], l[1], l[2]] for l in all_list if sum(l) == 0]
    #     return result

    # def get_all_list(self, nums):
    #     length = len(nums)
    #     all_list = []
    #     for i in range(length - 2):
    #         for j in range(i + 1, length - 1):
    #             if i == j:
    #                 continue
    #             for k in range(j + 1, length):
    #                 if k == j or k == i:
    #                     continue
    #                 if (nums[i], nums[j], nums[k])in all_list or (nums[i], nums[k], nums[j]) in all_list or (nums[j], nums[i], nums[k]) in all_list or (
    #                 nums[j], nums[k], nums[i]) in all_list or (nums[k], nums[i], nums[j]) in all_list or (
    #                 nums[k], nums[j], nums[i]) in all_list:
    #                     continue
    #                 all_list.append((nums[i], nums[j], nums[k]))
    #     return all_list
