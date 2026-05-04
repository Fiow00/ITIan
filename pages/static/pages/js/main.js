document.getElementById("hamburger").addEventListener("click", function() {
    const menu = document.getElementById("mobileMenu");
    const btn = document.getElementById("hamburger");
    menu.classList.toggle("show");
    btn.classList.toggle("open");
});