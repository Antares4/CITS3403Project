

var context;
var stave
// return two random numbers 
function getRandomCanidate(range){
    var canidates = []
    canidates[0] = Math.floor(Math.random() * range) 
    canidates[1] = canidates[0];
    while(canidates[1] == canidates[0]){
        canidates[1] =  Math.floor(Math.random() * range) 
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

function renderStaveKeys(element, clef, key){
    init(element,clef,null,200,key)
}

function renderStaveNotes(element, note, clef){
    init(element,clef,null,200,null)
    addnote(clef,[note],["q"]);
}

