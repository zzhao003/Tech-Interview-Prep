//remove deplicates in a array

const removeDuplicte = (arr) => {
  const newArr = new Set(arr);
  return newArr;
};

const arr = [1, 1, 1, 2, 1, 3];
console.log(removeDuplicte(arr));
