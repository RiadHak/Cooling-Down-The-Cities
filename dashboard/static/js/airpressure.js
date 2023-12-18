

var gauge = new RadialGauge({
    renderTo: 'gauge',
    colorNumbers: 'black',
    innerHeight: 200,
    minValue: 940,
    maxValue: 1060,
    majorTicks: ['940', '950', '960', '970', '980', '990', '1000', '1010', '1020', '1030', '1040', '1050', '1060'],
    highlights: [
        { from: 940, to: 1000, color: 'rgba(0, 0, 255, 0.2)' },
        { from: 1000, to: 1020, color: 'rgba(0, 0, 255, 0.5)' },
        { from: 1020, to: 1060, color: 'rgba(0, 0, 255, 0.8)' }
    ],
    units: 'hPa',
    animationDuration: 1500,
    animationRule: "linear",
}).draw();

// updateAirP(1020);
function updateAirP(val) {
    var pressureInput = val;
    gauge.value = pressureInput;
    gauge.draw();
}

