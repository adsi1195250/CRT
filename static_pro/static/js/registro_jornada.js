$(document).ready(function() {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var id_trabajador = '';
    $('#myModal').on('hidden.bs.modal', function (e) {
        $("#codigo").prop('disabled', false);
        $("#codigo").val('');
        $("#codigo").focus();
    });
    $("#submit_form_reg").click(function (e) {

        e.preventDefault();
        //console.log($(this));
        form = $('form input[type=radio]:checked');
        //console.log(form.serialize());
        //console.log(form.val());
        var accion_jornada = form.val();
        //console.log(accion_jornada);
        var accion_jornada_hora = $("#id_accion_jornada_hora").val();

        var csrftoken = getCookie('csrftoken');
        $.ajax({
            url: window.location.href,
            type:"POST",
            data: {
                csrfmiddlewaretoken: csrftoken,
                accion_jornada:accion_jornada,
                save:'Guardar',
                id_trabajadores: id_trabajador,
                accion_jornada_hora: accion_jornada_hora

             },
            success: function (json) {
                if('errors' in json){
                    var error=json['errors']['__all__'][0];
                    console.log(error);
                    $.alert({
						title: 'Registro de jornada!',
						content: error,
						theme:'material',
						animation: 'rotateYR',
						closeAnimation: 'rotateX',
						type: 'red',
						typeAnimated: true
					});
                } else {
                    console.log(json);
                    $.alert({
						title: 'Registro de jornada!',
						content: json['guardado'],
						theme:'material',
						animation: 'rotateYR',
						closeAnimation: 'rotateX',
						type: 'blue',
						typeAnimated: true
					});
                    $("#myModal").modal('toggle');

                }
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        })
    });

    $("#submit").click(function (e) {
        e.preventDefault();
        var csrftoken = getCookie('csrftoken');
        var codigo = $('#codigo').val();
        $.ajax({
            url: window.location.href, // the endpoint,commonly same url
            type: "POST", // http method
            data: {
                csrfmiddlewaretoken: csrftoken,
                codigo: codigo
                //password : password
            }, // data sent with the post request

            // handle a successful response
            success: function (json) {
            	if(json.length > 0) {
            	    //console.log(json); // another sanity check
                    var cont = 0;
                    //On success show the data posted to server as a message
                    $('#titulo_trabajador').text(json[0]['nombres']);
                    id_trabajador = json[0]['id'];
                    $("#codigo").prop('disabled', true);
                    $("#myModal").modal();
                }
            	else
            		$.alert({
						title: 'Registro de jornada!',
						content: 'No se encontro ningun colaborador!',
						theme:'material',
						animation: 'rotateYR',
						closeAnimation: 'rotateX',
						type: 'blue',
						typeAnimated: true

					});


            },

            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });
});
