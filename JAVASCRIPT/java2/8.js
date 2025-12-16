function concat(array) {
  let result = "";
  for (let i = 0; i < array.length; i++) {
    result += array[i];
  }
  return result;
}

// Hardcoded array ohjeen mukaan
const band = ["Johnny", "DeeDee", "Joey", "Marky"];

const combined = concat(band);
document.write(`<p>${combined}</p>`);
