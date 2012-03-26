$(document).ready(function(){
  $('.task-div').find('.task-info').hide().end().find('.task-title').click(function() {
     $(this).parent().next().slideToggle();
   });

  $('.task-op').hide().parent().hover(function() {
	$(this).children().next().append("Done?");
	for ( var i = 1; i <= 5; i++ ) {
		$(this).children().next().append("<a href='#'>" + i + "</a> ");
	}

	$(this).children().next().show(500).click(function(e) {
		// stop normal link click
		e.preventDefault();
	})
	},
	function() {
		$(this).children().next().empty();
	}

  );
});
            
