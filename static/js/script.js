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
    	 

// function addCommas(nStr)
// {
//       nStr += '';
//       x = nStr.split('.');
//       x1 = x[0];
//       x2 = x.length > 1 ? '.' + x[1] : '';
//       var rgx = /(\d+)(\d{3})/;
//       while (rgx.test(x1)) {
//         x1 = x1.replace(rgx, '$1' + ',' + '$2');
//       }
//       return x1 + x2;
// }

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}