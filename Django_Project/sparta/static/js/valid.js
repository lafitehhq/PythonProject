(function(jq){

	jq.extend({
        'ErrorMessage':function(container,msg){
			$error = container.find("div[class='sv-error-msg']");
            if($error.length>0){
                $error.text(msg);
            }else{
                var temp = "<div class='sv-error-msg'>"+msg+"</label>";
                container.append(temp);
            }
		},
		'EmptyError':function(container){
			$error = container.find("div[class='sv-error-msg']");
            if($error.length>0){
                $error.remove();
            }
		},
        'validate':function(form){
            var flag = true;
            var temp = {};
            $(form).find(':text,:password,textarea,select').each(function(){
                var name = $(this).attr('name');
                var label = $(this).attr('label');
                var val = $(this).val();
                var $parent = $(this).parent();
                var required = $(this).attr('required');
                if(required){
                    if(!val || val.trim() == ''){
                        flag = false;
                        $.ErrorMessage($parent,label+'不能为空');
                        return false;
                    }

                    var mobile = $(this).attr('mobile');
					if(mobile){
						var reg = /^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$/;
						if(!reg.test(val)){
							flag = false;
                            $.ErrorMessage($parent,'手机号码格式错误');
							return false;
						}
					}
                }
                if(val){
                    temp[name] = val.trim();
                }else{
                    temp[name] = val;
                }
                $.EmptyError($parent);
            });
            if(flag){
                return temp
            }else{
                return flag;
            }


		}
	});
	

})(jQuery)