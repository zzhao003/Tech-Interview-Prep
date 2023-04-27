function validateParenthese(str) {
  const hash = { "[": "]", "{": "}", "(": ")" };
  const stack = [str[0]];

  for (let i = 1; i < str.length; i++) {
    if (hash[stack[stack.length - 1]] === str[i]) {
      stack.pop(str[i - 1]);
    } else {
      stack.push(str[i]);
    }
  }
  console.log(stack);
  return stack.length === 0 ? true : false;
}

console.log(validateParenthese("(])"));
