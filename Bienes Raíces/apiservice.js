// Código de ejemplo
console.log('El archivo JavaScript externo se ha cargado correctamente');

async function cargarCasas() {
    const response = await fetch('http://localhost:8000/houses/api/houses/');
    const casas = await response.json();
    
    const anuncios = document.querySelectorAll('.contenedor-anuncio .anuncio');
    
    anuncios.forEach((anuncio, index) => {
        if (casas[index]) {
            const { title, description, price, rooms, parking, bathrooms } = casas[index];
            anuncio.querySelector('h3').innerText = title;
            anuncio.querySelector('p').innerText = description;
            anuncio.querySelector('.precio').innerText = `${price.toLocaleString()}$`;
            const iconos = anuncio.querySelectorAll('.iconito p');
            iconos[0].innerText = rooms;
            iconos[1].innerText = parking;
            iconos[2].innerText = bathrooms;
        }
    });
}

document.addEventListener('DOMContentLoaded', cargarCasas);
