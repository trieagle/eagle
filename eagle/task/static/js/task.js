$(document).ready(function() {
    $('.task-div').find('.task-info').hide().end()
    .find('.task-title').click(function() {
        $(this).parent().find('.task-info').slideToggle();
    });


    $('.task-op').find('.edit').click(function() {
        task = $(this).parent().parent().parent();

        taskTitle = task.find('.task-title');
        taskTitle.hide().after(
            '<input class="task-title-input" value="' 
            + taskTitle.html() + '" >');

        taskDetail = task.find('.task-detail');
        taskDetail.hide().after(
            '<input class="task-detail-input" value="' 
            + taskDetail.html() + '" >');

        editOption ='<div class="edit-op">'
            + '<button class="confirm">confirm</button>'
            + '<button class="cancel">cancel</button>'
			+ '</div>';

        taskOp = task.find('.task-op');
        taskOp.hide().after(editOption);

        task.find('.edit-op').find('.confirm').click(function() {
            taskTags = task.find('task-tags');

            taskObj = {
                title: task.find('.task-title-input').value(),
                detail: task.find('.task-detail-input').value(),
            };

            $.ajax({
                url: '/',
                type: 'post',
                dataType: 'json',
                data: JSON.stringify(taskObj),
                success: function(revTaskObj) {
                    taskTitle.html(revTaskObj.title).show()
                        .next().hide();
                    taskDetail.html(revTaskObj.detail).show()
                        .next().hide();
                    taskOp.show().next().hide();
                }
            });
        })
        .end().find('.cancel').click(function() {
            taskTitle.show().next().hide();
            taskDetail.show().next().hide();
            taskOp.show().next().hide();
        });

    }).end().find('.delete').click(function() {
        task = $(this).parent().parent().parent();
        task.remove();
    });
});
