
$(function(){
    var mobile_number = $("#id_mobile_number");
    var date_of_birth = $("#id_date_of_birth");
    var gender = $("#id_gender");
    

    mobile_number.focus(function(){
        $(this).css({
            'box-shadow': '0 0 4px #E4AF2C',
            'border': '1px solid #6FA7F8'
        })
    });
    mobile_number.blur(function(){
        $(this).css({
            'box-shadow': '0 0 4px white',
            'border': '1px solid #bdbfb9'
        })
    });

    date_of_birth.focus(function(){
        $(this).css({
            'box-shadow': '0 0 4px #E4AF2C',
            'border': '1px solid #6FA7F8'
        })
    });
    date_of_birth.blur(function(){
        $(this).css({
            'box-shadow': '0 0 4px white',
            'border': '1px solid #bdbfb9'
        })
    });

    gender.focus(function(){
        $(this).css({
            'box-shadow': '0 0 4px #E4AF2C',
            'border': '1px solid #6FA7F8'
        })
    });
    gender.blur(function(){
        $(this).css({
            'box-shadow': '0 0 4px white',
            'border': '1px solid #bdbfb9'
        })
    });

    // employee list 
    $("#employee-registered-modal").submit(function(event){
        var this_ = $(this)
        var empRMUrl = this_.attr('action')
        var empRMData = this_.serialize()
        $.ajax({
            url: empRMUrl,
            method: 'POST',
            data : empRMData,
            success: function(data){
                if (data.error_dict){
                    var EmpMErr = $("#emp-modal-error")
                    var username 
                    var password
                    if(data.error_dict){
                        alert("Opps! Invalid data.")
                    }
                    if (data.error_dict.form_errors.username){
                        username = data.error_dict.form_errors.username
                        $("#emp-modal-error-username").html(username)
                    }else{
                        $("#emp-modal-error-username").html("")
                    }

                    if (data.error_dict.emp_errors.date_of_birth){
                        date_of_birth = data.error_dict.emp_errors.date_of_birth
                        $("#emp-modal-error-date_of_birth").html(date_of_birth)
                    }else{
                        $("#emp-modal-error-date_of_birth").html("")
                    }
                    
                    if(data.error_dict.form_errors.password2){
                        password = data.error_dict.form_errors.password2
                        if(password.length == 1){
                            $("#emp-modal-error-pass1").html(password[0])
                        }
                        if(password.length == 2){
                            $("#emp-modal-error-pass1").html(password[0])
                            $("#emp-modal-error-pass2").html(password[1])
                        }
                        if(password.length == 3){
                            $("#emp-modal-error-pass1").html(password[0])
                            $("#emp-modal-error-pass2").html(password[1])
                            $("#emp-modal-error-pass3").html(password[2])
                        }
                        if(password.length == 4){
                            $("#emp-modal-error-pass1").html(password[0])
                            $("#emp-modal-error-pass2").html(password[1])
                            $("#emp-modal-error-pass3").html(password[2])
                            $("#emp-modal-error-pass4").html(password[3])
                        }
                        
                    }else{
                        $("#emp-modal-error-pass1").html("")
                            $("#emp-modal-error-pass2").html("")
                            $("#emp-modal-error-pass2").html("")
                            $("#emp-modal-error-pass2").html("")
                    }
        
                }
                else{
                    $("#emp-register-success-msg").html('<div class="alert alert-success msg" role="alert">Successfully Registration Complted!</div>')

                    setTimeout(function(){
                        document.location.href = empListUrl
                    }, 1500)
                }
            },error: function(){
                console.log("Error")
            }
        })

        event.preventDefault()
    })

})









