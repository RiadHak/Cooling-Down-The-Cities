// set custom attribute for chart value
var dashboardCharts = document.getElementsByClassName('dashboard-chart');
Array.prototype.forEach.call(dashboardCharts, chartField => {chartField.setAttribute('chart-value', "")});