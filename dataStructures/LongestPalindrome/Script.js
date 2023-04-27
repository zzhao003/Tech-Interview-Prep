//count the appearance of each letter in the string
//add all the even numbers
//add the greatest odd number

const test = "ccc";

var longestPalindrome = function (s) {
  const count = {};
  let res = 0;
  let Odd = 0;
  for (let i = 0; i < s.length; i++) {
    if (!count[s[i]]) count[s[i]] = 1;
    else count[s[i]]++;
  }
  if (Object.keys(count).length === 1) return count[s[0]];

  for (const key in count) {
    if (count[key] % 2 === 0) res += count[key];
    else {
      res += count[key] - 1;
      Odd++;
    }
  }
  return Odd ? res + 1 : res;
};

console.log(longestPalindrome(test));
