/*

var socket = io();
socket.on('connect', function() { console.log("CONNECTION");});

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


*/

/*****************************************************************/

window.addEventListener('load', function() {

    var frame = document.getElementById('slides_professeur').contentDocument;
    var frameBody = frame.body;
    var scriptElement = frame.createElement('script');
    scriptElement.src = '/static/injection_prof.js';

    frameBody.appendChild(scriptElement);




    var frame = document.getElementById('slides_eleve').contentDocument;
    var frameBody = frame.body;
    var scriptElement = frame.createElement('script');
    scriptElement.src = '/static/injection_eleve.js';

    frameBody.appendChild(scriptElement);

});
