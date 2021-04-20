
var stave = [];
var context = [];
const basicnotes = ["c/4","d/4","e/4","f/4","g/4","a/5","b/5","c/5","d/5","e/5","f/5","g/5","a/5","b/5"]
var position = 6;
const sharp = /[a-z]\#\/\d/g;
const flat = /[a-z]b\/\d/g
var existStave = 0;


function rotate(){

}

function init(element, clef, time){
  console.log("init")
  VF = Vex.Flow;

  // Create an SVG renderer and attach it to the DIV element named "boo".
  var div = document.getElementById(element)
  var renderer = new VF.Renderer(div, VF.Renderer.Backends.SVG);

  // Configure the rendering context.
  renderer.resize(500, 500);
  context[existStave] = renderer.getContext();
  context[existStave].setFont("Arial", 10, "").setBackgroundFillStyle("#eed");

  // Create a stave of width 400 at position 10, 40 on the canvas.
  stave[existStave] = new VF.Stave(10, 40, 200);

  // Add a clef and time signature.
  if(clef){
    stave[existStave].addClef(clef);
  }
  if(time){
    stave[existStave].addTimeSignature(time);
  }
  // Connect it to the rendering context and draw!
  stave[existStave].setContext(context[existStave]).draw();
  existStave++;
  return(existStave-1);
}


function removestave(staveId){
      parent = document.getElementById(staveId).parentNode;
      document.getElementById(staveId).remove();
      g = document.createElement('div'); 
      g.id = staveId;
      parent.appendChild(g);
      existStave--;
}


function addnote(index, clef, e, dur){
  console.log(e.length,dur.length);

  var notes = [];
  for(i=0; i<dur.length; i++){
    console.log(e, dur[i]);
    notes[i] = new VF.StaveNote({clef: clef, keys: [e], duration: dur[i]});
  }
	
  if(sharp.test(e)){
  	notes[0].addAccidental(0, new VF.Accidental("#"));
    console.log("sharp");
  }
  if(flat.test(e)){
  	console.log("flat");
  }
	var voice = new VF.Voice({num_beats: notes.length,  beat_value: 4});
  voice.addTickables(notes);
  var formatter = new VF.Formatter().joinVoices([voice]).format([voice], 400);
  
  // Render voice
  voice.draw(context[index], stave[index]);
}