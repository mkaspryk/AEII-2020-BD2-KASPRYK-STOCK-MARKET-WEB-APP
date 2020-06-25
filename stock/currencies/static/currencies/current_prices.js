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

// TODO: refreshing order after refreshing prices

var table = $('#current-prices-table');
$('#currency-id-header, #currency-price-header, #currency-change-header')
    .each(function(){
        var th = $(this),
            thIndex = th.index(),
            inverse = false;
        th.click(function(){
            var column = table.find('td').filter(function(){
                return $(this).index() === thIndex;
            })
            console.log(this.id)
            if(this.id==="currency-id-header"){
                column.sortElements(
                function(a, b){
                return $.text([a]) > $.text([b]) ?
                    inverse ? -1 : 1
                    : inverse ? 1 : -1;
            }, function(){
                // parentNode is the element we want to move
                return this.parentNode;
            });
            } else {
                column.sortElements(
                function(a, b){
                return parseFloat($.text([a])) > parseFloat($.text([b])) ?
                    inverse ? -1 : 1
                    : inverse ? 1 : -1;
            }, function(){
                // parentNode is the element we want to move
                return this.parentNode;
            });
            }
            inverse = !inverse;
        });
    });

refresh_prices()
$(document).ready(
    setInterval(function(){
        refresh_prices()
    }, 5000))