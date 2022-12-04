function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function obtenerProducto(){

    var form  = new FormData(document.getElementById('product-form'));
    var info  = document.getElementById('reference');
    fetch("/search_product", {
        method: "POST",
        body: form,
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
            "X-Requested-With": "XMLHttpRequest",

        }

    })
    .then(function(response) {
       return response.json();
        })
    .then(
        function(data) {
            
            custom = data.producto;
           
            //var p = document.createElement("p");
            //var p2 = document.createElement("p");
            //p.innerHTML = "Cedula: " + custom.id;
            //p2.innerHTML = "Nombre: " + custom.name;
        
            document.getElementById('name_product').value=(custom.name);
            document.getElementById('precio').value=(custom.price);
             //info.appendChild(p2);
            
            
        }
    );
    
    
}

function agregarProducto ()
{
    
    var info  = document.getElementById('name_product');
    if (info.value!=""){
        var cantidadFilas = document.getElementById("tb_product").rows.length;
        const rest=parseInt(document.getElementById('cant').value) 
        const p = parseFloat(document.getElementById('precio').value);
        var ref = '<td>'+document.getElementById('reference').value+'</td>' ;
        var name = '<td>'+document.getElementById('name_product').value+'</td>'; 
        var cant = '<td>'+document.getElementById('cant').value+'</td>'; 
        var pre = '<td>'+document.getElementById('precio').value+'</td>' ;
        var sub = '<td>'+rest*p+'</td>';   
        var op='<td align="center"><button class="btn btn-danger" onclick="eliminarFila('+cantidadFilas+');"><em class="fa fa-trash"></em></button></td>';
         
        var tr ='<tr id = "fila'+cantidadFilas+'"> ' +ref+name +' '+ cant+' ' + pre + ' '+ ' '+sub+' ' +op +' </tr>';
               

        //var btn = document.createElement("TR");
   	//btn.innerHTML=tr;
    document.getElementById("tb_product").innerHTML=(tr);

    cantidadFilas=cantidadFilas+1;

    
    document.getElementById('product-form').reset();

    }
    
}

function eliminarFila(index) {
    $("#fila" + index).remove();
  }
