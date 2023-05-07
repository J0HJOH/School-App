const dropdownAcc = document.querySelector('.dropdown-account')
const accountList = document.querySelector('.account-list')
const gettingStarted = document.querySelector('.getting-started')
const dropdownIntro = document.querySelector('.dropdown-intro')

dropdownAcc.addEventListener('click', ()=>{
    accountList.classList.toggle('list')
    console.log('hello')
})

dropdownIntro.addEventListener('click', ()=>{
    gettingStarted.classList.toggle('list')
    console.log('hello')
})

const mydata = document.querySelector('.bad-data').innerHTML
const btnCopy = document.querySelector('.copy-1')

// Just keeping a note for it

// const presever = document.createElement('textarea')
// presever.innerHTML = mydata
// btnCopy.addEventListener('click', ()=>{
//     console.log('hi')
//     navigator.clipboard.writeText(presever.value)
// })

const endpoint = document.querySelector('.create-endpoint').innerHTML
const copyCreatEndpoint = document.querySelector('.copy-2')


const pythonWay = document.querySelector('.python-way').innerHTML
const copyPythonCode = document.querySelector('.copy-3')

const listEndpoint = document.querySelector('.list-endpoint').innerHTML
const copyListEndpoint = document.querySelector('.copy-4')

const updateEndpoint = document.querySelector('.update-endpoint').innerHTML
const copyUpdateEndpoint = document.querySelector('.copy-5')

const retriveEndpoint = document.querySelector('.retrive-endpoint').innerHTML
const copyRetriveEndpoint = document.querySelector('.copy-6')

const myCopyFunc = (text, icon) =>{
    let preserveText = document.createElement('textarea')
    preserveText.innerHTML = text
    icon.addEventListener('click', ()=>{
        navigator.clipboard.writeText(preserveText.value)
        
    })

}
myCopyFunc(endpoint, copyCreatEndpoint)
myCopyFunc(mydata, btnCopy)
myCopyFunc(pythonWay, copyPythonCode)
myCopyFunc(listEndpoint, copyListEndpoint)
myCopyFunc(updateEndpoint, copyUpdateEndpoint),
myCopyFunc(retriveEndpoint, copyRetriveEndpoint)