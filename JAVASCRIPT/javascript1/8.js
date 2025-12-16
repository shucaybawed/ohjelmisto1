const rolls = Number(prompt("How many dice rolls?"));
let sum = 0;

for (let i = 0; i < rolls; i++) {
  const roll = Math.floor(Math.random() * 6) + 1;
  sum += roll;
}

document.write(`<p>Sum of dice rolls: ${sum}</p>`);
