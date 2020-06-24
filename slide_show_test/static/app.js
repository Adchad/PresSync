

var socket = io();

socket.on('connect', function() { console.log("CONNECTION");});



socket.emit("message" , "ceci est un message");

socket.on("message", function() { 
		document.querySelector(".testclass").innerHTML = "MESSAGE REçU"; });

document.querySelector(".btn").addEventListener('click', function(){send_msg("bouton exterieur")});

function send_msg(msg){
	socket.emit("message" , msg);
}



var iframe_DOM = document.getElementById("slide").contentDocument;



//var leftBtn =iframe_DOM.querySelector(".navigate-left"); 

//var rightBtn =iframe_DOM.querySelector(".navigate-right"); 



//rightBtn.addEventListener('click', function(){send_msg("droite")});
//leftBtn.addEventListener('click', function(){send_msg("gauche")});




var iframe_WIN = document.getElementById("slide").contentWindow;

function change_page(number){

	iframe_WIN.postMessage( JSON.stringify({ method: 'slide', args: [ number ] }), '*' );

}


window.addEventListener( 'message', event => {
  var data = JSON.parse( event.data );
  if( data.namespace === 'reveal' && data.eventName === 'slidechanged' ) {
		  send_msg("page " + data.state.indexh);
 }
} );


change_page(2);


