/* Optional: Add active class to the current button (highlight it) */
var container = document.getElementById("btnContainer");
var btns = container.getElementsByClassName("btn");
select = 0
for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    select = i;
    this.className += " active";
  });
}
var totalprice = document.getElementById("calculatedprice");
var quantity = document.getElementById("quant");
var pay = document.getElementsByClassName("Payable");
pay.addEventListener('click',function(){
    if(select == 0){
        totalprice.textContent += Number(399)*Number(quantity.textContent);
    }
    else{
        totalprice.textContent += Number(209)*Number(quantity.textContent);
    }
})
