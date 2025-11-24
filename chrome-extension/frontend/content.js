function extractComments() {
    let comments = [];
    document.querySelectorAll('#content-text').forEach(el => {
        comments.push(el.textContent.trim());
    });
    console.log("Extracted comments:", comments); // Debug
    return comments.slice(0, 50);
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "get_comments") {
        sendResponse({ comments: extractComments() });
    }
});
