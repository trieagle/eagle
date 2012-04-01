function Task(taskElem) {
  this.title = taskElem.find('.task-title');
  this.titleInput = taskElem.find('.task-title-input');
  this.detail = taskElem.find('.task-detail');
  this.detailInput = taskElem.find('.task-detail-input');
  this.tags = taskElem.find('.task-tags');
  this.tagsInput = taskElem.find('.task-tags-input');
  this.taskOp = taskElem.find('.task-op');
  this.editOp = taskElem.find('.edit-op');
}

Task.prototype.toggleTitle = function() {
  if (this.title.is(':visible')) {
    this.title.hide().next().val(this.title.html()).show();
  } else {
    this.title.show().next().hide();
  }
};

Task.prototype.toggleDetail = function() {
  if (this.detail.is(':visible')) {
    this.detail.hide().next().val(this.detail.html()).show();
  } else {
    this.detail.show().next().hide();
  }
};

Task.prototype.toggleTags = function() {
  //TODO
};

Task.prototype.toggleOption = function() {
  if (this.taskOp.is(':visible')) {
    this.taskOp.hide().next().show();
  } else {
    this.taskOp.show().next().hide();
  }
};

Task.prototype.toggleAll = function() {
    this.toggleTitle();
    this.toggleDetail();
    this.toggleOption();
};

$(document).ready(function() {
  $('.task-div').find('.task-info').hide().end()
  .find('.task-title').click(function() {
    $(this).parent().find('.task-info').slideToggle();
  });

  //hide
  $('.task-title-input').hide();
  $('.task-detail-input').hide();
  $('.edit-op').hide();

  //set action for task-op 
  $('.task-op').find('.edit').click(function() {
    var taskElem = $(this).parent().parent().parent();
    (new Task(taskElem)).toggleAll();

  }).end().find('.delete').click(function() {
    var taskElem = $(this).parent().parent().parent();
    taskElem.remove();
    //TODO
  }); //end task-op

  //set action for edit-op
  $('.edit-op').find('.confirm').click(function() {
    var taskElem = $(this).parent().parent().parent();
    var task = new Task(taskElem);
    task.toggleAll();

    var taskObj = {
      title: task.find('.task-title-input').value(),
      detail: task.find('.task-detail-input').value(),
    };

    $.ajax({
      url: '/',
      type: 'post',
      dataType: 'json',
      data: JSON.stringify(taskObj),
      success: function(revTaskObj) {
        //TODO
      }
    });
  })
  .end().find('.cancel').click(function() {
    var taskElem = $(this).parent().parent().parent();
    (new Task(taskElem)).toggleAll();
  }); //end edit-op

});
