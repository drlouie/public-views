<!-- Sample HTML file --> <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<jsp:useBean id="contactPerson"  class="org.kp.broker.vo.ContactPersonVO"  scope="session"></jsp:useBean>
<jsp:useBean id="secondaryContact"  class="org.kp.broker.vo.ContactPersonVO"  scope="session"></jsp:useBean>
<jsp:useBean id="primaryContact"  class="org.kp.broker.vo.ContactPersonVO"  scope="session"></jsp:useBean>
<jsp:useBean id="contactPersonDummy"  class="org.kp.broker.vo.ContactPersonVO"  scope="session"></jsp:useBean>
<jsp:useBean id="Phone"  class="org.kp.broker.vo.PhoneVO"  scope="session"></jsp:useBean>

<jsp:useBean id="brokerDropDownVO" class="org.kp.broker.vo.BrokerDropDownVO" />

<%
	brokerDropDownVO = (org.kp.broker.vo.BrokerDropDownVO)session.getAttribute("DropDowns");
%>





<HTML>
<HEAD>

<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<TITLE>Contact Person Information</TITLE>

<%@include file="script/ContactRequiredFields.js" %>


<SCRIPT language="javascript">
var oldNo = false;
var phoneIK = "0000";



//Added by Sathish in 12/18/2001

function addToList( theForm ) {

	if ( checkAllValid(theForm.CountryCode.value, theForm.AreaCode.value, theForm.Number.value, theForm.Ext.value) ) {
		if ( checkForDuplication( theForm ) ) {
			if ( validateContactForm(theForm) ) {
				theForm.StatusIndicator.value = "";
				theForm.PhoneAction.value = "AddPhone";
				theForm.typeaction.value = "PhoneAction";
				if ( theForm.PhoneIK.value == "") 
					theForm.PhoneIK.value = "0";

				theForm.submit();
			}
		}
	}

}



function deleteFromList( theForm ) {

	if ( theForm.OldNumberIndicator.value == "true" ) {

		if ( validateContactForm( theForm ) ) {

				theForm.StatusIndicator.value = "D";
				theForm.PhoneAction.value = "DeletePhone";
				theForm.typeaction.value = "PhoneAction";
				theForm.submit();


		}

	}
	else {
	
		alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.SelectRecordToDelete")%>' );
		//alert( "The Phone number should be selected from the list to delete" );
	}

}



//Rewrote by Sathish on 11/19/2001

function checkAllValid(iCountryCode,iAreaCode,iNumber,iExtension)
 {	

	var phoneErrorStatus = "false";
	var phoneErrorFields = "Please correct the following error(s):";

	if ( iCountryCode == "" ) {
		phoneErrorFields += "\n"+"CountryCode is a required field";
		phoneErrorStatus = "true";

	}
	else {
	
		/*
		if ( iCountryCode.length < 3 ) {
			phoneErrorFields += "\n"+"CountryCode should be 3 digits";
			phoneErrorStatus = "true";
		}
		else {
		*/
			checkChar(iCountryCode);
		//}

	}

	if ( iAreaCode == "" ) {
		phoneErrorFields += "\n"+"AreaCode is a required field";
		phoneErrorStatus = "true";

	}
	else {
		if ( iAreaCode.length < 3 ) {
			phoneErrorFields += "\n"+"AreaCode should be 3 digits";
			phoneErrorStatus = "true";
		}
		else {
			checkChar(iAreaCode);
		}

	}

	if ( iNumber == "" ) {
		phoneErrorFields += "\n"+"Number is a required field";
		phoneErrorStatus = "true";

	}
	else {
		if ( iNumber.length < 7 ) {
			phoneErrorFields += "\n"+"Number should be 7 digits";
			phoneErrorStatus = "true";
		}
		else {
			checkChar(iNumber);
		}

	}


	if ( iExtension != "" ) {
		checkChar(iExtension);
	}

	
	function checkChar(iValue) {

		var valid = "0123456789";  

	 	for (var i=0; i < iValue.length; i++) 
  		{
   			temp1 = "" + iValue.substring(i, i+1);
   			if (valid.indexOf(temp1) == "-1") 
     				{
					phoneErrorFields += "\n"+"Invalid Phone Number";
					phoneErrorStatus = "true";
					break;
     				}
 		}
	
	  }


	if ( phoneErrorStatus == "true" ) {

		alert( phoneErrorFields );
		return false;
	}
	else
		return true;
		

 }



   function checkChar(iValue) {

	var valid = "0123456789";  

 	for (var i=0; i < iValue.length; i++) 
  		{
   			temp1 = "" + iValue.substring(i, i+1);
   			if (valid.indexOf(temp1) == "-1") 
     				{
       				alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+' phone number\n' );					
					return false;
       				break;
     				}
 		}
	
   }




   function popAgain( popList, popValue ) {

	var values = popValue;

	for( var m=0; m < popList.length; m++ ) {
		if ( popList.options[m].selected == true ) {
			listIndex = m;
			break;
		}
	}


	var temp;

	var count = new Array();
	var splitData = new Array();
		
	var j = 0;
	for (var i=0; i < values.length; i++) {
		temp = "" + values.substring(i, i+1);

		if ( temp == (":" ) ) {
			count[j] = i;
			j++;
		}
		
	}
	count[j] = values.length;

	var k = 0;
	for ( i=0; i < count.length; i++ ) {
		splitData[i] = values.substring( k, count[i] );
		k = count[i]+1;
	}

	if ( splitData[1] == undefined || splitData[2] == undefined || splitData[3] == undefined) {
	
		alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.SelectProperRecord")%>');
		//alert( "Click on the Phone number you want to populate in the fields" );
	}
	else {	

		
		document.ContactPerson.PhoneType.value = splitData[0];
		document.ContactPerson.CountryCode.value = splitData[1];
		document.ContactPerson.AreaCode.value = splitData[2];
		document.ContactPerson.Number.value = splitData[3];
		document.ContactPerson.Ext.value = splitData[4];
		document.ContactPerson.StatusIndicator.value = splitData[5];
		document.ContactPerson.PhoneIK.value = splitData[6];
	
		if ( splitData[7] == "Y" )
			document.ContactPerson.Preference.checked = 1;
		else
			document.ContactPerson.Preference.checked = 0;
	
		document.ContactPerson.OldNumberIndicator.value = "true";
	}
   }



   function checkForDuplication(theForm) {

	
	var phntype = 	document.ContactPerson.PhoneType.value;
	var ccode = document.ContactPerson.CountryCode.value;
	var acode = document.ContactPerson.AreaCode.value;
	var num = document.ContactPerson.Number.value;
	var extn = document.ContactPerson.Ext.value;
	var phoneIndex = "-1";
	var phoneStatus = true;

	var phoneno = phntype+"-"+ccode+"-"+acode+"-"+num+"-"+extn;


	for( var m=0; m < theForm.PhoneList.length; m++ ) {
		if ( theForm.PhoneList.options[m].selected == true ) {
			phoneIndex = m;
			break;
		}
	}


	for( var s=0; s < theForm.PhoneList.length; s++ ) {

		if ( s != phoneIndex ) {

			var values = theForm.PhoneList.options[s].value;

			var temp;
			var count = new Array();
			var splitData = new Array();
		
			var j = 0;
			for (var i=0; i < values.length; i++) {
				temp = "" + values.substring(i, i+1);
	
				if ( temp == (":" ) ) {
					count[j] = i;
					j++;
				}
			
			}
			count[j] = values.length;

			var k = 0;
			for ( i=0; i < count.length; i++ ) {
				splitData[i] = values.substring( k, count[i] );
				k = count[i]+1;
			}

			var oldphone = splitData[0]+"-"+splitData[1]+"-"+splitData[2]+"-"+splitData[3]+"-"+splitData[4];

			if ( phoneno == oldphone ) {

				alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.PhoneNoAlreadyExists")%>');
				//alert( "Phone number already exists in the List" );
				phoneStatus = false;
				break;
			}


		}

	}

	if ( phoneStatus )
		return true;
	else
		return false;


   }




function popList(list,type,ctry,area,num,ext,pref)  {

	var errorStatus = false;
	var errorMessage = "";
	var countryCode="";
	if(ctry != "")
		{
	 		countryCode = ctry
		}
	var areaCode = area;
	var number	= num;
	var extension = ext;	

	//Added by Sathish on 11/19/2001
	if ( ext == "" )
		extension = "     ";
	else if ( ext.length == 5 )
		extension = ext+ " ";
	else if ( ext.length == 3 )
		extension = ext+ "  ";
	else if ( ext.length == 2 )
		extension = ext+ "   ";
	else if ( ext.length == 1 )
		extension = ext+ "    ";


	var prefText;
	var prefValue;
	var nonPrefText;
	var nonPrefValue;

	var check = checkAllValid(countryCode,areaCode,number,extension);

	if(check == false)
		{
			//refresh();
			return false;
		}

	var PhoneType ="";
	

	//var listLength = list.options.length;
	listLength = list.options.length;


 	if( type == "B")
          PhoneType =" Business";
       else if ( type =="P")
          PhoneType = "    Pager";
       else if ( type == "M")
          PhoneType ="   Mobile";
       else if ( type == "R")
          PhoneType = "Residence";
       else if ( type == "F")
          PhoneType = "      Fax";

     	var prefered = pref;	

	var lastHyphen ;

	if(prefered == false)
		{
			nonPrefText =PhoneType+":"+countryCode+"-"+areaCode+"-"+number+"-"+extension;
			nonPrefValue =type+":"+countryCode+"-"+areaCode+"-"+number+"-"+extension+"-"+phoneIK;			
			lastHyphen = nonPrefValue
		}
	
	if(prefered == true)	
		{	
			prefText = PhoneType+":"+countryCode+"-"+areaCode+"-"+number+"-"+extension+"*"		 
			prefValue =type+":"+countryCode+"-"+areaCode+"-"+number+"-"+extension+"*"+"-"+phoneIK;
			lastHyphen = prefValue;	
		}

	var nonPrefNo = new Option();
	nonPrefNo.value = nonPrefValue;
	nonPrefNo.text = nonPrefText;

	var prefNo = new Option();
       prefNo.value = prefValue;
       prefNo.text = prefText;


	
	var extraRow = new Option();
	extraRow.value = " ";
	extraRow.text = " ";

	var found = false;
	
	if(prefered == true && list.options.length >= 1)
		{
			var checkForExistsPhone = PhoneType+":"+countryCode+"-"+areaCode+"-"+number+"-"+extension
		       var exists = checkForExists(list,checkForExistsPhone);			
			if(exists == true)
				{
					//refresh();
					return false;
				}
		}
	else if(prefered == false  && list.options.length >= 1)
		{
			var checkForExistsPhone = PhoneType+":"+countryCode+"-"+areaCode+"-"+number+"-"+extension
		       var exists = checkForExists(list,checkForExistsPhone);
			if(exists == true)
				{
					//refresh();
					return false;
				}		
		}


	if(list.options.length == 0 )
		{	
		
			addFirstRow(list);
		}  	
	

	var tempFirstValue = list.options[0].value;
	var tempFirstText = list.options[0].text;	
	


	var tempSubValue = tempFirstValue;
	var tempTextLength = tempFirstText.length;

	

	var tempLastHyphen;
 	for( var j = 0 ; j < tempFirstValue.length ; j++)
  		{
   		 	if(tempFirstValue.substring(j,j+1) =="-")
     				{
      					tempLastHyphen=j;	
								
     				}
  		}
	var star = tempFirstValue.substring(tempLastHyphen,tempLastHyphen-1)
	
	var nonStar = new Option();
	var tempFirstPhoneIK = tempFirstValue.substring(tempLastHyphen);
	if(star == "*")
		{
			nonStar.value = tempFirstValue.substring(0,tempLastHyphen-1)+"-"+tempFirstPhoneIK;
			nonStar.text = tempFirstText.substring(0,tempTextLength-1);
		}
	else
   		{
			nonStar.value = tempFirstValue;
			nonStar.text = tempFirstText;
		}




	if(prefered == true && oldNo == false && listLength >0)
		{	
		
			pushDown(list);			
		
		}	
	else if(prefered == false && oldNo == false && listLength >0)
		{	
				
					addAtLast(list);
		}
		
	
	else if(prefered == true && oldNo == true && listLength >0)
        {
        for(var i=0 ; i < list.options.length; i++) 
		{	
			if(list.options[i].selected && list.options[i] != "") 
          			{	
					
					list.options[i].value = "";
					list.options[i].text = "";					
   	   			}
				
		  }	
		sortList(list);
		oldNo = false;
         }
         else if(prefered == false && oldNo == true && listLength >0) 
	   {	
		modifyAtSame(list);
	
          }


//---------------------------------------------
function sortList(ilist) 
	{	
		for(var i = 0; i < ilist.options.length; i++) 
			{
				if(ilist.options[i].value == "")  
					{	
						ilist.options[0].value = nonStar.value;
						ilist.options[0].text = nonStar.text;
//						ilist.options[0] = nonStar;
						for(var j = i; j > 0; j--)  
							{
							
								ilist.options[j].value = ilist.options[j - 1].value;
								ilist.options[j].text = ilist.options[j - 1].text;
							}					
   					}
			}
	ilist.options[0] = prefNo;
	oldNo = false;
	refresh();
       }
//----------------------------------------------------
function pushDown(ilist)
 {
		if(tempFirstText.substring(tempTextLength,tempTextLength-1)== "*")
				{
					
					ilist.options[listLength] = extraRow;						
					ilist.options[0].value = nonStar.value;
					ilist.options[0].text = nonStar.text;	
//					ilist.options[0] = nonStar;			
					for(var j = ilist.options.length ; j >1 ; j--)  
						{	
							ilist.options[j-1].value = ilist.options[j-2].value;
							ilist.options[j-1].text = ilist.options[j-2].text;
											
						}	
							ilist.options[0] = prefNo;	
							oldNo = false;													
							refresh();
   				}
			else	if(tempFirstText.substring(tempTextLength,tempTextLength-1)!= "*")
				{
							
					ilist.options[listLength] = extraRow;						
					for(var j = ilist.options.length ; j >1 ; j--)  
						{	
							ilist.options[j-1].value = ilist.options[j-2].value;
							ilist.options[j-1].text = ilist.options[j-2].text;
											
						}	
							ilist.options[0] = prefNo;														
							oldNo = false;											
							refresh();

   				}
	
 }

//------------------------------------------------------
function addFirstRow(ilist)
 {
	if(prefered == true)
		{
			document.ContactPerson.PhoneList.style.visibility = "";
			ilist.options[0]=prefNo;
			refresh();
		}
	else if (prefered == false)
		{	
			
			document.ContactPerson.PhoneList.style.visibility = "";
		       ilist.options[0]=nonPrefNo;									
			refresh();			
		}
 }
//--------------------------------------------------------------------
function addAtLast(ilist)
  {	
	document.ContactPerson.PhoneList.style.visibility = "";
	ilist.options[listLength] = nonPrefNo;
	refresh();

  }
//----------------------------------------------------------------------
function modifyAtSame(ilist)
 {	
	for(var i=0 ; i < ilist.options.length; i++) 
		{
			if(ilist.options[i].selected) 
          			{
					document.ContactPerson.PhoneList.style.visibility = "";
					ilist.options[i] = nonPrefNo;

					found=true;
					oldNo = false;
					refresh();
					break;
					
   	   			}	
		  }

  }






function checkForExists(ilist,iPhone)
 	{
	    if(ilist.options.length >=1)
              {
		for(var i=0 ; i < ilist.options.length; i++) 
			{	
				var listPhone = ilist.options[i].text
				var star = listPhone.substring(listPhone.length,listPhone.length-1);
				if(star == "*")
					listPhone = listPhone.substring(0,listPhone.length-1);													
				if( listPhone == iPhone && !ilist.options[i].selected)
					{	
						alert("This phone no already exists in List \n");
						document.ContactPerson.CountryCode.focus();												
						return true;					
       					
					}
			}				
	       }
	}



function refresh()
	{
		document.ContactPerson.PhoneType.value = "B";
		document.ContactPerson.CountryCode.value = "";
		document.ContactPerson.AreaCode.value = "";
		document.ContactPerson.Number.value = "";
		document.ContactPerson.Ext.value = "";
		document.ContactPerson.CountryCode.focus();
		document.ContactPerson.Preference.checked =0;

	}


	phoneIK = "0000";	
	return true;	
}//	 end of popList function

//--------------------------------------------------------------------




//-------------------------------------------------------------------------


 function validate(ilist)
{   
	var allphn = "";
	var allphnK = "";
	for(var i = 0; i < ilist.options.length; i++) {
	allphn = allphn+" % "+ilist.options[i].text;
	allphnK =allphnK+" % "+ilist.options[i].value;
}
//	 alert ( allphn );
//	alert ( allphnK );
document.ContactPerson.phoneconcat.value =allphn;
document.ContactPerson.phoneconcatK.value =allphnK;
}//vallidate list



    function submit_form() {
        var form = ContactPerson;
	var conttype =document.ContactPerson.contact.value;
//	 alert("contact" + document.ContactPerson.contact.value);
	var error_text = "";
	document.ContactPerson.chgmode.value="";
	document.ContactPerson.typeaction.value ="ctype";
	var flag = true;
	if(document.ContactPerson.firstName.value !="" || 
	  document.ContactPerson.middleName.value !="" ||
	document.ContactPerson.honorific.value !="" ||
	document.ContactPerson.lastName.value !="" ||
	document.ContactPerson.title.value !="" ||
	document.ContactPerson.suffix.value !="" ||
	document.ContactPerson.familiarName.value!="" ||
	document.ContactPerson.email.value !="" 
	)
	{
	flag = validateContactForm(ContactPerson)
       } 
//       alert("status" + flag);
  if(!flag)
	{
            		if(conttype=='1')
			{ 
			 document.ContactPerson.contact.options[1].selected =true;
			}
		            if(conttype=='2')
			{ 
			 document.ContactPerson.contact.options[0].selected =true;
			}


	}	

//	form.action.value = action;
     if(flag)	
    {
 form.submit();
 }  
return flag;
}// submit_form


function ResetForm()
{
	
	/*
	document.ContactPerson.honorific.value ="";
	document.ContactPerson.firstName.value="";
	document.ContactPerson.middleName.value ="";
	document.ContactPerson.lastName.value ="";
	document.ContactPerson.title.value ="";
	document.ContactPerson.contact.value ="";
	document.ContactPerson.suffix.value ="";
	document.ContactPerson.familiarName.value ="";
	document.ContactPerson.email.value ="";
	
	
	
	document.forms[0].reset();
	document.forms[0].PhoneAction.value = "";
	document.forms[0].PhoneIK.value = "";
	document.forms[0].OldNumberIndicator.value = "false";
	document.forms[0].StatusIndicator.value = "";
	*/
}


function enableContactForm(theForm ) {


}

function changemode(){
//alert("inside changemode");
document.ContactPerson.chgmode.value="save";
document.ContactPerson.typeaction.value ="stype"; 	
//alert(document.ContactPerson.chgmode.value);
}//chg mode



 
//-->



function populatePhoneList() {

	document.ContactPerson.honorific.focus();

//	document.ContactPerson.PhoneList.style.visibility = "hidden";
	document.ContactPerson.PhoneIK.value = "0";
	document.ContactPerson.OldNumberIndicator.value = "false";


	<% 
		if (contactPerson.getContactType().equals("1")) { 

			if ( primaryContact.getPhones() != null ) {
 
          			Vector phonesK = (Vector) primaryContact.getPhones();
				for ( int i=0; i<phonesK.size(); i++ ) {
					Phone = (org.kp.broker.vo.PhoneVO) phonesK.elementAt(i);

	%>

					var phntype = "<%=Phone.getPhoneType()%>";
					var PhoneType;

 					if( phntype == "B")
				          PhoneType =" Business";
				       	else if ( phntype =="P")
				          PhoneType = "    Pager";
				       	else if ( phntype == "M")
				          PhoneType ="   Mobile";
				       	else if ( phntype == "R")
				          PhoneType = "Residence";
				       	else if ( phntype == "F")
				          PhoneType = "      Fax";
					
					var ccode = "<%=Phone.getCountryCode()%>";
					var acode = "<%=Phone.getAreaCode()%>";
					var number = "<%=Phone.getNumber()%>";
					var extn = "<%=Phone.getExtension()%>";
					var pref = "<%=Phone.getPrefered()%>";
					var phnIK = "<%=Phone.getPhoneIK()%>";
					var stsind = "<%=Phone.getStatusIndicator()%>";
					
					var stsindtext = stsind;
				
					if ( stsindtext == "S" )
						stsindtext = " ";

					var ccodevalue = ccode;
					
					if ( ccode.length == 2 ) {
						ccode = " "+ccode;
					}
					else if ( ccode.length == 1 ) {
						ccode = "  "+ccode;
					}


					if ( acode.length == 2 ) {
						acode = "0"+acode;
					}
					else if ( acode.length == 1 ) {
						acode = "00"+acode;
					}

					if ( number.length == 6 ) {
						number = "0"+number;
					}
					else if ( number.length == 5 ) {
						number = "00"+number;
					}
					else if ( number.length == 4 ) {
						number = "000"+number;
					}
					else if ( number.length == 3 ) {
						number = "0000"+number;
					}
					else if ( number.length == 2 ) {
						number = "00000"+number;
					}
					else if ( number.length == 1 ) {
						number = "000000"+number;
					}

					if ( extn == "0" )
						extn = "";
						
					var exttext = extn;
					
				
					if ( exttext == "" )
						exttext = "      ";
					else if ( exttext.length == 1 ) {
						exttext = " x "+exttext+"    ";
						}
					else if ( exttext.length == 2 )
						exttext = " x "+exttext+"   ";
					else if ( exttext.length == 3 )
						exttext = " x "+exttext+"  ";
					else if ( exttext.length == 4 )
						exttext = " x "+exttext+" ";
					else if ( exttext.length == 5 )
						exttext = " x "+exttext;



					var PhonePref;
					if ( pref == "Y" )
						PhonePref = "*";
					else
						PhonePref = "";




					var addoptions = new Option();

					//addoptions.text = PhoneType+":"+ccode+"-"+acode+"-"+number+"-"+extn+"-"+stsind+"-"+PhonePref;
					addoptions.text = PhoneType+":"+ccode+"-"+acode+"-"+number+exttext+" "+stsindtext+" "+PhonePref;
					addoptions.value = phntype+":"+ccodevalue+":"+acode+":"+number+":"+extn+":"+stsind+":"+phnIK+":"+pref;

					document.ContactPerson.PhoneList.options[document.ContactPerson.PhoneList.options.length] = addoptions;			


					document.ContactPerson.PhoneList.style.visibility = "";
					
        <% 
				} 
			}
		} 
		if (contactPerson.getContactType().equals("2")) {  

			if ( secondaryContact.getPhones() != null ) {

          			Vector phonesK = (Vector) secondaryContact.getPhones();
				for ( int i=0; i<phonesK.size(); i++ ) {
					Phone = (org.kp.broker.vo.PhoneVO) phonesK.elementAt(i);
	%>	


					var phntype = "<%=Phone.getPhoneType()%>";
					var PhoneType;

 					if( phntype == "B")
				          PhoneType =" Business";
				       	else if ( phntype =="P")
				          PhoneType = "    Pager";
				       	else if ( phntype == "M")
				          PhoneType ="   Mobile";
				       	else if ( phntype == "R")
				          PhoneType = "Residence";
				       	else if ( phntype == "F")
				          PhoneType = "      Fax";
					
					var ccode = "<%=Phone.getCountryCode()%>";
					var acode = "<%=Phone.getAreaCode()%>";
					var number = "<%=Phone.getNumber()%>";
					var extn = "<%=Phone.getExtension()%>";
					var pref = "<%=Phone.getPrefered()%>";
					var phnIK = "<%=Phone.getPhoneIK()%>";
					var stsind = "<%=Phone.getStatusIndicator()%>";
					
					var stsindtext = stsind;
				
					if ( stsindtext == "S" )
						stsindtext = " ";

					
					var ccodevalue = ccode;

					if ( ccode.length == 2 ) {
						ccode = " "+ccode;
					}
					else if ( ccode.length == 1 ) {
						ccode = "  "+ccode;
					}


					if ( acode.length == 2 ) {
						acode = "0"+acode;
					}
					else if ( acode.length == 1 ) {
						acode = "00"+acode;
					}

					if ( number.length == 6 ) {
						number = "0"+number;
					}
					else if ( number.length == 5 ) {
						number = "00"+number;
					}
					else if ( number.length == 4 ) {
						number = "000"+number;
					}
					else if ( number.length == 3 ) {
						number = "0000"+number;
					}
					else if ( number.length == 2 ) {
						number = "00000"+number;
					}
					else if ( number.length == 1 ) {
						number = "000000"+number;
					}

					var exttext = extn;
					
				
					if ( exttext == "" )
						exttext = "      ";
					else if ( exttext.length == 1 ) {
						exttext = " x "+exttext+"    ";
						}
					else if ( exttext.length == 2 )
						exttext = " x "+exttext+"   ";
					else if ( exttext.length == 3 )
						exttext = " x "+exttext+"  ";
					else if ( exttext.length == 4 )
						exttext = " x "+exttext+" ";
					else if ( exttext.length == 5 )
						exttext = " x "+exttext;



					var PhonePref;
					if ( pref == "Y" )
						PhonePref = "*";
					else
						PhonePref = "";


					var addoptions = new Option();

					//addoptions.text = PhoneType+":"+ccode+"-"+acode+"-"+number+"-"+extn+"-"+stsind+"-"+PhonePref;
					addoptions.text = PhoneType+":"+ccode+"-"+acode+"-"+number+exttext+" "+stsindtext+" "+PhonePref;					
					addoptions.value = phntype+":"+ccodevalue+":"+acode+":"+number+":"+extn+":"+stsind+":"+phnIK+":"+pref;

					document.ContactPerson.PhoneList.options[document.ContactPerson.PhoneList.options.length] = addoptions;			

					document.ContactPerson.PhoneList.style.visibility = "";


	<%
				}
			} 
		} 
	%>
}




</SCRIPT>



<!--Dynamic CSS Javascript-->
<script language="javascript" src="script/common_css.js"></script>



<script language="Javascript">
<!--
//MOUSEOVER IMAGE PRELOAD

//add button
image15 = new Image();
image15.src = "limages/add_ov.gif";
image16 = new Image();
image16.src = "limages/add_off.gif";
//delete selected button
image17 = new Image();
image17.src = "limages/delsel_ov.gif";
image18 = new Image();
image18.src = "limages/delsel_off.gif";

//-->
</script>


</HEAD>

<BODY bgcolor="#0B5F77" onload="populatePhoneList()"> 
<Form name="ContactPerson"  method ="post"  OnSubmit="return validateContactForm(ContactPerson)" action= "ContactPersonServlet" >
<input type="hidden" name="action" value="">
<input type="hidden" name="typeaction" value="ctype">
<input type="hidden" name="phoneconcat" value="">
<input type="hidden" name="phoneconcatK" value="">
<input type="hidden" name="chgmode" value="">
<input type="hidden" name="indicator" value="0">
<input type="hidden" name="TypeChangeKey" value="">

<input type="hidden" name="PhoneAction" value="">
<input type="hidden" name="PhoneIK" value="">
<input type="hidden" name="OldNumberIndicator" value="false">
<input type="hidden" name="StatusIndicator" value="">
<INPUT type="hidden" name="SaveExitPage" value="No">

<input type="hidden" name="bkrbid" value="<%=session.getAttribute("BIDinSession")%>">




  <table width="95%" border="0" cellspacing="0" cellpadding="2" align="center">
    <tr align="center" valign="middle"> 
      <td> 
        <table width="670" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td align="left" width="3" height="20"><img src="limages/tleft3.gif" width="3" height="20"></td>
            <td bgcolor="#E6E9F0" width="332" align="left"><font class="stitle">&nbsp;&nbsp;&nbsp;Contact 
              Person Information</font></td>
            <td bgcolor="#E6E9F0" width="335" align="right"> 
              <input type="button" value="Edit" name="Edit" class="lebotton" onclick="enableContactForm(document.forms[0])">
              <input type="button" value="Reset" name="button" onclick="ResetForm()" class="lebotton">
            </td>
          </tr>
        </table>
        <table border="0" cellspacing="0" cellpadding="0" width="670">
          <tr> 
            <td><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td ><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
          <tr> 
            <td bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
          <tr> 
            <td width="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td width="668"> 
              <table cellpadding="0" cellspacing="0" width="668" height="0">
                <tbody> 
                <tr> 
                  <td  align="center" valign="bottom" width="121"><font class="ComTitle">Contact</font></td>
                  <td  width="75" height="25" valign="bottom"></td>
                  <td  align="center" width="100" height="25" valign="bottom"><font class="ComTitle">Honor</font></td>
                  <td  align="center" width="100" height="25" valign="bottom"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>First</font></td>
                  <td  align="center" width="100" height="25" valign="bottom"><font class="ComTitle">Middle</font></td>
                  <td  align="center" valign="bottom" width="122"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Last</font></td>
                  <td  align="center" valign="bottom" width="75"><font class="ComTitle">Suffix</font></td>
                </tr>
                <tr> 
                  <td  bgcolor="#E6E9F0" align="center" valign="bottom" width="121"> 
                    <select name="contact" class="select2" onchange=" validate(ContactPerson.PhoneList);return submit_form()" tabindex="1">
                            <OPTION value="1" <% if (contactPerson.getContactType().equals("1")) { %>="" <% } %>="">Primary </OPTION>
                            <OPTION value="2" <% if (contactPerson.getContactType().equals("2")) { %>="" selected <%}%>="">Secondary </OPTION>
                    </select>

<% 
	if (contactPerson.getContactType().equals("1") ) 
    	contactPersonDummy = primaryContact;
   	else
    	contactPersonDummy = secondaryContact;
         
        //added by Sathish on Feb 6,2002 to set null values to empty string
	if ( contactPersonDummy.getHonor() == null )
		contactPersonDummy.setHonor("");
	if ( contactPersonDummy.getFirstName() == null )
		contactPersonDummy.setFirstName("");
	if ( contactPersonDummy.getMiddleName() == null )
		contactPersonDummy.setMiddleName("");
	if ( contactPersonDummy.getLastName() == null )
		contactPersonDummy.setLastName("");
	if ( contactPersonDummy.getSuffix() == null )
		contactPersonDummy.setSuffix("");
	if ( contactPersonDummy.getEMailAddress() == null )
		contactPersonDummy.setEMailAddress("");
	if ( contactPersonDummy.getFamiliarName() == null )
		contactPersonDummy.setFamiliarName("");
	if ( contactPersonDummy.getTitle() == null )
		contactPersonDummy.setTitle("");
			
			
         
%>

                  </td>
                  <td class="title" width="75" bgcolor="#E6E9F0" align="right"><font class="stitle">Name 
                    &gt;&gt; </font></td>
                  <td valign="middle" align="center" width="100" bgcolor="#E6E9F0"> 
                    <input size="5" type="text" maxlength="10" name="honorific"  value ="<%=contactPersonDummy.getHonor() %>"  class="input2" tabindex="2">
                  </td>
                  <td valign="middle" align="center" width="100" bgcolor="#E6E9F0"> 
                    <input class="input2" size="15" type="text" maxlength="30" name="firstName" value= "<%=contactPersonDummy.getFirstName() %>" tabindex="3">
                  </td>
                  <td valign="middle" align="center" width="100" bgcolor="#E6E9F0"> 
                    <input class="input2" size="15" type="text" maxlength="30" name="middleName" value= "<%=contactPersonDummy.getMiddleName() %>" tabindex="4">
                  </td>
                  <td  bgcolor="#E6E9F0" align="center" valign="bottom" width="122"> 
                    <input class="input2" size="15" type="text" maxlength="30" name="lastName" value= "<%=contactPersonDummy.getLastName() %>" tabindex="5">
                  </td>
                  <td  bgcolor="#E6E9F0" align="center" valign="bottom" width="75"> 
                    <input class="input2" size="5" type="text" maxlength="30" name="suffix" value= "<%=contactPersonDummy.getSuffix() %>" tabindex="6">
                  </td>
                </tr>
                <tr>
                  <td  align="center" valign="bottom" width="121">&nbsp;</td>
                  <td class="title" width="75" align="right">&nbsp;</td>
                  <td valign="middle" align="center" width="100">&nbsp;</td>
                  <td valign="middle" align="center" width="100">&nbsp;</td>
                  <td valign="middle" align="center" width="100">&nbsp;</td>
                  <td  align="center" valign="bottom" width="122">&nbsp;</td>
                  <td  align="center" valign="bottom" width="75">&nbsp;</td>
                </tr>
                </tbody> 
              </table>
              <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                  <td valign="top" width="50%"> 
                    <table cellpadding="0" cellspacing="0" align="center">
                      <tbody> 
                      <tr valign="middle"> 
                        <td  align="center" width="175"><font class="ComTitle">Title</font></td>
                      </tr>
                      <tr valign="middle"> 
                        <td  align="center" width="175"> 
                          <input class="input2" size="35" type="text" maxlength="30" name="title" value= "<%=contactPersonDummy.getTitle() %>" tabindex="7">
                        </td>
                      </tr>
                      <tr valign="middle"> 
                        <td  align="center" width="175" valign="middle"><font class="ComTitle">Familiar Name </font></td>
                      </tr>
                      <tr valign="middle"> 
                        <td  align="center" width="175"> 
                          <input class="input2" size="35" type="text" maxlength="30" name="familiarName" value= "<%=contactPersonDummy.getFamiliarName() %>" tabindex="8">
                        </td>
                      </tr>
                      <tr valign="middle"> 
                        <td  align="center" width="175" valign="middle"><font class="ComTitle">Email</font></td>
                      </tr>
                      <tr valign="middle"> 
                        <td  align="center" width="175" valign="middle"> 
                          <input class="input2" size="35" type="text" maxlength="30" name="email" value="<%=contactPersonDummy.getEMailAddress() %>" tabindex="9">
                        </td>
                      </tr>
                      </tbody> 
                    </table>
                  </td>
                  <td width="50%"> 
                    <table width="375" border="0" cellspacing="0" cellpadding="0">
                      <tr> 
                        <td align="left" width="3" height="20"><img src="limages/tleft3.gif" width="3" height="20"></td>
                        <td bgcolor="#E6E9F0" width="369" align="center"><font class="stitle">Phone 
                          Numbers</font></td>
                        <td align="right" width="3" height="20"><img src="limages/tright3.gif" width="3" height="20"></td>
                      </tr>
                    </table>
                    <table width="375" border="0" cellspacing="0" cellpadding="0">
                      <tr> 
                        <td><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                        <td width="398"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                        <td><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                      </tr>
                      <tr> 
                        <td bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                        <td bgcolor="#E6E9F0" width="398"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                        <td bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                      </tr>
                      <tr> 
                        <td width="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                        <td width="373" align="center"> 
                          <table width="373" border="0" cellspacing="0" cellpadding="2">
                            <tr align="center" valign="bottom"> 
                              <td width="70" height="42"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Type<br>
                                </font> 
                                <select name="PhoneType" tabindex="10"  class="select2" onFocus="this.blur()">
			                    <% 
			
									java.util.Vector phnTypeText = new java.util.Vector();			
									java.util.Vector phnTypeValue = new java.util.Vector();

									phnTypeText = brokerDropDownVO.getPhoneTypeText();									
									phnTypeValue = brokerDropDownVO.getPhoneTypeValue();		
						
									for(int i = 0 ; i < phnTypeText.size(); i++) {
								%>
								
        				            <OPTION value="<%=phnTypeValue.elementAt(i)%>"><%=phnTypeText.elementAt(i)%></OPTION>
     			               <%
									}
						       %>
                                </select>
                              </td>
                              <td width="25" height="42"> <font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Ctry</font><br>
                                <input size="3" type="text" maxlength="3" name="CountryCode" tabindex="11"  class="input2" onFocus="this.blur()">
                              </td>
                              <td height="42" width="25"> <font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Area</font><br>
                                <input size="3" type="text" maxlength="3" name="AreaCode" tabindex="12" class="input2" onFocus="this.blur()">
                              </td>
                              <td height="42" width="30"> <font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Number</font><br>
                                <input size="7" type="text" maxlength="7" name="Number" tabindex="13" class="input2" onFocus="this.blur()">
                              </td>
                              <td height="42" width="25"> <font class="ComTitle">Ext</font><br>
                                <input size="5" type="text" maxlength="5" name="Ext" tabindex="14" class="input2" onFocus="this.blur()">
                              </td>
                              <td height="42" width="20"> <font class="ComTitle">Pref</font><br>
                                <input type="checkbox" name="Preference" tabindex="15">
                              </td>
                              <td height="42" width="178" align="center"><a href="#" OnClick="addToList(document.ContactPerson)" onMouseOver="javascript:add.src = image15.src;" onMouseOut="javascript:add.src = image16.src;"><img src="limages/add_off.gif" width="50" height="19" border="0" alt="Add" name="add" tabindex="16"></a> 
                                <input type="hidden" name="StatusIndicator2" value="">
                              </td>
                            </tr>
                            <tr align="center" valign="bottom"> 
                              <td colspan="7"> 
                                <select size="3" name="PhoneList" onclick="popAgain(document.ContactPerson.PhoneList,document.ContactPerson.PhoneList.value)" class="multiselect" style="background-color:#ffffff">
                                </select>
                              </td>
                            </tr>
                            <tr align="center" valign="bottom"> 
                              <td colspan="7"><a href="#" OnClick="deleteFromList( document.ContactPerson )" onMouseOver="javascript:delsel.src = image17.src;" onMouseOut="javascript:delsel.src = image18.src;"><img src="limages/delsel_off.gif" width="138" height="19" border="0" alt="Delete Selected" name="delsel" vspace="0"></a> 
                              </td>
                            </tr>
                          </table>
                        </td>
                        <td width="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                      </tr>
                      <tr> 
                        <td height="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                        <td height="1" bgcolor="#E6E9F0" width="398"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                        <td height="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
              
            </td>
            <td width="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
          <tr> 
            <td height="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td height="1" bgcolor="#E6E9F0" width="398"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td height="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
        </table>
      </td>
    </tr>
  </table>





<input type="hidden" name="phonor" value="">
<input type="hidden" name="pfirstname" value="">
<input type="hidden" name="pmiddlename" value="">
<input type="hidden" name="plastname" value="">
<input type="hidden" name="ptitle" value="">
<input type="hidden" name="psuffix" value="">
<input type="hidden" name="pfamiliarname" value="">
<input type="hidden" name="pemail" value="">
<input type="hidden" name="pphone" value="">

<input type="hidden" name="shonor" value="">
<input type="hidden" name="sfirstname" value="">
<input type="hidden" name="smiddlename" value="">
<input type="hidden" name="slastname" value="">
<input type="hidden" name="stitle" value="">
<input type="hidden" name="ssuffix" value="">
<input type="hidden" name="sfamiliarname" value="">
<input type="hidden" name="semail" value="">
<input type="hidden" name="sphone" value="">











</form>
</BODY>
</HTML>