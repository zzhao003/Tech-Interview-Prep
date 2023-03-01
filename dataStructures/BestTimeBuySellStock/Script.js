//two pointer technique.

const fn = (arr) => {
  let l = 0;
  let maxP = 0;
  for (let r = 1; r < arr.length; r++) {
    if (arr[l] < arr[r]) {
      maxP = Math.max(maxP, arr[r] - arr[l]);
    } else {
      l = r;
    }
  }
  return maxP;
};

const testCase = [7, 1, 5, 3, 6, 4];
console.log(fn(testCase));
