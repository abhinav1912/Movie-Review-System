$(document).ready(function(){
    function emptyOrUndefined(input){
        return (input == null) || (input == "") || (typeof input =="undefined");
    }
    function validateEmail(email) {
        const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(email);
    }
    $(".account-buttons").on({
        focus: function(){
            $(this).blur()
        }
    });
    var registerModal = $("#registerModal");
    var registerAlert = $("#registerAlert");
    var loginModal = $("#loginModal");
    var loginAlert = $("#loginAlert");
    var registerButton = $("#registerButton");
	registerModal.on('hidden.bs.modal', function(){
		$("#registerAlert").remove();
	});
	loginModal.on('hidden.bs.modal', function(){
		$("#loginAlert").remove();
	});    
    if(registerAlert.length != 0){
        $("#registerModal").modal('show');
    }
    else if(loginAlert.length != 0){
        $("#loginModal").modal('show');
    }

    if (registerButton.length != 0) {
        function registerFunc() {
            var cnf_pwd = $("#cnf_password").val();
            var pass = $("#r_password").val();
            if (cnf_pwd != pass){
                $("#cnf_alert").text("Passwords don't match");
                $("#cnf_alert").show();
            }
            else{
                $("#cnf_alert").text("");
                $("#cnf_alert").hide();
            }
            if (!emptyOrUndefined(pass)){
                $("#password_alert").text("");
                $("#password_alert").hide();
            }
        }
        function username_validate(){
            var user_id = $("#user_id");
            if (emptyOrUndefined(user_id.val())){
                if (first_err == null){
                    first_err = user_id;
                }
                $("#username_alert").text("Username is required");
                $("#username_alert").show();
            }
            else {
                $("#username_alert").text("");
                $("#username_alert").hide();
            }
        }
        function email_validate(){
            var email = $("#email_address");
            if (emptyOrUndefined(email.val())){
                first_err = email;
                $("#email_alert").text("Email is required");
                $("#email_alert").show()
            }
            else if (validateEmail(email.val()) == false){
                first_err = email;
                $("#email_alert").text("Input is not an email");
                $("#email_alert").show();
            }
            else {
                $("#email_alert").text("");
                $("#email_alert").hide();
            }
        }
        $("#cnf_password").keyup(registerFunc);
        $("#r_password").keyup(registerFunc);
        $("#user_id").keyup(username_validate);
        $("#email_address").keyup(email_validate);
        registerButton.on('click', function(){
            var first_err = null;
            var email = $("#email_address");
            var user_id = $("#user_id");
            var pwd = $("#r_password");
            var cnf_pwd = $("#cnf_password");
            if (emptyOrUndefined(email.val())){
                first_err = email;
                $("#email_alert").text("Email is required");
                $("#email_alert").show()
            }
            else if (validateEmail(email.val()) == false){
                first_err = email;
                $("#email_alert").text("Input is not an email");
                $("#email_alert").show();
            }
            else {
                $("#email_alert").text("");
                $("#email_alert").hide();
            }

            if (emptyOrUndefined(user_id.val())){
                if (first_err == null){
                    first_err = user_id;
                }
                $("#username_alert").text("Username is required");
                $("#username_alert").show();
            }
            else {
                $("#username_alert").text("");
                $("#username_alert").hide();
            }

            if (emptyOrUndefined(pwd.val())) {
                if (first_err == null){
                    first_err = pwd;
                }
                $("#password_alert").text("Password is required");
                $("#password_alert").show();
            }
            else if (pwd.val().length < 8){
                if (first_err == null){
                    first_err = pwd;
                }
                $("#password_alert").text("Password must be atleast 8 characters");
                $("#password_alert").show();
            }
            else{
                $("#password_alert").text("");
                $("#password_alert").hide();
            }

            if (cnf_pwd.val() != pwd.val()){
                if (first_err == null){
                    first_err = cnf_pwd;
                }
                $("#cnf_alert").text("Passwords don't match");
                $("#cnf_alert").show();
            }
            else{
                $("#cnf_alert").text("");
                $("#cnf_alert").hide();
            }

            if (first_err != null){
                first_err.focus();
            }
            else{
                $("#registerForm").submit();
            }

        });
        
    }
});