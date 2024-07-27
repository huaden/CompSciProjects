
var timerFunc = null;




function updateDay(){

    changeButtonEnd();
    const now = new Date();
    var month = now.getMonth();
    var today = now.getDate();
    var hour = now.getHours();

    var el = document.getElementById("endDate");
    var endDate = el.valueAsDate;
    if(endDate === null){
        endDate = new Date('2024-08-17T00:00');
    }
    else{
        endDate.setTime(endDate.getTime() + 4 * 60 * 60 * 1000);
    }

    document.getElementById("dateInfo").innerHTML = "Countdown until: " + endDate.toLocaleDateString();

    var dif = (endDate-now)/1000;
    var difDays = Math.trunc(dif/60/60/24);
    dif -= difDays*60*60*24;
    var difHours = Math.trunc(dif/60/60);
    dif -= difHours*60*60;
    var difMin = Math.trunc(dif/60);
    dif -= difMin*60;
    var difSec = Math.trunc(dif);


    timerFunc = setInterval(function() {
    if(difSec < 0){
        difMin -= 1;
        difSec = 59;
    }
    if(difMin < 0){
        difHours -= 1;
        difMin = 59;
    }
    if(difHours < 0){
        difDays -= 1;
        difHours = 23;
    }
    if(difDays < 0){
        clearInterval(timerFunc);
        document.getElementById("timer").innerHTML = "YIPPEE UR DONE WITH WORK!!!"
    }
    else{
        document.getElementById("days").innerHTML = difDays;
        document.getElementById("hours").innerHTML = difHours;
        document.getElementById("min").innerHTML = difMin;
        document.getElementById("sec").innerHTML = difSec;
        difSec -= 1;
    }

 }, 1000);


}

function changeButtonEnd(){
    document.getElementById("updateTimer").innerHTML = "New Date?";
    clearInterval(timerFunc);
}
