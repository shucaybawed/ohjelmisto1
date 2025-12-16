const confirmCalc = confirm("Should I calculate the square root?");

if (confirmCalc) {
  const number = Number(prompt("Enter a number:"));

  if (number < 0) {
    document.write("<p>The square root of a negative number is not defined.</p>");
  } else {
    const result = Math.sqrt(number);
    document.write(`<p>Square root: ${result}</p>`);
  }
} else {
  document.write("<p>The square root is not calculated.</p>");
}
