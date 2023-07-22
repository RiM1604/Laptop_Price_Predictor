
function onClickedEstimatePrice() {

    console.log("estimate price clicked");
    var c_name = document.getElementById("comp");
    var m = document.getElementById("mem");
    var r = document.getElementById("ram_value");
    var O = document.getElementById("windows_os");
    var size = document.getElementById("size_of_screen");
    var estPrice = document.getElementById("uiEstimatedPrice");
    console.log(c_name.value)
    console.log(m.value)
    console.log(r.value)
    console.log(O.value)
    console.log(size.value)
    var url = "http://127.0.0.1:5000/predict_prices";
    $.post(url, {//post request u can do get request as well
        company: c_name.value,
        memory: m.value,
        ram: r.value,
        os: O.value,
        size_in_inches: size.value
    }, function (data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + "rupees</h2>";
        console.log(status);
    });
}