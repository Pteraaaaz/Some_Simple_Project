// Menu toggle for phones
document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('nav');

    if (!toggle || !nav) return;
    
    toggle.addEventListener('click', () => {
        nav.classList.toggle('active');
    });
});

// For counter feature in productPage
let count = 0;
const countDisplay = document.getElementById("count");
const plusBtn = document.getElementById("plus");
const minBtn = document.getElementById("minus");

plusBtn.addEventListener("click", () => {
    count++;
    countDisplay.textContent = count;
});

minBtn.addEventListener("click", () => {
    if (count > 0) {
        count--;
        countDisplay.textContent = count;
    }
});