VF = Vex.Flow
function intermediate(location){
    loc = document.getElementById(location)
    var renderer = new VF.Renderer(loc, VF.Renderer.Backends.SVG);
    renderer.resize(600, 120);
    var context = renderer.getContext();

    var stave1 = new VF.Stave(0, 0, 250);
    stave1.addClef("treble").addKeySignature("A").addTimeSignature("6/8").setContext(context).draw();;
    var stave2 = new Vex.Flow.Stave(stave1.width + stave1.x, 0 , 200);
    stave2.setContext(context).draw();

    var stave1notes = [
        new VF.StaveNote({clef: "treble", keys: ["f/4"], duration: "16" }),
        new VF.StaveNote({clef: "treble", keys: ["g/4"], duration: "16" }),
        new VF.StaveNote({clef: "treble", keys: ["c/4"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["e/4"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["b/4"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["c/4"], duration: "q" })
    ];
    var beam1 = VF.Beam.generateBeams(stave1notes);
    Vex.Flow.Formatter.FormatAndDraw(context, stave1, stave1notes);
    beam1.forEach(function(b) {
        b.setContext(context).draw()
    })
    var stave2notes = [
        new VF.StaveNote({clef: "treble", keys: ["c/4"], duration: "16" }),
        new VF.StaveNote({clef: "treble", keys: ["f/4"], duration: "16" }),
        new VF.StaveNote({clef: "treble", keys: ["c/5"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["f/4"], duration: "q" }),
        new VF.StaveNote({clef: "treble", keys: ["c/4"], duration: "8" })
    ];
    var beam2 = VF.Beam.generateBeams(stave2notes);
    Vex.Flow.Formatter.FormatAndDraw(context, stave2, stave2notes);
    beam2.forEach(function(b) {
        b.setContext(context).draw()
    })
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

