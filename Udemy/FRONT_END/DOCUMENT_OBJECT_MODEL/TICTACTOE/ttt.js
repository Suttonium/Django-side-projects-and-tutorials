//Restart Game Button
var restart = document.querySelector("#restart button");

//Grab all the squares
var table_cells = document.querySelectorAll("td");

//Clear all the squares
function clear_cells() {
    for (var i = 0; i < table_cells.length; i++) {
        table_cells[i].textContent = "";
    }
}


//Check the square marker
function change_marker() {
    if (this.textContent === "") {
        this.textContent = "X";
    }
    else if (this.textContent === "X") {
        this.textContent = "O";
    }
    else {
        this.textContent = "";
    }
}


//For loop to add event listeners to all the squares
for (var i = 0; i < table_cells.length; i++) {
    table_cells[i].addEventListener("click", change_marker);
}
restart.addEventListener("click", clear_cells);

