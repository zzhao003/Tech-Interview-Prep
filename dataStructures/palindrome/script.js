var isPalindrome = function (s) {
  const alphArr = "0123456789abcdefghijklmnopqrstuvwxyz".split("");

  //to lowercase to array.
  s = s.toLowerCase().split("");
  // console.log(s);
  const temp = [];

  //remove spaces
  //remove punctruation
  for (let i = 0; i < s.length; i++) {
    if (s.length === 0) {
      return true;
    }
    if (alphArr.includes(s[i])) {
      temp.push(s[i]);
    }
  }
  console.log("19", temp.join(""));
  const temp2 = temp.slice().reverse(); // .reverse() mutates the original array!!!
  console.log("21", temp2.join(""));
  const tempJoined = temp.join("");
  const temp2Joined = temp2.join("");
  console.log("24", tempJoined);
  console.log("25", temp2Joined);
  if (tempJoined === temp2Joined) {
    console.log(tempJoined);
    console.log(temp2Joined);
    return true;
  }
  //reverse the string with a for loop, push the element into an []
  //or reverse the arr with .reverse()  O(n)
  //compare the two arrs
};

// console.log(isPalindrome("race a car"));
// ABOVE SOLOTION DOES NOT WORK WHEN THERE IS NUMBERS********************

var isPalindrome2 = function (s) {
  const alphArr = "0123456789abcdefghijklmnopqrstuvwxyz".split("");

  //to lowercase to array.
  s = s.toLowerCase().split("");

  // 0 1 2 3 4
  let l = 0;
  let r = s.length - 1;
  while (l < r) {
    while (l < r && !alphArr.includes(s[l])) {
      l++;
    }
    while (l < r && !alphArr.includes(s[r])) {
      r--;
    }
    if (s[l] !== s[r]) {
      return false;
    }
    l++;
    r--;
  }
  return true;
};

console.log(isPalindrome2(" "));
