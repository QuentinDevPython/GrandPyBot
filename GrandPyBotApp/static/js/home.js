let submit = document.getElementById('submit');
let text_in_form = document.getElementById('form');

let map;

let data_maps_lat;
let data_maps_lng;

let number = 0;

submit.addEventListener('click', function(event){
    var text = text_in_form.value;
    var p = document.createElement("p");
    
    document.getElementById('card').appendChild(p).innerHTML = "<p id='card_user'>" + text + "</p>";
    event.preventDefault();
    event.stopPropagation();
    var text = text_in_form.value = "";
},

$('#submit').click(function(){
    $.ajax({
        url: "/question/",
        method: "GET",
        dataType: "json",
        data: {
            'question' : text_in_form.value
        }
        })

    .done(function(response){

        let sentence_wikipedia = JSON.stringify(response[0][1]);
        let url_wikipedia = JSON.stringify(response[0][2]);

        number += 1;

        data_maps_lat = JSON.stringify(response[1][0]);
        data_maps_lng = JSON.stringify(response[1][1]);

        var p = document.createElement("p");
        var p1 = document.createElement("p");
        var p2 = document.createElement("p");

        document.getElementById('card').appendChild(p).innerHTML = "<p class='card_bot'>" + sentence_wikipedia + "</p>";
        document.getElementById('card').appendChild(p1).innerHTML = "<p class='card_bot'>" + url_wikipedia + "</p>";

        document.getElementById('card').appendChild(p2).innerHTML = "<p class='card_bot general_map_style' id='map" + number.toString() + "'>" + "</p>";
        console.log(number);
        initMap(data_maps_lat, data_maps_lng, number);
        

        console.log('done');
        })

    .fail(function(error){
        alert("La requête s'est terminée en échec. Infos : " + JSON.stringify(error));
        })

    .always(function(){
        alert("Requête effectuée");
        });
}));

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

