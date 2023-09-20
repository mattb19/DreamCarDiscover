const myBtn = document.getElementById("login");
myBtn.addEventListener("click", function(e) {
    document.getElementById("welcome").style.animationName = "welcomeOut";
    document.getElementById("welcome").style.animationDelay = "0s";
    document.getElementById("welcome2").style.animationName = "welcomeOut2";
    document.getElementById("welcome2").style.animationDelay = "0s";
    document.getElementById("login").style.animationName = "plateOut";
    document.getElementById("login").style.animationDelay = "0s";
    document.getElementById("bmwFront").style.animationName = "carOut";
    document.getElementById("bmwFront").style.opacity = "1.0";
    document.getElementById("bmwFront").style.animationDelay = "1.2s";
    setTimeout(loginPage, 2500)
});

function loginPage() {
    window.location.href = "/login"
}