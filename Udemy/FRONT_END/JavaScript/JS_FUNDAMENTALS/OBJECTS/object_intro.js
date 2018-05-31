var car_one = {make:"Toyota", year: "1990", model:"Camry"};
var should_be_toyota = car_one["make"];

var my_new_object = {a:"hello", b:[1, 2, 3], c: {inside:['a', 'b']}};  // not typically this nested
var grabbing_hello = my_new_object["a"];  // this is equal to "hello"
var grabbing_array = my_new_object["b"];  // this is the array
var grabbing_specific_array_value = my_new_object["b"][1];  // this is 2 in the array in the object
var grabbing_from_the_object_in_the_object = my_new_object["c"]["inside"][1];  // this is 'b' in the embedded object

car_one["year"] = 2006; // change the value of an object


// iterating through an object

for (var item in car_one) {
    console.log(item);  // takes each item in the object and prints it to the console
    console.log(car_one[item]);  // takes a specific value in the object
}
