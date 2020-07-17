console.log("current_prices has been loaded")

function format(price){
    return parseFloat(price).toFixed(2).toString()
}

function format_percentage(price_change){
    return parseFloat(price_change).toFixed(3).toString()+"%"
}

function refresh_prices() {
    $.getJSON('/currencies/prices.json/', function (data) {
        $.each(data, function(){
            $("#"+this.name+"_price").html(format(this.current_price))
            let price_change = $("#"+this.name+"_price_change_percentage_24h")
            price_change.html(format_percentage(this.price_change_percentage_24h))
            if(this.price_change_percentage_24h < 0.0){
                price_change.css('color', 'red')
            }else{
                price_change.css('color', 'green')
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