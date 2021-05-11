var timeElements = document.getElementsByClassName('trim-time');
for (let i = 0; i < timeElements.length; i++) {
  var timetomilisec = timeElements[i].innerHTML;
  console.log(timetomilisec);
  timeElements[i].innerHTML = timetomilisec.split(" ")[0]
}
