$('#second_section').hide();
$(document).ready(function(){
  // $(document).mousemove(function(event) {
  //   console.log(event.pageX, noBtn.left, noBtn);
  //   if(event.pageX == noBtn.left  && event.pageY == noBtn.top){
  //     console.log("oops");
  //   }
  // });
});

function responder(){
  $('#first_section').hide();
  $('#second_section').show();
};

function si(){

};

function no(){

};

$('#no').mouseover(function(event){
    $(this).offset(
      { top : event.pageY > 50 ? event.pageY - 50 : event.pageY + 50,
        left: event.pageX > 50 ? event.pageX - 50 : event.pageX + 50
      });
});
