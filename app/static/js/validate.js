function submissionvalidate(){
    var warnings = document.getElementsByClassName("warning")
    if(warnings != null){
        len = warnings.length;
        for(i=0; i<len; i++){
            warnings[0].remove();
        }
    }
    var answerField = document.getElementsByClassName("response");
    for(i = 0; i<answerField.length; i++){
        if(answerField[i].value == ""){
            var error = document.createElement("div")
            error.innerHTML = "Can not have empty field"
            error.className = "warning"
            answerField[i].parentNode.insertBefore(error,answerField[i].nextSibling)
            event.preventDefault()
        }
        else if(answerField[i].value.length > 100){
            var error = document.createElement("div")
            error.innerHTML = "exeed word limit"
            error.className="warning"
            answerField[i].parentNode.insertBefore(error,answerField[i].nextSibling)
            event.preventDefault()
        }
    }
    return true
}