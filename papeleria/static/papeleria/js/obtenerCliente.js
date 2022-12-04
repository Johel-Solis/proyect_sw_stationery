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

function obtenerCliente(){

    var form  = new FormData(document.getElementById('customer-form'));
    var info  = document.getElementById('name_customer');
    fetch("/set_customer", {
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
            
            custom = data.customer;
           
            //var p = document.createElement("p");
            //var p2 = document.createElement("p");
            //p.innerHTML = "Cedula: " + custom.id;
            //p2.innerHTML = "Nombre: " + custom.name;
        
            document.getElementById('name_customer').value=(custom.name);
             //info.appendChild(p2);
            
            
        }
    );
    
    
}

