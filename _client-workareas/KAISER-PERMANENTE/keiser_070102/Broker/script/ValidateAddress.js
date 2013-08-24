
<Script language="JavaScript">



function go(loc) {
	window.location.href = loc;
}


//Loads the current date for date field

function defaultValue() {
	var dt = new Date();
	var month = dt.getMonth();
	var date = dt.getDate();
	var year = dt.getYear();


	if ( OrgEffDate == "" || OrgEffDate == "null" )
	 	document.AddTypeForm.AddressEffectiveDate.value =  (month+1) + "/" +date+ "/" +year;
	else
		document.AddTypeForm.AddressEffectiveDate.value = OrgEffDate;

}


//Function clears all the values on changing the Address Type

function validate( theForm ) {

	var clearFlag = 0;
	var line1value = theForm.AddressLine1.value;
	var line2value = theForm.AddressLine2.value;
	var line3value = theForm.AddressLine3.value;
	var mailstop = theForm.MailStop.value;
	var cityvalue = theForm.City.value;
	
	theForm.State.disabled = false;
	theForm.Country.disabled = false;
	theForm.AddressEffectiveDate.disabled = false;
	
	var statevalue = theForm.State.value;
	var zipvalue = theForm.Zip.value;	
	var datevalue = theForm.AddressEffectiveDate.value;
	var countryvalue = theForm.Country.value;
	var countyvalue = theForm.County.value;
	var provincevalue = theForm.Province.value;

	var valid = "1234567890"

	var invalid = "0123456789$";

	var validdate = "0123456789/";
	var slashcount = 0;


	var dt = new Date();
	var month = dt.getMonth();
	var date = dt.getDate();
	var year = dt.getYear();


	var errorStatus = false;
	var errorFields ="";
	var errorEntry = "";

	if (line1value == "" && line2value == "" && line3value == "" && mailstop == "" && 
		cityvalue == "" && statevalue == "" && zipvalue == "" && 
			countyvalue == "" && provincevalue == "" )  {

		errorStatus = false;

	}
	else  {


		if (line1value == "" ) {
 	      	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.Line1Required")%>'+"\n";
			errorStatus = true;
		}
		if (cityvalue == "" ) {
  	     	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.CityRequired")%>'+"\n";
			errorStatus = true;
		}
		else {
			checkCity ( theForm.City.value);
		}


		if ( countryvalue != "" ) {

			if ( countryvalue == "USA" || countryvalue == "CAN" ) {

				if ( theForm.State.value == "" ) {
			       	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.StateRequired")%>'+"\n";
					errorStatus = true;
				}
				else {

					if ( countryvalue == "USA" )
						checkState (theForm.State.value);
					else if ( countryvalue == "CAN" )
						checkCanadianState (theForm.State.value);
				}

				if ( theForm.Zip.value == "" ) {
			       	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipRequired")%>'+"\n";
					errorStatus = true;
				}
				else {
					checkCountry( theForm.Country.value );
				}
			}
			else {
				if ( zipvalue != "" ) {
					//checkForValidZip( zipvalue );
				}

			}

		}
		if (datevalue != "" ) {
			var effDtSts = checkDateValidation (theForm.AddressEffectiveDate.name,theForm.AddressEffectiveDate.value);
	
			if ( !effDtSts ) {
		       	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Address.EffDateNotValid")%>'+"\n";
				errorStatus = true;
			}
			
		}
		if (countyvalue != "" ) {
			checkCounty (theForm.County.value);
		}
		if (provincevalue != "" ) {
			checkProvince (theForm.Province.value);
		}
	
	} // else 


	if (errorStatus == true){
		alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.ErrorMessagePrefix")%>' + "\n" + errorFields);
		return false;
	}
	else
		return true;

 

	function checkZip ( zip ) {
		
		var zipvalue = zip;

		for (var i=0; i < zipvalue.length; i++) {
			temp = "" + zipvalue.substring(i, i+1);
				if (valid.indexOf(temp) == "-1") {
					errorFields+= '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipInvalid")%>' + "\n";
					errorStatus = true;
					theForm.Zip.focus();
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
			errorFields+= '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipFormatInvalid")%>' + "\n";
			errorStatus = true;
			theForm.Zip.focus();
			return false;
		}


		for (var i=0; i < zipFour.length; i++) {
			temp = "" + zipFour.substring(i, i+1);
				if (valid.indexOf(temp) == "-1") {
					errorFields+= '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipInvalid")%>' + "\n";
					errorStatus = true;
					theForm.Zip.focus();
					return false;
				}
		}

		for (var i=0; i < zipFive.length; i++) {
			temp = "" + zipFive.substring(i, i+1);
				if (valid.indexOf(temp) == "-1") {
					errorFields+= '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipInvalid")%>' + "\n";
					errorStatus = true;
					theForm.Zip.focus();
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
					errorFields+= '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipInvalid")%>' + "\n";
					errorStatus = true;
					theForm.Zip.focus();
					return false;
				}
		}
	}


	function checkState ( state ) {
		
		var found = false;
		var state = state;
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
			errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.StateNotValid")%>' + "\n";
			errorStatus = true;	
		}

	}

	function checkCanadianState ( state ) {
		
		var found = false;
		var state = state;
		state = state.toUpperCase();	
		for(var i = 0 ; i < canadianStates.length ; i++)
		{	
			if(state == canadianStates[i])
				{					
					found = true;		
					break;
				}
			else
				continue;
		}
		if(found == false)
		{
			errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.StateNotValid")%>' + "\n";
			errorStatus = true;	
		}

	}


	function checkCountry ( country ) {
		
		var countryvalue = country;
		var zipvalue = theForm.Zip.value;

			if (country == "USA" && zipvalue.length > 0 ) {
			
				if ( zipvalue.length != 5 ) {
					
					if ( zipvalue.length == 10 ) {
						checkZip5Plus4( zipvalue );
					}
					else if ( zipvalue.length == 9 ) {
						errorFields+= '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipFormatUSA")%>' + "\n";
						errorStatus = true;
						theForm.Zip.focus();
						return false;
					}
					else {
						errorFields+= '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipDigitsUSA")%>' + "\n";
						errorStatus = true;
						theForm.Zip.focus();
						return false;
					}
				}
				else if ( zipvalue.length == 5 )
					checkZip( zipvalue );
				
			}


			if (country == "CAN" && zipvalue.length > 0 && zipvalue.length!=6) {
				errorFields+= '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipCanada")%>' + "\n";
				errorStatus = true;
				theForm.Zip.focus();
				return false;
			}
			else if ( country == "CAN" && zipvalue.length == 6 )
				checkCanZip( zipvalue );

	}


	function checkCity ( city ) {
		

		var cityvalue = city;

		for (var i=0; i < cityvalue.length; i++) {
			temp = "" + cityvalue.substring(i, i+1);
			if (invalid.indexOf(temp) != "-1") {
				errorFields += '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.CityInvalid")%>' + "\n";
				errorStatus = true;
				theForm.City.focus();
				return false;
			}
		}
	}

	function checkDate ( date ) {
		var dateval = date;
		
		for (var i=0; i < dateval.length; i++) {
			temp = "" + dateval.substring(i, i+1);
			if (temp == "/") 
				slashcount++;
			if (validdate.indexOf(temp) == "-1") {
				errorFields += '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Address.EffDateNotValid")%>' + "\n";
				errorStatus = true;
				theForm.AddressEffectiveDate.focus();
				return false;
			}
		}
	}

	function checkCounty ( county ) {
		var countyvalue = county;
	
		for (var i=0; i < countyvalue.length; i++) {
			temp = "" + countyvalue.substring(i, i+1);
			if (invalid.indexOf(temp) != "-1") {
				errorFields += '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.CountyInvalid")%>' + "\n";
				errorStatus = true;
				theForm.County.focus();
				return false;
			}
		}
	}

	function checkProvince ( province ) {
		var provincevalue = province;

			for (var i=0; i < provincevalue.length; i++) {
			temp = "" + provincevalue.substring(i, i+1);
			if (invalid.indexOf(temp) != "-1") {
				errorFields += '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ProvinceInvalid")%>' + "\n";
				errorStatus = true;
				theForm.Province.focus();
				clearFlag = 1;
				return false;
			}
		}
	}
	
	
	function checkDateValidation(datename, datevalue){


		var dateStatus = true;
		
	 	var validdate = "1234567890/";
         	var err=0
         	var psj=0;
	      var a="";

         	a=datevalue;
		
	 	if (a.length != 10) {
			//errorFields += "\n" +  "Invalid "+datename;
			//errorStatus = true;
			dateStatus = false;
		}
		else {
			for (var i=0; i < a.length; i++) {
			temp = "" + a.substring(i, i+1);
				if (validdate.indexOf(temp) == "-1") {
					//errorFields += "\n" +  "Invalid Characters in "+datename;
					//errorStatus = true;
					dateStatus = false;
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
			//errorFields += "\n" + datename + "'s month invalid";
			//errorStatus = true;
			dateStatus = false;
		 }
         	 if (c != '/' || e != '/' ) {
			//errorFields += "\n" + "Invalid "+datename;
			//errorStatus = true;
			dateStatus = false;
		 }
         	 if (b<1 || b>31) {
			//errorFields += "\n" + datename + "'s date invalid";
			//errorStatus = true;
			dateStatus = false;
		 }
         	 if (f<1900 || f>4000) {
			//errorFields += "\n" + datename + "'s year invalid";
			//errorStatus = true;
			dateStatus = false;
		 }

         	 // months with 30 days
         	 if (d==4 || d==6 || d==9 || d==11){
             	if (b==31) {
				//errorFields += "\n" + "Only 30 days are there in the month of "+datename;
				//errorStatus = true;
				dateStatus = false;
			}
         	 }

	      // february, leap year
         	 if (d==2){
              	// feb
              	var g=parseInt(f/4)
              	if (isNaN(g)) {
				//errorFields += "\n" + "Month does not match for the leap year in "+datename;
				//errorStatus = true;
					dateStatus = false;

	            }

             	if (b>29) {
				//errorFields += "\n" + "Month and Date do not match in "+datename;
				//errorStatus = true;
				dateStatus = false;
		 	}

             	if (b==29 && ((f/4)!=parseInt(f/4))) {
				//errorFields += "\n" + "Invalid "+datename;
				//errorStatus = true;
				dateStatus = false;
	       	}
		 }
		 
		 if ( dateStatus )
		 	return true;
		 else
		 	return false;

	} // end of checkValidation()
	

}



</Script>