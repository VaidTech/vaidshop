 $(function(){

 	// load attendence delete form
 	$(".attendence-delete-btn").click(function(){
 		var btn = $(this)
 		$.ajax({
 			url: btn.attr('data-url'),
 			type: 'get',
 			dataType: 'json',
 			beforeSend: function(){
				$("#attendenceModal").modal('show')
 			},
 			success: function(data){
 				$("#attendence-modal-content").html(data.html_form)
 			}
 		})
 	})

 	// delete attendence form 
 	$("#attendenceModal").submit(function(event){
 		event.preventDefault()
 		var formData = $(this).find('form').serialize()
 		$.ajax({
 			url: $(this).find('form').attr('action'),
 			method: 'POST',
 			data: formData,
 			success: function(data){
 				if (data.is_success){
	 				swal("Good job!", "Attendence is deleted!", {
	                    icon : "success",
	                    buttons: {
	                        confirm: {
	                            className : 'btn btn-success'
	                        }
	                    },
	                }).then(function(){
	                    window.location.href = "/attendences/list/"
	                });
 				}
 			},
 			error: function(){
 				console.log('Error')
 			}
 		})
 		
 	})


    // attendences date picker 
    $("#employee-attendence-datepicker").datepicker({
   		
    });

    $('#employee-entry-time').timepicker({
	    showNowButton: true,
	    showDeselectButton: true,
	    defaultTime: '',  
    	showCloseButton: true
	})

	$('#employee-exit-time').timepicker({
	    showNowButton: true,
	    showDeselectButton: true,
	    defaultTime: '',  
    	showCloseButton: true
	})



 });