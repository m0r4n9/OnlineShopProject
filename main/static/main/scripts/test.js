$(function(){
     $('.sizeBox').hover(function() {
          $(this).children("div").css({
              display: 'block'
          })
     }, function (){
         $(this).children("div").css({
              display: 'none'
          })
     });
   })
