
var stave;
var context;

const sharp = /[a-z]\#\/\d/g;
const flat = /[a-z]b\/\d/g


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
  context = renderer.getContext();
  context.setFont("Arial", 10, "").setBackgroundFillStyle("#eed");

  // Create a stave of width 400 at position 10, 40 on the canvas.
  stave= new VF.Stave(10, 40, 200);

  // Add a clef and time signature.
  if(clef){
    stave.addClef(clef);
  }
  if(time){
    stave.addTimeSignature(time);
  }
  // Connect it to the rendering context and draw!
  stave.setContext(context).draw();

}


function removestave(staveId){
      parent = document.getElementById(staveId).parentNode;
      document.getElementById(staveId).remove();
      g = document.createElement('div'); 
      g.id = staveId;
      parent.appendChild(g);
}


function addnote(clef, e, dur){


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
  voice.draw(context, stave);
}