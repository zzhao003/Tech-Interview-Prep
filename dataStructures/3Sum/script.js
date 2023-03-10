// sort the array so that no duplicates in output
//for each non repeating el, find the other two els using 2sum2
//push combos where sum=zero into res.

function threeSum(arr) {
  const sortedArr = arr.sort((a, b) => a - b);
  const res = [];

  for (let i = 0; i < sortedArr.length - 3; i++) {
    if (i > 0 && sortedArr[i] === sortedArr[i - 1]) {
      continue;
    }
    let l = i + 1;
    let r = sortedArr.length - 1;
    while (l < r) {
      let sum = sortedArr[i] + sortedArr[l] + sortedArr[r];
      if (sum > 0) {
        r--;
      } else if (sum < 0) {
        l++;
      } else {
        res.push([sortedArr[i], sortedArr[l], sortedArr[r]]);
        l++;
        while (sortedArr[l] == sortedArr[l - 1] && l < r) {
          l++;
        }
      }
    }
  }
  return res;
}

console.log(threeSum([-1, 0, 1, 2, -1, -4]));
