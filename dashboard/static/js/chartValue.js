
console.log("ChartValue.js loaded");
fetch("http://127.0.0.1:8000/getDataFromDB/").then(response => response.json()).then(data => {
    console.log(data);
    let temp = data['data'][1];
    let Co2 = data['data'][2];
    let humidity = data['data'][3];
    let airP = data['data'][4];
    let thermometer = data['data'][5];
    allCharts(Co2, temp, humidity, airP, thermometer);
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