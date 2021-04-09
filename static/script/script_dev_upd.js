$(document).ready(function(){


	setInterval(function() {

		var form_data = $('.get_last_data_form');
		var data = {};
		var csrf_token = $('.get_last_data_form [name="csrfmiddlewaretoken"]').val();
		data["csrfmiddlewaretoken"] = csrf_token;
		var url = form_data.attr("action");
		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			cache: true,
			success: function(data){
                console.log(data);
                $('.list_device_data ul').html("");
                $.each(data, function(k, v){
                    	$('.list_device_data ul').append('<li>'
                    		+'<div class="item_data">'+
                    			'<div>'
                    				+'sn: '+v.sn+ '</br>'
                    				+'time: '+v.time+ '</br>'
                    				+'icsmain: '+ v.icsmain + ';    '
                    				+'icsz1: ' + v.icsz1 + ';    '
                    				+'icsz2: ' + v.icsz2 + ';   '
                    				+'icsz3: ' + v.icsz3 + ';   '
                    				+'icsboiler: ' + v.icsboiler + '; ' +'</br>'
                    				+'t1: ' + v.t1 + ';   '
                    				+'t2: ' + v.t2 + ';   '
                    				+'t3: ' + v.t3 + ';   '
                    				+'t4: ' + v.t4 + ';   '
                    				+'t5: ' + v.t5 + ';   '
                    				+'t6: ' + v.t6 + ';   '
                    				+'t7: ' + v.t7 + ';   ' + '</br>'
                    				+'rt1: ' + v.rt1 + ';   '
                    				+'rt2: ' + v.rt2 + ';   '
                    				+'rt3: ' + v.rt3 + ';   ' + '</br>'
                    				+'endswitch: ' + v.endswitch + ';   ' + '</br>' + '</br>' +
                    			'</div>'+

                    		'</div>'+
        				'</li>');
					})
			},
			error: function(data){
                console.log("error");
			}
		})
    }, 1000);

});