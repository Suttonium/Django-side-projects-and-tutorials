var car_info = {
    make: "Toyota",
    year: 1990,
    model: "Camry",
    carAlert: function () {
        alert("We've got a car here!");
    }
};

var simple = {
    prop: "Hello",
    my_method: function () {
        console.log("The my_method was called");
    }
};

simple.my_method();  // prints 'The my_method was called'

var my_obj = {
    name: "Austin",
    greet: function () {
        console.log("Hello " + this.name);
    }
};