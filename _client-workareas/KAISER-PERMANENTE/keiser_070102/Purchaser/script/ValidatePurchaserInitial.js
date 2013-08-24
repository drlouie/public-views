<SCRIPT language="JavaScript1.1">
function validate( theForm ) {

	var errorStatus = false;
	var errorFields = "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.ErrorMessagePrefix")%>"+"\n";;
	var validZipValues = "1234567890";

	if ( theForm.origEffectiveDate.value == "" ) {
		errorFields += "\n" + "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.OrigEffDtRequired")%>";
		errorStatus = true;
	}
	else {
	checkDateValidation( theForm.origEffectiveDate.name,theForm.origEffectiveDate.value );
//checkCurrentDate( theForm.origEffectiveDate.name, theForm.origEffectiveDate.value );
	}
  	if ( theForm.regionDivision.value == "" )  {
 		errorFields += "\n" + "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.RegionDivionRequired")%>";
		errorStatus = true;
		
	}
	if ( theForm.PID.value == ""  &&  theForm.TPAID.value == "" ) {
		errorFields += "\n" + "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.PidTpaIdRequired")%>";
		errorStatus = true;
	}
	if ( theForm.PID.value !="")
	 {
	checkPurchaserName(theForm.PID.name,theForm.PID.value)
	}
	if ( theForm.TPAID.value !="")
	 {
	checkPurchaserName(theForm.TPAID.name,theForm.TPAID.value)
	}
	if ( theForm.size.value == "" )  {
		errorFields += "\n" + "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.SalesUnitRequired")%>";
		errorStatus = true;
 
	}

	if ( theForm.taxId.value == ""  ) {
		errorFields += "\n" + "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.TaxIdRequired")%>";
		errorStatus = true;
	}
	else
	{
	checkPurchaserName(theForm.taxId.name,theForm.taxId.value)
	}	
 	if ( theForm.directSale.value == "" ) {
		errorFields += "\n" + "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.DirectSaleRequired")%>";
		errorStatus = true;
	}
	if ( theForm.purchaserName.value == "" ) {
		errorFields += "\n" + "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.PurNameRequired")%>";
		errorStatus = true;
	}
	else
	{
	checkPurchaserName(theForm.purchaserName.name,theForm.purchaserName.value)
	}	
	if ( theForm.line1.value == "" ) {
		errorFields += "\n" + "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.Line1Required")%>";
		errorStatus = true;
	}
	else
	{
	checkPurchaserName(theForm.line1.name,theForm.line1.value)
	}	 
	
	if ( theForm.line2.value !="")
	 {
	checkPurchaserName(theForm.line2.name,theForm.line2.value)
	}

	if ( theForm.line3.value !="")
	 {
	checkPurchaserName(theForm.line3.name,theForm.line3.value)
	}	
	
	if ( theForm.mailStop.value !="")
	 {
	checkPurchaserName(theForm.mailStop.name,theForm.mailStop.value)
	}
	
	if ( theForm.country.value == "USA" ||  theForm.country.value == "CAN")
	{
	if ( theForm.state.value == "")
	 {
		errorFields += "\n"+"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.StateRequired")%>";
		errorStatus = true;
	}
	else
	{
		var found = false;
		var state = theForm.state.value;
		state = state.toUpperCase();		
		for(var i = 0 ; i < states.length ; i++)
		{	
			if(state == states[i])
				{	
					found = true;		
					break;
				}
			else
				continue;
		}
		if(found == false)
		{
			errorFields+= "\n"+"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.StateNotValid")%>";
			errorStatus = true;	
			theForm.state.focus();
		}
   	}
  }
	//checkPurchaserName(theForm.state.name,theForm.state.value)
	
	
	if ( theForm.city.value == "" ) {
		errorFields += "\n" + "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.CityRequired")%>";
		errorStatus = true;
	}
	else
	{
	checkPurchaserName(theForm.city.name,theForm.city.value)
	}	
	if ( theForm.country.value == "" ) {
		errorFields += "\n" + "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.CountryRequired")%>";
		errorStatus = true;
	}
	else
	{
		checkCountry( theForm.country.value);
	}

	if ( theForm.administrativeSystem.value == "" ) {
		errorFields += "\n" + "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.AdminSysRequired")%>";
		errorStatus = true;
	}
	if ( theForm.administrator.value == "" ) {
		errorFields += "\n" + "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.AdministratorRequired")%>";
		errorStatus = true;
	}

	if ( theForm.billingFrequency.value == "" ) {
		errorFields += "\n" + "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.BillingFreqRequired")%>";
		errorStatus = true;
	}

	if ( theForm.effDate.value == "" ) {
		errorFields += "\n" + "<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.EffDtRequired")%>";
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
 

	if ( theForm.terminationDate.value != "" )  {
		checkDateValidation( theForm.terminationDate.name, theForm.terminationDate.value );
		//checkDateComparison( theForm.EffectiveDate, theForm.EndDate );
	}
 
checkPhoneInGeneral("000",theForm.areaCode.value,theForm.phoneNumber.value,theForm.extension.value);


	if (errorStatus==true) {
		alert( errorFields );
	     	return false;
	}
	else {
	
		return true;
	}


	function checkPurchaserName(name,value) {


		var Name = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";	
		var Line1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890, ";
		var City = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
		var MailStop = "#1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
		var pid = "1234567890";
		var valid = "";
		if( name == "purchaserName" || name =="state" || name =="country") {
			valid = Name;
		}
 		if( name == "PID" ||  name == "TPAID" || name == "taxId" || name =="zip" ) {
			valid = pid;
		}
		 if(name == "line1" || name == "line2" || name == "line3")
			{
				valid = Line1;
			}
 		 if(name == "city" )
			{
			valid = City;
			}
  		if(name == "mailStop")  
			{
		valid = MailStop;
			}
		if(name == "taxId" && value.length < 9)
			{
				errorFields+= "\n" +name+" should be 9 digits \n";	
				errorStatus = true;
     			}
		if(name == "zip" && value.length < 5)
				{
				errorFields+="\n" +name+" should be 5 digits \n";	
				errorStatus = true;
     				}


		if(valid.length > 1) {
			 for (var i=0; i < value.length; i++) {
				temp = "" + value.substring(i, i+1);
				if (valid.indexOf(temp) == "-1") {
			      	errorFields+="\n" + '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.InvalidChar")%>'+name;
			      	errorStatus=true;      
			      	break;
				}
			}
		}

	}



	function checkCountry ( country ) {
		
		var countryvalue = country;
		var zipvalue = theForm.zip.value;

			if (country == "USA" && zipvalue.length > 0 ) {
			
				if ( zipvalue.length != 5 ) {
					
					if ( zipvalue.length == 10 ) {
						checkZip5Plus4( zipvalue );
					}
					else if ( zipvalue.length == 9 ) {
						errorFields+='\n'+'<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipFormatUSA")%>';
						errorStatus = true;
						theForm.zip.focus();
						return false;
					}
					else {
						errorFields+='\n'+'<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipDigitsUSA")%>';
						errorStatus = true;
						theForm.zip.focus();
						return false;
					}
				}
				else if ( zipvalue.length == 5 )
					checkZip( zipvalue );
				
			}


			if (country == "CAN" && zipvalue.length > 0 && zipvalue.length!=6) {
				errorFields+='\n'+'<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipCanada")%>';
				errorStatus = true;
				theForm.zip.focus();
				return false;
			}
			else if ( country == "CAN" && zipvalue.length == 6 )
				checkCanZip( zipvalue );

	}


	function checkZip ( zip ) {
		
		var zipvalue = zip;

		for (var i=0; i < zipvalue.length; i++) {
			temp = "" + zipvalue.substring(i, i+1);
				if (validZipValues.indexOf(temp) == "-1") {
					errorFields+='\n'+'<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipInvalid")%>';
					errorStatus = true;
					theForm.zip.focus();
					return false;
				}
		}
	}

	function checkZip5Plus4 ( zip ) {
		
		var zipvalue = zip;
		var zipFive = zipvalue.substring(0,5);
		var zipFour = zipvalue.substring(6,10);
		var zipDelimiter = zipvalue.substring(5,6);
		
		if ( zipDelimiter != "-" ) {
			errorFields+='\n'+'<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipFormatInvalid")%>';
			errorStatus = true;
			theForm.zip.focus();
			return false;
		}


		for (var i=0; i < zipFour.length; i++) {
			temp = "" + zipFour.substring(i, i+1);
				if (validZipValues.indexOf(temp) == "-1") {
					errorFields+='\n'+'<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipInvalid")%>';
					errorStatus = true;
					theForm.zip.focus();
					return false;
				}
		}

		for (var i=0; i < zipFive.length; i++) {
			temp = "" + zipFive.substring(i, i+1);
				if (validZipValues.indexOf(temp) == "-1") {
					errorFields+='\n'+'<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipInvalid")%>';
					errorStatus = true;
					theForm.zip.focus();
					return false;
				}
		}
	}
	
	function checkCanZip ( zip ) {
		
		var zipvalue = zip;
		var canZipValid = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm";

		for (var i=0; i < zipvalue.length; i++) {
			temp = "" + zipvalue.substring(i, i+1);
				if (canZipValid.indexOf(temp) == "-1") {
					errorFields+='\n'+'<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipInvalid")%>';
					errorStatus = true;
					theForm.zip.focus();
					return false;
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

					errorFields += "\n" + datename +"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Date.DayLesser")%>";
					errorStatus = true;
				}
			}
			else {
				errorFields += "\n" + datename +"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Date.MonthLesser")%>";
				errorStatus = true;
			}

		}
		else {
			errorFields += "\n" + datename +"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Date.YearLesser")%>";
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

 function checkPhoneInGeneral(iCountryCode,iAreaCode,iNumber,iExtension)
 {	
	var phoneErrorStatus = false;
	if ( iCountryCode == "" ) {
		errorFields += "\n"+"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Phone.CountryCodeRequired")%>";
		phoneErrorStatus = true;

	}
	else {
		if ( iCountryCode.length < 3 ) {
			errorFields += "\n"+"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Phone.CountryCodeSize")%>";
			phoneErrorStatus = true;
		}
		else {
			checkChar(iCountryCode);
		}

	}
	if ( iAreaCode == "" ) {
		errorFields += "\n"+"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Phone.AreaCodeRequired")%>";
		phoneErrorStatus = true;

	}
	else {
		if ( iAreaCode.length < 3 ) {
			errorFields += "\n"+"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Phone.AreaCodeSize")%>";
			phoneErrorStatus = true;
		}
		else {
			checkChar(iAreaCode);
		}

	}

	if ( iNumber == "" ) {
		errorFields += "\n"+"Number is a required field";
		phoneErrorStatus = true;

	}
	else {
		if ( iNumber.length < 7 ) {
			errorFields += "\n"+"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Phone.NumberRequired")%>";
			phoneErrorStatus = true;
		}
		else {
			checkChar(iNumber);
		}

	}

	if ( iExtension != "" ) {
		checkChar(iExtension);
	}

	
	function checkChar(iValue)
	  {	
		var valid = "0123456789 ";  

	 	for (var i=0; i < iValue.length; i++) 
  		{
   			temp1 = "" + iValue.substring(i, i+1);
   			if (valid.indexOf(temp1) == "-1") 
     				{
					errorFields += "\n"+"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Phone.InvalidPhoneNumber")%>";
					phoneErrorStatus = true;
					break;
     				}
 		}
	
	  }

	if ( phoneErrorStatus ==true ) 
	{
	     errorStatus = true;
	}
}//End of checkPhoneGeneral


}// end of validate()

</SCRIPT>