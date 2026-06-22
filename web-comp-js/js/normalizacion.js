function mapBook(doc) {
    return {
        title: doc.title,
        author: doc.author_name?.author_name || 'Autor desconocido',
        year: doc.first_publish_year || 'Año desconocido',
        cover: doc.cover_i ? `https://covers.openlibrary.org/b/id/${doc.cover_i}-M.jpg` : 'https://via.placeholder.com/150x200?text=No+Cover'
    };
}