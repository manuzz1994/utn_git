function decodificarHTML(texto) {
    const el = document.createElement('textarea');
    el.innerHTML = texto;
    return el.value;
}

function mezclar(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

function estilosBase() {
    return `
        .card {
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 2em;
            max-width: 500px;
            width: 100%;
            box-shadow: 0 2px 12px rgba(0,0,0,0.1);
        }
    `;
}