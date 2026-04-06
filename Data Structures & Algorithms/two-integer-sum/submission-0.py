class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, value in enumerate(nums):
            if value in dic:
                return [dic[value], index]
            else:
                dic[target - value] = index

        #Time complexity of O(n)
        #Space complexity of O(n)

        #enumerate prints out the current index and value for example:
        # 0 a 
        # 1 b 
        # 2 c 
