function format(price){
    return price.toFixed(2).toString()
}

function refresh_prices() {
    $.getJSON('currencies/prices.json', function (data) {
        console.log(data)
        $("#bitcoin_price").html(format(data.bitcoin))
        $("#ethereum_price").html(format(data.ethereum))
        $("#ripple_price").html(format(data.ripple))
        $("#litecoin_price").html(format(data.litecoin))
        $("#tether_price").html(format(data.tether))
        $("#tezos_price").html(format(data.tezos))
        $("#monero_price").html(format(data.monero))
        $("#eos_price").html(format(data.eos))
        $("#binancecoin_price").html(format(data.binancecoin))
        let elements = document.getElementsByClassName("red_green_yellow")
        Array.prototype.forEach.call(elements, function(elem){
            let value = parseFloat(elem.innerHTML)
            if(value < 0.0){
              elem.style.color = 'red'
            }else{
              elem.style.color = 'green'
            }
        })
    })
}

refresh_prices()
$(document).ready(
    setInterval(function(){
        refresh_prices()
}, 10000))