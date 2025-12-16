const dogs = [];

for (let i = 0; i < 6; i++) {
  dogs.push(prompt("Anna koiran nimi:"));
}

dogs.sort().reverse();

document.write("<ul>");
for (const dog of dogs) {
  document.write(`<li>${dog}</li>`);
}
document.write("</ul>");
