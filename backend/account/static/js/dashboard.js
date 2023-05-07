const btnMenu = document.querySelector("#btn")
const sidebar = document.querySelector('.sidebar')

btnMenu.addEventListener('click', ()=>{
    sidebar.classList.toggle('active')
})