function minimize(point, k) {
  // Write your code here

  const n = point.length;
  //sort the arr in asd order and initialize res
  point.sort((a, b) => a - b);

  let tempMin = point[0];
  let tempMax = point[n - 1];
  let res = tempMax - tempMin;
  //compare each el
  for (let i = 1; i < n; i++) {
    if (point[i] < 0) continue;
    tempMin = Math.min(point[0] + k, point[i] - k);
    tempMax = Math.max(point[i - 1] + k, point[n - 1] - k);
    res = Math.min(res, tempMax - tempMin);
  }
  return res;
}
const point = [0, 1, 2, 3];
const k = 3;
console.log(minimize(point, k));
