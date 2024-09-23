function primeFactors(n) {
  let nn = n;
  let factors = [];
  for (let i = 2; i < Math.sqrt(nn); i++) {
    while (nn % i == 0) {
      nn /= i;
      factors.push(i);
    }
    if (nn > 1) {
      factors.push(nn);
    }
  }
  return factors;
}
