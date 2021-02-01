const button = document.getElementById("read")
const text_box = document.getElementById("caixa_texto")
const form = document.getElementById("form")

button.addEventListener('click',function (e){

        console.log('his shauidisa')
        const Http = new XMLHttpRequest();
        Http.open("GET", '/mensages');
        Http.send();

        Http.onreadystatechange = (e) => {
            text_box.value = Http.responseText
            console.log(Http.responseText)
        }

})

