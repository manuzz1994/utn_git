import 'components/BookCards.js';

// Normalización de datos
function mapBook(doc) {
    return {
        title: doc.title,
        author: doc.author_name?.author_name || 'Autor desconocido',
        year: doc.first_publish_year || 'Año desconocido',
        cover: doc.cover_i ? `https://covers.openlibrary.org/b/id/${doc.cover_i}-M.jpg` : 'https://via.placeholder.com/150x200?text=No+Cover'
    };
}

// Fetch + estados
const app = document.getElementById('app');
const estado = document.getElementById('estado');

let currentPage = 1;
const limit = 10;
let currentQuery = '';

async function fetchBooks() {
    setLoading(true);

    try {
        const resp = await fetch (
          `https://openlibrary.org/search.json?q=${currentQuery}&page=${currentPage}&limit=${limit}`  
        );

        if (!resp.ok) throw new Error("Error en la API");

        const data = await resp.json();

        
    }
}