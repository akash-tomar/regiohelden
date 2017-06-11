$(document).ready(function() {
	$("#submit").click(function() {
		var data={"old_first_name":first_name,"old_last_name":last_name};
		if(first_name!=$('[name="first_name"]').val()) {
			data["first_name"]=$('[name="first_name"]').val();
		}
		if(last_name!=$('[name="last_name"]').val()) {
			data["last_name"]=$('[name="last_name"]').val();
		}
		if(countrycode!=$('[name="countrycode"]').val()) {
			data["countrycode"]=$('[name="countrycode"]').val();
		}
		if(checksum!=$('[name="checksum"]').val()) {
			data["checksum"]=$('[name="checksum"]').val()
		}
		if(swiftcode!=$('[name="swiftcode"]').val()) {
			data["swiftcode"]=$('[name="swiftcode"]').val()
		}
		if(accountnumber!=$('[name="accountnumber"]').val()) {
			data["accountnumber"]=$('[name="accountnumber"]').val()
		}
		getAjaxRequest(url,data);
	});
});

function handleRequest(resp) {
	if(resp.success) {
		window.location.replace(home);
	} else {
		$("body").append(resp.failed);
	}
}

function getAjaxRequest(url,data) {
	// var csrf_token = $.cookie('csrftoken');
	console.log(url,data);
    var ajax = $.ajax({
        url: url,
        data: JSON.stringify(data),
        type: 'POST',
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrf_token);
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