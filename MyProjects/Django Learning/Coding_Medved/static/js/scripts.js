$(document).ready(function () {
    var form = $('#form_ordering_product')
    console.log(form)
    form.on('submit', function (e) {
        e.preventDefault()
        console.log('123')
        var num = $('#number').val()
        console.log(num)
        var submit_btn = $('#submit_btn')
        var product_id = submit_btn.data('product-id')
        var product_name = submit_btn.data('product-name')
        var product_price = submit_btn.data('product-price')
        console.log(product_id, product_name, product_price * num)

        var data = {}
        data.product_id = product_id
        data.num = num
        var csrf_token = $('#form_ordering_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr('action')

        console.log(data)

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OKi")
            },
            error: function () {
                console.log("error")
            }
        })


        $('.cart-items ul').append('<li>' + product_name + '<br />Quantity: ' + num + ' Price: ' + product_price + ' mon <a class="delete-item" href="#">x</a></li>')
    })

    function showingCart() {
        $('.cart-items').removeClass('hidden')
    }

    $('.cart-container').on('click', function (e) {
        e.preventDefault()
        showingCart()
    })
    $('.cart-container').mouseover(function () {
        showingCart()
    })

    // $('.cart-container').mouseout(function () {
    //     showingCart()
    // })

    $(document).on('click', '.delete-item', function (e) {
        e.preventDefault()
        $(this).closest('li').remove()
    })

})