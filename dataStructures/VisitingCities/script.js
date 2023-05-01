function minimumCost(red, blue, blueCost) {
  let redArr;
  let blueArr;
  let res;
  redArr.push(0);
  blueArr.push(0);
  res.push(0);
  for (let i = 0; i < red.length; i++) {
    redArr[i] = Math.min(redArr[i - 1] + red[i], blueArr[i - 1] + red[i]);
    redArr[i] = Math.min(redArr[i - 1] + red[i], blueArr[i - 1] + red[i]);
  }
}
