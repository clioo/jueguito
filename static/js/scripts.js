$(document).ready(function(){
    $( "#Container" ).sortable({connectWith:'#Source'});
    $("#Source").droppable({
drop: function( evento, ui ) {
  ui.helper.remove();
}
});
});
var container;
var dragging;
window.addEventListener('load',init);
function init(){
  container = document.querySelector(".container");
  container.addEventListener('dragover',dragover,false)
  container.addEventListener('dragleave',dragleave,false)
  container.addEventListener('dragenter',dragenter,false)
  container.addEventListener('drop',drop,false)
  var elements = document.getElementsByClassName('instrucciones');
  for (i in elements){
      var element = elements[i];
      if(typeof element.style != "undefined"){
          element.addEventListener('dragstart',dragstart,false);
          element.addEventListener("dragend",dragend,false);
      }
  }
}

function dragend(e){
  dragging.style.background = "#212020";
  dragging.style.color = "white";
}
function dragover(e){
  e.preventDefault();
  this.classList.add('over');
  return false;
}
function dragenter(){

}
function GetNumber(i,f, texto1, texto2) {
  //Ingresamos un mensaje a mostrar
  var val = prompt(texto1,'','');
  while ((val > f || val < i) || (parseFloat(val) != val)) {
      val = prompt(texto2,'','');
  }
  return val;
}
function contarescogidos(){
  var elements = document.getElementsByClassName('escogidos');
  var lenescogidos = 0;
  for (i in elements)
      {
          var element = elements[i];
          if(typeof element.style != "undefined"){
             lenescogidos +=1;
          }
      }
  return lenescogidos;
}
function dragleave(e){
  e.preventDefault();
  this.classList.remove('over');
  return false;
}
function dragstart(e){
  this.style.color="black";
  this.style.background="white";
  dragging = this;
}

function drop(e){
  e.preventDefault();
  var padre = document.createElement('p');
  var clon = dragging.cloneNode(true);
  clon.addEventListener('dragstart',dragstart,false);
  clon.addEventListener("dragend",dragend,false);
  clon.style.background = "#212020";
  clon.style.color = "white";
  clon.className = "escogidos";
  if (clon.textContent != "Entrada" && contarescogidos() == "0") return;
  if (clon.getAttribute("tipo") == "normal"){
      this.appendChild(clon);return;
  }
  if (clon.getAttribute("tipo") == "piso"){
      var Numero = GetNumber(0,6,"Introduzca el número de piso [0-6]:","Introduzca solo números de piso [0-6]:");
      clon.setAttribute("Numero", Numero);
      clon.textContent = clon.getAttribute("text") + Numero + "]"
      this.appendChild(clon);return;
  }
  if (contarescogidos() > 0){
      var Numero = GetNumber(1,contarescogidos(),"Introduzca el número de línea a saltar:","Introduzca solo números de líneas que existan:");
      clon.setAttribute("Numero", Numero);
      clon.textContent = clon.getAttribute("text") + Numero + "]"
      this.appendChild(clon);
  }
}
