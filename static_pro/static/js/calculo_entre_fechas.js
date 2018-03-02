function calcular_dias() {
    var periodo_inicial = moment($("#id_periodoIncapacidadInicial").val());
    //console.log(periodo_final);
    var periodo_final = moment($("#id_periodoIncapacidadFinal").val());
    if (periodo_inicial !== undefined && periodo_final !== undefined)
    {
        var total_dias = periodo_final.diff(periodo_inicial, 'days');
        if(total_dias <= 0){
                $("#id_totalDiasIncapacidad").val(0);
        }else {

            $("#id_totalDiasIncapacidad").val(total_dias);
        }
        //console.log(total_dias, ' dias de diferencia');
    } else {
        $("#id_totalDiasIncapacidad").val(0);

    }
}

$(document).ready(function(){
    var fecha = new Date();
    var hora = String(fecha.getHours());
    if(parseInt(hora) < 10)
        hora = '0'+hora;
    var minutos = String(fecha.getMinutes());
    if(parseInt(minutos) < 10)
        minutos = '0'+minutos;
    var mes = (fecha.getMonth()+1);
    var dia = fecha.getDate();
    if(mes<10)
        mes = '0'+mes;
    if(dia<10)
        dia = '0'+dia;
    var v = fecha.getFullYear()+'-'+mes+'-'+dia;
    //console.log(v);
    //$("#id_fechaNacimiento").value('1996-11-11');
    if($("#id_periodoIncapacidadInicial").val() == '' || $("#id_periodoIncapacidadInicial").val() == undefined){
        $("#id_periodoIncapacidadInicial").val(v);
    }

    if($("#id_periodoIncapacidadFinal").val() == '' || $("#id_periodoIncapacidadFinal").val() == undefined) {
        $("#id_periodoIncapacidadFinal").val(v);
    }

    if($("#id_periodoIncapacidadFinal").val() == v && $("#id_periodoIncapacidadInicial").val() == v) {
        console.log($("#id_horaInicial").val());
        if($("#id_horaInicial").val() == '' && $("#id_horaFinal").val() == '') {
            $("#id_horaInicial").val(hora + ':' + minutos);
            $("#id_horaFinal").val(hora + ':' + minutos);
            $("#id_horaInicial").prop('disabled', false);
            $("#id_horaFinal").prop('disabled', false);

            $("#id_horaInicial").removeAttr('data-toggle');
            $("#id_horaFinal").removeAttr('data-toggle');
            $("#id_horaInicial").removeAttr('title');
            $("#id_horaFinal").removeAttr('title');
        }
    } else {
        $("#id_horaInicial").val('');
        $("#id_horaFinal").val('');

        $("#id_horaInicial").attr('data-toggle','tooltip');
        $("#id_horaInicial").attr('title','Solo aplica para el mismo día.');
        $("#id_horaFinal").prop('data-toggle','tooltip');
        $("#id_horaFinal").prop('title','Solo aplica para el mismo día');
        $("#id_horaInicial").prop('disabled',true);
        $("#id_horaFinal").prop('disabled',true);
    }

    $("#id_periodoIncapacidadFinal").on("input", function() {
        calcular_dias();
        if($(this).val() === $("#id_periodoIncapacidadInicial").val()){
            $("#id_horaInicial").val(hora+':'+minutos);
            $("#id_horaFinal").val(hora+':'+minutos);
            $("#id_horaInicial").prop('disabled',false);
            $("#id_horaFinal").prop('disabled',false);

            $("#id_horaInicial").removeAttr('data-toggle');
            $("#id_horaFinal").removeAttr('data-toggle');
            $("#id_horaInicial").removeAttr('title');
            $("#id_horaFinal").removeAttr('title');
        } else {
            $("#id_horaInicial").val('');
            $("#id_horaFinal").val('');

            $("#id_horaInicial").attr('data-toggle','tooltip');
            $("#id_horaInicial").attr('title','Solo aplica para el mismo día.');
            $("#id_horaFinal").prop('data-toggle','tooltip');
            $("#id_horaFinal").prop('title','Solo aplica para el mismo día');
            $("#id_horaInicial").prop('disabled',true);
            $("#id_horaFinal").prop('disabled',true);

        }
    });

    $("#id_periodoIncapacidadInicial").on("input", function() {
        calcular_dias();
        if($(this).val() === $("#id_periodoIncapacidadFinal").val()){
            $("#id_horaInicial").val(hora+':'+minutos);
            $("#id_horaFinal").val(hora+':'+minutos);
            $("#id_horaInicial").prop('disabled',false);
            $("#id_horaFinal").prop('disabled',false);

            $("#id_horaInicial").removeAttr('data-toggle');
            $("#id_horaFinal").removeAttr('data-toggle');
            $("#id_horaInicial").removeAttr('title');
            $("#id_horaFinal").removeAttr('title');
        } else {
            $("#id_horaInicial").val('');
            $("#id_horaFinal").val('');
            $("#id_horaInicial").attr('data-toggle','tooltip');
            $("#id_horaInicial").attr('title','Solo aplica para el mismo día.');
            $("#id_horaFinal").prop('data-toggle','tooltip');
            $("#id_horaFinal").prop('title','Solo aplica para el mismo día');
            $("#id_horaInicial").prop('disabled',true);
            $("#id_horaFinal").prop('disabled',true);
        }
    });

    $("#id_prorroga").on("input",function () {
       var valor_prorroga =  $(this).val();
       var dias =$("#id_totalDiasIncapacidad").val();
       var dias_cargados = parseInt(valor_prorroga)+parseInt(dias);
       $("#id_diasCargados").val(dias_cargados);
    });

    $("#id_totalDiasIncapacidad").on("input", function () {
        var valor_prorroga =  $(this).val();
       var dias =$("#id_prorroga").val();
       var dias_cargados = parseInt(valor_prorroga)+parseInt(dias);
       $("#id_diasCargados").val(dias_cargados);
    });
});




//////////////////////////////////////////////////////////////////////////////////////




