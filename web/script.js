document.querySelector("button").onclick = function () {  
    eel.holi()(function(respuesta){                      
      document.querySelector(".test").innerHTML = respuesta;
    })
  }