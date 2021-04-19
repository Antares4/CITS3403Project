VF = Vex.Flow
function staveinit(question){
    //Create an SVG renderer and attach it to the DIV element named "boo".
    div = document.getElementById("boo")
    var renderer = new VF.Renderer(div, VF.Renderer.Backends.SVG);
    // Size our SVG:
    renderer.resize(500, 500);
    //And get a drawing context:
    var context = renderer.getContext();
    //Create a stave at position 10, 40 of width 400 on the canvas.
    var stave = new VF.Stave(10, 40, 400);
    //Add a clef and time signature.
    stave.addClef("treble").addTimeSignature("4/4");
    //Connect it to the rendering context and draw!
    var notes = [
        // A quarter-note C.
        new VF.StaveNote({clef: "treble", keys: ["c/4"], duration: "q" }),
      
        // A quarter-note D.
        new VF.StaveNote({clef: "treble", keys: ["d/4"], duration: "q" }),
      
        // A quarter-note rest. Note that the key (b/4) specifies the vertical
        // position of the rest.
        new VF.StaveNote({clef: "treble", keys: ["b/4"], duration: "qr" }),
      
        // A C-Major chord.
        new VF.StaveNote({clef: "treble", keys: ["c/4", "e/4", "g/4"], duration: "q" })
      ];
      
      // Create a voice in 4/4 and add the notes from above
      var voice = new VF.Voice({num_beats: 4,  beat_value: 4});
      voice.addTickables(notes);
      
      // Format and justify the notes to 400 pixels.
      var formatter = new VF.Formatter().joinVoices([voice]).format([voice], 400);
      
      stave.setContext(context).draw();
      // Render voice
      voice.draw(context, stave);
}

// system.addStave({
//     voices: [score.voice(score.notes('C#5/q, B4, A4, G#4'))]
// }).addClef('treble').addTimeSignature('4/4');
// vf.draw();
function modify(){

}


function a(){
    $.getJSON($SCRIPT_ROOT + '/a', {
        a: 9,
        b: 6
        }, function(data) {
        $("#boo").text(data.result);
        console.log(data.result);
        document.getElementById("sta").innerHTML = data.result;
    }) 
}

$(document).ready(s => {
    $("#bt").bind("click", a);
})
