//greatCommonDivisor

function euclideanAlgorithm(a, b) {
  let a = Math.abs(a);
  let b = Math.abs(b);
  while (a != 0 && b != 0 && a != b) {
    [a, b] = a > b ? [a - b, b] : [a, b - a];
  }
  return a || b;
}
