// VexFlow library used to create helper music diagram renderding functions(https://www.vexflow.com/)

var stave;
var context;

const sharp = /[a-z]\#\/\d/;
const flat = /[a-z]b\/\d/;
const dotted = /[a-z]*\d*d/;

//create stave
function init(element, clef, time,stavelength, key){
  VF = Vex.Flow;
  var div = document.getElementById(element)
  var renderer = new VF.Renderer(div, VF.Renderer.Backends.SVG);
  renderer.resize(stavelength, 100);
  context = renderer.getContext();
  context.setFont("Arial", 10, "").setBackgroundFillStyle("#eed");
  stave= new VF.Stave(0, 0, stavelength);
  if(clef){
    stave.addClef(clef);
  }
  if(time){
    stave.addTimeSignature(time);
  }
  if(key){
    stave.addKeySignature(key)
  }
  stave.setContext(context).draw();
}

//remove stave
function removestave(staveId){
      parent = document.getElementById(staveId).parentNode;
      document.getElementById(staveId).remove();
      g = document.createElement('div'); 
      g.id = staveId;
      g.className = "stave";
      parent.insertBefore(g,parent.childNodes[0]);
}

//add notes with duration
function addnote(clef, e, dur){
  var notes = [];
  for(i=0; i<dur.length; i++){
    notes[i] = new VF.StaveNote({clef: clef, keys: [e[i]], duration: dur[i]});
    if(sharp.test(e[i])){
      notes[i].addAccidental(0, new VF.Accidental("#"));
    }
    if(flat.test(e[i])){
      notes[i].addAccidental(0, new VF.Accidental("b"));
    }
    if(dotted.test(dur[i])){
      notes[i].addDotToAll();
    }
  }
  var beams = VF.Beam.generateBeams(notes);
  var formatter = new VF.Formatter.FormatAndDraw(context, stave, notes)
  beams.forEach(function(b) {b.setContext(context).draw()})
}

