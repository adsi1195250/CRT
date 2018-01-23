$(document).ready(function(){
    $("#id_fechaNacimiento").on("keyup", function() {
        var fecha_nacimiento = $(this).val().split('-')[0];
        var fecha_hoy = new Date().getFullYear();
        var edad = fecha_hoy - fecha_nacimiento;
        console.log(fecha_hoy);
        console.log(fecha_nacimiento);
        console.log('-------------')
        console.log(edad)
        $( "#id_edad" ).val( Number(edad) );
  });

});