const form = document.getElementById("search-form");
const queryInput = document.getElementById("query");
const resultsDiv = document.getElementById("results");

form.addEventListener("submit", function (event) {
  event.preventDefault(); // estää sivun uudelleenlatauksen

  const query = queryInput.value;
  const url = `https://api.tvmaze.com/search/shows?q=${query}`;

  fetch(url)
    .then(response => response.json())
    .then(data => {
      console.log(data); // 🔹 vaadittu: tulostus consoleen

      showResults(data);
    })
    .catch(error => {
      console.error("Error:", error);
    });
});
