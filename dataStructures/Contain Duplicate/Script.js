var containsDuplicate = function (nums) {
  const set = new Set(nums);
  // console.log(set.size);

  return !(set.size === nums.length);
};

const testCase = [1, 2, 3, 1];
containsDuplicate(testCase);
