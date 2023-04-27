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

// const testCase = [7, 1, 5, 3, 6, 4];
// console.log(fn(testCase));

//------------------------------------ nested for loop
const fn2 = (arr) => {
  let diff = 0;
  for (let i = 0; i < arr.length - 1; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      const temp = arr[j] - arr[i];

      if (temp > diff) {
        diff = temp;
      }
    }
  }
  return diff;
};

const testCase = [];
console.log(fn2(testCase));
