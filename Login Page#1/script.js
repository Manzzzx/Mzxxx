const passwordBtn = document.getElementById("password-eye");

passwordBtn.addEventListener("click", (e) => {
  const passwordInput = document.getElementById("password");
  const icon = passwordBtn.querySelector("i");
  const isVisible = icon.classList.contains("ri-eye-line");
  passwordInput.type = isVisible ? "password" : "text";
  icon.setAttribute("class", isVisible ? "ri-eye-off-line" : "ri-eye-line");
});
