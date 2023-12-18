

// updateHumidity(10);
function updateHumidity(val) {
    document.getElementById('humidity-chart').setAttribute('chart-value',val);
    water.style.height = document.getElementById("humidity-chart").getAttribute('chart-value') + '%';
    document.getElementById('percentage').innerText = document.getElementById("humidity-chart").getAttribute('chart-value') + '%';

    console.log(val);

}