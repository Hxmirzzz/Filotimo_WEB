// init Isotope
var $grid = $('.collection-list').isotope({
});

// filter items on button click
$('.filter-button-group').on( 'click', 'button', function() {
    var filterValue = $(this).attr('data-filter');
    resetFilterBtns();
    $(this).addClass('active-filter-btn');
    $grid.isotope({ filter: filterValue });
    });

    var filterBtns = $('.filter-button-group').find('button');
    function resetFilterBtns(){
    filterBtns.each(function(){
    $(this).removeClass('active-filter-btn');
    });
    }

// Carrito

const carrito = document.getElementById('carrito');
const elemetos1 = document.getElementById('list-1'); 
const elemetos2 = document.getElementById('list-2'); 
const lista = document.querySelector('#lista-carrito tbody');
const vaciarCarritoBtn = document.getElementById('vaciar-carrito');

cargarEventListeners();

function cargarEventListeners(){
    elemetos1.addEventListener('click', comprarElemento);
    elemetos2.addEventListener('click', comprarElemento);
    carrito.addEventListener('click', eliminarElemento);
    vaciarCarritoBtn.addEventListener('click', vaciarCarrito);
}

function comprarElemento(e) {
    e.preventDefault();
    if(e.target.classList.contains('btn')){
        const elemento = e.target.parentElement.parentElement;
        leerDatosElemento(elemento);
    }
}

function leerDatosElemento(elemento) {
    const infoElemento = {
        imagen: elemento.querySelector('img').src,
        titulo: elemento.querySelector('p').textContent,
        precio: elemento.querySelector('.precio').textContent,
        id: elemento.querySelector('a').getAtribute('data-ic')
    }
    insertarCarrito(infoElemento);
}

function insertarCarrito(elemento) {
    const row=document.createElement('tr');
    row.innerHTML = `
        <td>
            <img src="${elemento.imagen}" width=100 >
        </td>

        <td>
            ${elemento.titulo}
        </td>

        <td>
            ${elemento.precio}
        </td>

        <td>
            <a href="#" class="borrar" data-id="${elemento.id}"
        </td>
    `;

    lista.appendChild(row);
}

function eliminarElemento(e){
    e.preventDefault();
    let elemento,
        elementoId;
    if(e.target.classList.contains('borrar')) {
        e.target.parentElement.parentElement.remove();
        elemento = e.target.parentElement.parentElement;
        elementoId = elemento.querySelector('a').getAtribute('data-id');
    }
}

function vaciarCarrito(e) {
    while(lista.firstChild) {
        lista.removeChild(lista.firstChild);
    }
    return false;
}