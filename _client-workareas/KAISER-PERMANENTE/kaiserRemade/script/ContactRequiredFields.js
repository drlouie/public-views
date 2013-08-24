<Script language="JavaScript">


function validateContactForm(theForm)
 {	
var errorStatus = false;
var errorFields ='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.ErrorMessagePrefix")%>'+'\n';
if(theForm.firstName.value == "")
   {
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Name.FirstNameRequired")%>'+'\n';
	errorStatus	= true;			
   }  else
   {
	checkFirstName(theForm.firstName.value);
   }
  if(theForm.lastName.value == "")
   {
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Name.LastNameRequired")%>'+'\n';
 	errorStatus = true;		
   }
  else
   {
	checkLastName(theForm.lastName.value);
   }  

if (theForm.honorific.value != "")
	checkHonor(theForm.honorific.value);

if (theForm.middleName.value != "")
	checkMiddleName(theForm.middleName.value);

if (theForm.suffix.value != "")
	checkSuffix(theForm.suffix.value);

if (theForm.title.value != "")
	checkTitle(theForm.title.value);

if (theForm.familiarName.value != "")
	checkFamiliarName(theForm.familiarName.value);


if(theForm.email.value !="")
   {
	 isEmail(theForm.email)
   }


if ((errorStatus == true))
{
	alert(errorFields);
	return false;
}
else
	return true;


function checkFirstName(field)
 {
  var valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
  

for (var i=0; i < field.length; i++) 
 {
  temp = "" + field.substring(i, i+1);
  if (valid.indexOf(temp) == "-1") 
    {
      errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'First Name \n';
	errorStatus = true;
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
      errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'Last Name \n';
	errorStatus = true;
      break;
    }
 }
 }//End of checkFirstLast function
// Check for email address: look for [@] and [.]
function isEmail(elm) {
    if (elm.value.indexOf("@") + "" != "-1" &&
        elm.value.indexOf(".") + "" != "-1" && elm.value != "") 
        return true;
    else{ 
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+'Email \n';
       errorStatus=true;
 	};
}
function checkMiddleName(field)
{
 var valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
  
for (var i=0; i < field.length; i++)
 {
  temp = "" + field.substring(i, i+1);
  if (valid.indexOf(temp) == "-1") 
    {
      errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'Middle Name \n';
	errorStatus = true;
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
      errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'Honor\n';
	errorStatus = true;
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
      errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'Suffix\n';
	errorStatus = true;
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
      errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'Familiar Name \n';
	errorStatus = true;
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
      errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+'Title\n';
	errorStatus = true;
      break;
    }
 } 
} //End of title function


}//End of validateForm function

</Script>