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


$(document).on('submit', '#quick-buy-form', function(e){
    e.preventDefault();
    $.ajax({
        type:'POST',
        url:'/perform_quick_buy/',
        data:{
            buy_amount:$('#id_buy_amount').val(),
            buy_currency:$('#id_buy_currency').val(),
            pay_amount:$('#id_pay_amount').val(),
            pay_currency:$('#id_pay_currency').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){
            console.log($('#id_buy_amount').val())
            console.log($('#id_buy_currency').val())
            console.log($('#id_pay_amount').val())
            console.log($('#id_pay_currency').val())
            alert("woo hoo")
        }
    })
})
