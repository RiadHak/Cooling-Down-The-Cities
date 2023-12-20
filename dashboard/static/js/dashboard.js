google.charts.load('current', {'packages':['corechart']});



document.addEventListener('DOMContentLoaded', function() {
    var dashboardCharts = document.getElementsByClassName('dashboard-chart');
    Array.prototype.forEach.call(dashboardCharts, chartField => {chartField.setAttribute('chart-value', "")});

    var isTemperatureGraphLoaded = false;
    var isCO2GraphLoaded = false;
    var isAirPressureGraphLoaded = false;
    var isHumidityGraphLoaded = false;

    $('#temperature-chart').on('click', function() {
        if (!isTemperatureGraphLoaded) {
            loadTemperatureGraph();
            isTemperatureGraphLoaded = true;
            isHumidityGraphLoaded = false;
            isCO2GraphLoaded = false;
            isAirPressureGraphLoaded = false;
        }
    });

    $('#co2-chart').on('click', function() {
        if (!isCO2GraphLoaded) {
            loadCO2Graph();
            isCO2GraphLoaded = true;
            isHumidityGraphLoaded = false;
            isTemperatureGraphLoaded = false;
            isAirPressureGraphLoaded = false;
        }
    });

    $('#pressure-chart').on('click', function() {
        if (!isAirPressureGraphLoaded) {
            loadAirPressureGraph();
            isAirPressureGraphLoaded = true;    
            isTemperatureGraphLoaded = false;
            isCO2GraphLoaded = false;
            isAirPressureGraphLoaded = false;
        }
    });

    $('#humidity-chart').on('click', function() {
        if (!isHumidityGraphLoaded) {
            loadHumidityGraph();
            isHumidityGraphLoaded = true;
            isTemperatureGraphLoaded = false;
            isCO2GraphLoaded = false;
            isAirPressureGraphLoaded = false;
        }
    });

    $('#aqi-chart').on('click', function() {
        loadAQIGraph();
        isHumidityGraphLoaded = false;
        isTemperatureGraphLoaded = false;
        isCO2GraphLoaded = false;
        isAirPressureGraphLoaded = false;
    });

    
    function generateWeekData(dataType) {
        var currentDate = new Date();
        var daysOfWeek = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']; // Days of the week
        var sensorData = [];

        // Generate data for each day of the week
        for (var i = 0; i < 7; i++) {
            var day = daysOfWeek[currentDate.getDay()];
            var temperature = dataType == chartValues.temperature ? dataType : null;
            var co2 = dataType == chartValues.co2 ? dataType : null;
            var airPressure = dataType == chartValues.airP ? dataType : null;
            var humidity = dataType == chartValues.humidity ? dataType : null;
            var air = dataType == chartValues.aqi ? dataType : null;

            sensorData.push({
                timestamp: day + ' ' + currentDate.getDate() + ' ' + getMonthAbbreviation(currentDate.getMonth()),
                temperatuur: temperature,
                co2: co2,
                luchtdruk: airPressure,
                luchtvochtigheid: humidity,
                luchtkwaliteit: air
            });

            currentDate.setDate(currentDate.getDate() - 1);
        }

        return sensorData.reverse(); 
    }

    
    function getMonthAbbreviation(monthIndex) {
        var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        return months[monthIndex];
    }

    function loadTemperatureGraph() {
        var temperatureData = chartValues.temperature;
        console.log(temperatureData);
        var temperatureChartData = generateWeekData(temperatureData);

        google.charts.setOnLoadCallback(function() {
            var dataTable = new google.visualization.DataTable();
            dataTable.addColumn('string', 'Timestamp');
            dataTable.addColumn('number', 'Temperatuur');

            temperatureChartData.forEach(function(entry) {
                dataTable.addRow([entry.timestamp, entry.temperatuur]);
            });

            var options = {
                title: 'Temperatuur Data',
                legend: { position: 'none' },
                hAxis: { title: 'Timestamp' },
                vAxis: { title: 'Temperatuur' }
            };

            var chart = new google.visualization.ColumnChart(document.getElementById('weather-frame'));
            chart.draw(dataTable, options);
        });
    }

    function loadCO2Graph() {
        var co2Data = chartValues.co2;

        var co2ChartData = generateWeekData(co2Data);

        google.charts.setOnLoadCallback(function() {
            var dataTable = new google.visualization.DataTable();
            dataTable.addColumn('string', 'Timestamp');
            dataTable.addColumn('number', 'CO2');

            co2ChartData.forEach(function(entry) {
                dataTable.addRow([entry.timestamp, entry.co2]);
            });

            var options = {
                title: 'CO2 Data',
                legend: { position: 'none' },
                hAxis: { title: 'Timestamp' },
                vAxis: { title: 'CO2' }
            };

            var chart = new google.visualization.ColumnChart(document.getElementById('weather-frame'));
            chart.draw(dataTable, options);
        });
    }

    function loadAirPressureGraph() {
        var airPressureData = chartValues.airP;

        var airPressureChartData = generateWeekData(airPressureData);

        google.charts.setOnLoadCallback(function() {
            var dataTable = new google.visualization.DataTable();
            dataTable.addColumn('string', 'Timestamp');
            dataTable.addColumn('number', 'Luchtdruk');

            airPressureChartData.forEach(function(entry) {
                dataTable.addRow([entry.timestamp, entry.luchtdruk]);
            });

            var options = {
                title: 'Luchtdruk Data',
                legend: { position: 'none' },
                hAxis: { title: 'Timestamp' },
                vAxis: { title: 'Luchtdruk' }
            };

            var chart = new google.visualization.ColumnChart(document.getElementById('weather-frame'));
            chart.draw(dataTable, options);
        });
    }

    function loadHumidityGraph() {
        var humidityData = chartValues.humidity;

        var humidityChartData = generateWeekData(humidityData);

        google.charts.setOnLoadCallback(function() {
            var dataTable = new google.visualization.DataTable();
            dataTable.addColumn('string', 'Timestamp');
            dataTable.addColumn('number', 'Luchtvochtigheid');

            humidityChartData.forEach(function(entry) {
                dataTable.addRow([entry.timestamp, entry.luchtvochtigheid]);
            });

            var options = {
                title: 'Luchtvochtigheid Data',
                legend: { position: 'none' },
                hAxis: { title: 'Timestamp' },
                vAxis: { title: 'Luchtvochtigheid' }
            };

            var chart = new google.visualization.ColumnChart(document.getElementById('weather-frame'));
            chart.draw(dataTable, options);
        });
    }

    function loadAQIGraph() {
        var aqiData = chartValues.aqi;

        var aqiChartData = generateWeekData(aqiData);

        google.charts.setOnLoadCallback(function() {
            var dataTable = new google.visualization.DataTable();
            dataTable.addColumn('string', 'Timestamp');
            dataTable.addColumn('number', 'Air Quality');

            aqiChartData.forEach(function(entry) {
                dataTable.addRow([entry.timestamp, entry.luchtkwaliteit]);
            });

            var options = {
                title: 'Air Quality',
                legend: { position: 'none' },
                hAxis: { title: 'Timestamp' },
                vAxis: { title: 'Air Quality' }
            };

            var chart = new google.visualization.ColumnChart(document.getElementById('weather-frame'));
            chart.draw(dataTable, options);
        });
    }

});
