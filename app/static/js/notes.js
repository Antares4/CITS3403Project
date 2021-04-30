
var stave;
var context;

const sharp = /[a-z]\#\/\d/;
const flat = /[a-z]b\/\d/;

function init(element, clef, time,stavelength,keysig=null){
  console.log("init")
  VF = Vex.Flow;
  var div = document.getElementById(element)
  var renderer = new VF.Renderer(div, VF.Renderer.Backends.SVG);
  renderer.resize(stavelength, 200);
  context = renderer.getContext();
  context.setFont("Arial", 10, "").setBackgroundFillStyle("#eed");
  stave= new VF.Stave(0, 0, stavelength);
  if(clef){
    stave.addClef(clef);
  }
  if(time){
    stave.addTimeSignature(time);
  }
  if(keysig){
    stave.addKeySignature(keysig);
  }
  stave.setContext(context).draw();

}


function removestave(staveId){
      parent = document.getElementById(staveId).parentNode;
      document.getElementById(staveId).remove();
      g = document.createElement('div'); 
      g.id = staveId;
      g.className = "stave";
      parent.insertBefore(g,parent.childNodes[0]);
}


function addnote(clef, e, dur){
  var notes = [];
  for(i=0; i<dur.length; i++){
    notes[i] = new VF.StaveNote({clef: clef, keys: [e[i]], duration: dur[i]});
    if(sharp.test(e[i])){
      notes[i].addAccidental(0, new VF.Accidental("#"));
      console.log("sharp");
    }
    if(flat.test(e[i])){
      notes[i].addAccidental(0, new VF.Accidental("b"));
      console.log("flat");
    }
  }
  var beams = VF.Beam.generateBeams(notes);
  var formatter = new VF.Formatter.FormatAndDraw(context, stave, notes)
  beams.forEach(function(b) {
    b.setContext(context).draw()
  })
}