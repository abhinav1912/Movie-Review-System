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
    $("#addToFav").on('click', function(){
        if($("#addToFav").hasClass("del")){
            $("#addToFav").removeClass("del")
            $("#favText").text("Add To Favourites")
        }
        else {
            $("#addToFav").addClass("del")
            $("#favText").text("Remove from Favourites")
        }
    })
}) 