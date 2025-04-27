document.getElementById("darkModeToggle").addEventListener("click", function() {
    const darkModeToggle = document.getElementById("darkModeToggle");
    const body = document.body;
    document.querySelectorAll('input[type="text"], textarea').forEach((v) => {
        v.classList.toggle('black-bg-input');
        v.classList.toggle('text-black');
    });
    body.classList.toggle("light-mode");
    body.classList.toggle("bg-gray-900");
    body.classList.toggle("text-white");

    if (localStorage.getItem("theme") === "light") {
        darkModeToggle.innerText = "☀️";
        localStorage.setItem("theme", 'dark');
    }
    else {
        darkModeToggle.innerText = "🌙";
        localStorage.setItem("theme", 'light')
    }
});


const text = "Hi, I'm Erri4!";
let index = 0;
function gettheme() {
    if (localStorage.getItem("theme") === "light") {
        darkModeToggle.innerText = "🌙";
        const body = document.body;
        body.classList.toggle("light-mode");
        body.classList.toggle("bg-gray-900");
        body.classList.toggle("text-white");
        document.querySelectorAll('input[type="text"], textarea').forEach((v) => {
            v.classList.toggle('black-bg-input');
            v.classList.toggle('text-black');
        });
    }
}
function typeEffect() {
    if (index < text.length) {
        document.getElementById("intro-text").innerHTML += text.charAt(index);
        index++;
        setTimeout(typeEffect, 100);
    }
}
document.addEventListener("DOMContentLoaded", gettheme);
document.addEventListener("DOMContentLoaded", typeEffect);
