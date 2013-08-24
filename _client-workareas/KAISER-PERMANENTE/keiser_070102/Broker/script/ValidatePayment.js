<Script language="JavaScript">

function validate( theForm ) {

	var errorStatus = false;
	var errorFields = '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.ErrorMessagePrefix")%>'

	if ( theForm.Honorific.value == "" && theForm.FirstName.value == "" && theForm.LastName.value == "" && 
		theForm.MiddleName.value == "" && theForm.Suffix.value == "" &&  theForm.TransactionType.value == "" && 
		 theForm.RoutingNo.value == "" &&  theForm.AccountType.value == "" &&  theForm.AccountNo.value == "" && 
		 theForm.SignedDate.value == "" &&  theForm.ReceivedDate.value == "" &&  theForm.EcomDate.value == "" && 
		 theForm.PreNoteDate.value == "" ) {

	}
	else {

	if ( theForm.FirstName.value == "" ) {
		errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Name.FirstNameRequired")%>';
		errorStatus = true;
	}
	else {
		checkName( theForm.FirstName.name,theForm.FirstName.value);
	}

	if ( theForm.LastName.value == "" ) {
		errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Name.LastNameRequired")%>';
		errorStatus = true;
	}
	else {
		checkName( theForm.LastName.name,theForm.LastName.value);
	}

	if ( theForm.Honorific.value != "" )  {
		checkName( theForm.Honorific.name,theForm.Honorific.value);
	}

	if ( theForm.MiddleName.value != "" )  {
		checkName( theForm.MiddleName.name,theForm.MiddleName.value);
	}

	if ( theForm.Suffix.value != "" )  {
		checkName( theForm.Suffix.name,theForm.Suffix.value);
	}

	if ( theForm.RoutingNo.value == "" ) {
		errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Payment.RoutingNoRequired")%>';
		errorStatus = true;
	}
	else {
		checkNumber( theForm.RoutingNo.name,theForm.RoutingNo.value);
	}

	if ( theForm.AccountNo.value == "" ) {
		errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Payment.AccountingNoRequired")%>';
		errorStatus = true;
	}
	else {
		checkNumber( theForm.AccountNo.name,theForm.AccountNo.value);
	}

	if ( theForm.SignedDate.value == "" ) {
		errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Payment.SignedDateRequired")%>';
		errorStatus = true;
	}
	else {
		checkDateValidation(theForm.SignedDate.name , theForm.SignedDate.value );
	}

	if ( theForm.ReceivedDate.value == "" ) {
		errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Payment.ReceivedDateRequired")%>';
		errorStatus = true;
	}
	else {
		checkDateValidation(theForm.ReceivedDate.name , theForm.ReceivedDate.value );
		checkDateComparison(theForm.SignedDate, theForm.ReceivedDate );
		
		
		if ( theForm.EcomDate.value != "" ) {
	
			checkDateValidation(theForm.EcomDate.name , theForm.EcomDate.value );
			checkDateComparison(theForm.ReceivedDate, theForm.EcomDate );
			
			if ( theForm.PreNoteDate.value != "" ) {
		
				checkDateValidation(theForm.PreNoteDate.name , theForm.PreNoteDate.value );
				checkDateComparison(theForm.EcomDate, theForm.PreNoteDate );
			}

		}
		else {
		
			if ( theForm.PreNoteDate.value != "" ) {
				errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Payment.EcomDepenedentInvalid")%>';
				errorStatus = true;
			}
		
		}
		
	}





	}//end of else

	if (errorStatus==true) {
		alert( errorFields );
	     	return false;
	}
	else {
		return true;
	}


	function checkName(name,value) {


		var Name = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";	
		var EffDate = "1234567890/";
		var valid = "";
		if( name == "Honorific" ||  name == "FirstName" || name == "MiddleName" || name == "LastName" || name == "Suffix" ) {
			valid = Name;
		}

		if(valid.length > 1) {
			 for (var i=0; i < value.length; i++) {
				temp = "" + value.substring(i, i+1);
				if (valid.indexOf(temp) == "-1") {
			      	errorFields+="\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+name;
			      	errorStatus=true;      
			      	break;
				}
			}
		}

	}


	function checkNumber( name,value) {

		var valid = "1234567890";

		if(valid.length > 1) {
			 for (var i=0; i < value.length; i++) {
				temp = "" + value.substring(i, i+1);
				if (valid.indexOf(temp) == "-1") {
			      	errorFields+="\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+name;
			      	errorStatus=true;      
			      	break;
				}
			}
		}


	}


	function checkAmount( name,value) {

		var valid = ".1234567890";

		if(valid.length > 1) {
			 for (var i=0; i < value.length; i++) {
				temp = "" + value.substring(i, i+1);
				if (valid.indexOf(temp) == "-1") {
			      	errorFields+="\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+name;
			      	errorStatus=true;      
			      	break;
				}
			}
		}

	}



	function checkDateValidation(datename, datevalue){


	 	var validdate = "1234567890/";
         	var err=0;
         	var psj=0;
	      var a="";

         	a=datevalue;
		
		
	 	if (a.length != 10) {
			errorFields += "\n" +  '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+datename;
			errorStatus = true;
			return false;
		}
		else {
			for (var i=0; i < a.length; i++) {
			temp = "" + a.substring(i, i+1);
				if (validdate.indexOf(temp) == "-1") {
					errorFields += "\n" +  '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+datename;
					errorStatus = true;
					return false;
				}
			}
		 }

   	       d = a.substring(0, 2);
      	 c = a.substring(2, 3);
         	 b = a.substring(3, 5);
         	 e = a.substring(5, 6);
         	 f = a.substring(6, 10);

 	       //basic error checking

      	 if (d<1 || d>12) {
			errorFields += "\n" + datename + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidMonth")%>';
			errorStatus = true;
			return false;
		 }
         	 if (c != '/' || e != '/' ) {
			errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+datename;
			errorStatus = true;
			return false;
		 }
         	 if (b<1 || b>31) {
			errorFields += "\n" + datename + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidDate")%>';
			errorStatus = true;
			return false;
		 }
       
         
         
         	 if (f<1900 || f>4000) {
			errorFields += "\n" + datename +  '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidYear")%>';
			errorStatus = true;
			return false;
		 }



         	 // months with 30 days
         	 if (d==4 || d==6 || d==9 || d==11){
             	if (b==31) {
				errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.30DaysInAMonth")%>'+datename;
				errorStatus = true;
				return false;
			}
         	 }


	      // february, leap year
         	 if (d==2){
              	// feb
              	var g=parseInt(f/4)
              	if (isNaN(g)) {
				errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.MonthForLeapYear")%>'+datename;
				errorStatus = true;
				return false;
	            }

             	if (b>29) {
				errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.MonthDateNoMatch")%>'+datename;
				errorStatus = true;
				return false;
		 	}

             	if (b==29 && ((f/4)!=parseInt(f/4))) {
				errorFields += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+datename;
				errorStatus = true;
				return false;
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
					errorFields += "\n" + changeddate.name + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.DateComparisonInJavaScript")%>' + originaldate.name;
					errorStatus = true;
				}
			}
			else {
				errorFields += "\n" + changeddate.name + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.DateComparisonInJavaScript")%>' + originaldate.name;
				errorStatus = true;
			}

		}
		else {
			errorFields += "\n" + changeddate.name + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.DateComparisonInJavaScript")%>' + originaldate.name;
			errorStatus = true;
		}


	} // end of checkDateComparison

}// end of validate()

</Script>