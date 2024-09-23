function pascalTriangle(n) {
  let triangle = new Array(n).fill(null).map(() => []);
  console.log(triangle);

  for (let i = 0; i < n; i++) {
    triangle[i] = new Array(i + 1).fill(1);
    console.log(triangle);
    for (let j = 0; j <= i; j++) {
      // The first and last elements of each row are 1
      if (j === 0 || j === i) {
        triangle[i][j] = 1;
      } else {
        // Other elements are the sum of the two elements above
        triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
      }
    }
  }

  return triangle;
}

console.log(pascalTriangle(5));
