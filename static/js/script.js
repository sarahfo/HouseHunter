$(document).ready(function(){

        $(".city").click(function(event) {
         var item = $(event.currentTarget).data();
    	 var setView = [item.lon, item.lat];
    	 var city_id = (item.city);
        	$.ajax({url: "/get_homes", data: {city_id:city_id}})
        });
});

// TODO TOMORROW:  have it pull out the city data.  send this info to server.
     	 // console.log(setView)
    	 // console.log(city_id)
