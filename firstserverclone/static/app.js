var iframe_DOM = document.getElementById("slide").contentDocument;

iframe_DOM.getElementById("btn-1").addEventListener('click',send_msg);


var socket = io();

socket.on('connect', function() { console.log("CONNECTION");});



socket.emit("message" , "ceci est un message");
console.log("test");

socket.on("message", function() { 
		document.querySelector(".testclass").innerHTML = "MESSAGE REçU"; });

document.querySelector(".btn").addEventListener('click', function() { iframe_DOM.getElementById("btn-1").click();  });


function send_msg(){
	socket.emit("message" , "Bouton clické");
}



