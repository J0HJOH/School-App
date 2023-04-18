let showPassword = false
let showConfirmPassword = true

const userPassword = document.querySelector(".user-password")
const confirmPassword = document.querySelector(".confirm-password")
const eyeOpenPassword = document.querySelector(".eye-slash-password")
const eyeOpenConfirmPassword = document.querySelector(".eye-open-password")

const test = () =>{
    eyeOpenPassword.addEventListener("click", ()=>{
        if (showPassword === false){
            eyeOpenPassword.classList.remove("fa-eye")
            eyeOpenPassword.classList.add('fa-eye-slash')
            userPassword.type = "text"
            showPassword = true
        }
        else{
            eyeOpenPassword.classList.remove("fa-eye-slash")
            eyeOpenPassword.classList.add('fa-eye')
            userPassword.type = "password"
            showPassword = false
    
        }
    })
    
    eyeOpenConfirmPassword.addEventListener("click", ()=>{
        if(showConfirmPassword === true){
            eyeOpenConfirmPassword.classList.remove("fa-eye")
            eyeOpenConfirmPassword.classList.add("fa-eye-slash")
            confirmPassword.type = 'text'
            showConfirmPassword = false
            
        }
        else{
            eyeOpenConfirmPassword.classList.remove("fa-eye-slash")
            eyeOpenConfirmPassword.classList.add("fa-eye")
            confirmPassword.type = 'password'
            showConfirmPassword = true

        }
    })

}

test()


