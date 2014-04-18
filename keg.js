$(document).ready(function() {
  keg_stats();
});



function keg_stats() {
	$.getJSON('/_temperature', function(data) {
		$("#temperature").text(data.temperature);
		$("#thermostat").text(data.thermostat);
		setTimeout(function(){temperature();},500);
	});
}

// <script type=text/javascript>
//  $(
//  function keg_stats()
//  {
//    $.getJSON('/_temperature', function(data)
//      {
//        $("#temperature").text(data.temperature);
//        $("#thermostat").text(data.thermostat);
//        setTimeout(function(){temperature();},500);
// 
//      });
//  }
//  );
//  
//  $(
//  function thermostat()
//  {
//    $.getJSON('/_temperature', function(data)
//      {
//        $("#thermostat").text(data.thermostat);setTimeout(function(){thermostat();},500);
//      });
//  }
//  );
//  
// </script>
