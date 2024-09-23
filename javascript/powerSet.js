function powerSet(
  originalSet,
  allSubsets = [[]],
  currentSet = [],
  startAt = 0
) {
  for (let i = startAt; i < originalSet.length; i++) {
    currentSet.push(originalSet[i]);
    allSubsets.push([...currentSet]);
    powerSet(originalSet, allSubsets, currentSet, startAt + 1);
    currentSet.pop();
  }
  return allSubsets;
}
