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

Task.prototype.updateTagList = function() {

}

Task.prototype.updateMode = function() {
}

Task.prototype.updateTime = function() {
  
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
    $(this).next().slideToggle("slow")
    .find('.task-body').hide("slow").end()
    .find('.task-footer').hide("slow");
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
  });

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
