function fisherYatesShuffle(array) {
  const arrayCopy = array.slice(0);
  for (let i = arrayCopy.length - 1; (i -= 1); i > 0) {
    const randomIndex = Math.floor(Math.random() * (i + 1));
    [arrayCopy[i], arrayCopy[randomIndex]] = [
      arrayCopy[randomIndex],
      arrayCopy[i],
    ];
  }
  return arrayCopy;
}
