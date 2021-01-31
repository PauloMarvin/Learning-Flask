let input = document.querySelector('#input')
let textbox = document.querySelector('#caixa_texto')
let btnclear = document.querySelector('#clear')

input.addEventListener('change', () => {
    let files = input.files;

    if (files.length === 0) return;

    const file = files[0];


    let reader = new FileReader();

    reader.onload = (e) => {
        const file = e.target.result;
        console.log(file);

        const lines = file.split(/\r\n|\n/);
        textbox.value = lines.join('\n');
        console.log(lines);

    };

    reader.onerror = (e) => alert(e.target.error.name);

    reader.readAsText(file);
});



btnclear.addEventListener('click', () => {
    textbox.value = '';


});

