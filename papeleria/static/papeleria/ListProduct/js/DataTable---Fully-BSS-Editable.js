$(document).ready(function() {
    $('.mydatatable').DataTable({
        dom: 'Bfrtip',
        buttons: [
           'excel', 'pdf', 'print'
        ],
        scrollY: 300,
        scrollX: true,
        autoWidth: false,
        scrollCollapse: true,
        paging: true
    });
});