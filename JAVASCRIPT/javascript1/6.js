const year = Number(prompt("Enter a year:"));
let leapYear;

if (year % 400 === 0) {
  leapYear = true;
} else if (year % 100 === 0) {
  leapYear = false;
} else if (year % 4 === 0) {
  leapYear = true;
} else {
  leapYear = false;
}

document.write(
  `<p>${year} is ${leapYear ? "" : "not "}a leap year.</p>`
);
