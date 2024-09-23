function nestedWeightSum(array, depth = 1) {
  let sum = 0;
  for (let i = 0; i < array.length; i++) {
    if (typeof array[i] == "number") {
      sum += array[i] * depth;
    } else {
      sum += nestedWeightSum(array[i], depth + 1);
    }
  }
  return sum;
}

console.log(nestedWeightSum([1, [1, 2, 3], [[[2]]], 2, [2]]));
