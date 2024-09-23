function leastCommonMultiple(a, b) {
  let a = Math.abs(a);
  let b = Math.abs(b);
  return a === 0 || b === 0 ? 0 : Math.abs(a * b) / euclideanAlgorithm(a, b);
}
