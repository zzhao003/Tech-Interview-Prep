//construct a prefix and a postfix array.
//each el should have the value of prefix times postfix
const fn = (arr) => {
  const pre = [1];
  const post = [1];
  for (let i = 1; i < arr.length; i++) {
    pre.push(arr[i - 1] * pre[i - 1]);
  }
  for (let i = arr.length - 2; i >= 0; i--) {
    post.unshift(arr[i + 1] * post[0]);
  }

  console.log(pre * post);
};

const arr = [1, 2, 3, 4];
fn(arr);
