$(function(){
	// order delete section 
	$(".order-delete-btn").click(function(){
		var btn = $(this)
		$.ajax({
			url: btn.attr('data-url'),
			method: 'get',
			dataType: 'json',
			beforeSend: function(){
				$("#orderDeleteModal").modal('show')
			},
			success: function(data){
				$("#order-delete-modal-content").html(data.html_form)
			}
		});
	})

	// select2 
	$('.js-example-basic-multiple').select2({
		placeholder: 'Click Here And Choose Product',
	}).on('select2:select', function (e) {
    	var data = e.params.data;
    	$(".order-product-quantity").append("<div id='"+data.id+"'>"+"<label for='"+data.id+"'>"+data.text+" quantity: </lable>"+ "<input type='number' value='1' data_product_id='"+data.id+"'/><br><br>"+"</div>")
	}).on('select2:unselect', function (e) {
    	var data = e.params.data;
    	$("#" + data.id).remove()

    })

	// order create and update 
	$(".order-create-form").submit(function(event){
		event.preventDefault()
		var OrderCreateForm = $(this)
		$.ajax({
			url: OrderCreateForm.attr('action'),
			method: OrderCreateForm.attr('method'),
			data: OrderCreateForm.serialize(),
			success: function(data){
				var product_id_quantity = []
				$('*.order-product-quantity input').each(function(i,val){
					var product_id = val.attributes.data_product_id.value
					var product_quantity = val.value
					product_id_quantity.push([product_id,product_quantity])
				})
				var pathUrl;
				if(data.is_update){
					pathUrl = "/orders/order-product/update/"+ data.order_id +"/"
				}else{
					pathUrl = "/orders/order-product/"+ data.order_id +"/"
				}
				$.ajax({
					url: pathUrl,
					method: 'post',
					dataType: 'json',
					data: {
						"product_id_quantity": JSON.stringify(product_id_quantity)
					},
					success: function(data){
						if(data.is_success && data.is_update){
							swal("Well Done!","Order is updated.", {
			                    icon : "success",
			                    buttons: {
			                        confirm: {
			                            className : 'btn btn-success'
			                        }
			                    },
			                }).then(function(){
			                    window.location.href = "/orders/list/"
			                });
						}
						else{
							swal("Well Done!","Order is Created.", {
			                    icon : "success",
			                    buttons: {
			                        confirm: {
			                            className : 'btn btn-success'
			                        }
			                    },
			                }).then(function(){
			                    window.location.href = "/orders/list/"
			                });
						}
					}
				})
			}
		})
	})
});