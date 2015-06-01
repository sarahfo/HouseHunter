$(document).ready(function(){

	// var setView = []
	$(".city").click(function (event) { 
         var item = $(event.currentTarget).data();
    	 // setView.push([item.lon, item.lat]);   - going to see if this can be on python server side
    	 // alert(item.lon, item.lat)
    	 // alert(setView)
    	 var city_id = (item.city);
         console.log(city_id)
    	 var form = document.createElement('form');
    	 	$(form).attr("action", "/get_homes");
    	 	$("<input>").attr({
    	 			name: "city_id",
    	 			value: city_id
    	 			}).appendTo(form);
    	 	$(form).submit();
    	 });
  	
    	 
    	  // COULD USE THE MULTIPLE RETURN OPTION HERE?
        	// $.ajax({url: "/get_homes", data: {city_id:city_id}})

// function makeMap(setView) {
// 	L.mapbox.accessToken = 'pk.eyJ1Ijoic2FyYWhmbyIsImEiOiJaQmdHLWZJIn0.eEg4zenYs0-qcPsMBZ9i1g';
// 	var map = L.mapbox.map('map', 'sarahfo.ma312pld').setView([setView], 12);
// 	console.log(setView)
// 	// var myLayer = L.mapbox.featureLayer().addTo(map);
// 	// var features = [];
// };

});  
// 	
// 	
// }
// could use for multiple calls:
// function funname_get(url) {

// 	return $.ajax({
// 		url: url,
// 		type: 'get',
// 		dataType: 'datatypespecified',

// 	});
// }

// funname_get('/index').done(function(data) {
// 	//stuff you want to do with the data
// });

// ________________________________________
// TODO TOMORROW:  have it pull out the city data.  send this info to server.
     	 // console.log(setView)
    	 // console.log(city_id)

// SILENT FORM OPTION FOR AJAX

