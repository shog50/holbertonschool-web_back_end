export default function cleanSet(set, startString) {
  return [...set]
    .filter((value) => value.startsWith(startString) && startString !== '')
    .map((value) => value.slice(startString.length))
    .join('-');
}

