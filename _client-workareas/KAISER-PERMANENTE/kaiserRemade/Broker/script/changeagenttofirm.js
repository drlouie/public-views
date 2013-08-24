function validateForm(theForm)
 {	
var errorStatus = false;
var errorFields ="Please correct the following error(s)\n";

  if(document.agenttofirm.taxId.value == "")
   {
	errorFields+="Tax ID is a required field \n";
	errorStatus = true;
   }	
  else
   {
   	checkTaxID(document.agenttofirm.taxId.value);
   }

if(document.agenttofirm.firmName.value == "")
   {
	errorFields+="Firm Name is a required field\n";
	errorStatus	= true;			
   }  else
   {
	checkFirmName(document.agenttofirm.firmName.value);
   }
  if(document.agenttofirm.locName.value != "")
   {
   
   /*
	errorFields+="Location Name is a required field\n";
 	errorStatus = true;		
   }
  else
   {
   */
   
	checkLocName(document.agenttofirm.locName.value);
   }  

  if(document.agenttofirm.businessType.value == "")
   {
	errorFields+="Business Type is a required field\n";
 	errorStatus = true;		
   }


if ( errorFields == true )
{
	alert(errorFields);
	return false;
}
else
	return true;




function checkTaxID(TaxID)
 {
   var checkOK = "0123456789";
   var checkStr = TaxID;
   var allValid = true;
   var decPoints = 0;
   var allNum = "";
   for (i = 0;  i < checkStr.length;  i++)
    {
     ch = checkStr.charAt(i);
     for (j = 0;  j < checkOK.length;  j++)
     if (ch == checkOK.charAt(j))
     break;
     if (j == checkOK.length)
      {
      	allValid = false;
      	break;
      }
     allNum += ch;
     }
    if (!allValid)
     {
        errorFields+="Tax ID should contain only digits \n";
    	document.agenttofirm.taxId.focus();
    	errorStatus = true;
     }
	
    if (theForm.taxId.value.length<9)
     {
	errorFields+="Tax ID should be 9 digits \n";
	document.agenttofirm.taxId.focus();
	errorStatus = true;
     }
		
 }//End of checkTaxID function


function checkFirmName(field)
 {
  var valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
  

for (var i=0; i < field.length; i++) 
 {
  temp = "" + field.substring(i, i+1);
  if (valid.indexOf(temp) == "-1") 
    {
      errorFields+="Firm Name should contain alphabetic characters only \n";
	document.agenttofirm.firmName.focus();
      break;
    }
 }
 }//End of checkFirstName function

function checkLocName(field)
 {
  var valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
  

for (var i=0; i < field.length; i++) 
 {
  temp = "" + field.substring(i, i+1);
  if (valid.indexOf(temp) == "-1") 
    {
      errorFields+="Location Name should contain alphabetic characters only \n";
      document.agenttofirm.locName.focus();
	break;
    }
 }
 }//End of checkFirstLast function


}//End of validateForm function
function clearForm(form) {


          document.agenttofirm.taxId.value="";
	  document.agenttofirm.firmName.value ="";	
	  document.agenttofirm.locName.value ="";
	  document.agenttofirm.locName.value ="";	
          document.agenttofirm.businessType.value =""
          document.agenttofirm.taxId.text ="";
	  document.agenttofirm.firmName.text ="";	
	  document.agenttofirm.locName.text ="";
	  document.agenttofirm.locName.text ="";	
          document.agenttofirm.businessType.text =""
           
}
