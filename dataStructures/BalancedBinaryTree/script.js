var isBalanced = function (root) {
  const dfs = (root) => {
    if (!root) return [true, 0];
    //if root is null return true and height of 0

    let left = dfs(root.left);
    let right = dfs(root.right);
    let balanced = left[0] && right[0] && Math.abs(left[1] - right[1]) <= 1;
    return [balanced, 1 + Math.max(left[1], right[1])];
  };
  return dfs(root)[0];
};
