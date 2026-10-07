class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 0이 아닌 숫자가 새로 둘어와서 삽입될 위치(인덱스)
        insert_pos = 0

        for i, num in enumerate(nums):
            if num != 0:
                if i != insert_pos:
                    nums[i], nums[insert_pos] = nums[insert_pos], nums[i]
                insert_pos += 1
