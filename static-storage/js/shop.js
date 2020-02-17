$(function(){

	// shop create 
	var shopForm = $("#shop-create-form")
	shopForm.submit(function(event){
		var shopForm = $(this)
		var shopFormUrl = shopForm.attr("action")
		var shopEnctype = shopForm.attr("enctype")
		var formData = new FormData(shopForm[0]);
		$.ajax({
			url: shopFormUrl,
			type: shopForm.attr("method"),
			enctype: shopEnctype,
			data: formData,
			async: true,	
			cache: false,
			processData: false,
			contentType: false,
			success: function(data){
				if(data.errors){
					$(".shop-create-error").html(data.errors.name_error)
				}
				else{
					$(".shop-create-error").html("")
					
					swal("Well Done!", "Shop is successfully created.", {
                    icon : "success",
                    buttons: {
                        confirm: {
                            className : 'btn btn-success'
                        }
                    },
                }).then(function(){
                    window.location.href = shopListUrl
                });
				}
			}
		});

		event.preventDefault()
	});

	// shop create modal 
	$("#shop-create-modal-form").submit(function(event){
		
		event.preventDefault()
	});



})






