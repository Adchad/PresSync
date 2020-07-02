/* Script d'injection pour la page destinée aux élèves */
/*******************************************************/
window.addEventListener('load', function() {


    var frame = document.getElementById('slides_eleve').contentDocument;
    var frameBody = frame.body;
    var scriptElement = frame.createElement('script');
    scriptElement.src = '/static/injection_eleve.js';
		frame.title = document.title
    frameBody.appendChild(scriptElement);

});
