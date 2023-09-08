const url = 'https://cors-anywhere.herokuapp.com/linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=c++&location=Canada&start='

let form = document.getElementsByTagName('form').item(0)
let keywords = document.getElementById('keyword')
let unwanted = document.getElementById('unwanted')


form.addEventListener('submit', async (e) => {
    e.preventDefault()
    let texts = await fetch(url);
    console.log(texts)
})