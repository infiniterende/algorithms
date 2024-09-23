import isPrime from "./isPrime.mjs ";
function sieve(n) {
  let res = [];
  for (let i = 2; i < n; i++) {
    if (isPrime(i)) {
      res.push(i);
    }
  }
  return res;
}

console.log(sieve(10));
