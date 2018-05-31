var header_one = document.querySelector("#HOVER");
var header_two = document.querySelector("#CLICK");
var header_three = document.querySelector("#DCLICK");

header_one.addEventListener('mouseover', function() {
    header_one.textContent = "Mouse Currently Over Me";
    header_one.style.color = "red";
});

header_one.addEventListener("mouseout", function(){
   header_one.textContent = "HOVER OVER ME";
   header_one.style.color = "black";
});

header_two.addEventListener("click", function(){
   header_two.textContent = "Click On";
   header_two.style.color = "blue";
});

header_three.addEventListener("dblclick", function(){
   header_three.textContent = "I Was Double Clicked";
   header_three.style.color = "green";
});