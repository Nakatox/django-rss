window.addEventListener('DOMContentLoaded', () => {
    const emailInput = document.querySelector('.register_email_input')
    const passwordInput = document.querySelector('.register_password_input')
    const confirmInput = document.querySelector('.register_confirm_input')
    const emailLabel = document.querySelector('.register_mail_label')
    const passwordLabel = document.querySelector('.register_password_label')
    const confirmLabel = document.querySelector('.register_confirm_label')
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
    confirmInput.addEventListener('click', () => {
        if (confirmInput === document.activeElement) {
            confirmLabel.style.top = "0"
        }
    })
});