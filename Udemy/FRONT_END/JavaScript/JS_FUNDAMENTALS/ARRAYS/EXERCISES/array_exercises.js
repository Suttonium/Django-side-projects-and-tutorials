var roster = [];

function addNew() {
    var name = prompt("What name would you like to add?");
    roster.push(name);
}

function remove() {
    var name = "What name would you like to remove?";
    var index = roster.indexOf(name);
    roster.splice(index, 1);
}

function display() {
    console.log(roster);
}

function loop() {
    while (request !== "quit") {
        request = prompt("Please select an action: add, remove, display, or quit");
        if (request === "add") {
            addNew();
        }
        else if (request === "remove") {
            remove();
        }
        else if (request === "display") {
            display();
        }
    }
}

var start = prompt("Would you like to start the roster web app? y/n");
var request = "";
if (start === "y") {
    loop()
}
else {
    alert('Thank for using the web app, please refresh to start over');
}

