$(document).ready(
	$('#get_link').click(function() {
		$.ajax({
			type:'get',  //request的类型，（get 默认，post，put，delete）
			url:'/update/', //请求的页面的地址
		    	dataType: 'json',  //服务器端传回来的数据格式（xml，json，script，html）
		    	data: '', 
		   	success: function(data) {
		        	var items = [];
		        	$.each(data, function(key, val) {
		            		items.push(key+" " + val);
		        	});
				if($("#get_data").html().length==0){
					$('#get_data').hide();
				}
				$('#get_data').html(
					items.join(",")
					).toggle(1000);	
		        	
		    	}  
        	})
	})
)

$(document).ready(
	$('#post_link').click(function() {
		var json_obj = {
			username: 'wfwei',
			password: 'password',
		};
		var json_str = JSON.stringify(json_obj);    
        $.ajax({
            url:'/update2/',
			type:'post',
            dataType: 'json',
            data: json_str, //要传到服务器端的数据，自动转换为String，object必须是key/value对
            success: function(data) {	

		var items = [];
		$.each(data["0"]["fields"], function(key, val) {
            		items.push(key+" " + val);
	        	});	

		if($("#post_data").html().length==0){
			$('#post_data').hide();
			}
		$('#post_data').html(
			items.join(",")
			).slideToggle(1000);

            }//当request成功是调用的方法，其中data是从服务器端返回的数据，并且已经格式化为指定的dataType。
        })
    })
)


            
