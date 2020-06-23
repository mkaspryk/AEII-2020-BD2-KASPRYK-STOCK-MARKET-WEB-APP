console.log("current_prices sie zaladowal")

function refresh_prices() {
    $.getJSON('currencies/prices.json', function (data) {
        console.log(data)
        $("#btc_price").html(data.btc)
        $("#eth_price").html(data.eth)
        $("#xrp_price").html(data.xrp)
        $("#ltc_price").html(data.ltc)
        $("#usdt_price").html(data.usdt)
        $("#libra_price").html('NaN')
        $("#xmr_price").html(data.xmr)
        $("#eos_price").html(data.eos)
        $("#bnb_price").html(data.bnb)
    })
}

$(document).ready(refresh_prices)

setInterval(function(){
    refresh_prices()
}, 5000);