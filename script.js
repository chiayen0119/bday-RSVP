// First Modal
var modal = document.getElementById("rsvp-modal");
var btn = document.getElementById("rsvp-button");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
  modal.style.display = "flex";
}

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Second Modal
var modal2 = document.getElementById("rsvp-modal-2");
var continueButton = document.getElementById("continue-button");

continueButton.onclick = function() {
  modal.style.display = "none";
  modal2.style.display = "flex";
}

var closeButtons = document.getElementsByClassName("close");

for (let i = 0; i < closeButtons.length; i++) {
  closeButtons[i].onclick = function() {
    modal.style.display = "none";
    modal2.style.display = "none";
  }
}

window.onclick = function(event) {
  if (event.target == modal2) {
    modal2.style.display = "none";
  }
}
