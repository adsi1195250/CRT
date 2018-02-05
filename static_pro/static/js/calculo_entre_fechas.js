function calcular_dias() {
    var periodo_inicial = moment($("#id_periodoIncapacidadInicial").val());
    console.log(periodo_final);
    var periodo_final = moment($("#id_periodoIncapacidadFinal").val());
    if (periodo_inicial !== undefined && periodo_final !== undefined)
    {
        var total_dias = periodo_final.diff(periodo_inicial, 'days');
        if(total_dias <= 0){
                $("#id_totalDiasIncapacidad").val(1);
        }else {

            $("#id_totalDiasIncapacidad").val(total_dias);
        }
        console.log(total_dias, ' dias de diferencia');
    } else {
        $("#id_totalDiasIncapacidad").val(1);

    }
}

$(document).ready(function(){
    //$("#id_fechaNacimiento").value('1996-11-11');
    $("#id_periodoIncapacidadFinal").on("input", function() {
        calcular_dias();
    });

    $("#id_periodoIncapacidadInicial").on("input", function() {
        calcular_dias();
    });

});




//////////////////////////////////////////////////////////////////////////////////////




