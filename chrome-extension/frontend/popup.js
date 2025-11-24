let lastResults = [];

// Analyze button fetches comments and predicts sentiment
document.getElementById("analyze").onclick = function() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, {action: "get_comments"}, function(response) {
            if (response && response.comments.length > 0) {
                fetch("https://adamEl26-Youtube-Comment-analyzer.hf.space/predictbatch", {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify({comments: response.comments})
                }).then(apiResponse => apiResponse.json())
                  .then(result => {
                    lastResults = result.results;
                    renderComments(lastResults, document.getElementById("filter").value);
                    showStats(lastResults);
                }).catch(err => {
                    document.getElementById("results").innerText = "API fetch failed: " + err;
                });
            } else {
                document.getElementById("results").innerText = "No comments found.";
                document.getElementById("stats").innerText = "";
            }
        });
    });
};

// Displays comments filtered by sentiment
function renderComments(results, filterVal = "all") {
    const colors = {"1": "positive", "0": "neutral", "-1": "negative"};
    let filtered = (filterVal === "all") ? results : results.filter(r => String(r.sentiment) === filterVal);
    document.getElementById("results").innerHTML = filtered.map(r =>
      `<div class="comment ${colors[String(r.sentiment)]}">${r.comment} (${r.sentiment}${r.confidence !== undefined ? ", conf: " + r.confidence.toFixed(2) : ""})</div>`
    ).join('');
}

// Show global statistics as percent and count
function showStats(results) {
    let stats = {"1":0, "0":0, "-1":0};
    results.forEach(r => { stats[String(r.sentiment)]++; });
    let total = results.length;
    let statText = total === 0 ? "" :
      `Positives: ${(stats["1"]/total*100).toFixed(1)}% (${stats["1"]})<br>` +
      `Neutrals: ${(stats["0"]/total*100).toFixed(1)}% (${stats["0"]})<br>` +
      `Negatives: ${(stats["-1"]/total*100).toFixed(1)}% (${stats["-1"]})<br>`;
    document.getElementById("stats").innerHTML = statText;
}

// Filter dropdown changes displayed results
document.getElementById("filter").onchange = function() {
    renderComments(lastResults, this.value);
};

// Copy results to clipboard
document.getElementById("copy").onclick = function() {
    let text = document.getElementById("results").innerText;
    if (text.trim().length === 0) {
      alert("No results to copy!");
      return;
    }
    navigator.clipboard.writeText(text);
    alert("Results copied to clipboard!");
};

// Toggle dark/light mode
document.getElementById("toggle-mode").onclick = function() {
  document.body.classList.toggle("light");
};
