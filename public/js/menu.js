$(document).ready(function() {
  $.get("/menu", function(data, status) {
    console.log(status);
    console.log(data);

    data = JSON.parse(data);
    data.forEach(bebida => {
      $("#menu").append( 
        htmlDeBebida(bebida.bebida_id, bebida.nombre, bebida.tiene_alcohol) 
      );
    });
  });
});

function htmlDeBebida(id, nombre, tiene_alcohol) {
  return `    
    <div class="col mb-4">
      <div class="card bg-light mb-3">        
        <img src="static/img/${id}.png" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">${nombre}</h5>
          <h6>${(tiene_alcohol)?"Bebida alcohólica":""}</h6>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          <a class="btn btn-sm btn-primary" href="/detalle?id=${id}">Ordenar</a>
        </div>
      </div>
    </div>`;  
}

