$(document).ready(function(){

	$("#slctCountry").change(function(){
		var country = $("#slctCountry").val();

		if(country == "Australia"){
			$('#slctCity option[value="Ketchup"]').attr('selected','selected');
		}
			
	});
});