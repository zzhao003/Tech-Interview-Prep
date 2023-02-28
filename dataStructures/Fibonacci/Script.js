//[0,1,1,2,3,5,8,13,21,34,55,89]
// recursion
let counter = 0;
const fiboRecursion = (n) => {
  counter++;
  if (n < 2) {
    return n;
  }
  return fiboRecursion(n - 1) + fiboRecursion(n - 2);
};

// console.log("fiboRecursion:", fiboRecursion(8));
// console.log(counter);

// recursion optimized with memoization
const fibo2Master = () => {
  const cache = {};
  return function fibo2(n) {
    counter++;
    if (n in cache) {
      return cache[n];
    } else {
      if (n < 2) {
        return n;
      }
      cache[n] = fibo2(n - 2) + fibo2(n - 1);
      return cache[n];
    }
  };
};

const fibo2 = fibo2Master();
// console.log("fibo2:", fibo2(8));
// console.log(counter);

//Iteration method
const fiboIt = (n) => {
  let arr = [0, 1];

  for (let i = 2; i <= n; i++) {
    arr.push(arr[i - 1] + arr[i - 2]);
  }

  return arr[n];
};

console.log("fitIt:", fiboIt(8));
