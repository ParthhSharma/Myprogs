document.getElementById("btn0").addEventListener("click",function(){
    document.getElementById("res").insertAdjacentHTML("beforeend","0");
})
document.getElementById("btn1").addEventListener("click",function(){
    document.getElementById("res").insertAdjacentHTML("beforeend","1");
})
document.getElementById("btnClr").addEventListener("click",function(){
    document.getElementById("res").innerHTML = "";
})
function action(event) {
    var btn = event.target;
    document.getElementById("res").insertAdjacentHTML("beforeend",btn.innerHTML);
}
function solve() {
    let str = document.getElementById("res").innerHTML;
    let a = str.match(/(0|1)+/g);
    var b = str.match(/(\+|\-|\*|\/)+/g);
    var x = a.map(dec);
    function dec(num) {
        return(parseInt(num,2));
    }
    var arr = [];
    for(let i=0;i<x.length;i++){
        arr.push(x[i]);
        arr.push(b[i]);
    }
    var y = eval(arr.join('')).toString(2);
    document.getElementById("res").innerHTML = y;
}
document.getElementById("btnSum").onclick = action;
document.getElementById("btnSub").onclick = action;
document.getElementById("btnMul").onclick = action;
document.getElementById("btnDiv").onclick = action;
document.getElementById("btnEql").onclick = solve;
