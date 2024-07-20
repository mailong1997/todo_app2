// Retrieve todo from local storage or initialize an empty array
const loginButton = document.getElementById("login-btn");
const registerButton = document.getElementById("register-btn");

// Initialize
document.addEventListener("DOMContentLoaded", function () {
  loginButton.addEventListener('click',login);
  registerButton.addEventListener('click',register)
});

function login(){
    window.location.href = "/login-rq";
    fetch('/login-rq', {
        method: 'POST',
    })
    .then(response => {
        // Chuyển hướng đến trang 
        window.location.href = "/login-rq";
    })
    .catch(error => {
        console.error('Error:', error);
    });

}

function register(){
    fetch('/register-rq', {
        method: 'POST',
    })
    .then(response => {
        // Chuyển hướng đến trang 
        window.location.href = "/register-rq";
    })
    .catch(error => {
        console.error('Error:', error);
    });
}



