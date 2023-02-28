// given an arr return the min max and avg in a obj

const fn = (arr) => {
  const obj = {};
  const arrSorted = arr.sort((a, b) => a - b);
  obj.min = arrSorted[0];
  obj.max = arrSorted[arrSorted.length - 1];
  obj.avg = arrSorted.reduce((acc, crr) => acc + crr, 0) / arrSorted.length;
  return obj;
};

const arr = [1, 5, 10, 33, -4, 0];
console.log(fn(arr));
