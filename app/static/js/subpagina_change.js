function change_subpagina(option) {
    const div1 = document.getElementById("subpagina1")
    const div2 = document.getElementById("subpagina2")
    if (option == 1 ) {
        div1.style.display = 'block'
        div2.style.display = 'none'
    }

    if (option == 2 ) {
        div1.style.display = 'none'
        div2.style.display = 'block'
    }

    
}


