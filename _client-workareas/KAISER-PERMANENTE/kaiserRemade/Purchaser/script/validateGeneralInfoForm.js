<SCRIPT Language="JavaScript1.1">
function validateGeneralForm(theForm)
 {	 
	var errorStatus = false;
	var errorFields ="";
	errorStatus = checkCategoryInGeneralListBox(theForm);
	if(errorStatus)
		return false;	
      beforeSaveGeneral(theForm);
     	enableGeneralform(theForm);
	theForm.StatusDate.disabled = false;
      checkPhoneInGeneral("000",theForm.Area.value,theForm.Number.value,theForm.Ext.value);
  if(theForm.IRSTaxID.value == "")
   {
	errorFields+="<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.TaxIdRequired")%>"+"\n";
	errorStatus = true;
   }	
  else
   {
   	checkCompleteSetup(theForm.IRSTaxID.name,theForm.IRSTaxID.value);
   }	   
 /*  if(theForm.FName.value == "")
   {
	errorFields+="<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Name.FirstNameMissing")%>"+"\n";
	errorStatus	= true;			
   }
  else
   {
	checkCompleteSetup(theForm.FName.name,theForm.FName.value);
   }*/
 	if(theForm.FName.value != "")
   {
		checkCompleteSetup(theForm.FName.name,theForm.FName.value);
   
   		if(theForm.LName.value == "")
   		{
			errorFields+="<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Name.LastNameMissing")%>"+"\n";
 			errorStatus = true;		
   		}
  		else
   		{
			checkCompleteSetup(theForm.LName.name,theForm.LName.value);
   		}  
   		if(theForm.Honor.value != "")
   		{
			checkCompleteSetup(theForm.Honor.name,theForm.Honor.value);
   		}
		if(theForm.MName.value != "")
   		{
			checkCompleteSetup(theForm.MName.name,theForm.MName.value);
   		}
		if(theForm.Suffix.value != "")
   		{
			checkCompleteSetup(theForm.Suffix.name,theForm.Suffix.value);
   		}
		if(theForm.Title.value != "")
   		{
			checkCompleteSetup(theForm.Title.name,theForm.Title.value);
   		}

   }
 if(theForm.Line1.value == "")
   {
	errorFields+="<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.Line1Required")%>"+"\n";
	errorStatus	= true;	
   }
  else
   {
	checkCompleteSetup(theForm.Line1.name,theForm.Line1.value);
   }

if(theForm.Line2.value != "")
   {
	checkCompleteSetup(theForm.Line2.name,theForm.Line2.value);
   }
if(theForm.Line3.value != "")
   {
	checkCompleteSetup(theForm.Line3.name,theForm.Line3.value);
   }
if(theForm.MailStop.value != "")
   {
	checkCompleteSetup(theForm.MailStop.name,theForm.MailStop.value);
   }

  if(theForm.City.value == "")
   {
	errorFields+="<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.CityRequired")%>"+"\n";
	errorStatus	= true;	
   }
  else
   {
	checkCompleteSetup(theForm.City.name,theForm.City.value);
   }
  if(theForm.State.value.toUpperCase() == "" && ( theForm.Country.value.toUpperCase() == "CAN" || theForm.Country.value.toUpperCase() == "USA" ) )
   {
	errorFields+="<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.StateRequired")%>"+"\n";
	errorStatus	="true"	
   }
  else if ( theForm.Country.value.toUpperCase() == "CAN" || theForm.Country.value.toUpperCase() == "USA"  )
   {	
	var found = false;
	var state = theForm.State.value;
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
	errorFields+="Enter Valid State \n";
	errorStatus = true;	
	theForm.State.focus();
	}
   }
  if(theForm.Zip.value == "")
   {
	errorFields+="<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipRequired")%>"+"\n";
	errorStatus	=true;	
   }
  else
   {
   //	checkCompleteSetup(theForm.Zip.name,theForm.Zip.value);
   }
   if(theForm.Country.value == "" )
   {
	errorFields+="<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.CountryRequired")%>"+"\n";
	errorStatus	=true;
   }
   else
   {
	checkCountry(theForm);
   }	

  if(theForm.OrigEffectiveDate.value =="")
   {
	errorFields+="<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.EffDtRequired")%>"+"\n";
	errorStatus = true;
   }
  else
   {
	checkDateValidation(theForm.OrigEffectiveDate.name,theForm.OrigEffectiveDate.value);
   }
   if(theForm.TerminationDate.value != "" )
   {
	checkDateValidation(theForm.TerminationDate.name,theForm.TerminationDate.value);
   }
   if (errorStatus==true)
   {
	alert( errorFields +  "\n" + "   Please enter those information");
     	return false;
   }
   else
   { 
   		return true;
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



function checkCompleteSetup(name,value)
{
var TaxID = "1234567890";
var Name = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";	
var Line1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890, ";
var City = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
var MailStop = "#1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
var EffDate = "1234567890/";
var EMail = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@1234567890.";
var ZipCanada = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
var ZipUSA = "1234567890";
var valid = "";
if(name == "Zip-CAN" )
{
	valid = ZipCanada;
}
else if( name == "Zip-USA" )
{
	valid = ZipUSA;
}
else if(name == "IRSTaxID" )
	{	
		valid = TaxID;
	}
else if(name == "Honor" ||  name == "FName" || name == "MName" || name == "LName" || name == "Suffix" || name == "Title" || name == "FamiliarName" )
	{
		valid = Name;
	}
else if(name == "Line1" || name == "Line2" || name == "Line3")
	{
		valid = Line1;
	}
else if(name == "City" || name == "Province" || name == "County" || name == "Location")
	{
		valid = City;
	}
else if(name == "MailStop")  
	{
		valid = MailStop;
	}
else if(name == "OrigEffectiveDate")
	{
		valid = EffDate;
	}
else if(name == "TerminationDate" )
       {
		valid = EffDate;
       }
else if(name == "EMail")
	{
		valid = EMail;
	}
if(name == "IRSTaxID" && value.length < 9)
	{
	errorFields+=name+" should be 9 digits \n";	
	errorStatus = true;
     	}

if (name.substring(1,3) == "Zip")
	name = "Zip";
if(valid.length > 1)
{
 for (var i=0; i < value.length; i++) 
  {
   temp = "" + value.substring(i, i+1);
   if (valid.indexOf(temp) == "-1") 
     {
       errorFields+="Invalid characters in "+name+" \n";
       errorStatus=true;      
       break;
     }
  }
 }
}//End of checkCompleteSetup

function checkCountry(theForm)
{
	var found = false;
	var country = theForm.Country.value;
	country = country.toUpperCase();
	var name = theForm.Zip.name;
	for(var i = 0 ; i < countries.length ; i++)
	{	
		if(country == countries[i])
		{
			found = true;
			break;
		}
	}
	if( found == true )
	{
            if(theForm.Country.value.toUpperCase() == "CAN" )
		 	checkCompleteSetup("Zip-CAN",theForm.Zip.value);
		else if (theForm.Country.value.toUpperCase() == "USA" )
		 	checkCompleteSetup("Zip-USA",theForm.Zip.value);

		if( theForm.Zip.value.length < 5 && theForm.Country.value.toUpperCase()=="USA")
		{
			errorFields+=name+"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipSize1")%>"+"\n";	
			errorStatus = true;
     		}
		if(  theForm.Zip.value.length > 5 && theForm.Country.value.toUpperCase() == "USA" )
		{	
		
	  		if (theForm.Zip.value.length < 9 )
	 		 {
				errorFields+=name+"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipSize2")%>"+"\n";
  				errorStatus = true;
	  		 }
		}
		if( theForm.Zip.value.length != 6 &&   theForm.Country.value.toUpperCase()=="CAN")
		{
			errorFields+=name+"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.ZipSize3")%>"+"\n";	
			errorStatus = true;
		}

	}
	else
	{
		errorStatus = true;
		errorFields = "Country is invalid";
	}
}//End of checkCountry()

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
		errorFields += "\n"+"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Phone.NumberRequired")%>";
		phoneErrorStatus = true;

	}
	else {
		if ( iNumber.length < 7 ) {
			errorFields += "\n"+"<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Phone.NumberSize")%>";
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
}//End of validateForm function
function enableGeneralform(theForm)
{
	theForm.OrigEffectiveDate.disabled = false ;
	theForm.TerminationDate.disabled = false ;
	theForm.Status.disabled = false ;
	theForm.StatusDate.disabled = false ;
	theForm.RegionDivision.disabled = false ;
	theForm.Size.disabled = false ;
	theForm.IRSTaxID.disabled = false;
      theForm.Category.Focus = "";
	theForm.CommissionCategoryList.disabled = false;
	if(theForm.Size.value == "LGS")
	{
		for(var i=0; i<	theForm.Required.length; i++)
		{
     			theForm.Required[i].disabled = false;
			theForm.Received[i].disabled = false;
		}
	}
	else
	{
		theForm.Required.disabled = false;
		theForm.Received.disabled = false;
	}
      theForm.Line1.disabled = false;
	theForm.Line2.disabled = false;
	theForm.Line3.disabled = false;
	theForm.City.disabled = false;
	theForm.MailStop.disabled = false;
	theForm.State.disabled = false;	
	theForm.Zip.disabled = false;
	theForm.Country.disabled = false;
	theForm.Area.disabled = false;
	theForm.Number.disabled = false;
	theForm.Ext.disabled = false;
	theForm.Honor.disabled = false;
	theForm.FName.disabled = false;
	theForm.MName.disabled = false;
	theForm.LName.disabled = false;
	theForm.Suffix.disabled = false;
	theForm.Title.disabled = false;
}
function beforeSaveGeneral(theForm)
{
      theForm.SelectedAction.value = "Save";
}
function checkCategoryInGeneralListBox(theForm) 
{
	
	var popList = theForm.CommissionCategoryList;
	for( var m=0; m < popList.length; m++ )
      {
		var temp;
		var values = theForm.CommissionCategoryList.options[m].value;
		var count = new Array();
		var tokenizedData = new Array();
		var j = 0;
		for (var i=0; i < values.length; i++)
      	{
			temp = "" + values.substring(i, i+1);
			if ( temp == ("," ) )
                	{
				count[j] = i;
				j++;
			}
		
		}
		count[j] = values.length;
		var k = 0;
		for ( i=0; i < count.length; i++ ) 
        	{
			tokenizedData[i] = values.substring( k, count[i] );
			k = count[i]+1;
		}
            
      	if ( tokenizedData[3] == "C")
		{
			if(tokenizedData[0] > 100 && theForm.Category.value == "Pre-Broker")
			{
				alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.EnterValidCategory")%>");
  				return true;
			}
			else if(tokenizedData[0] < 100  && theForm.Category.value == "Post-Broker")
			{
				alert("<%=org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.EnterValidCategory")%>");
				return true;
			}
		}
   	}
} 

</SCRIPT>



