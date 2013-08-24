function validateForm(theForm)
 {	
 //alert("inside jfff validate");
var errorStatus = false;
var errorFields ="";
var todays = "";
if(document.Relationship.primaryRole.value  == "")
   {
	errorFields+="primaryRole is  Missing \n";
	errorStatus	= true;			
   }  
 
if(document.Relationship.secondaryBid.value  == "")
   {
	errorFields+="secondaryBid Missing \n";
	errorStatus	= true;			
   }  else
   {
	checkBrokerID(theForm.secondaryBid.value);
   }
if(document.Relationship.secondaryRole.value == "")
   {
	errorFields+="secondaryRole is  Missing \n";
	errorStatus	= true;			
   }  
  if(document.Relationship.effectiveDate.value  == "")
   {
	errorFields+="effectiveDate Missing \n";
 	errorStatus = true;		
   }else  
   {
          checkeffectiveDate(theForm.effectiveDate.value)  
	 
   }
	
  if(document.Relationship.endDate.value  == "")
   {
	errorFields+="endDate Missing \n";
 	errorStatus = true;		
   }else
   {
          checkendDate(theForm.endDate.value)  
 	compareDate(theForm.effectiveDate.value,theForm.endDate.value);
   }
if ((errorFields.length) > 0)
{
	alert(errorFields + "\n" + "Please enter the modifications");
	return false;
}
else
	return true;


function checkBrokerID(BrokerID)
 {
   var checkOK = "0123456789";
   var checkStr = BrokerID;
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
        errorFields+="BrokerID should contain only digits \n";
    	document.Relationship.secondaryBid.focus();
     }
		
 }//End of checkBrokerID function
function checkeffectiveDate(theDate) {
    var elmstr = theDate;
    if (elmstr.length != 10)
   	{
	   errorFields+="effectiveDate should be in mm/dd/yyyy format \n";
	  return false ;	
	}
		 
    for (var i = 0; i < elmstr.length; i++) {
        if ((i < 2 && i > -1) ||
            (i > 2 && i < 5) || 
            (i > 5 && i < 10)) {
            if (elmstr.charAt(i) < "0" || 
                elmstr.charAt(i) > "9") {
		errorFields+="effectiveDate should be in mm/dd/yyyy format \n";
		break;
		}
        }
        else if (elmstr.charAt(i) != "/") {
		errorFields+="effectiveDate should be in mm/dd/yyyy format \n";
		return false ;	
		}
    }
    return true;
}// is date
  
function checkendDate(theDate) {
    var elmstr = theDate;
    if (elmstr.length != 10)
   	{
	   errorFields+="endDate should be in mm/dd/yyyy format \n";
	  return false ;	
	}
		 
    for (var i = 0; i < elmstr.length; i++) {
        if ((i < 2 && i > -1) ||
            (i > 2 && i < 5) || 
            (i > 5 && i < 10)) {
            if (elmstr.charAt(i) < "0" || 
                elmstr.charAt(i) > "9") {
		errorFields+="endDate should be in mm/dd/yyyy format \n";
		break;
		}
        }
        else if (elmstr.charAt(i) != "/") {
		errorFields+="endDat should be in mm/dd/yyyy format \n";
		return false ;	
		}
    }
    return true;
}// is date
function defaultValue() {
var date = new Date();
var d  = date.getDate();
var day = (d < 10) ? '0' + d : d;
var m = date.getMonth() + 1;
var month = (m < 10) ? '0' + m : m;
var yy = date.getYear();
var year = (yy < 1000) ? yy + 1900 : yy;

todays = (day + "/" + month + "/" + year);
//alert("today" + todays);	
}//defaultValue

function compareDate(date1,date2) {

//defaultValue() ;


  var month1 = date1.substring(0,2);
  var day1 = date1.substring(3,5);
  var year1 = date1.substring(6,10);
  

  var month2 = date2.substring(0,2);
  var day2 = date2.substring(3,5);
  var year2 =date2.substring(6,10);
        
     if(year1 > year2)
	{
	errorFields+="endDate is less than effective date \n";
	return false;
	}

	if(year1 == year2)
	{
	if(month1 > month2)
	{
	
	errorFields+="endDate is less than effective date \n";
	return false;
	} 
	}
    if(year1 == year2 && month1 == month2 && day1 > day2)
	{
	
	errorFields+="endDate is less than effective date \n";
	return false;
	}  
}//end of compare date


}//End of validateForm function
