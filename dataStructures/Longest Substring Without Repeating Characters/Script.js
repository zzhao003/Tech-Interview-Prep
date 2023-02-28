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

// console.log(lengthOfLongestSubstring("dvdf"));
//Test case = 'abcabcbb'

//sliding window method
// travese the right pointer and store el in a set and update max length, until duplicate is found
// then increment the left pointer and continue treversing the right pointer and update max length
//return max value

const slidingWindow = (arr) => {
  let l = 0;
  let max = 0;
  cache = {};
  for (let r = 0; r < arr.length; r++) {
    while (arr[r] in cache) {
      delete cache[arr[l]];
      l++;
    }
    cache[arr[r]] = 1;
    max = Math.max(max, r - l + 1);
  }
  return max;
};

const arr = "abcabcbb";
console.log(slidingWindow(arr));
