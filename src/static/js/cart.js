$(window).on("scroll", function () {
   // fixed the shopping card when scrolling down
   if ($(window).scrollTop() > 38) {
      $('#cart').css({
         "position": "fixed",
         "top": "50px",
         "right": "30px",
         "z-index": "1001",
         "border": "1.5px solid green",
         "border-radius": "14px",
      });
   } else {
      $('#cart').css({
         "position": "absolute",
         "top": "9px",
         "right": "140px",
         "border": "",
      });
   }
});

// Animation when adding a new product into shopping cart
$("button").on("click", function () {
   $(".badge").addClass("zoom")

   setTimeout(function () {
      $(".badge").removeClass("zoom");
   }, 1000);
});