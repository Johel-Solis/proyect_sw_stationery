//elimina el objeto de la base de datos
function deleteObject(url,id) {
    var r = confirm("¿Está seguro?");
    if (r == true) {
        fetch(url + id, {
            method: 'DELETE'
    })
    .then (Response => Response.json())
    .then (data => {
        alert(data.message);
        location.reload();
    });
}
}