var Data = function () {
    const startWaarde = 350;

    const stapGrootte = 1162.5;
    const value1 = startWaarde + stapGrootte;
    const value2 = value1 + stapGrootte;
    const value3 = value2 + stapGrootte;
    const value4 = value3 + stapGrootte;
    
    return [value1, value2, value3, value4];
};

var randomValue = function () {
    return Math.min(5000, Math.max(350, Math.random() * (5000 - 350) + 350));
};

var config = {
    type: 'gauge',
    data: {
        labels: [null, null, null, null],
        datasets: [{
            data: Data(),
            value: randomValue(),
            backgroundColor: ['green', 'yellow', 'orange', 'red'],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
        },
        layout: {
            padding: {
                bottom: 30
            }
        },
        needle: {
            radiusPercentage: 2,
            widthPercentage: 3.2,
            color: 'rgba(0, 0, 0, 1)'
        },
        valueLabel: {
            display: true,
            formatter: function (value) {
                return value.toFixed(2);
            },
            color: 'rgba(0, 0, 0, 1.0)',
            backgroundColor: null,
            font: {
                size: 20,
                weight: 'bold'
            }
        },
        plugins: {
            datalabels: {
                display: false
            }
        }
    }
};

function calculateNeedleAngle(value) {
    var normalizedValue = Math.min(5000, Math.max(350, value));
    var percentage = (normalizedValue - 350) / (5000 - 350);
    var degrees = percentage * 180;
    return degrees;
}

window.onload = function () {
    var ctx = document.getElementById('chart').getContext('2d');
    window.myGauge = new Chart(ctx, config);
};
config.data.datasets[0].data = Data();
var newValue = randomValue();
config.data.datasets[0].value = newValue;
config.options.needle.rotation = calculateNeedleAngle(newValue);
window.myGauge.update();





