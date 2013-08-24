




	function validateAmendment( theForm ) {

		var errorStatus = false;	
		var errorFields = "Please correct the following error(s):";



		if ( theForm.PayeeBID.value == "" ) {
			errorStatus = true;
			errorFields += "\nSelect a Payee BID for which you want to add an Amendment";		
		}
		else if ( theForm.AssociatedAgreement.value == "" ) {
			errorStatus = true;
			errorFields += "\nSelect an Associated Agreement for which you want to add an Amendment";		
		
		}
		else {
		
			//validate amendment
			
			if ( theForm.FirstName.value == "" ) {
				errorFields += "\n" + "FirstName is a required field";
				errorStatus = true;
			}
			else {
				checkName( theForm.FirstName.name,theForm.FirstName.value);
			
			}
		
			if ( theForm.LastName.value == "" ) {
				errorFields += "\n" + "LastName is a required field";
				errorStatus = true;
			}
			else
				checkName( theForm.LastName.name,theForm.LastName.value);
		
			if ( theForm.Honorific.value != "" )
				checkName( theForm.Honorific.name,theForm.Honorific.value);
		
			if ( theForm.MiddleName.value != "" )
				checkName( theForm.MiddleName.name,theForm.MiddleName.value);
		
			if ( theForm.Suffix.value != "" )
				checkName( theForm.Suffix.name,theForm.Suffix.value);
		
			if ( theForm.EffectiveDate.value == "" ) {
				errorFields += "\n" + "EffectiveDate is a required field";
				errorStatus = true;
			}
			else
				checkDateValidation( theForm.EffectiveDate.name, theForm.EffectiveDate.value );
		
			if ( theForm.EndDate.value != "" )
				checkDateValidation( theForm.EndDate.name, theForm.EndDate.value );
	
						
			if ( theForm.Generated.value != "" ) {
		
				if ( theForm.DateMailed.value != "" ) {
					checkDateValidation( theForm.DateMailed.name, theForm.DateMailed.value );
					
					if ( theForm.FaxSignedReceived.value != "" ) {
						checkDateValidation( theForm.FaxSignedReceived.name, theForm.FaxSignedReceived.value );
							
						if ( theForm.OrigSignedReceived.value != "" ) {
							checkDateValidation( theForm.OrigSignedReceived.name, theForm.OrigSignedReceived.value );
						}
	
					}
					else {
					
						if ( theForm.OrigSignedReceived.value != "" ) {
							errorFields += "\n" + "Fax Signed/Received has no value, so the dependent information Original Signed/Received cannot have value";
							errorStatus = true;
					
						}
					
					}

				}
				else {
				
					if ( theForm.FaxSignedReceived.value != "" || theForm.OrigSignedReceived.value != "") {
						errorFields += "\n" + "Date Mailed has no value, so the dependent information like Fax Signed/Received and Original Signed/Received cannot have value";
						errorStatus = true;
					}				
				
				}
				

			}
			
		
		
		
		
		}
			
	
		if ( errorStatus ) {
		
			alert( errorFields );
			return false;
		}
		else
			return true;
	
	
	
	
	function checkName(name,value) {

		var Name = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";	
		var valid = "";
		if( name == "Honorific" ||  name == "FirstName" || name == "MiddleName" || name == "LastName" || name == "Suffix" ) {
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
             	if (b==31) {
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
	
	
	
	}//end of Validate Amendment
