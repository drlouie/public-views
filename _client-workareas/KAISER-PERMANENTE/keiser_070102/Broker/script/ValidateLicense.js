

<Script language="JavaScript">

var errorStatus = false;
var errorMessage = "Please correct the following error(s):";


function validate() {
	
	errorStatus = false;
	errorMessage = '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.ErrorMessagePrefix")%>';
	
	doireq = document.LicenseForm.DOIRequestedDate;
	doieff = document.LicenseForm.DOIEffectiveDate;
	doiexp = document.LicenseForm.DOIExpirationDate;

	state = document.LicenseForm.LicState;
	licnum = document.LicenseForm.LicNumber;
	mainname = document.LicenseForm.LicMainName;
	dbaname = document.LicenseForm.LicDBAName;
	issued = document.LicenseForm.LicIssuedDate;
	renewed = document.LicenseForm.LicRenewedDate;
	licexp = document.LicenseForm.LicExpirationDate;
	licext = document.LicenseForm.LicExtensionDate;


	if ( doireq.value == "" && doieff.value == "" && doiexp.value == "" && state.value == "" && licnum.value == "" &&
		mainname.value == "" && dbaname.value == "" && issued.value == "" && renewed.value == "" && licexp == "" && licext == "") {

	}
	else {

		validateDOIValues( document.LicenseForm );
	
		if ( state.value == "" ) {
			errorMessage += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.license.StateRequired")%>';
		      errorStatus = true;
		}

		if ( licnum.value == "" ) {
			errorMessage += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.license.LicNoRequired")%>';
			errorStatus = true;
		}

	
		if ( mainname.value == "" ) {
			errorMessage += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.license.MainNameRequired")%>';
		      errorStatus = true;
		}
		else {
			checkName(document.LicenseForm.LicMainName.name,document.LicenseForm.LicMainName.value);
		}
	
		if ( dbaname.value != "" ) {
			checkName(document.LicenseForm.LicDBAName.name,document.LicenseForm.LicDBAName.value);
	
		}
	
	
		if ( issued.value == "" ) {
			errorMessage += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.license.IssuedDateRequired")%>';
		      errorStatus = true;
		}
		else {
			checkDateValidation( document.LicenseForm.LicIssuedDate.name, document.LicenseForm.LicIssuedDate.value);
		}
		if ( renewed.value != "" ) {
			checkDateValidation( document.LicenseForm.LicRenewedDate.name, document.LicenseForm.LicRenewedDate.value);
			checkDateComparison( document.LicenseForm.LicIssuedDate, document.LicenseForm.LicRenewedDate);
		}
	
		
		if ( licexp.value == "" ) {
			errorMessage += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.license.ExpirationDateRequired")%>';
	        errorStatus = true;
		}
		else {
			checkDateValidation( document.LicenseForm.LicExpirationDate.name, document.LicenseForm.LicExpirationDate.value);
			
			if ( renewed.value != "" )
				checkDateComparison( document.LicenseForm.LicRenewedDate, document.LicenseForm.LicExpirationDate);
			else ( issued.value != "" )
				checkDateComparison( document.LicenseForm.LicIssuedDate, document.LicenseForm.LicExpirationDate);
		
		}
		
		if ( licext.value != "" ) {
			checkDateValidation( document.LicenseForm.LicExtensionDate.name, document.LicenseForm.LicExtensionDate.value);
			checkDateComparison( document.LicenseForm.LicExpirationDate, document.LicenseForm.LicExtensionDate);
		}


	} //end of else





    
    if (errorStatus == true) {
		alert( errorMessage );
		return false;
	}
	else
	   	return true;


}


	function validateDOIValues( theForm ) {
	
		var	doirequested = theForm.DOIRequestedDate;
		var doieffective = theForm.DOIEffectiveDate;
		var doiexpiration = theForm.DOIExpirationDate;

		if ( doirequested.value != "" ) {

			checkDateValidation( theForm.DOIRequestedDate.name, theForm.DOIRequestedDate.value);

			if ( doieffective.value != "" ) {
				checkDateValidation( theForm.DOIEffectiveDate.name, theForm.DOIEffectiveDate.value);
				checkDateComparison( theForm.DOIRequestedDate, theForm.DOIEffectiveDate);

				if ( doiexpiration.value != "" ) {
					checkDateValidation( theForm.DOIExpirationDate.name, theForm.DOIExpirationDate.value);
					checkDateComparison( theForm.DOIEffectiveDate, theForm.DOIExpirationDate);
				}
		
			}
			else {
				if ( doiexpiration.value != "" ) {
					alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.license.DOIExpWithoutDOIEff")%>' );
					return false;
				}
			}
			
	
		}
		else {
		
			if ( doieffective.value != "" ) {
			
				alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.license.DOIEffWithoutDOIReq")%>');
				return false;
			}
			else {
				if ( doiexpiration.value != "" ) {
					alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.license.DOIExpWithoutDOIEff")%>' );
					return false;
				}
			}
			
		
		}
		
	}

	
	
	
	function checkName(name,value) {


		var Name = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";	
		var EffDate = "1234567890/";
		var valid = Name;


		if(valid.length > 1) {
			 for (var i=0; i < value.length; i++) {
				temp = "" + value.substring(i, i+1);
				if (valid.indexOf(temp) == "-1") {
			      	errorMessage+="\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+name;
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
			errorMessage += "\n" +  '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+datename;
			errorStatus = true;
			return false;
		}
		else {
			for (var i=0; i < a.length; i++) {
			temp = "" + a.substring(i, i+1);
				if (validdate.indexOf(temp) == "-1") {
					errorMessage += "\n" +  '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+datename;
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
			errorMessage += "\n" + datename + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidMonth")%>';
			errorStatus = true;
			return false;
		 }
         	 if (c != '/' || e != '/' ) {
			errorMessage += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+datename;
			errorStatus = true;
			return false;
		 }
         	 if (b<1 || b>31) {
			errorMessage += "\n" + datename + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidDate")%>';
			errorStatus = true;
			return false;
		 }
       
         
         
         	 if (f<1900 || f>4000) {
			errorMessage += "\n" + datename +  '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidYear")%>';
			errorStatus = true;
			return false;
		 }



         	 // months with 30 days
         	 if (d==4 || d==6 || d==9 || d==11){
             	if (b==31) {
				errorMessage += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.30DaysInAMonth")%>'+datename;
				errorStatus = true;
				return false;
			}
         	 }


	      // february, leap year
         	 if (d==2){
              	// feb
              	var g=parseInt(f/4)
              	if (isNaN(g)) {
				errorMessage += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.MonthForLeapYear")%>'+datename;
				errorStatus = true;
				return false;
	            }

             	if (b>29) {
				errorMessage += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.MonthDateNoMatch")%>'+datename;
				errorStatus = true;
				return false;
		 	}

             	if (b==29 && ((f/4)!=parseInt(f/4))) {
				errorMessage += "\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+datename;
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

					errorMessage += "\n" + datename + "'s day cannot be lesser than today";
					errorStatus = true;
					return false;
				}
			}
			else {
				errorMessage += "\n" + datename + "'s month cannot be lesser than current month";
				errorStatus = true;
				return false;
			}

		}
		else {
			errorMessage += "\n" + datename + "'s year cannot be lesser than current year";
			errorStatus = true;
			return false;
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
					errorMessage += "\n" + changeddate.name + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.DateComparisonInJavaScript")%>'+ originaldate.name;
					errorStatus = true;
					return false;
				}
			}
			else {
				errorMessage += "\n" + changeddate.name + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.DateComparisonInJavaScript")%>' + originaldate.name;
				errorStatus = true;
				return false;
			}

		}
		else {
			errorMessage += "\n" + changeddate.name + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.DateComparisonInJavaScript")%>' + originaldate.name;
			errorStatus = true;
			return false;
		}


	} // end of checkDateComparison



</Script>