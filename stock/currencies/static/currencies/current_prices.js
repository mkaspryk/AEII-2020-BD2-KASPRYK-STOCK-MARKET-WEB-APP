console.log("current_prices sie zajebal")

let currency = "USD"

function format(price){
    return currency + ' ' + price.toFixed(2).toString()
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
    })
}

$(document).ready(refresh_prices)

setInterval(function(){
    refresh_prices()
}, 10000);