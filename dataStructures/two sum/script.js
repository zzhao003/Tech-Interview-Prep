var twoSum = function (nums, target) {
  const obj = {};

  for (let i = 0; i < nums.length; i++) {
    obj[nums[i]] = i;
  }

  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];
    if (obj[diff]) {
      console.log([i, obj[diff]]);
    }
  }
};

const nums = [3, 2, 4];
const target = 6;

// twoSum(nums, target);

var twoSum2 = function (nums, target) {
  const obj = {};

  for (let i = 0; i < nums.length; i++) {
    const current = nums[i];
    const complement = target - current;
    obj[complement] = i;
    console.log(current);
    console.log(obj);
    console.log(obj[current]);
    if (obj[current] !== undefined) {
      //ZERO IS FALSY!!!! obj[current] is 0;
      console.log("twosum2:", [obj[current], i]);
      return;
    }
  }
  return [];
};

twoSum2(nums, target);

// ----------------------------------------
const twoSum3 = (array, goal) => {
  let memo = {};
  let complement;
  for (let i = 0; i < array.length; i++) {
    complement = goal - array[i];
    memo[array[i]] = complement;
    console.log(memo);

    if (memo[complement]) {
      console.log("complement", complement);
      return [array.indexOf(complement), array.indexOf(array[i])];
    }
  }
  return [];
};

// console.log("twoSum3:", twoSum3(nums, target));
