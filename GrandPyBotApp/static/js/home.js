let submit = document.getElementById('submit');
let text_in_form = document.getElementById('form');

submit.addEventListener('click', function(event){
    var text = text_in_form.value;
    var p = document.createElement("p");
    document.getElementById('card').appendChild(p).innerHTML = "<p id='card_user'>" +  text + "</p>";
    text_in_form.value = "";
    event.preventDefault();
    event.stopPropagation();
});
