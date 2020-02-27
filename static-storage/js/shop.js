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

	// shop update modal load form
	$("#shop-update-modal-btn").click(function(){
		var btn = $(this)
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType: 'json',
			beforeSend: function(){
				$("#shopUpdateModal").modal("show");
			},
			success: function(data){
				$("#shop-update-modal-content").html(data.html_form)
			},
			error: function(){
				console.log("error")
			}
		})
	});

	// shop save form modal 
	$("#shopUpdateModal").submit(function(event){
		var shopUpdateForm = $(this).find("form")
		var shopUpdateFormUrl = shopUpdateForm.attr("action")
		var shopUpdateFormEnctype = shopUpdateForm.attr("enctype")
		var shopUpdateFormData = new FormData(shopUpdateForm[0])
		$.ajax({
			url: shopUpdateFormUrl,
			type: 'post',
			enctype: shopUpdateFormEnctype,
			data: shopUpdateFormData,
			async: true,
			cache: false,
			processData: false,
			contentType: false,
			success: function(data){
				if(data.errors){
					$(".shop-update-modal-error").html(data.errors.name_error)
				}
				else{
					$(".shop-update-modal-error").html("")

					swal("Well Done!", "Your Shop Is Updated.", {
                    icon : "success",
                    buttons: {
                        confirm: {
                            className : 'btn btn-success'
                        }
                    },
		                }).then(function(){
		                    window.location.href = shopDetailUrl;
		               });
					}
			}
		})

		event.preventDefault()
	});

	// shop delete modal load form 
	$("#shop-delete-modal-btn").click(function(){
		var btn = $(this)
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType: 'json',
			beforeSend: function(){
				$("#shopDeleteModal").modal('show')
			},
			success: function(data){
				$("#shop-delete-modal-content").html(data.html_form)
			}
		})
	})

});






