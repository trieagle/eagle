$(document).ready(function() {
    $('.task-div').find('.task-info').hide().end()
    .find('.task-title').click(function() {
        $(this).parent().find('.task-info').slideToggle();
    });


    $('.task-op').find('.edit').click(function() {
/*        task = $(this).parent().parent().parent();
        taskTags = task.find('task-tags');

        taskObj = {
            title: task.find('.task-titile').html(),
            detail: task.find('.task-detail').html(),
            priority: task.find('.task-priority').html(),
            tags: tagList
        };

        $.ajax({
            url: '/',
            type: 'post',
            dataType: 'json',
            data: taskObj
            success: function(revTaskObj) {

            }
        });*/
        task = $(this).parent().parent().parent();

        taskTitle = task.find('.task-title');
        taskTitle.hide().after(
            '<input class="task-title-input" value="' 
            + taskTitle.html() + '" >');
        taskDetail = task.find('.task-detail');
        taskDetail.hide().after(
            '<input class="task-detail-input" value="' 
            + taskDetail.html() + '" >');

    }).end().find('.delete').click(function() {
        task = $(this).parent().parent().parent();
        task.remove();
    });
});
