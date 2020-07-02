/* Script pour la page destinée au professeur */
/**********************************************/

window.addEventListener('load', function() {

    var frame = document.getElementById('slides_professeur').contentDocument;
    var frameBody = frame.body;
    var scriptElement = frame.createElement('script');
    scriptElement.src = '/static/injection_prof.js';
	  frame.title=document.title;
    frameBody.appendChild(scriptElement);

//en cas d'erreur de routage, on s'assure que le script de js est injecté dans la page
    scriptElement.src = '/static/js/reveal.js';
    frameBody.appendChild(scriptElement);
    });
