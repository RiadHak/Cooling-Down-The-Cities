let tempValue = 10;

let value = tempValue* 2.64;
document.getElementById("span1").innerHTML = tempValue;


document.getElementById("temparature-meter__inner-ring").innerHTML += "<style>#temparature-meter__inner-ring::after{transform: rotatez(" + (value) + "deg);}</style>";


