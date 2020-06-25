var socket = io();
socket.on('connect', function() { console.log("CONNECTION");});

socket.emit("message" , "message de l'élève");


var iframe_WIN = document.getElementById("slide").contentWindow;

function change_page(number){

	iframe_WIN.postMessage( JSON.stringify({ method: 'slide', args: [ number ] }), '*' );

}


socket.on('message', function(msg) { 
		console.log("message reçu"+msg);

		if(msg.substr(0,11) == "change_page"){
				change_page(msg.substr(12,1));
				console.log("je dois mettre la page" + msg.substr(12,1));
		}

});




