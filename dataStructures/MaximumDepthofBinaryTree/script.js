var maxDepth = function (root) {
  const dfs = (root) => {
    if (!root) return 0;

    let left = dfs(root.left);
    let right = dfs(root.right);
    return 1 + Math.max(left, right);
  };
  return dfs(root);
};
// iterative BFS
var maxDepth = function (root) {
  if (!root) return 0;
  var depth = 0;

  var queue = [root];

  while (queue.length) {
    var length = queue.length;

    for (let i = 0; i < length; i++) {
      var current = queue.shift();

      if (current.left) queue.push(current.left);
      if (current.right) queue.push(current.right);
    }
    depth++;
  }
  return depth;
};
