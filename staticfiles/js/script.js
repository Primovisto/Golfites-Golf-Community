
    jQuery(document).ready(function(){
  jQuery('.slider-active').owlCarousel({
    loop:true,
      navText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
      animateIn: 'fadeIn',
      nav:true,
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



$(document).ready(function() {
    $('.nav .dropdown').hover(function() {
        $(this).addClass('open');
    }, function() {
        $(this).removeClass('open');
    });
});
