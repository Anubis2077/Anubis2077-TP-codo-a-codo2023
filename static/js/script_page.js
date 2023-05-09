document.getElementById('add-to-cart-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var product_id = document.querySelector('input[name="product_id"]').value;
    $.ajax({
      url: "/add/",
      type: "POST",
      data: {
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        product_id: product_id,
      },
      success: function (data) {
        console.log(data); // para verificar si los datos son correctos
        if (data.success) {
          $('.cart-item-count').text(data.total_productos);
        }
      },
      error: function () {
        alert("Se produjo un error al agregar el producto.");
      },
    });
  });