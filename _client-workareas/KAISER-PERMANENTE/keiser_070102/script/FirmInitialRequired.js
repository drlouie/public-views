<Script language="JavaScript">



function validateForm(theForm)
 {	

var errorStatus = false;
var errorFields ="";
  if(theForm.TaxID.value == "")
   {
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.TaxIDRequired")%>'+'\n';
	errorStatus = true;
   }	
  else
   {
   	checkInitialSetup(theForm.TaxID.name,theForm.TaxID.value)
   }	   
  if(theForm.FirmName.value == "")
   {
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.FirmNameRequired")%>'+'\n';
	errorStatus = true;			
   }
  else
   {
	checkInitialSetup(theForm.FirmName.name,theForm.FirmName.value);
   }
   
  /*
  if(theForm.Location.value == "")
   {
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.LocationRequired")%>'+'\n';
	errorStatus = true;			
   }
  else
   {
	checkInitialSetup(theForm.Location.name,theForm.Location.value)
   }
   */
   
if(theForm.Location.value != "")
	checkInitialSetup(theForm.Location.name,theForm.Location.value)
     
if(theForm.Line1.value == "")
   {
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.Line1Required")%>'+'\n';
	errorStatus = true;	
   }
else
   {
	checkInitialSetup(theForm.Line1.name,theForm.Line1.value);
   }
if(theForm.Line2.value != "")
	{
		checkInitialSetup(theForm.Line2.name,theForm.Line2.value);
	}
if(theForm.Line3.value != "")
	{
		checkInitialSetup(theForm.Line3.name,theForm.Line3.value);
	}
if(theForm.City.value == "")
   {
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.CityRequired")%>'+'\n';
	errorStatus = true;	
   }
else
   {
	checkInitialSetup(theForm.City.name,theForm.City.value);
   }
if(theForm.County.value != "")
	{
		checkInitialSetup(theForm.County.name,theForm.County.value);
	}
if(theForm.Province.value != "")
	{
		checkInitialSetup(theForm.Province.name,theForm.Province.value);
	}
if(theForm.MailStop.value != "")
	{
		checkInitialSetup(theForm.MailStop.name,theForm.MailStop.value);
	}






//Included by Sathish
	var validZipValues = "0123456789";

	var countryvalue = theForm.Country.value;
	var zipvalue = theForm.Zip.value;

	//Included to check state, zip validation
	if ( countryvalue != "" ) {

		if ( countryvalue == "USA" || countryvalue == "CAN" ) {

			if ( theForm.State.value == "" ) {
				errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.StateRequired")%>'+'\n';
				errorStatus = true;
				
			}
			else {

				if ( countryvalue == "USA" )
					checkState (theForm.State.value);
				else if ( countryvalue == "CAN" )
					checkCanadianState (theForm.State.value);

			}

			if ( theForm.Zip.value == "" ) {
				errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipRequired")%>'+'\n';
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
			errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.StateNotValid")%>'+'\n';
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
			errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.StateNotValid")%>'+'\n';
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
						errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipFormatUSA")%>'+'\n';
						errorStatus = true;
						theForm.Zip.focus();
						return false;
					}
					else {
						errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipDigitsUSA")%>'+'\n';
						errorStatus = true;
						theForm.Zip.focus();
						return false;
					}
				}
				else if ( zipvalue.length == 5 )
					checkZip( zipvalue );
				
			}


			if (country == "CAN" && zipvalue.length > 0 && zipvalue.length!=6) {
				errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipCanada")%>'+'\n';
				errorStatus = true;
				theForm.Zip.focus();
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
					errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipInvalid")%>'+'\n';
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
			errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipFormatInvalid")%>'+'\n';
			errorStatus = true;
			theForm.Zip.focus();
			return false;
		}


		for (var i=0; i < zipFour.length; i++) {
			temp = "" + zipFour.substring(i, i+1);
				if (validZipValues.indexOf(temp) == "-1") {
					errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipInvalid")%>'+'\n';
					errorStatus = true;
					theForm.Zip.focus();
					return false;
				}
		}

		for (var i=0; i < zipFive.length; i++) {
			temp = "" + zipFive.substring(i, i+1);
				if (validZipValues.indexOf(temp) == "-1") {
					errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipInvalid")%>'+'\n';
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
					errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipInvalid")%>'+'\n';
					errorStatus = true;
					theForm.Zip.focus();
					return false;
				}
		}
	}



if (errorStatus==true)
   {
		alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.ErrorMessagePrefix")%>'+'\n'+ errorFields );
	return false;
   }
   else
   		return true;



function checkInitialSetup(name,value)
 {

var TaxID = "1234567890"
var FirmName = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'& ";	
var Line1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890, ";
var City = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
var MailStop = "#1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
var valid = "";
if(name == "TaxID" || name =="Zip")
	{	
		valid = TaxID;
	}
else if(name == "FirmName")
	{
		valid = FirmName;
	}
else if(name == "Line1" || name =="Line2" || name =="Line3")
	{
		valid = Line1;
	}
else if(name == "City" || name =="Province" || name =="County" || name =="Location")
	{
		valid = City;
	}
else if(name == "MailStop")  
	{
		valid = MailStop;
	}
if(name == "TaxID" && value.length < 9)
	{
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.TaxIDDigits")%>'+'\n';
	errorStatus = true;
     	}
if(name == "Zip" && value.length < 5)
	{
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.Zip5Digits")%>'+'\n';
	errorStatus = true;
     	}

if(valid.length > 1)
{
 for (var i=0; i < value.length; i++) 
  {
   temp = "" + value.substring(i, i+1);
   if (valid.indexOf(temp) == "-1") 
     {
       errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+name+" \n";
       errorStatus=true;      
       break;
     }
  }
 }
}

}//End of validateForm function


</Script>