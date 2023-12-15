
function updateThermometer(val) {
    const liquid = document.getElementById("thermometer-liquid");
    const valueDisplay = document.getElementById("value-display");
    const outerBorder = document.getElementById("outer-line");
    const color = getColor(val);
    const height = (val / 5) * 100 + "%";
    liquid.style.height = height;
    if(val == 0){
        liquid.style.height = 5+"%";
    }
    outerBorder.style.borderColor = color;
    liquid.style.backgroundColor = color;
    liquid.style.backgroundColor = color;
    valueDisplay.innerText = Math.ceil(val);
}

function getColor(value) {
    if (value <= 1) {
        return "green";
    } else if (value <= 2) {
        return "yellow";
    } else if (value <= 4) {
        return "orange";
    } else {
        return "red";
    }
}

// updateThermometer(1);