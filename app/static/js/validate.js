/* Validation functions for form validation */ 

//Checks for missing field and word limit of a submission
function submissionvalidate(admin){
    if(admin != 0){
        removewarning();
        var answerField = document.getElementsByClassName("response");
        for(i = 0; i<answerField.length; i++){
            if(answerField[i].value == ""){
                createwarning("[This field is required.]",answerField[i])
            }
            else if(answerField[i].value.length > 100){
                createwarning("[Exeed word limit]",answerField[i]);
            }
        }
        return true
    }
    else{
        return true
    }   
}

//check for missing field in login 
function loginValidate(){
    removewarning();
    var usernamefield = document.getElementById("loginname");
    var passwordfield = document.getElementById("loginpwd");
    if(usernamefield.value == ""){
        createwarning("[This field is required.]",usernamefield);
    }
    if(passwordfield.value == ""){
        createwarning("[This field is required.]",passwordfield)
    }
}

//check for invalid registration input 
function registerValidate(){
    removewarning();
    var usernamefield = document.getElementById("regUsrName");
    var passwordfield = document.getElementById("regPwd");
    var cfmpasswordfield = document.getElementById("regCfmPwd");
    var firstnamefield = document.getElementById("regFirst");
    var lastnamefield = document.getElementById("regLast");
    var emailfield = document.getElementById("regEmail");
    field_list = [usernamefield,passwordfield,cfmpasswordfield,firstnamefield,lastnamefield,emailfield];
    //missing field
    for(var i=0; i<field_list.length;i++){
        if(field_list[i].value == ""){
            createwarning("[This field is required]",field_list[i]);
        }
    }
    //username too long
    if(usernamefield.value.length > 100){
        console.log(usernamefield.value.length )
        createwarning("[Username must be between 1 to 100 characters long.]",usernamefield);
    }
    //password invalid length
    if(passwordfield.value.length < 6 && passwordfield.value.length != 0 || passwordfield.value.length > 80){
        createwarning("[Password must be between 6 to 80 characters long.]",passwordfield);
    }
    //password missmatch
    if(cfmpasswordfield.value != passwordfield.value  && cfmpasswordfield.value.length != 0){
        createwarning("[Password must match.]",cfmpasswordfield);
    }
    //first name too long
    if(firstnamefield.value .length > 129){
        createwarning("[Firstname cannot exceed 130 characters]",firstnamefield);
    }
    //last name too long
    if(lastnamefield.value .length > 129){
        createwarning("[Lastname cannot exceed 130 characters]",lastnamefield);
    }
    //email validation
    if(checkemail(emailfield.value) != true && emailfield.value.length != 0){
        createwarning("[Invalid Email]",emailfield);
    }
}

//removes previous warning
function removewarning(){
    var warnings = document.getElementsByClassName("warning")
    if(warnings != null){
        len = warnings.length;
        for(i=0; i<len; i++){
            warnings[0].remove();
        }
    }
}

//creates warning
function createwarning(message,field){
    var error = document.createElement("div")
    error.innerHTML = message
    error.className = "warning"
    field.parentNode.insertBefore(error,field.nextSibling)
    event.preventDefault()
}

//email validation
function checkemail(email){
    const eml = /^[a-z0-9\-\.\_]+\@[a-z\-]+\.[a-z]{2,}/i;
    if (eml.test(email)){
        return true;
    }
    else{
        return false;
    }
}

