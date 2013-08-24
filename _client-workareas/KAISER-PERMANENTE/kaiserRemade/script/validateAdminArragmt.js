

function validate( theForm ) {

 
	var errorStatus = false;
	var errorFields = "Please correct the follwing error(s): ";

	if ( theForm.origEffectiveDate.value == "" ) {
		errorFields += "\n" + "OrigEffectiveDate is a required field";
		errorStatus = true;
	}
	else {
	checkDateValidation( theForm.origEffectiveDate.name,theForm.origEffectiveDate.value );
//checkCurrentDate( theForm.origEffectiveDate.name, theForm.origEffectiveDate.value );
	}
	if ( theForm.status.value == "" ) {
		errorFields += "\n" + "Status is a required field";
		errorStatus = true;
	}
  	if ( theForm.regionDivision.value == "" )  {
 		errorFields += "\n" + "RegionDivision is a required field";
		errorStatus = true;
		
	}

	if ( theForm.size.value == "" )  {
		errorFields += "\n" + "Size is a required field";
		errorStatus = true;
 
	}


	if ( theForm.purchaserName.value == "" ) {
		errorFields += "\n" + "Name is a required field";
		errorStatus = true;
	}
	else
	{
	checkPurchaserName(theForm.purchaserName.name,theForm.purchaserName.value)
	}	
 
	if ( theForm.administrativeSystem.value == "" ) {
		errorFields += "\n" + "Administrative System is a required field";
		errorStatus = true;
	}
	if ( theForm.administrator.value == "" ) {
		errorFields += "\n" + "Administrator is a required field";
		errorStatus = true;
	}

	if ( theForm.billingFrequency.value == "" ) {
		errorFields += "\n" + "billing Frequency is a required field";
		errorStatus = true;
	}

	if ( theForm.effDate.value == "" ) {
		errorFields += "\n" + "effDate is a required field";
		errorStatus = true;
	}
	else {
		checkDateValidation( theForm.effDate.name, theForm.effDate.value );
		//checkCurrentDate( theForm.effDate.name, theForm.effDate.value );
	}

	if ( theForm.endDate.value != "" )  {
		checkDateValidation( theForm.endDate.name, theForm.endDate.value );
		//checkDateComparison( theForm.EffectiveDate, theForm.EndDate );
	}
 

	if (errorStatus==true) {
		alert( errorFields );
	     	return false;
	}
	else {
	
		return true;
	}


	function checkPurchaserName(name,value) {


		var Name = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";	
		var EffDate = "1234567890/";
		var valid = "";
		if( name == "purchaserName") {
			valid = Name;
		}
 

		if(valid.length > 1) {
			 for (var i=0; i < value.length; i++) {
				temp = "" + value.substring(i, i+1);
				if (valid.indexOf(temp) == "-1") {
			      	errorFields+="\n" + "Invalid characters in "+name;
			      	errorStatus=true;      
			      	break;
				}
			}
		}

	}



	function checkDateValidation(datename, datevalue){


	 	var validdate = "1234567890/";
         	var err=0
         	var psj=0;
	      var a="";

         	a=datevalue;
		
	 	if (a.length != 10) {
			errorFields += "\n" +  "Invalid "+datename;
			errorStatus = true;
		}
		else {
			for (var i=0; i < a.length; i++) {
			temp = "" + a.substring(i, i+1);
				if (validdate.indexOf(temp) == "-1") {
					errorFields += "\n" +  "Invalid Characters in "+datename;
					errorStatus = true;
				}
			}
		 }

   	       d = a.substring(0, 2)
      	 c = a.substring(2, 3)
         	 b = a.substring(3, 5)
         	 e = a.substring(5, 6)
         	 f = a.substring(6, 10)

 	       //basic error checking

      	 if (d<1 || d>12) {
			errorFields += "\n" + datename + "'s month invalid";
			errorStatus = true;
		 }
         	 if (c != '/' || e != '/' ) {
			errorFields += "\n" + "Invalid "+datename;
			errorStatus = true;
		 }
         	 if (b<1 || b>31) {
			errorFields += "\n" + datename + "'s date invalid";
			errorStatus = true;
		 }
         	 if (f<1900 || f>4000) {
			errorFields += "\n" + datename + "'s year invalid";
			errorStatus = true;
		 }

         	 // months with 30 days
         	 if (d==4 || d==6 || d==9 || d==11){
             	if (d==31) {
				errorFields += "\n" + "Only 30 days are there in the month of "+datename;
				errorStatus = true;
			}
         	 }

	      // february, leap year
         	 if (d==2){
              	// feb
              	var g=parseInt(f/4)
              	if (isNaN(g)) {
				errorFields += "\n" + "Month does not match for the leap year in "+datename;
				errorStatus = true;

	            }

             	if (b>29) {
				errorFields += "\n" + "Month and Date do not match in "+datename;
				errorStatus = true;
		 	}

             	if (b==29 && ((f/4)!=parseInt(f/4))) {
				errorFields += "\n" + "Invalid "+datename;
				errorStatus = true;
	       	}
		 }

	} // end of checkValidation()


	function checkCurrentDate( datename, datevalue ) {

		var dt = new Date();
		var month = dt.getMonth();
		var date = dt.getDate();
		var year = dt.getYear();

		month = month +1 ;
	

		if ( ( month / 2 ) < 5 )
			month = "0" + month;

		if ( ( date / 2 ) < 5 )
			date = "0" + date;

		var currentDate =  month + "/" +date+ "/" +year;


   	      var chmm = datevalue.substring(0, 2);
         	var chdd = datevalue.substring(3, 5);
         	var chyyyy = datevalue.substring(6, 10);


		if ( chyyyy > year ) {
		
		}
		else if ( chyyyy == year ) {

			if ( chmm > month ) {
			}
			else if ( chmm == month ) {
				if ( chdd < date ) {

					errorFields += "\n" + datename + "'s day cannot be lesser than today";
					errorStatus = true;
				}
			}
			else {
				errorFields += "\n" + datename + "'s month cannot be lesser than current month";
				errorStatus = true;
			}

		}
		else {
			errorFields += "\n" + datename + "'s year cannot be lesser than current year";
			errorStatus = true;
		}

	}




	function checkDateComparison( originaldate, changeddate ) {

		
		var orgmmddyyyy = originaldate.value;
		var chmmddyyyy = changeddate.value;
	
   	      var orgmm = orgmmddyyyy.substring(0, 2);
         	var orgdd = orgmmddyyyy.substring(3, 5);
         	var orgyyyy = orgmmddyyyy.substring(6, 10);

   	      var chmm = chmmddyyyy.substring(0, 2);
         	var chdd = chmmddyyyy.substring(3, 5);
         	var chyyyy = chmmddyyyy.substring(6, 10);




		if ( chyyyy > orgyyyy ) {
		
		}
		else if ( chyyyy == orgyyyy ) {

			if ( chmm > orgmm ) {

			}
			else if ( chmm == orgmm ) {

				if ( chdd < orgdd ) {
					errorFields += "\n" + changeddate.name + " cannot be lesser than " + originaldate.name;
					errorStatus = true;
				}
			}
			else {
				errorFields += "\n" + changeddate.name + " cannot be lesser than " + originaldate.name;
				errorStatus = true;
			}

		}
		else {
			errorFields += "\n" + changeddate.name + " cannot be lesser than " + originaldate.name;
			errorStatus = true;
		}


	} // end of checkDateComparison

}// end of validate()