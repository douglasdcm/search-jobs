// setup some JSON to use
window.onload = function() {
    // setup the button click
    document.getElementById("send_message").onclick = function() {
        doWork()
    };
}
function doWork() {
    var message_field = document.getElementById('message_field').value;
    
    if (message_field === "") {
        alert("Preencha o campo, por favor!");
        return
    }
    document.getElementById("send_message").disabled = true;
    document.getElementById('send_message').value
            = 'Pesquisando...';	

    var settings = {
        "url": "/receiver",
        "method": "POST",
        "timeout": 0,
        "headers": {
        "Content-Type": "application/json"
        },
        "data": JSON.stringify({"message": message_field }),
    };

    // ajax the JSON to the server
    $.ajax(settings).done(function (response) {
        document.getElementById("response").innerHTML = response
        document.getElementById('send_message').value
            = 'Pesquisar';
        document.getElementById("send_message").disabled = false;
    });
    // stop link reloading the page
    event.preventDefault();
}
