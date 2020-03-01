
function runcounter(){

    var i;
    var k = 1;
    for (i = 0; i < 15000; i++) {
        if(i % 1000 === 0){
            console.log("Reached " + k + "seconds");
        }
    }
}