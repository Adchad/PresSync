

var socket = io();

socket.on('connect', function() { console.log("CONNECTION");});



socket.emit("message" , "ceci est un message");


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

socket.on("message", function(msg) { 
		document.querySelector(".testclass").innerHTML ="message reçu : " +  msg;

		if(msg == "change page"){
				change_page(2);
		}

});


window.addEventListener( 'message', event => {
  var data = JSON.parse( event.data );
  if( data.namespace === 'reveal' && data.eventName === 'slidechanged' ) {
		  send_msg("page " + data.state.indexh);
 }
} );




