document.getElementById('humidity-chart').setAttribute('chart-value', Math.floor(Math.random() * 100) + 1);
water.style.height = document.getElementById("humidity-chart").getAttribute('chart-value') + '%';
document.getElementById('percentage').innerText = document.getElementById("humidity-chart").getAttribute('chart-value') + '%';
