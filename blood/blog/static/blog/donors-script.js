var criterion_map = {
		"Name": 0,
		"Email": 1,
		"Blood Group": 2,
		"Mobile number": 3,
		"Eligible by(days)": 4,
		"event": 5,
		"Everything": 6,
	};

var column_names=[
	"Name",
	"Email",
	"Blood Group",
	"Mobile number",
	"Eligible by(days)",
	"event",
	"Everything",
];

function editTable(){
	var textArea = document.getElementById("id_filtered_recipients");
	textArea.value="";
	var emailId="hello";
	var table = document.getElementById("myTable");
	var tr = table.getElementsByTagName("tr");
	for(var i=1; i<tr.length; i++){
		if(tr[i].style.display != "none"){
			if(tr[i].getElementsByTagName("td")[1]){
				emailId = tr[i].getElementsByTagName("td")[1].innerHTML;
				textArea.value += emailId + ", ";
			}
		}
	}
}
// function showForm(button){
	
// 	var form = document.getElementById("email-form");
// 	if(button.innerHTML=="Compose"){
// 		form.style.display = "inline";
// 		button.className="btn btn-outline-danger";
// 		button.innerHTML="Close"
// 		// now show the emails in the tables with display != "none"
// 		editTable();
// 	}

// 	else{
// 		form.style.display = "none";
// 		button.className= "btn btn-outline-info";
// 		button.innerHTML="Compose";
// 	}

// }

function clearText(){
	var textArea = document.getElementById("email-to-list");
	textArea.value="";
}
function showForm(button){
	
	var form = document.getElementById("email-form");

	if(button.className == "btn btn-info"){
		form.style.display = "inline";
		button.className="btn btn-danger";
		//rotate the button
		button.style.animation= "rf 1.2s forwards";
		//make the form appear
		form.style.animation ="appear 1.2s forwards";
		// now show the emails in the tables with display != "none"
		editTable();
	}

	else{
		button.className= "btn btn-info";
		//rotate the button backwards
		button.style="animation: rb 1.2s forwards";
		//make the form go away
		form.style.animation="disappear 1.2s forwards";
		form.style.display = "none";
	}

}


function changeFilter(index, eventId) {
	if(index != -1){
		document.getElementById("criterion").innerHTML = column_names[index];
	}
	if(eventId!=-1){
		document.getElementById("eventId").innerHTML = eventId;
	}
	myFunction();
}

function myFunction() {
	// Declare variables 
	var input = document.getElementById("myInput");
	var filter = String(input.value).toUpperCase();
	var table = document.getElementById("myTable");
	var tr = table.getElementsByTagName("tr");
	var criterion = document.getElementById("criterion").innerHTML;
	var eventId = document.getElementById("eventId");

	// Loop through all table rows, and hide those who don't match the search query
	for (var i = 1; i < tr.length; i++) {
		td = tr[i].getElementsByTagName("td");
		tr[i].style.display = "none";
		var j = criterion_map[criterion];
		if(criterion ==="Everything"){
			//enable display if atleast one of the fields match the query
		    for(var j =0; j<td.length-2; j++){
		    	if(td[j])
		    		if(td[j].innerHTML.toUpperCase().indexOf(filter)>-1)
		    			tr[i].style.display = "";
		    }
		}
		else if(j==4){
			if(td[j])
				if(Number(td[j].innerHTML)+Number(filter)>112)
					tr[i].style.display = "";
		}
		else{
			//enable display if the particular field match the query
			if(td[j])
				if(td[j].innerHTML.toUpperCase().indexOf(filter)>-1)
					tr[i].style.display = "";
		}

		if(td[td.length-1].innerHTML != eventId.innerHTML){
			if(eventId.innerHTML!=0){
				tr[i].style.display = "none";
			}
		}
		if(filter=="" && eventId.innerHTML==0 )
			tr[i].style.display = "";
	}	

	editTable();
}