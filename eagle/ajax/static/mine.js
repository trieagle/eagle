$(document).ready(
	$('#get_link').click(function() {
		$.ajax({
			type:'get',  //request�����ͣ���get Ĭ�ϣ�post��put��delete��
            url:'/update/', //�����ҳ��ĵ�ַ
            dataType: 'json',  //�������˴����������ݸ�ʽ��xml��json��script��html��
            data: '', //Ҫ�����������˵����ݣ��Զ�ת��ΪString��object������key/value��
            success: function(data) {
                var items = [];
                $.each(data, function(key, val) {
                    items.push(key+" " + val);
                });
                $('#get_data').html(items.join(","));
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
            data: json_str, 
            success: function(data) {	
				var d = data[0];
                $('#post_data').html(d['fields'].username);
            }//��request�ɹ��ǵ��õķ���������data�Ǵӷ������˷��ص����ݣ������Ѿ���ʽ��Ϊָ����dataType��
	
        })
    })
)


            
