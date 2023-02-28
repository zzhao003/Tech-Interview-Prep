let conter = 0;
const fibo = (n) => {
  conter++;
  if (n < 2) {
    return n;
  }
  return fibo(n - 1) + fibo(n - 2);
};

console.log(fibo(30));
console.log(conter);
