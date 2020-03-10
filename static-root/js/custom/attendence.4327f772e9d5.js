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
 	// delete attendence confirm 
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
 			}
 		})
 	})

 	// Employee annual attendence chart 
 	var barChartData = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        datasets: []
    };
    // load data 
    var attendenceChartUrl = $("#attendenceChart").attr('data-url')
   $.ajax({
    url: attendenceChartUrl,
    type: 'get',
    dataType: 'json',
    success: function(data){
        try{
            data.labels.forEach(function (e, i) {
            bgColor = `rgb(${[1,2,3].map(x=>Math.random()*256|0)}).`
            bgColor = bgColor.repeat(12)
            bgColor = bgColor.split(".")
            barChartData.datasets.push({
                label: e,
                backgroundColor: bgColor,
                data: data.data[i],
            	});
        	});
            fetchChart()
        }
        catch{}  
    	}
	})
   // chart demo 
    function fetchChart(){
        var ctx = document.getElementById('attendenceChart').getContext('2d');
        var myBar = new Chart(ctx, {
        type: 'bar',
        data: barChartData,
        options: {
            animation: {
                duration: 0
                },
                hover: {
                    animationDuration: 0
                },
                responsiveAnimationDuration: 0,
            title: {
                display: true,
                text: 'Employee Anual Attendence'
            },
            tooltips: {
                mode: 'index',
                intersect: true
            },
            responsive: true,
            scales: {
                xAxes: [{
                stacked: true
            }],
                yAxes: [{
                    stacked: true,
                    display: true,
                    ticks: {
                        suggestedMin: 0, 
                        suggestedMax: 30
                    }
                }]
            }
        }
    })
    };
    // year selection section 
    $(".chart-year-select").change(function(){
        var ChartYearSelectForm = $(".chart-year-select-form")
        var ChartYearSelectFormUrl = ChartYearSelectForm.attr('action')
        $.ajax({
            url: ChartYearSelectFormUrl,
            method: 'get',
            data: ChartYearSelectForm.serialize(),
            success: function(data){
                // remove data 
                data.labels.forEach(function (e, i) {
                barChartData.datasets.pop()
                });
                // add update data 
                try{
                    data.labels.forEach(function (e, i) {
                    color = `rgb(${[1,2,3].map(x=>Math.random()*256|0)}).`
                    color = color.repeat(12)
                    color = color.split(".")
                    barChartData.datasets.push({
                        label: e,
                        backgroundColor: color,
                        data: data.data[i]
                    });
                });
                }
                catch{}
                fetchChart()
            }
        })
    })

    // attendences date & time picker 
    $("#employee-attendence-date").datepicker({});
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