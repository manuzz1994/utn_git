class BookCard extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        this._bookData = null; // esta propiedad se usará para almacenar los datos del libro
    }

    set bookData(data) {
        this._bookData = data;
        this.render();
    }

    get bookData() {
        return this._bookData;
    }

    render() {
        if (!this._bookData) return; // Si no hay datos, no renderizamos
        const { title, author, year, cover } = this._bookData;

        this.shadowRoot.innerHTML = `
            <style>
                .item {
                    flex-grow: 1;
                    flex-basis: 200px;
                }
                .card {
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    padding: 16px;
                    max-width: 200px;
                    text-align: center;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    display: flex;
                    flex-direction: column;
                    align-items: center;    
                }
            </style>
            <div class="card">
                <img src="${cover}" alt="Portada de ${title}" width="100%">
                <h3>${title}</h3>
                <p><strong>Autor:</strong> ${author}</p>
                <p><strong>Año:</strong> ${year}</p>
            </div>
        `;
    }
}

customElements.define('book-card', BookCard);