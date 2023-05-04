var maxDepth = function (root) {
  const dfs = (root) => {
    if (!root) return 0;

    let left = dfs(root.left);
    let right = dfs(root.right);
    return 1 + Math.max(left, right);
  };
  return dfs(root);
};
