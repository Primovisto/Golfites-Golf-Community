$(document).ready(function(){
  $('.slider-active').owlCarousel({
    loop:true,
      navText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
      animateIn: 'fadeIn',
    nav:true,
      autoHeight:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:1
        }
    }
})
});


$('ul.nav li.dropdown').hover(function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn(500);
}, function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut(500);
});