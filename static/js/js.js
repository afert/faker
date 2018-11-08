function checkField(s){

	var regu=/[\w\d\s\.\?\!]/;
	var re=new RegExp(regu);

	if(re.test(s)){

		return true;
	}
	else{

		$('.textpage').after("ERROR");
	}
}