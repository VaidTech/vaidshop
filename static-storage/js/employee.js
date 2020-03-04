
$(function(){

    // employee list 
    $("#employee-registered-modal-form").submit(function(event){
        var employeeRegisterForm = $(this)
        var empRMUrl = employeeRegisterForm.attr('action')
        var empRMData = new FormData(employeeRegisterForm[0])
        var employeeRegisterModalEnctype = employeeRegisterForm.attr('enctype')
        $.ajax({
            url: empRMUrl,
            type: 'post',
            enctype: employeeRegisterModalEnctype,
            data : empRMData,
            async: true,
            cache: false,
            processData: false,
            contentType: false,
            success: function(data){
                if (data.error_dict){
                    var EmpMErr = $("#emp-modal-error")
                    var username 
                    var password
                    if(data.error_dict){
                        swal("Opps!", "Invalid, Please check your data.", {
                        icon : "error",
                        buttons: {
                            confirm: {
                                    className : 'btn btn-warning'
                                }
                            }
                         });
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
                    $("#emp-modal-error-pass1").html("")
                    $("#emp-modal-error-pass2").html("")
                    $("#emp-modal-error-pass2").html("")
                    $("#emp-modal-error-pass2").html("")
                    $("#emp-modal-error-date_of_birth").html("")
                    $("#emp-modal-error-username").html("")
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


    // employee update modal form load
    var loadForm = function (event) {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#employeeUpdateModal").modal("show");
      },
      success: function (data) {
        $("#employeeUpdateModal .update-modal-content").html(data.html_form); 
      }
    });
  };
  $("#employee-table").on("click", ".update-employee", loadForm);

  // employee update modal form save
  $("#employeeUpdateModal").submit(function(event){
    var this_ = $(this)
    var employeeUpdateForm = this_.find("form")
    var employeeUpdateUrl = employeeUpdateForm.attr("action")
    var employeeUpdateFormEnctype = employeeUpdateForm.attr("enctype")
    var employeeFormData = new FormData(employeeUpdateForm[0])
    $.ajax({
        url: employeeUpdateUrl,
        method: 'post',
        data: employeeFormData,                               
        enctype: employeeUpdateFormEnctype,
        async: true,
        cache: false,
        processData: false,
        contentType: false,
        success: function(data){
            if(data.errors || data.username_error){
                swal("Opps!", "Invalid, Please check your data.", {
                    icon : "error",
                    buttons: {
                        confirm: {
                            className : 'btn btn-warning'
                        }
                    },
                });

                if(data.errors){
                    if(data.errors.employee_errors.date_of_birth){
                        $("#employee-update-errors1").html(data.errors.employee_errors.date_of_birth)
                    }else{
                        $("#employee-update-errors1").html("")
                    }
                    if(data.errors.employee_user_errors.username){
                        $("#employee-update-errors3").html(data.errors.employee_user_errors.username)
                    }else{
                        $("#employee-update-errors3").html("")
                    }
                }
                if(data.username_error){
                    $("#employee-update-errors2").html(data.username_error.error)
                }else{
                    $("#employee-update-errors2").html("")
                }
            }
            else{
                swal("Good job!", "Employee is updated.", {
                    icon : "success",
                    buttons: {
                        confirm: {
                            className : 'btn btn-success'
                        }
                    },
                }).then(function(){
                    window.location.href = empListUrl
                });
                
                $("#employeeUpdateModal").modal("hide");
            }
        },
    });
    event.preventDefault()
  });

    // employee delete 
    $(".delete-employee").click(function(){
        var btn = $(this)
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $("#employeeDeleteModal").modal("show");
            },
            success: function(data){
                $("#employeeDeleteModal .delete-modal-content").html(data.html_form)
            }

        })
        
    });


    // employee date picker 
      $("#id_date_of_birth").datepicker();



});





