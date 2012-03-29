$(document).ready(function(){
  $('.task-div').find('.task-info').hide().end().find('.task-title').click(function() {
     $(this).parent().find('.task-info').slideToggle();
   });
});
            
