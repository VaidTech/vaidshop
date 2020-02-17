$(function(){

	$("#product-add-form").submit(function(event){
		// loader 
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
				if(data.is_success){
					console.log('success')
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
		                    window.location.href = shopListUrl
		                });
					}, 800)
				}
			}
		});
		event.preventDefault()
	})


});




