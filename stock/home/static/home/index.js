var barCount = 60;
var initialDateStr = '01 Apr 2020 00:00 Z';
function initChart(chartName, label){
	var ctx = document.getElementById(chartName).getContext('2d');
	var chart = new Chart(ctx, {
		type: 'candlestick',
		data: {
			datasets: [{
				label: label,
				data: getRandomData(initialDateStr, barCount)
			}]
		},
		options: {
			scales: {
				x: {
					afterBuildTicks: function(scale) {
						const majorUnit = scale._majorUnit;
						const ticks = scale.ticks;
						const firstTick = ticks[0];
						let i, ilen, val, tick, currMajor, lastMajor;

						val = luxon.DateTime.fromMillis(ticks[0].value);
						if ((majorUnit === 'minute' && val.second === 0)
								|| (majorUnit === 'hour' && val.minute === 0)
								|| (majorUnit === 'day' && val.hour === 9)
								|| (majorUnit === 'month' && val.day <= 3 && val.weekday === 1)
								|| (majorUnit === 'year' && val.month === 0)) {
							firstTick.major = true;
						} else {
							firstTick.major = false;
						}
						lastMajor = val.get(majorUnit);

						for (i = 1, ilen = ticks.length; i < ilen; i++) {
							tick = ticks[i];
							val = luxon.DateTime.fromMillis(tick.value);
							currMajor = val.get(majorUnit);
							tick.major = currMajor !== lastMajor;
							lastMajor = currMajor;
						}
						return ticks;
					}
				}
			}
		}
	});
}

initChart("chart1", "Bitcoin (BTC)");
initChart("chart2", "Ethereum (ETH)");
initChart("chart3", "Ripple (XRP)");
initChart("chart4", "Litecoin (LTC)");
initChart("chart5", "Tether (USDT)");
initChart("chart6", "Libra (LIBRA)");
initChart("chart7", "Monero (XMR)");
initChart("chart8", "EOS (EOS)");
initChart("chart9", "Binance Coin (BNB)");

var getRandomInt = function(max) {
	return Math.floor(Math.random() * Math.floor(max));
};

function randomNumber(min, max) {
	return Math.random() * (max - min) + min;
}

function randomBar(date, lastClose) {
	var open = randomNumber(lastClose * 0.95, lastClose * 1.05).toFixed(2);
	var close = randomNumber(open * 0.95, open * 1.05).toFixed(2);
	var high = randomNumber(Math.max(open, close), Math.max(open, close) * 1.1).toFixed(2);
	var low = randomNumber(Math.min(open, close) * 0.9, Math.min(open, close)).toFixed(2);
	return {
		t: date.valueOf(),
		o: open,
		h: high,
		l: low,
		c: close
	};

}

function getRandomData(dateStr, count) {
	var date = luxon.DateTime.fromRFC2822(dateStr);
	var data = [randomBar(date, 30)];
	while (data.length < count) {
		date = date.plus({days: 1});
		if (date.weekday <= 5) {
			data.push(randomBar(date, data[data.length - 1].c));
		}
	}
	return data;
}

var update = function() {
	var dataset = chart.config.data.datasets[0];

	// candlestick vs ohlc
	var type = document.getElementById('type').value;
	dataset.type = type;

	// linear vs log
	var scaleType = document.getElementById('scale-type').value;
	chart.config.options.scales.y.type = scaleType;

	// color
	var colorScheme = document.getElementById('color-scheme').value;
	if (colorScheme === 'neon') {
		dataset.color = {
			up: '#01ff01',
			down: '#fe0000',
			unchanged: '#999',
		};
	} else {
		delete dataset.color;
	}

	// border
	var border = document.getElementById('border').value;
	var defaultOpts = Chart.defaults.elements[type];
	if (border === 'true') {
		dataset.borderColor = defaultOpts.borderColor;
	} else {
		dataset.borderColor = {
			up: defaultOpts.color.up,
			down: defaultOpts.color.down,
			unchanged: defaultOpts.color.up
		};
	}
	chart.update();
};