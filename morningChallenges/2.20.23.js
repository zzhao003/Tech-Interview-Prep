const findCountAndSum = (arr) => {
  const count = arr.filter((item) => item >= 0).length;
  const sum = arr.filter((item) => item < 0).reduce((acc, crr) => acc + crr, 0);
  return [count, sum];
};

const arr = [-2, 0, 4, 1, -1];
console.log(findCountAndSum(arr));
