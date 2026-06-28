const auditButton = document.getElementById("audit-btn");
const urlInput = document.getElementById("url");

const loading = document.getElementById("loading");
const results = document.getElementById("results");

const score = document.getElementById("score");
const pages = document.getElementById("pages");
const issues = document.getElementById("issues");

auditButton.addEventListener("click", () => {

    const url = urlInput.value.trim();

    if (url === "") {
        alert("Please enter a website URL.");
        return;
    }

    results.classList.add("hidden");
    loading.classList.remove("hidden");

    auditButton.disabled = true;
    auditButton.textContent = "Auditing...";

    setTimeout(() => {

        loading.classList.add("hidden");
        results.classList.remove("hidden");

        animateNumber(score, 82, "/100");
        animateNumber(pages, 8);
        animateNumber(issues, 14);

        auditButton.disabled = false;
        auditButton.textContent = "Audit Website";

    }, 2000);

});


function animateNumber(element, target, suffix = "") {

    let current = 0;

    const step = Math.ceil(target / 30);

    const interval = setInterval(() => {

        current += step;

        if (current >= target) {

            current = target;

            clearInterval(interval);

        }

        element.textContent = current + suffix;

    }, 25);

}
