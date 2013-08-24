// Shared functions for CMXtra
// Copyright 2003-2004 P.R. Newman, CommunityMX.com

var days_array = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
var months_array = ["January","February","March","April","May","June","July","August","September","October","November","December"];
var newDate = "";

function formatDate(theDate, format){
	
	if(arguments.length > 0){
		if(format == 0){
			// result: "Saturday, June 2, 2001"
			newDate = days_array[theDate.getDay()] + ", " + months_array[theDate.getMonth()] + " " + theDate.getDate() + ", " + theDate.getUTCFullYear();
			return newDate;
		}
		else if(format == 1){
			// result: "6/2/2001"
			newDate = (theDate.getMonth()+1) + "/" + theDate.getDate() + "/" +  theDate.getUTCFullYear();
			return newDate;
		}
		else if(format == 2){
			// result: "Jun 2 2003"
			var date_array = theDate.toString().split(" ");
			newDate = date_array[1] + " " + date_array[2] + " " + date_array[5];
			return newDate;
		}
	}
	else{
		// result: "Sat Jun 2 11:14:02 GMT+0100 2001"
		return theDate.toString();
	}
}
