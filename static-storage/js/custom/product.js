$(function(){
	// product create
	$("#product-add-form").submit(function(event){
		$(".product-add-btn").html("<span class='spinner-border spinner-border-sm' role='status' aria-hidden='true'></span> Loading...")
		var productAddForm = $(this)
		var productAddFormUrl = productAddForm.attr("action")
		var productAddFormEnctype = productAddForm.attr("enctype")
		var productAddFormData = new FormData(productAddForm[0])
		$.ajax({
			url: productAddFormUrl,
			type: 'post',
			enctype: productAddFormEnctype,
			data: productAddFormData,
			async: true,
            cache: false,
            processData: false,
            contentType: false,
			success: function(data){
				if(data.errors){
					$(".product-create-error").html(data.errors.stock_form_error.__all__[0])
					$(".product-add-btn").html("Add")
					$(".quantity-error-msg").html("")
				}
				if(data.is_success){
					$(".product-create-error").html("")
					setTimeout(function(){
						$(".product-add-btn").html("Add")
						swal("Well Done!", "Product is added to shop.", {
		                    icon : "success",
		                    buttons: {
		                        confirm: {
		                            className : 'btn btn-success'
		                        }
		                    },
		                }).then(function(){
		                    window.location.href = "/products/detail/" + data.product_id +"/"
		                });
					}, 800)
				}
			},
			error: function(){
				$(".product-add-btn").html("Add")
			}
		});
		event.preventDefault()
	})

	//  stock quantity validity
	$(".product-stock-type").change(function(){
		var stock_type = $(this).find("option:selected");
		var stock_type = stock_type.text()
		var stock_quantity_val = $(".product-stock-quantity").val()
		var stockQuantityRegx = /[.]/
		if(stockQuantityRegx.test(stock_quantity_val) && (stock_type == "piece")){
			$(".quantity-error-msg").html("According to stock type, given stock quantity is invalid.")
		}
		else{
			$(".quantity-error-msg").html("")
		}
		$(".product-stock-quantity").keyup(function(event){
			var stockQuantityVal = $(this).val()
			if ((stockQuantityRegx.test(stockQuantityVal) || event.which == 190) && stock_type == 'piece'){
				$(".quantity-error-msg").html("According to stock type, given stock quantity is invalid.")
			}
			else{
				$(".quantity-error-msg").html("")
			}
		})
	})
});