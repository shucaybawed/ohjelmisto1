function showResults(data) {
  resultsDiv.innerHTML = ""; // 🔹 tyhjennä vanhat tulokset

  for (const tvShow of data) {
    const article = document.createElement("article");

    // Name
    const name = document.createElement("h2");
    name.textContent = tvShow.show.name;

    // Link
    const link = document.createElement("a");
    link.href = tvShow.show.url;
    link.textContent = "Show details";
    link.target = "_blank";

    // Image (optional chaining)
    const img = document.createElement("img");
    img.src = tvShow.show.image?.medium || "";
    img.alt = tvShow.show.name;

    // Summary (already contains <p>)
    const summary = document.createElement("div");
    summary.innerHTML = tvShow.show.summary || "No summary available.";

    // Append elements
    article.appendChild(name);
    article.appendChild(link);
    article.appendChild(img);
    article.appendChild(summary);

    resultsDiv.appendChild(article);
  }
}
