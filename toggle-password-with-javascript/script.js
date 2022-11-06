let visible = false

const toggle = () => {
  if(visible){
    document.getElementById("password").setAttribute("type", "password")
    document.getElementById("visibility").innerHTML = "show"
    visible = false
  } else {
    document.getElementById("password").setAttribute("type", "text")
    document.getElementById("visibility").innerHTML = "hide"
    visible = true
  }
}