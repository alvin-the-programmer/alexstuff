# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swapped = True
        while swapped:
          swapped = False
          # [1,0,3,0,12]
          # [1,3,12,0,0]
          for idx, num in enumerate(nums):
            if num == 0 and idx != (len(nums) - 1) and nums[idx + 1] != 0:
              temp = nums[idx + 1]
              nums[idx + 1] = num
              nums[idx] = temp
              swapped = True

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
      zero_idx = 0
      nonzero_idx = 0

      found_zero = False
      found_num = False
      while :
        for idx in range(len(nums)):
          curr = nums[idx]
          if curr == 0 and found_zero == False:
            zero_idx = idx
            found_zero = True
          if curr != 0 and found_zero == True and found_num == False:
            nonzero_idx = idx
            found_num = True

      
      def moveZeroes(self, nums: List[int]) -> None:
        last_zero_idx = 0
        for idx in range(len(nums)):
          curr = nums[idx]
          if curr != 0:
            nums[last_zero_idx] = nums[idx]
            last_zero_idx += 1

        for idx in range(last_zero_idx, len(nums)):
          nums[idx] = 0
      
                
                # pointer_idx = 3
                # zeroes = 2
                # [1,3,0,0,12]
               

               

void moveZeroes(vector<int>& nums) {
    int lastNonZeroFoundAt = 0;
    // If the current element is not 0, then we need to
    // append it just in front of last non 0 element we found. 
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != 0) {
            nums[lastNonZeroFoundAt++] = nums[i];
        }
    }
 	// After we have finished processing new elements,
 	// all the non-zero elements are already at beginning of array.
 	// We just need to fill remaining array with 0's.
    for (int i = lastNonZeroFoundAt; i < nums.size(); i++) {
        nums[i] = 0;
    }
}

  lnzfa = 3
 nums = [1,3,12,0,0]
                  

