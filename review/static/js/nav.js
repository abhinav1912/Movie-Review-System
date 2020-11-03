$(document).ready(function(){
    $(".account-buttons").on({
        focus: function(){
            $(this).blur()
        }
    });
    var registerModal = $("#registerModal");
    var registerAlert = $("#registerAlert");
    var loginModal = $("#loginModal");
    var loginAlert = $("#loginAlert");
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
});