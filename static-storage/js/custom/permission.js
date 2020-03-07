$(function(){
	// permission select2
    $('.employee-permission-multiple-select').select2({
    	placeholder: 'Click Here And Select Permission',
    }).on('select2:unselect', function (e) {
    	var data = e.params.data;
	})
})