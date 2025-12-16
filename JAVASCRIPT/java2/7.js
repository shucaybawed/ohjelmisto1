function rollDice(sides) {
  return Math.floor(Math.random() * sides) + 1;
}

const sides = Number(prompt("Anna nopan sivujen määrä:"));

document.write("<ul>");

let roll;
do {
  roll = rollDice(sides);
  document.write(`<li>${roll}</li>`);
} while (roll !== sides);

document.write("</ul>");
