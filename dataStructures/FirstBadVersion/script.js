var solution = function (isBadVersion) {
  /**
   * @param {integer} n Total versions
   * @return {integer} The first bad version
   */
  return function (n) {
    let bad = n.length;
    let l = 1;
    let r = n.length;
    while (l <= r) {
      let mid = Math.floor((l + r) / 2);
      if (isBadVersion(mid)) {
        bad = mid;
        r = mid - 1;
      } else {
        l = mid + 1;
      }
    }
    return bad;
  };
};
