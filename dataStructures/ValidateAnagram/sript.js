var isAnagram = function (s, t) {
  if (s.length !== t.length) {
    return false;
  }
  const hash = {};

  for (let i = 0; i < s.length; i++) {
    hash[s[i]] ? hash[s[i]]++ : (hash[s[i]] = 1);
  }
  for (let i = 0; i < t.length; i++) {
    hash[t[i]] ? hash[t[i]]-- : false;
  }
  if (!Object.values(hash).reduce((crr, acc) => (acc += crr), 0)) {
    return true;
  } else {
    return false;
  }
};
