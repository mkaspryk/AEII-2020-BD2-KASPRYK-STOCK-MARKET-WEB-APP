const crypto_names = ['btc', 'eht', 'xrp']
const url = 'https://bitbay.net/API/Public/btc/ticker.json/'

function updatePrice(){
    console.log("zaczynam")
    //$.getJSON("https://api.bitfinex.com/v1/ticker/btcusd", function(data){
    //    console.log(data)
    //    var element = document.getElementById(crypto_name+"_price")
    //    element.innerHTML = String(data.last)
    //})

    var httpreq = new XMLHttpRequest()
    httpreq.open("GET", url, false)
    httpreq.send(null)
    console.log(httpreq.responseText)
    var json = JSON.parse(httpreq.responseText)
    var price = json.last
    var element = document.getElementById("btc_price")
    element.innerHTML = String(2137)
}

updatePrice()