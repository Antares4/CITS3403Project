VF = Vex.Flow
function intermediate(location){
    loc = document.getElementById(location)
    var renderer = new VF.Renderer(loc, VF.Renderer.Backends.SVG);
    renderer.resize(600, 120);
    var context = renderer.getContext();

    var stave1 = new VF.Stave(0, 0, 250);
    stave1.addClef("treble").addKeySignature("F#m").addTimeSignature("6/8").setContext(context).draw();
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



function difficult(location1,location2){
    loc = document.getElementById(location1)
    var renderer = new VF.Renderer(loc, VF.Renderer.Backends.SVG);
    renderer.resize(600, 120);
    var context = renderer.getContext();

    var stave1 = new VF.Stave(0, 0, 300);
    stave1.addClef("treble").addKeySignature("F").setContext(context).draw();
    var stave2 = new Vex.Flow.Stave(stave1.width + stave1.x, 0 , 250);
    stave2.setContext(context).draw();

    var stave1notes = [
        new VF.StaveNote({clef: "treble", keys: ["a/5"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["d/5"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["b/4"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["g/5"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["d/5"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["b/4"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["b/5"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["d/5"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["b/4"], duration: "8" })
    ];
    var beam1 = VF.Beam.generateBeams(stave1notes,{
        groups: [new Vex.Flow.Fraction(3, 8)]
    });
    Vex.Flow.Formatter.FormatAndDraw(context, stave1, stave1notes);
    beam1.forEach(function(b) {
        b.setContext(context).draw()
    })
    var stave2notes = [
        new VF.StaveNote({clef: "treble", keys: ["a/5"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["d/5"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["b/4"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["g/5"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["d/5"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["b/4"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["f/5"], duration: "8" }),
        new VF.StaveNote({clef: "treble", keys: ["c#/5"], duration: "8" }).addAccidental(0, new VF.Accidental("#")),
        new VF.StaveNote({clef: "treble", keys: ["g/4"], duration: "8" })
    ];
    var beam2 = VF.Beam.generateBeams(stave2notes,{
        groups: [new Vex.Flow.Fraction(3, 8)]
    });
    Vex.Flow.Formatter.FormatAndDraw(context, stave2, stave2notes);
    beam2.forEach(function(b) {
        b.setContext(context).draw()
    })
    
    loc2 = document.getElementById(location2)
    renderer = new VF.Renderer(loc2, VF.Renderer.Backends.SVG);
    renderer.resize(600, 120);
    context = renderer.getContext();

    var stave1 = new VF.Stave(0, 0, 300);
    stave1.addClef("bass").addKeySignature("F").setContext(context).draw();
    var stave2 = new Vex.Flow.Stave(stave1.width + stave1.x, 0 , 250);
    stave2.setContext(context).draw();

    stave1notes2 = [
        new VF.StaveNote({clef: "bass", keys: ["a/3"], duration: "8" }),
        new VF.StaveNote({clef: "bass", keys: ["d/3"], duration: "8" }),
        new VF.StaveNote({clef: "bass", keys: ["b/2"], duration: "8" }),
        new VF.StaveNote({clef: "bass", keys: ["g/3"], duration: "8" }),
        new VF.StaveNote({clef: "bass", keys: ["d/3"], duration: "8" }),
        new VF.StaveNote({clef: "bass", keys: ["b/2"], duration: "8" }),
        new VF.StaveNote({clef: "bass", keys: ["b/3"], duration: "8" }),
        new VF.StaveNote({clef: "bass", keys: ["d/3"], duration: "8" }),
        new VF.StaveNote({clef: "bass", keys: ["b/2"], duration: "8" })
    ];
    var beam1 = VF.Beam.generateBeams(stave1notes2,{
        groups: [new Vex.Flow.Fraction(3, 8)]
    });
    Vex.Flow.Formatter.FormatAndDraw(context, stave1, stave1notes2);
    beam1.forEach(function(b) {
        b.setContext(context).draw()
    })
    stave2notes2 = [
        new VF.StaveNote({clef: "bass", keys: ["a/3"], duration: "8" }),
        new VF.StaveNote({clef: "bass", keys: ["d/3"], duration: "8" }),
        new VF.StaveNote({clef: "bass", keys: ["b/2"], duration: "8" }),
        new VF.StaveNote({clef: "bass", keys: ["g/3"], duration: "8" }),
        new VF.StaveNote({clef: "bass", keys: ["d/3"], duration: "8" }),
        new VF.StaveNote({clef: "bass", keys: ["b/2"], duration: "8" }),
        new VF.StaveNote({clef: "bass", keys: ["f/3"], duration: "8" }),
        new VF.StaveNote({clef: "bass", keys: ["d#/3"], duration: "8" }).addAccidental(0, new VF.Accidental("#")),
        new VF.StaveNote({clef: "bass", keys: ["g/2"], duration: "8" })
    ];
    var beam2 = VF.Beam.generateBeams(stave2notes2,{
        groups: [new Vex.Flow.Fraction(3, 8)]
    });
    Vex.Flow.Formatter.FormatAndDraw(context, stave2, stave2notes2);
    beam2.forEach(function(b) {
        b.setContext(context).draw()
    })
}