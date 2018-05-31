var countries = ["USA", "GERMANY", "CHINA"];  //basic syntax
countries[2] = "FRANCE";  //change specific value in array, very similar to other languages
// countries now equals ["USA", "GERMANY", "FRANCE"]

// you can index through arrays and strings the same way, but you cannot change specific values within strings
// EX:
var country_one = "SPAIN";
country_one[2] = "B";  // does not change the string at all


// JS arrays can have mixed data types
var mixed_types = [true, 20, "string"];
var length_of_mixed_types = mixed_types.length;

var my_array = ['one', 'two', 'three'];
// removing from arrays in JS is similar to the stacks --> pop()
var last_item_of_my_array = my_array.pop();  //last item now equals 'three'
var new_item = 'four';
my_array.push(new_item);  // appending to an array is also similar to stacks or python logic

// getting the last item again...
var last_item_of_my_array_v_two = my_array[my_array.length - 1];

var matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]; // yay 2D arrays...

var length_is_still_three = matrix.length;

//array iteration
var array = ["A", "B", "C"];
for (var i = 0; i < array.length; i++) {
    // do stuff
}

array.forEach(alert); // for each loop

function add_awesome(name){
    return name + " is awesome!";
}

var topics = ["python", "django", "SQL"];
topics.forEach(add_awesome); // will iterate and output function result