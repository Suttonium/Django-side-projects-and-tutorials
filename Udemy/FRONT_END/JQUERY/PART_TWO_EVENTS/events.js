//CLICKS
$('h1').click(function(){
    $(this).text("I was changed");
});

$('li').click(function() {
    console.log('any li was clicked');
});

//KEY PRESS
$('input').eq(0).keypress(function(event){
    if (event.which === 13) {  //13 is the keycode for enter
        $('h3').toggleClass('turnBlue');
    }
});

//on()
$('h1').on('mouseenter', function(){
   $(this).toggleClass('turnBlue');
});

//events and animations
$('input').eq(1).on('click', function(){
   $('.container').fadeOut(3000);
});

