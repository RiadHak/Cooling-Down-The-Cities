
var tempValue = 10;
// setTempValue(25);

let value = tempValue* 2.64;
document.getElementById("span1").innerHTML = tempValue;


document.getElementById("temparature-meter__inner-ring").innerHTML += "<style>#temparature-meter__inner-ring::after{transform: rotatez(" + (value) + "deg);}</style>";

function setTempValue(val) {

    tempValue = val;
    document.getElementById("span1").innerHTML = tempValue;
    if (val < 0) {
        val = val*6.5;
    }
    else if (val > 0) {
        val = val*2.4;
    }
    document.getElementById("temparature-meter__inner-ring").innerHTML += "<style>#temparature-meter__inner-ring::after{transform: rotatez(" + (val) + "deg);}</style>";
}





// export default setTempValue;    

// export{tempValue}
