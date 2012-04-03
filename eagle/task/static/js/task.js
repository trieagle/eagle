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

Task.prototype.toggleEdit = function() {
  this.task.children().each(function() {
    if ($(this).is(':visible')) {
      $(this).hide();
    } else {
      $(this).show();
    }
  });
}


Task.prototype.getTagList = function() {
  //fixme
  var tagText = this.tagsInput.val();
  var tagList = tagText.split(' ');
};

Task.prototype.getID = function() {
  return parseInt(this.task.attr('id').substring(5)); //task-123213
};

Task.prototype.getTitleInput = function() {
  return this.titleInput.val();
};

Task.prototype.getDetailInput = function() {
  return this.detailInput.val();
};

Task.prototype.setTitle = function(title_) {
  this.title.html(title_);
};

Task.prototype.setDetail = function(detail_) {
  this.detail.html(detail_);
};

Task.prototype.setTags = function(tags_) {
};







$(document).ready(function() {
  $('.task-div').find('.task-info').hide().end()
  .find('.task-title').click(function() {
    $(this).parent().find('.task-info').slideToggle();
  });
  $('.add-new-task').click(function() {
    $('.new-task-box').slideToggle();
  });

  //hide
  $('ul .task-title-input').hide();
  $('ul .task-detail-input').hide();
  $('ul .task-tags-input').hide();
  $('ul .edit-op').hide();
  $('.new-task-box').slideToggle();

  //set action for new task
  $('.new-task-box .edit-op .confirm').click(function() {
    taskElem = $('.new-task-box');
    task = new Task(taskElem);
    var taskObj = {
      title: task.getTitleInput(),
      detail: task.getDetailInput(),
      priority: 1
    };
    
    $.ajax({
      url: '/task/create/',
      type: 'post',
      data: JSON.stringify(taskObj),
      success: function(revTaskObj) {
        revTaskObj = revTaskObj[0];
        //TODO

        $('.new-task-box').slideToggle();

      }
    });

  });
  $('.new-task-box .edit-op .cancel').click(function() {
    $('.new-task-box').slideToggle();
  });

  //set action for task-op 
  $('.task-op').find('.edit').click(function() {
    var taskElem = $(this).parent().parent().parent();
    (new Task(taskElem)).toggleAll();

  }).end().find('.delete').click(function() {
    var taskElem = $(this).parent().parent().parent();
    var task = new Task(taskElem);
    var taskIdObj = {
      id: task.getID()
    };
    $.ajax({
      url: '/task/delete/',
      type: 'post',
      dataType: 'json',
      data: JSON.stringify(taskIdObj),
      success: function(delFlag) {
        //TODO
        delFlag && taskElem.remove();
      }
    });
  }); //end task-op

  //set action for edit-op
  $('.task-op .edit-op').find('.confirm').click(function() {
    var taskElem = $(this).parent().parent().parent();
    var task = new Task(taskElem);

    var taskObj = {
      id: task.getID(),
      title: task.getTitleInput(),
      detail: task.getDetailInput(),
      priority: 1,
      tag: task.getTagList()
    };

    $.ajax({
      url: '/task/update/',
      type: 'post',
      dataType: 'json',
      data: JSON.stringify(taskObj),
      success: function(revTaskObj) {
        revTaskObj = revTaskObj[0];
        //TODO
        var taskId = '#task-' + revTaskObj['pk'];
        //var task = new Task($(taskId));
        task.setTitle(revTaskObj.fields['title']);
        task.setDetail(revTaskObj.fields['detail']);
        task.setTags(revTaskObj.fields['tag']);
        task.toggleAll();
      }
    });
  })
  .end().find('.cancel').click(function() {
    var taskElem = $(this).parent().parent().parent();
    (new Task(taskElem)).toggleAll();
  }); //end edit-op

  //set action for done-op, default rate is 5
  $('.task-rate').click(function() {
    var taskElem = $(this).parent();
    var task = new Task(taskElem);
    var taskObj = {
      id: task.getID(),
      rate: 5
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
