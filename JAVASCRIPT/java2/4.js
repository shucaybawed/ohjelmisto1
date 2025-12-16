const nums = [];
let input;

while (true) {
  input = Number(prompt("Anna numero (0 lopettaa):"));
  if (input === 0) break;
  nums.push(input);
}

nums.sort((a, b) => b - a);
console.log(nums);
