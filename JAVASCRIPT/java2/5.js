const values = [];
let number;

while (true) {
  number = Number(prompt("Anna numero:"));

  if (values.includes(number)) {
    alert("Numero on jo annettu!");
    break;
  }

  values.push(number);
}

values.sort((a, b) => a - b);
console.log(values);
