//loop over the element and pop each el into a stack until a operand is found
//do the operation with the 2 els in front and pop them off the stack
//continue until theres nothing in the stack

var evalRPN = function (tokens) {
  const stack = [];

  for (let i = 0; i < tokens.length; i++) {
    if (tokens[i] == "+") {
      stack.push(stack.pop() + stack.pop());
    } else if (tokens[i] == "-") {
      let a = stack.pop();
      let b = stack.pop();
      stack.push(b - a);
    } else if (tokens[i] == "*") {
      stack.push(stack.pop() * stack.pop());
    } else if (tokens[i] == "/") {
      let a = stack.pop();
      let b = stack.pop();
      stack.push(Math.trunc(b / a));
    } else {
      stack.push(+tokens[i]);
    }
  }

  return stack[0];
};

const test = [
  "10",
  "6",
  "9",
  "3",
  "+",
  "-11",
  "*",
  "/",
  "*",
  "17",
  "+",
  "5",
  "+",
];
Output: 22;
console.log(evalRPN(test));
