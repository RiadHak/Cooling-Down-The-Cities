var airP;
var temperature;
var humidity

fetch("http://127.0.0.1:8000/getDataFromDB/").then(response => response.json()).then(data => {
    
    let tempFetch = data['data'][1];
    let Co2Fetch = data['data'][2];
    let humidityFetch = data['data'][3];
    let airPressureFetch = data['data'][4];
    let thermometerFetch = data['data'][5];
    window.chartValues = { airP: airPressureFetch, temperature: tempFetch, humidity: humidityFetch, co2: Co2Fetch, aqi: thermometerFetch };
    allCharts(Co2Fetch, tempFetch, humidityFetch, airPressureFetch, thermometerFetch);
});


function allCharts(co2, temp, humidity, airP, thermometer) {
    setTempValue(temp); // update temperature gauge
    updateCo2(co2); // update co2 gauge
    updateHumidity(humidity); // update humidity gauge
    updateAirP(airP); // update air pressure gauge
    updateThermometer(thermometer); // update air quality gauge
}


















// function allCharts() {
//     updateAirP(1020); // update air pressure gauge
//     setTempValue(25); // update temperature gauge
//     updateHumidity(60); // update humidity gauge
//     updateThermometer(25); // update air quality gauge
//     updateCo2(500); // update co2 gauge
// }