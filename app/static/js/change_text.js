function change_text(text_test) {
        const urlParams = new URLSearchParams(window.location.search);
        const text = urlParams.get('texto');
        console.log(text)
        document.getElementById('caixa_texto').value = text || 'Não há nada para exibir'

    }