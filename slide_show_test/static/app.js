/* Script d'injection général */
/**********************************************/


window.addEventListener('load', function() {

    //injection dans l'iframe professeur
    var frame = document.getElementById('slides_professeur').contentDocument;
    var frameBody = frame.body;
    var scriptElement = frame.createElement('script');
    scriptElement.src = '/static/injection_prof.js';

    frameBody.appendChild(scriptElement);



    //injection dans l'iframe eleve
    var frame = document.getElementById('slides_eleve').contentDocument;
    var frameBody = frame.body;
    var scriptElement = frame.createElement('script');
    scriptElement.src = '/static/injection_eleve.js';

    frameBody.appendChild(scriptElement);

});
