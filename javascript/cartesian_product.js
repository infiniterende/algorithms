function getCartesianProduct(setA, setB) {
  output = [];
  for (let i = 0; i < setA.length; i++) {
    for (let j = 0; j < setB.length; j++) {
      output.push([setA[i], setB[j]]);
    }
  }
  return output;
}
