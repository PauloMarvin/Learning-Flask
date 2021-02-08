const text_box = document.getElementById("caixa_texto")
const token = document.getElementById('token').value




function request(url) {
    const Http = new XMLHttpRequest();
        Http.open("GET", url);
        Http.setRequestHeader('Authorization',token);
        Http.send();

        Http.onreadystatechange = (e) => {


            text_box.value = Http.responseText



        }

}