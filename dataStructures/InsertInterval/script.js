var insert = function (intervals, newInterval) {
  //loop over the intervals arr
  //if startNewI falls within any interval, take the lower boundry,
  //check if endNewI falls within any interval, take the upper boundry.
  //push [lower, upper] into stack
  // push the rest of the intervals into stack
  const stack = [];
  let lower;
  let upper;
  for (let i = 0; i < intervals.length; i++) {
    if (
      newInterval[0] >= intervals[i][0] &&
      newInterval[0] <= intervals[i][1]
    ) {
      lower = intervals[i][0];
    } else if (
      newInterval[1] >= intervals[i][0] &&
      newInterval[1] <= intervals[i][1]
    ) {
      upper = intervals[i][1];
      stack.push([lower, upper]);
    } else {
      stack.push(intervals[i]);
    }
  }
  return stack;
};

const intervals = [
  [1, 3],
  [6, 9],
];
const newInterval = [2, 5];

console.log(insert(intervals, newInterval));
