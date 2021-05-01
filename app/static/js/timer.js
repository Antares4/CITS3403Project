

var context;
var stave
function getRandomCanidate(){
    var canidates = []
    canidates[0] = Math.floor(Math.random() * 8) 
    canidates[1] = canidates[0];
    while(canidates[1] == canidates[0]){
        canidates[1] =  Math.floor(Math.random() * 8) 
    }
    return canidates
}

function btnAssingInOrder(btn1ID, btn2ID, contents){
    document.getElementById(btn1ID).innerHTML = contents[0][1];
    document.getElementById(btn2ID).innerHTML = contents[1][1];
}
function btnAssignReOrder(btn1ID, btn2ID, contents){
    document.getElementById(btn1ID).innerHTML = contents[1][1];
    document.getElementById(btn2ID).innerHTML = contents[0][1];
}

function getRandomClef(){
    clef = Math.round(Math.random())
    return clef == 0 ? "treble" : "bass"
}

function renderStaveNotes(element, note, clef){
    var base = init(element,clef,null,200,null)
    addnote(clef,[note],["q"], base);
}



