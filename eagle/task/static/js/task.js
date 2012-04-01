function Task(taskElem) {
  this.task = taskElem;
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
  if (this.tags.is(':visible')) {
    //TODO
    var tagList = [];
    this.tags.children().each(function() {
      tagList.push($(this).text());
    });
    this.tags.hide().next().val(tagList.join()).show();
  } else {
    this.tags.show().next().hide();
  }
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
  this.toggleTags();
  this.toggleOption();
};

Task.prototype.getTagList = function() {
  //fixme
  var tagText = this.tagsInput.val();
  var tagList = tagText.split(' ');
};

Task.prototype.getID = function() {
  return this.task.attr('id');
};

Task.prototype.getTitleInput = function() {
  return this.titleInput.val();
};

Task.prototype.getDetailInput = function() {
  return this.detailInput.val();
};

$(document).ready(function() {
  $('.task-div').find('.task-info').hide().end()
  .find('.task-title').click(function() {
    $(this).parent().find('.task-info').slideToggle();
  });

  //hide
  $('.task-title-input').hide();
  $('.task-detail-input').hide();
  $('.task-tags-input').hide();
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
      id: task.getID(),
      title: task.getTitleInput(),
      detail: task.getDetailInput(),
      priority: 1,
      tags: task.getTagList()
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
