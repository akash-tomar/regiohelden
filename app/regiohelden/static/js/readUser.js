$(document).ready(function() {
	$("#submit").click(function() {
		var first_name = $("#id_first_name").val();
		var last_name = $("#id_last_name").val();
		url+="?first_name="+first_name+"&last_name="+last_name;
		getAjaxRequest(url)
	});
});

function getAjaxRequest(url) {
    var ajax = $.ajax({
        url: url,
        type: 'GET',
        contentType: "application/json",
        beforeSend: function(xhr) {
        },
        error : function(response){
            console.log(response);
        },
        success: function(resp){
            console.log(resp);
            handleRequest(resp);
        }
    });
}

function handleRequest(resp) {
	$("#getdetails").remove();
	if("failed" in resp) {
		$("#showdetails").append("<div>"+resp.failed+"</div>")
	} else {
		$("#showdetails").append("<div>First name: "+resp.first_name+"</div>");
		$("#showdetails").append("<div>Last name: "+resp.last_name+"</div>");
		$("#showdetails").append("<div>IBAN: "+resp.countrycode+" "+resp.checksum+" "+resp.swiftcode+" "+resp.accountnumber+"</div>");
	}
}