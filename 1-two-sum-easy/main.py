class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_backup = nums
        nums = sorted(nums)
        left_inx, right_inx = 0, len(nums) - 1
        while left_inx < right_inx:
            try_sum = nums[left_inx] + nums[right_inx]
            if try_sum == target:
                break
            if try_sum < target:
                left_inx+=1
            else:
                right_inx-=1
        smaller_int, bigger_int = nums[left_inx], nums[right_inx]
        index1 = nums_backup.index(smaller_int)
        # if smaller_int == bigger_int first and last occurence of it will be the solution
        index2 = len(nums) - 1 - nums_backup[::-1].index(bigger_int)
        return [index1, index2]
