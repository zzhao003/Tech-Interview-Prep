// https://leetcode.com/problems/longest-substring-without-repeating-characters/
/* Loop over each element and store them in an obj until a char is repeated.
    When a char is repeated, create a new obj for subsequent chars until the string ends.
      Push the obj into an array.
        Compare the length of the objs and return the longest. */

var lengthOfLongestSubstring = function (s) {
  let array = [];
  let temp = {};
  for (let i = 0; i < s.length; i++) {
    if (temp[s[i]] === undefined) {
      temp[s[i]] = 1;
    } else {
      array.push(Object.keys(temp).length);
      temp = {};
      temp[s[i]] = 1;
    }
  }
  array.push(Object.keys(temp).length);

  for (let i = s.length - 1; i >= 0; i--) {
    if (temp[s[i]] === undefined) {
      temp[s[i]] = 1;
    } else {
      array.push(Object.keys(temp).length);
      temp = {};
      temp[s[i]] = 1;
    }
  }
  array.push(Object.keys(temp).length);

  return Math.max(...array);
};

console.log(lengthOfLongestSubstring("dvdf"));
