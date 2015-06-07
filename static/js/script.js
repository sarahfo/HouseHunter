$(document).ready(function(){

    
	$(".city").click(function (event) { 
         var item = $(event.currentTarget).data();
    	 var city_id = (item.city);
         
         console.log(city_id);
    	 var form = document.createElement('form');
    	 	$(form).attr("action", "/get_homes");
    	 	$("<input>").attr({
    	 			name: "city_id",
    	 			value: city_id
    	 			}).appendTo(form);
    	 	$(form).submit();
    	 });
  });	
    	 



