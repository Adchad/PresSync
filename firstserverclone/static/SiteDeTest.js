let bonjour = document.getElementById('b1');
let ajouter = document.getElementById('b2');
var userName = prompt('Entrez votre prénom :')


bonjour.addEventListener('click', alerte);
ajouter.addEventListener('click', ajout);
/*nom.addEventListener('submit', nom);*/

function alerte(){
	alert('Bonjour');
}

function ajout(){
	let para = document.createElement('p');
	//let nom = document.getElementById("name").value;
	para.textContent = "T'es le plus beau " + userName + " de toutes les " + userName;
	document.body.appendChild(para);
}
