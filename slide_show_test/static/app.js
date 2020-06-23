var iframe_DOM = document.getElementById("slide").contentDocument;

iframe_DOM.querySelector(".navigate-right").addEventListener('click', function(){send_msg("droite")});

iframe_DOM.querySelector(".navigate-left").addEventListener('click',function(){send_msg("gauche")});


var socket = io();

socket.on('connect', function() { console.log("CONNECTION");});



socket.emit("message" , "ceci est un message");

socket.on("message", function() { 
		document.querySelector(".testclass").innerHTML = "MESSAGE REçU"; });

document.querySelector(".btn").addEventListener('click', function(){send_msg("bouton exterieur")});

function send_msg(msg){
	socket.emit("message" , msg);
}



