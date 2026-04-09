class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i] 
                count += 1

        return count 



        # just rebuild the array, no need to pop, just reassign the numbers 
        # You were checking if it was in the array 
        # You want to check if its not in the array 
        
        
        