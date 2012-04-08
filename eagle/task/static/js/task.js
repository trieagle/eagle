function Task(taskElem) {
  this.task = taskElem;
  this.header = taskElem.find('.task-header');
  this.detail = taskElem.find('.task-body');
  this.tags = taskElem.find('.task-footer');
}

Task.prototype.getTagList = function() {
  //fixme
  var tagText = this.tagsInput.val();
  var tagList = tagText.split(' ');
};

Task.prototype.getID = function() {
  return parseInt(this.task.attr('id').substring(5)); //task-123213
};

Task.prototype.updateDetail = function(detail) {
  var updateInfo = {
    id: this.getID(),
    detail: detail,
  };
  $.ajax({
    url: '/task/update/',
    type: 'post',
    dataType: 'json',
    data: JSON.stringify(updateInfo),
    success: function(revTaskObj) {
    }
  });
}

Task.prototype.updateTagList = function() {

}

Task.prototype.updateMode = function() {
}

Task.prototype.updateTime = function() {

}

Task.prototype.removeTask = function() {
  var removeInfo = {
    id: this.getID(),
  };
  $.ajax({
    url: '/task/delete/',
    type: 'post',
    dataType: 'json',
    data: JSON.stringify(removeInfo),
    success: function(delFlag) {
      //TODO
      this.task.hide();
      this.task.remove();
    }
  });

}

function initHide() {
  $('ul .task-body').hide();
  $('ul .task-footer').hide();
  $('.edit-task-box').hide();
}

$(document).ready(function() {
  //init hide
  initHide();

  //set toggle for task-div
  $('.task-div-header').click(function() {
    $(this).next().slideToggle()
    .find('.task-body').hide().end()
    .find('.task-footer').hide();
  });

  //set toggle for task-title
  $('.task-div .task-header .task-title').click(function() {
    $(this).parent().next().slideToggle()  //task-body
    .next().slideToggle();  //task-footer
  });

  //set toggle for add-new-task
  $('.add-new-task').click(function() {
    $('.edit-task-box').slideToggle();
  });

  //set action for edit new task
  $('.edit-task-box .task-edit-option .confirm').click(function() {
    var createInfo = {
      title: $('.edit-task-box .task-title-input').val(),
      detail: $('.edit-task-box .task-detail-input').val(),
      priority: 1,
    };
    $.ajax({
      url: '/task/create/',
      type: 'post',
      data: JSON.stringify(createInfo),
      success: function(revTaskObj) {
        revTaskObj = revTaskObj[0];
        $('.edit-task-box').slideToggle();
        //TODO 

      }
    });
  });

  //set action for cancel new task
  $('.edit-task-box .task-edit-option .cancel').click(function() {
    $('.edit-task-box .task-title-input').val("");
    $('.edit-task-box .task-detail-input').val("");
    $('.edit-task-box .task-tags-input').val("");
    $('.edit-task-box').slideToggle();
  });

  //set action for task-detail
  $('.task-body .task-detail').editable({
    type: 'textarea',
    onSubmit: function(content) {
      if (content.current !== content.previous) {
        (new Task($(this).parents('.task-li'))).updateDetail(
          content.current);
      }
    },
  });

  $('.task-header .task-remove').click(function() {
    (new Task($(this).parents('.task-li'))).removeTask();
  });

  //set action for edit-op
  $('.task-op .edit-op').find('.confirm').click(function() {
    var taskElem = $(this).parent().parent().parent();
    var task = new Task(taskElem);

    var taskObj = {
      id: task.getID(),
      title: task.getTitleInput(),
      detail: task.getDetailInput(),
      priority: 1,
      tag: task.getTagList(),
    };
  });

  //set action for done-op, default rate is 5
  $('.task-rate').click(function() {
    var taskElem = $(this).parent();
    var task = new Task(taskElem);
    var taskObj = {
      id: task.getID(),
      rate: 5,
    };
    $.ajax({
      url: '/task/done/',
      type: 'post',
      dataType: 'json',
      data: JSON.stringify(taskObj),
      success: function(doneFlag) {
        doneFlag;
        $('#done').append(taskElem)
      }
    });
  });
});
