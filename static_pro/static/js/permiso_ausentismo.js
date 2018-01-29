//For getting CSRF token
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

    $(document).ready(function(){
      $("#myInput").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        console.log(value);
        $("#myTable").find("tr").filter(function() {
          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
      });
    });

    ////////Calcular el total de días de incapacidad
/*
    $(document).ready(function () {
        $("#id_periodoIncapacidadFinal").on("keyup",function () {
          //var periodo_inicial = $("#id_periodoIncapacidadInicial").val();
          var periodo_final = $(this).val();
          //console.log(periodo_inicial);
          console.log(periodo_final);
          //console.log()
      });
    });

*/



    //For doing AJAX post
    $("#submit").click(function(e) {
        e.preventDefault();
        var csrftoken = getCookie('csrftoken');
        var codigo = $('#codigo').val();
        //var password = $('#inputPassword').val();
        //This is the Ajax post.Observe carefully. It is nothing but details of where_to_post,what_to_post
        var progress = $(".loading-progress").progressTimer({
            timeLimit: 1.35,
            onFinish: function () {
                //alert('completed!');
            }
        });
        $.ajax({
             url : window.location.href, // the endpoint,commonly same url
             type : "POST", // http method
             data : {
                csrfmiddlewaretoken : csrftoken,
                codigo : codigo
             //password : password
             }, // data sent with the post request

            // handle a successful response
            success : function(json) {
                //console.log(json); // another sanity check
                //On success show the data posted to server as a message
                document.getElementById("myTable").innerHTML = "<tr><td>" + " " + "</td></tr>";
                for (x in json['codigos']) {
                    document.getElementById("myTable").innerHTML += "<tr><td><a style='color: #fefefe' class='btn btn-primary' class=\"close\" data-dismiss=\"modal\">" + x + "</a></td><td>"+json['codigos'][x]+"</td></tr>";
                    //document.getElementById("demo").innerHTML += x +' '+ json['codigos'][x] + "<br>";
                }
                $( "a" ).click(function() {
                    var text = $( this ).text();
                    $( "#id_codigoDiagnostico" ).val( text );

                });

            },

            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            },
            always:function () {
               // document.getElementById("barra_progreso").removeChild();
            }
        }).done(function () {
            progress.progressTimer('complete');

        });
    });