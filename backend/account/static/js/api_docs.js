const mydata = document.querySelector('.authorized-request').innerHTML
const btnCopy = document.querySelector('.copy')
const presever = document.createElement('textarea')
presever.innerHTML = mydata
btnCopy.addEventListener('click', ()=>{
    console.log('hi')
    navigator.clipboard.writeText(presever.value)
})