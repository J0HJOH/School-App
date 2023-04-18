let showLoginPassword = true

const loginPassword = document.querySelector(".login-password")

const loginHidePassword = document.querySelector(".login-hide-password")

loginHidePassword.addEventListener('click', ()=>{
    if (showLoginPassword === true){
        loginHidePassword.classList.remove('fa-eye')
        loginHidePassword.classList.add('fa-eye-slash')
        loginPassword.type = 'text'
        showLoginPassword = false
    }
    else{
        loginHidePassword.classList.remove('fa-eye-slash')
        loginHidePassword.classList.add('fa-eye')
        loginPassword.type = 'password'
        showLoginPassword = true

    }
})