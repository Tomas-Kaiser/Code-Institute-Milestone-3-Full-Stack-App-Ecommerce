$(function () {
   $('.addProductBtn').on('click', function (e) {
      let productId = $(this).attr("productId")
      url = url.replace('0', productId)

      $.ajax({
         type: 'POST',
         url: url,
         data: {
            productId: productId,
            quantity: 1,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
         },
         success: function (data) {
            if ($('.badge').length === 0) {
               $('#cart').append("<span class='badge badge-warning'>1</span>")
            } else {
               let numberItems = $('.badge').text()
               numberItems++
               $('.badge').text(numberItems)
            }
         }
      });

      e.preventDefault();
   });
});