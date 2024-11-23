document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM fully loaded and parsed');
    cargarCasas();
    cargarOpcionesEliminar();
});

document.getElementById('boton-eliminar').addEventListener('click', () => {
    console.log('Eliminar botón clickeado');
    const selectCasas = document.getElementById('select-casas');
    const houseId = selectCasas.value;
    eliminarCasa(houseId);
});

async function cargarCasas() {
    console.log('Cargando casas...');
    const response = await fetch('http://localhost:8000/houses/api/houses/');
    const casas = await response.json();
    console.log('Casas cargadas:', casas);
    
    const contenedorAnuncios = document.querySelector('.contenedor-anuncio');
    contenedorAnuncios.innerHTML = ''; // Limpiar contenedor antes de agregar nuevos anuncios

    casas.forEach(casa => {
        const { title, description, price, rooms, parking, bathrooms } = casa;

        const anuncio = document.createElement('div');
        anuncio.classList.add('anuncio');

        anuncio.innerHTML = `
            <img src="img/anuncio1.jpg" alt="casa en el lago">
            <div class="contenido-anuncio">
                <h3>${title}</h3>
                <p>${description}</p>
                <p class="precio">${price.toLocaleString()}$</p>
                <ul class="iconito">
                    <li>
                        <img src="img/icono_dormitorio.svg" alt="">
                        <p>${rooms}</p>    
                    </li>
                    <li>
                        <img src="img/icono_estacionamiento.svg" alt="">
                        <p>${parking}</p>    
                    </li>
                    <li>
                        <img src="img/icono_wc.svg" alt="">
                        <p>${bathrooms}</p>    
                    </li>
                </ul>
                <a href="anuncio.html" class="boton boton-amarillo d-block">Ver Propiedad</a>
            </div>
        `;

        contenedorAnuncios.appendChild(anuncio);
    });
}

async function crearCasa(houseData) {
    const response = await fetch('http://localhost:8000/houses/api/houses/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(houseData),
    });
    const casa = await response.json();
    console.log(casa);
}

async function cargarOpcionesEliminar() {
    try {
        console.log('Cargando opciones para eliminar...');
        const response = await fetch('http://localhost:8000/houses/api/houses/');
        const casas = await response.json();
        
        console.log('Casas recibidas:', casas); // Agregar console.log para verificar los datos

        const selectCasas = document.getElementById('select-casas');
        selectCasas.innerHTML = ''; // Limpiar opciones antes de agregar nuevas

        casas.forEach(casa => {
            const option = document.createElement('option');
            option.value = casa.house_id;
            option.textContent = casa.title;
            selectCasas.appendChild(option);
        });
    } catch (error) {
        console.error('Error al cargar las opciones de eliminación:', error);
    }
}

async function eliminarCasa(houseId) {
    const response = await fetch(`http://localhost:8000/houses/api/houses/${houseId}/`, {
        method: 'DELETE',
    });

    if (response.ok) {
        console.log('Casa eliminada correctamente');
        cargarOpcionesEliminar(); // Recargar las opciones del select
    } else {
        console.error('Error al eliminar la casa');
    }
}