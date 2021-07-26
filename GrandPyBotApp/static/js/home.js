let submit = document.getElementById('submit');
let text_in_form = document.getElementById('form');

let map;

let data_maps_lat;
let data_maps_lng;

let number = 0;

$('#submit').click(function(event){

    var text = text_in_form.value;
    var p = document.createElement("p");
    
    document.getElementById('card').appendChild(p).innerHTML = "<p id='card_user'>" + text + "</p>";
    event.preventDefault();
    event.stopPropagation();

    number += 1;

    var div = document.createElement("div");

    document.getElementById('card').appendChild(div).innerHTML = "<div class='general_loader' id='loader" + number.toString() + "' style='display:none'> <img src='../static/img/ajax-loader.gif' /></div>"

    $(document).ajaxStart(function() {
        // show loader on start
        var string_loader = "#loader"+number.toString()
        console.log(string_loader);
        $(string_loader).css("display","block");
    })

    $.ajax({
        url: "/question/",
        method: "GET",
        dataType: "json",
        data: {
            'question' : text_in_form.value
        }
    })

    .done(function(response){

        let response_address = JSON.stringify(response[2]).slice(1,-1);
        let response_wikipedia = JSON.stringify(response[3]).slice(1,-1);
        let another_question = JSON.stringify(response[4]).slice(1,-1);

        let sentence_wikipedia = JSON.stringify(response[0][1]);
        let valid_text_wikipedia = "";

        for(let step=0;step<sentence_wikipedia.length;step++){
            if(sentence_wikipedia.charAt(step) != '\\'){
                valid_text_wikipedia += sentence_wikipedia.charAt(step);
            }  
            else{
                valid_text_wikipedia += '<br>';
                step++;
            }  
        }
        let url_wikipedia = JSON.stringify(response[0][2]).slice(1,-1);        

        data_maps_lat = JSON.stringify(response[1][0]);
        data_maps_lng = JSON.stringify(response[1][1]);
        formatted_address = JSON.stringify(response[1][2]);

        var p = document.createElement("p");
        var p1 = document.createElement("p");
        var p2 = document.createElement("p");
        var p3 = document.createElement("p");

        document.getElementById('card').appendChild(p).innerHTML = "<p class='card_bot'>" + response_address + formatted_address + "</p>";
        document.getElementById('card').appendChild(p1).innerHTML = "<p class='card_bot general_map_style' id='map" + number.toString() + "'>" + "</p>";
        console.log(sentence_wikipedia.replace('\n', '<br />'));
        document.getElementById('card').appendChild(p2).innerHTML = "<p class='card_bot'>" + response_wikipedia + valid_text_wikipedia + "<a class='link' href='" + url_wikipedia + "'> [En savoir plus sur Wikipedia]" + "</p>";
        document.getElementById('card').appendChild(p3).innerHTML = "<p class='card_bot'>" + another_question + "</p>";

        console.log(number);
        initMap(data_maps_lat, data_maps_lng, number);

        var string_loader = "#loader"+number.toString()
        $(string_loader).css("display","none");
        console.log('ok' + string_loader);

        console.log('done');
        })

    .fail(function(error){
        alert("La requête s'est terminée en échec. Infos : " + JSON.stringify(error));
        var string_loader = "#loader"+number.toString()
        $(string_loader).css("display","none");
        console.log('ok' + string_loader);
        })

    .always(function(){

        });
    var text = text_in_form.value = "";
});

function initMap(data_maps_lat, data_maps_lng, number){
    console.log('on passe dedans');
    console.log(data_maps_lat);
    console.log(data_maps_lng);

    var string_id = "map"+number.toString();
    console.log(string_id);

    map = new google.maps.Map(document.getElementById(string_id), {
        center: { lat: parseFloat(data_maps_lng), lng: parseFloat(data_maps_lat) },
        zoom: 10,
    });
    const marker = new google.maps.Marker({
        position: { lat: parseFloat(data_maps_lng), lng: parseFloat(data_maps_lat) },
        map: map,
    });
}

