<Script language="JavaScript">


function validateForm(theForm)
 {	
var errorStatus = false;
var errorFields ='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.ErrorMessagePrefix")%>'+'\n';

  if(document.firmtoagent.taxId.value == "")
   {
	errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.TaxIDRequired")%>'+'\n';
	document.firmtoagent.taxId.focus();
	errorStatus = true;
   }	
  else
   {
   	checkTaxID(document.firmtoagent.taxId.value);
   }

  if(document.firmtoagent.businessType.value == "")
   {
	errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.BusinessTypeRequired")%>'+'\n';
 	errorStatus = true;		
   }


if(document.firmtoagent.firstName.value == "")
   {
	errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Name.FirstNameRequired")%>'+'\n';
	//document.firmtoagent.firstName.focus();
	errorStatus	= true;			
   }  else
   {
	checkFirstName(theForm.firstName.value);
   }
  if(document.firmtoagent.lastName.value == "")
   {
	errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Name.LastNameRequired")%>'+'\n';
	//document.firmtoagent.lastName.focus();
 	errorStatus = true;		
   }
  else
   {
	checkLastName(theForm.lastName.value);
   }  

if (document.firmtoagent.honorific.value != "")
	checkHonor(firmtoagent.honorific.value);

if (document.firmtoagent.middleName.value != "")
	checkMiddleName(firmtoagent.middleName.value);

if (document.firmtoagent.suffix.value != "")
	checkSuffix(document.firmtoagent.suffix.value);

if (document.firmtoagent.title.value != "")
	checkTitle(document.firmtoagent.title.value);

if (document.firmtoagent.familiarName.value != "")
	checkFamiliarName(document.firmtoagent.familiarName.value);




   if ( errorStatus == true )
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
		errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'TaxID\n';
    	document.firmtoagent.taxId.focus();
    	errorStatus = true;
     }
	
    if (theForm.taxId.value.length<9)
     {
	errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.TaxIDDigits")%>'+'\n';
	document.firmtoagent.taxId.focus();
	errorStatus = true;
     }
		
 }//End of checkTaxID function


function checkFirstName(field)
 {
  var valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
  

for (var i=0; i < field.length; i++) 
 {
  temp = "" + field.substring(i, i+1);
  if (valid.indexOf(temp) == "-1") 
    {
		errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'First Name\n';
	//document.firmtoagent.firstName.focus();
      break;
    }
 }
 }//End of checkFirstName function

function checkLastName(field)
 {
  var valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
  

for (var i=0; i < field.length; i++) 
 {
  temp = "" + field.substring(i, i+1);
  if (valid.indexOf(temp) == "-1") 
    {
		errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'Last Name\n';
	//document.firmtoagent.lastName.focus();
      break;
    }
 }
 }//End of checkFirstLast function

function checkMiddleName(field)
{
 var valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
  
for (var i=0; i < field.length; i++)
 {
  temp = "" + field.substring(i, i+1);
  if (valid.indexOf(temp) == "-1") 
    {
		errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'Middle Name\n';
	//document.firmtoagent.middleName.focus();
      break;
    }
 } 
} //End of checkmiddle function

function checkHonor(field)
{
 var valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .";
  
for (var i=0; i < field.length; i++) 
 {
  temp = "" + field.substring(i, i+1);
  if (valid.indexOf(temp) == "-1") 
    {
		errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'Honor\n';
	//document.firmtoagent.honorific.focus();
      break;
    }
 } 
} //End of checkHonor function
function checkSuffix(field)
{
 var valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
  
for (var i=0; i < field.length; i++)
 {
  temp = "" + field.substring(i, i+1);
  if (valid.indexOf(temp) == "-1") 
    {
		errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'Suffix\n';
	//document.firmtoagent.suffix.focus();
      break;
    }
 } 
} //End of checkSuffix function
function checkFamiliarName(field)
{
 var valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
  
for (var i=0; i < field.length; i++)
 {
  temp = "" + field.substring(i, i+1);
  if (valid.indexOf(temp) == "-1") 
    {
		errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'Familiar Name\n';
	//document.firmtoagent.familiarName.focus();
      break;
    }
 } 
} //End of FamiliarName function
function checkTitle(field)
{
 var valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
  
for (var i=0; i < field.length; i++)
 {
  temp = "" + field.substring(i, i+1);
  if (valid.indexOf(temp) == "-1") 
    {
		errorFields +='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'Title\n';
	//document.firmtoagent.title.focus();
      break;
    }
 } 
} //End of title function


}//End of validateForm function
function clearForm(form) {


          document.firmtoagent.taxId.value="";
	   document.firmtoagent.honorific.value ="";	
	   document.firmtoagent.firstName.value= "";
          document.firmtoagent.middleName.value= "";	
          document.firmtoagent.lastName.value =  "";
          document.firmtoagent.title.value= "";
	   document.firmtoagent.suffix.value="";	
          document.firmtoagent.familiarName.value=""  ;     
	  document.firmtoagent.businessType.value =""	
          document.firmtoagent.taxId.text="";
	   document.firmtoagent.honorific.text ="";	
	   document.firmtoagent.firstName.text= "";
          document.firmtoagent.middleName.text= "";	
          document.firmtoagent.lastName.text =  "";
          document.firmtoagent.title.text= "";
	   document.firmtoagent.suffix.text="";	
          document.firmtoagent.familiarName.text=""  ;  
         document.firmtoagent.businessType.text =""  


}


</Script>