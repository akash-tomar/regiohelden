$(document).ready(function() {
	setValuesInForm();
});


function setValuesInForm() {
	$("#id_first_name").val(first_name);
	$("#id_last_name").val(last_name);
	$("#id_countrycode").val(countrycode);
	$("#id_checksum").val(checksum);
	$("#id_swiftcode").val(swiftcode);
	$("#id_accountnumber").val(accountnumber);
}