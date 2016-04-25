$(document).ready(function(){

	$("#slctCountry").change(function(){
		var country = $("#slctCountry").val();
		$("#slctState").empty()
		$("#slctCity").empty()
		appenddata = "<option value = ''>Select</option>";
      	$("#slctCity").append(appenddata);
    	$("#slctState").append(appenddata);
		$.ajax({
			 url: "/statedata",
		      type: 'POST',
		      data: 'country=' + country,
		      datatype: 'JSON',
		      success: function(result){
	    	 	for (var i = 0; i < result.length; i++) {
	    		 	appenddata = "<option value = '" + result[i] + " '>" + result[i] + " </option>";
	    		 	$("#slctState").append(appenddata);
		    	}
		     }
		});
	});

	$("#slctState").change(function(){
		var state = $("#slctState").val();
		$("#slctCity").empty()
		$.ajax({
			 url: "/citydata",
		      type: 'POST',
		      data: 'state=' + state,
		      datatype: 'JSON',
		      success: function(result){
		      	appenddata = "<option value = ''>Select</option>";
		    	$("#slctCity").append(appenddata);
	    	 	for (var i = 0; i < result.length; i++) {
	    		 	appenddata = "<option value = '" + result[i] + " '>" + result[i] + " </option>";
	    		 	$("#slctCity").append(appenddata);
		    	 }
		     }
		});
	});
});