const count = Number(prompt("Osallistujien määrä:"));
const participants = [];

for (let i = 0; i < count; i++) {
  participants.push(prompt("Anna nimi:"));
}

participants.sort();

document.write("<ol>");
for (const name of participants) {
  document.write(`<li>${name}</li>`);
}
document.write("</ol>");
