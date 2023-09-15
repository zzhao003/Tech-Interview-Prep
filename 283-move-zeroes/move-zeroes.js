/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
        let insertPosition = 0;

    for (let i = 0; i < nums.length; i++) {
      // FIll all non-zero numbers
      if (nums[i] != 0) {
        nums[insertPosition] = nums[i];
        insertPosition++;
      }
    }

    while (insertPosition < nums.length) {
      nums[insertPosition++] = 0;
    }
  }
