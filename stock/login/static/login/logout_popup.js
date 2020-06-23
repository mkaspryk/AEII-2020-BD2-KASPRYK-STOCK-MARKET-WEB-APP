console.log("logout_popup has ben loaded")

function logout_popup_handling() {
    var elem = document.getElementById("logout_button");
    var confirmIt = function(e){
        if(!confirm('Do you really want to log out?')) e.preventDefault();
    };

    if(elem) elem.addEventListener('click', confirmIt, false);
}
