var majorityElement = function (nums) {
  let result = {};

  for (let i = 0; i < nums.length; i++) {
    if (result[nums[i]]) {
      result[nums[i]]++;
    } else {
      result[nums[i]] = 1;
    }
  }
  console.log(result);
};

// majorityElement([2, 2, 1, 1, 1, 2, 2]);

// Could you solve the problem in linear time and in O(1) space?
var majorityElement2 = function (nums) {
  let res = 0;
  let counter = 0;

  for (let i = 0; i < nums.length; i++) {
    counter === 0 ? (res = nums[i]) : null;
    nums[i] === res ? counter++ : counter--;
  }
  return res;
};
console.log(majorityElement2([2, 2, 1, 2, 1, 3, 2, 2, 1, 4, 2]));
