function register_validation(){

	var username = document.getElementById('id_username').value;
	var email = document.getElementById('id_email').value;
	var password = document.getElementById('id_password').value;
	var result = true;

	if(username==""){
		document.getElementById('form-errors').innerHTML="Username is required!";
		result = false;
	}
	if(email==""){
		document.getElementById('form-errors').innerHTML="Email is required!";
		result = false;
	}
	if(password.length < 6){
		document.getElementById('form-errors').innerHTML="Invalid password length!";
		result = false;
	}

	return result;
}