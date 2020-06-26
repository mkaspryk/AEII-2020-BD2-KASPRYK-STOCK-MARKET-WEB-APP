console.log("quick_purchase_panel has been loaded")

var balanceField = document.getElementById("balance-field")
var visibilityToggle = document.getElementById("balance-visibility-toggle")
var locked_on = false

visibilityToggle.onmouseover = function() {mouseOver()};
visibilityToggle.onmouseout = function() {mouseOut()};
visibilityToggle.onclick = function() {click()};

function click() {
    locked_on = !locked_on
}

function mouseOut() {
    if(!locked_on) {
        balanceField.innerHTML = "balance";
    }
}

function mouseOver() {
    if(!locked_on){
        balanceField.innerHTML = "$45,227.19";
    }
}