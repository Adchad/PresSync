var socket = io();
var SYNC=true;
var current_page=0;
socket.on('connect', function() { console.log("CONNECTION");});

socket.emit("message" , "message de l'élève");


var iframe_WIN = document.getElementById("slide").contentWindow;

function change_page(number){

	iframe_WIN.postMessage( JSON.stringify({ method: 'slide', args: [ number ] }), '*' );

}

document.querySelector('.btn').addEventListener('click', function(){
		SYNC= !SYNC;
		if(SYNC){
				change_page(current_page);
		}
		
});
		

socket.on('message', function(msg) { 
		console.log("message reçu"+msg);

		if(msg.substr(0,11) == "change_page"){

				current_page=msg.substr(12,1);

				if(SYNC){

					change_page(msg.substr(12,1));
				}
		}

});




