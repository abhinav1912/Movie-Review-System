$(document).ready(function(){
    $("#addToFav").hover(function(){
        if($("#addToFav").hasClass("del")){
            return;
        }
        $("#heart-icon").addClass('fas');
        $("#heart-icon").removeClass('far');
    })
    $("#addToFav").on('mouseleave', function(){
        if($("#addToFav").hasClass("del")){
            return;
        }
        $("#heart-icon").addClass('far');
        $("#heart-icon").removeClass('fas');
    })
}) 