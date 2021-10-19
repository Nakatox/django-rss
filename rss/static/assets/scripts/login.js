window.addEventListener('DOMContentLoaded', () => {
    const emailInput = document.querySelector('.login_email_input')
    const passwordInput = document.querySelector('.login_password_input')
    const emailLabel = document.querySelector('.login_email_label')
    const passwordLabel = document.querySelector('.login_password_label')
    emailInput.addEventListener('click', () => {
        if (emailInput === document.activeElement) {
            emailLabel.style.top = "0"
        }
    })
    passwordInput.addEventListener('click', () => {
        if (passwordInput === document.activeElement) {
            passwordLabel.style.top = "0"
        }
    })
});