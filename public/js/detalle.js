function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
    });
    return vars;
}

function getUrlParam(parameter, defaultvalue){
    var urlparameter = defaultvalue;
    if(window.location.href.indexOf(parameter) > -1){
        urlparameter = getUrlVars()[parameter];
        }    
    return urlparameter;
}

$(document).ready(function() {
    $.ajax({url: "/detalleDeBebida", type:"get", data: { id: getUrlParam("id", 0)}, 
        success: function(data, status) {
            console.log(status);
            console.log(data);  
            data = JSON.parse(data);          
            $("#bebida").append(htmlDeBebida(data.bebida_id, data.nombre, data.tiene_alcohol));
        }     
    });
});  
  
  function htmlDeBebida(id, nombre, tiene_alcohol) {
    return `    
        <div class="jumbotron">
            <h1 class="display-4">${nombre}</h1>
            <p class="lead">This is a simple hero unit, a simple jumbotron-style component for calling extra attention to featured content or information.</p>
            <hr class="my-4">
            <p>${(tiene_alcohol)?"Esta bebida contiene alcohol":""}</p>
            <button class="btn btn-success btn-lg" role="button">Ordenar</button>
        </div>`;  
  }
  
  