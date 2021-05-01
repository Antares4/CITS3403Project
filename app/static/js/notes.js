


const sharp = /[a-z]\#\/\d/;
const flat = /[a-z]b\/\d/;
const dotted = /[a-z]*\d*d/

function init(element, clef, time,stavelength,keysig=null){
  VF = Vex.Flow;
  var div = document.getElementById(element)
  var renderer = new VF.Renderer(div, VF.Renderer.Backends.SVG);
  renderer.resize(stavelength, 200);
  var context = renderer.getContext();
  context.setFont("Arial", 10, "").setBackgroundFillStyle("#eed");
  var stave= new VF.Stave(0, 0, stavelength);
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
  base = [context,stave];
  return base;
}


function removestave(staveId){
      parent = document.getElementById(staveId).parentNode;
      document.getElementById(staveId).remove();
      g = document.createElement('div'); 
      g.id = staveId;
      g.className = "stave";
      parent.insertBefore(g,parent.childNodes[0]);
}


function addnote(clef, e, dur, context){
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
    if(dotted.test(dur[i])){
      notes[i].addDotToAll();
    }
  }
  var beams = VF.Beam.generateBeams(notes);
  var formatter = new VF.Formatter.FormatAndDraw(context[0], context[1], notes)
  beams.forEach(function(b) {
    b.setContext(context).draw()
  })
}




