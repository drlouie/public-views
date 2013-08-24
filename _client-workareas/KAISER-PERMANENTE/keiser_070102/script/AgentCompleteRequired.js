function validateForm(theForm)
 {	
alert("inside");
theForm.Status.disabled = false;			
theForm.StatusReason.disabled = false;
theForm.BrokerCategory.disabled = false;
theForm.BrokerCategoryYear.disabled = false;
theForm.Country.disabled = false;

var errorStatus = false;
var errorFields ="";
  if(theForm.TaxID.value == "")
   {
	errorFields+="Tax ID Missing \n";
	errorStatus = true;
   }	
  else
   {
   	checkCompleteSetup(theForm.TaxID.name,theForm.TaxID.value);
   }	   
  if(theForm.FName.value == "")
   {
	errorFields+="First Name Missing \n";
	errorStatus	= true;			
   }
  else
   {
	checkCompleteSetup(theForm.FName.name,theForm.FName.value);
   }
  if(theForm.LName.value == "")
   {
	errorFields+="Last Name Missing \n";
 	errorStatus = true;		
   }
  else
   {
	checkCompleteSetup(theForm.LName.name,theForm.LName.value);
   }  
  if(theForm.Line1.value == "")
   {
	errorFields+="Line1 Missing\n";
	errorStatus	= true;	
   }
  else
   {
	checkCompleteSetup(theForm.Line1.name,theForm.Line1.value);
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
if(theForm.FamiliarName.value != "")
   {
	checkCompleteSetup(theForm.FamiliarName.name,theForm.FamiliarName.value);
   }

if(theForm.Line2.value != "")
   {
	checkCompleteSetup(theForm.Line2.name,theForm.Line2.value);
   }
if(theForm.Line3.value != "")
   {
	checkCompleteSetup(theForm.Line3.name,theForm.Line3.value);
   }
if(theForm.Province.value != "")
   {
	checkCompleteSetup(theForm.Province.name,theForm.Province.value);
   }
if(theForm.County.value != "")
   {
	checkCompleteSetup(theForm.County.name,theForm.County.value);
   }
if(theForm.MailStop.value != "")
   {
	checkCompleteSetup(theForm.MailStop.name,theForm.MailStop.value);
   }

  if(theForm.City.value == "")
   {
	errorFields+="City Missing \n";
	errorStatus	= true;	
   }
  else
   {
	checkCompleteSetup(theForm.City.name,theForm.City.value);
   }
  if(theForm.State.value == "")
   {
	errorFields+="State Missing \n";
	errorStatus	="true"	
   }
  else
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
	errorFields+="Zip Missing \n";
	errorStatus	=true;	
   }
  else
   {
   	checkCompleteSetup(theForm.Zip.name,theForm.Zip.value);
   }
 if(theForm.EMail.value !="")
   {
	checkCompleteSetup(theForm.EMail.name,theForm.EMail.value);
	checkEmail(theForm.EMail.value);
   }
  if(theForm.EffDate.value =="")
   {
	errorFields+="Effective Date Missing \n";
	errorStatus = true;
   }
  else
   {
	
	checkCompleteSetup(theForm.EffDate.name,theForm.EffDate.value);
	var sysDate = theForm.CurrentDate.value;	
	var jspDate = theForm.EffDate.value;	
	
     if(theForm.EffDateChanged.value != theForm.EffDate.value)
       {
	
	if(jspDate < sysDate)
	errorStatus = true;	
	errorFields+="Effective Date should should be greater than today's date \n";
       }       

   }

  if(theForm.PhoneList.options.length =="")
   {
	errorFields+="You should have atleast one phone no \n";
	errorStatus = true;
   }
  else
   {
	for(var i = 0 ; i <theForm.PhoneList.options.length ; i++)
          {
		theForm.PhoneNumbers.value+= theForm.PhoneList.options[i].value;
		theForm.PhoneNumbers.value+="%";
	  }
   }

for(var count = 0 ; count < category.length ; count++)
	{
		
		var both = category[count]+"-"+categoryYear[count];
		theForm.AllCategory.value+= both +"/"
	}

if (errorStatus==true)
   {
	alert( "Please correct the following error(s): "+"\n"+ errorFields );
     	return false;
   }
	

function checkCompleteSetup(name,value)
{

var TaxID = "1234567890";
var Name = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";	
var Line1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890, ";
var City = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
var MailStop = "#1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
var EffDate = "1234567890/";
var EMail = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@1234567890.";
var valid = "";
if(name == "TaxID" || name =="Zip")
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
else if(name == "EffDate")
	{
		valid = EffDate;
	}
else if(name == "EMail")
	{
		valid = EMail;
	}
if(name == "TaxID" && value.length < 9)
	{
	errorFields+=name+" should be 9 digits \n";	
	errorStatus = true;
     	}
if(name == "Zip" && value.length < 5)
	{
	errorFields+=name+" should be 5 digits \n";	
	errorStatus = true;
     	}

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

}

function checkEmail(email) 
 {
  invalidChars = " /:,;"
   for (i=0; i<invalidChars.length; i++) 
     {    
	badChar = invalidChars.charAt(i)
	if (email.indexOf(badChar,0) > -1) 
         {
	   errorFields+="Invalid characters in Email\n";
           errorStatus=true;
	 }
    }
  atPos = email.indexOf("@",1)	
  if (atPos == -1)
   {
  	errorFields+="Enter proper Email \n";
       errorStatus=true;
	return;
	
   }

  if (email.indexOf("@",atPos+1) != -1)
   {	
  	errorFields+="Enter proper Email  \n";
       errorStatus=true;
	return;
   }

  periodPos = email.indexOf(".",atPos)
  if (periodPos == -1)
   {	  
	errorFields+="Enter proper Email  \n";
        errorStatus=true;
	return;
   }

  if (periodPos+4 > email.length)	
    {	
       errorFields+="Enter proper Email  \n";
       errorStatus=true;

    } 
 }


}//End of validateForm function
