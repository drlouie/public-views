<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<TITLE>Broker Firm(Maintenance)</TITLE>
<jsp:useBean id="brokerVO" class="org.kp.broker.vo.BrokerVO" />
<jsp:useBean id="firmVO" class="org.kp.broker.vo.FirmVO" />
<jsp:useBean id="addressVO" class="org.kp.broker.vo.AddressVO" />
<jsp:useBean id="brokerDropDownVO" class="org.kp.broker.vo.BrokerDropDownVO" />
<jsp:useBean id="categoryVO" class="org.kp.broker.vo.CategoryVO" />
<jsp:useBean id="statusDropDownVO" class="org.kp.broker.vo.StatusDropDownVO" />
<jsp:useBean id="statusVO" class="org.kp.broker.vo.StatusVO" />
<jsp:useBean id="Phone" class="org.kp.broker.vo.PhoneVO" />
<%
	brokerVO = (org.kp.broker.vo.BrokerVO)session.getAttribute("Broker");
	firmVO = (org.kp.broker.vo.FirmVO)brokerVO.getFirm();
	addressVO = (org.kp.broker.vo.AddressVO) brokerVO.getAddress();
	statusVO = (org.kp.broker.vo.StatusVO)brokerVO.getStatus();
	brokerDropDownVO = (org.kp.broker.vo.BrokerDropDownVO)session.getAttribute("DropDowns");
	statusDropDownVO = (org.kp.broker.vo.StatusDropDownVO)brokerVO.getStatusDropDown();
%>


<%@ include file="script/ValidateAddress.js" %>


<Script src="script/ValidateDOI.js">
</Script>

<%@ include file="script/ContactRequiredFields.js" %>

<Script src="script/PrintScript.js">
</Script>

<SCRIPT language="javascript">
var states = new Array() ;
var canadianStates = new Array();
var bsnstype = new Array();
var countries = new Array();
var category = new Array();
var categoryYear = new Array();
var statusReasonText = new Array();
var statusReasonValue = new Array();
var statusReasonCode = new Array();
var state = "";
function init()
  {
	
		
	  document.FirmMaintenance.PhoneList.style.fontFamily = "Courier New";

		<% 
			java.util.Vector v = new java.util.Vector();
			v = brokerDropDownVO.getState();						
			for(int i = 0 ; i < v.size(); i++){
			%>
			states[<%=i%>] = '<%=v.elementAt(i)%>';
		<%}%>	
		

	<% 
		java.util.Vector canSt = new java.util.Vector();
		canSt = brokerDropDownVO.getCanadianStates();						
		for(int i = 0 ; i < canSt.size(); i++){
	%>
			canadianStates[<%=i%>] = '<%=canSt.elementAt(i)%>';
	<%}%>	

		<%
			
			java.util.Vector brokerCategories = new java.util.Vector();
			brokerCategories = brokerVO.getCategories();
			for(int count = 0 ; count < brokerCategories.size() ; count++)
			{			
				categoryVO = (org.kp.broker.vo.CategoryVO)brokerCategories.elementAt(count);			
			%>
				category[<%=count%>] = '<%=categoryVO.getBrokerCategory()%>';
				categoryYear[<%=count%>] = '<%=categoryVO.getBrokerCategoryYear()%>';
				                    
                    <%								 
			}
		    %>
		<%
			java.util.Vector SRText = new java.util.Vector();
			java.util.Vector SRValue = new java.util.Vector();
			java.util.Vector SRCode = new java.util.Vector();						
			SRText = brokerDropDownVO.getStatusReasonText();
			SRValue = brokerDropDownVO.getStatusReasonValue();
			SRCode = brokerDropDownVO.getStatusReasonCode();
			for(int i = 0 ; i < SRText.size(); i++)
			{
		%>		
			
			statusReasonText[<%=i%>] = '<%=SRText.elementAt(i)%>';
			statusReasonValue[<%=i%>] = '<%=SRValue.elementAt(i)%>';
			statusReasonCode[<%=i%>] = '<%=SRCode.elementAt(i)%>';
		<%
			}
		%>
		
		


	document.FirmMaintenance.BroadcastMedium.value = '<%=brokerVO.getBroadcastMedium()%>';
	document.FirmMaintenance.BusinessType.value = '<%=brokerVO.getBusinessType()%>';
	document.FirmMaintenance.Country.value = '<%=addressVO.getCountry()%>';
	document.FirmMaintenance.BrokerCategory.value = category[0];	
	
	state = '<%=addressVO.getState()%>';
	setState( document.FirmMaintenance);
	
	document.FirmMaintenance.changeType[1].checked = true;
	
  }




//Added by Sathish

function populatePhoneList() {

//	document.forms[0].PhoneList.style.visibility = "hidden";
	document.forms[0].PhoneIK.value = "0";
	document.forms[0].OldNumberIndicator.value = "false";


	<% 

			if ( brokerVO.getPhones() != null ) {
 
          			Vector phonesK = (Vector) brokerVO.getPhones();
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

					document.forms[0].PhoneList.options[document.forms[0].PhoneList.options.length] = addoptions;			


					document.forms[0].PhoneList.style.visibility = "";
					
        <% 
				} 
			}

	%>

}









function resetForm()
{
	document.FirmMaintenance.reset();
	document.FirmMaintenance.BroadcastMedium.value = '<%=brokerVO.getBroadcastMedium()%>';
	document.FirmMaintenance.BusinessType.value = '<%=brokerVO.getBusinessType()%>';
	document.FirmMaintenance.Country.value = '<%=addressVO.getCountry()%>';
	document.FirmMaintenance.BrokerCategory.value = category[0];	
	document.FirmMaintenance.State.value = '<%=addressVO.getState()%>';
}
</SCRIPT>



<SCRIPT language="javascript">


function submitForm( theForm ) {

	if ( submitDestinationForm() ) {
		if (validateForm( theForm ) ) {
			if ( parent.destination != undefined ) {
				if ( parent.destination.document.forms[0] != undefined ) {
					parent.destination.document.forms[0].submit();
				}
			}
			return true;
		}			
		else 
			return false;
	}
	else
		return false;

}


function submitDestinationForm() {


	//Added by Sathish to include the SAVE functionality

	if ( parent.destination != undefined ) {
		if ( parent.destination.document.forms[0] != undefined ) {

			parent.destination.document.forms[0].SaveExitPage.value = document.FirmMaintenance.SaveExitPage.value;
			
			if ( parent.destination.document.forms[0].name == "ContactPerson" ) {
				parent.destination.document.forms[0].chgmode.value="save";
				parent.destination.document.forms[0].typeaction.value ="stype";

				var allphn = "";
				var allphnK = "";

				for(var i = 0; i < parent.destination.document.forms[0].PhoneList.options.length; i++) {
					allphn = allphn+" % "+parent.destination.document.forms[0].PhoneList.options[i].text;
					allphnK =allphnK+" % "+parent.destination.document.forms[0].PhoneList.options[i].value;
					parent.destination.document.forms[0].phoneconcat.value =allphn;
					parent.destination.document.forms[0].phoneconcatK.value =allphnK;
				}

			}

			if ( parent.destination.document.forms[0].name == "AddTypeForm" ) {

				if ( validate(parent.destination.document.forms[0]) ) {
					if ( parent.destination.document.forms[0].AddressLine1.value != "" ) {
						parent.destination.document.forms[0].TypeChangeKey.value = "Submit";
						//parent.destination.document.forms[0].submit();
					}
					document.FirmMaintenance.WhereToGo.value="AdditionalAddress.jsp";					
					return true;
				}
				else
					return false;

			}
			else if ( parent.destination.document.forms[0].name == "ContactPerson" ) {

				if ( validateContactForm(parent.destination.document.forms[0]) ) {
					parent.destination.document.forms[0].TypeChangeKey.value = "Submit";
					//parent.destination.document.forms[0].submit();
					document.FirmMaintenance.WhereToGo.value="ContactPersonInfo.jsp";					
					return true;
				}
				else
					return false;

			}
			else if ( parent.destination.document.forms[0].name == "Relationship" ) {
				parent.destination.document.forms[0].opmode.value="save";
				parent.destination.document.forms[0].submitField.value="submit";
				//parent.destination.document.forms[0].submit();
				document.FirmMaintenance.WhereToGo.value="Relationship.jsp";				
				return true;
			}
			else if ( parent.destination.document.forms[0].name == "LicenseForm" ) {
				
				if ( validateDOIValues(parent.destination.document.forms[0]) ) {
				
					parent.destination.document.forms[0].TypeChangeKey.value = "Submit";
					//parent.destination.document.forms[0].submit();
					document.FirmMaintenance.WhereToGo.value="License_DOI.jsp";
					return true;
				}
				else
					return false;
			
			}			
			else {
			
				if ( parent.destination.document.forms[0].name == "AgreementsForm" )
					document.FirmMaintenance.WhereToGo.value="Agreements.jsp";				
				else if ( parent.destination.document.forms[0].name == "PaymentControlsForm" )
					document.FirmMaintenance.WhereToGo.value="PaymentControls.jsp";				
			
				parent.destination.document.forms[0].TypeChangeKey.value = "Submit";
				//parent.destination.document.forms[0].submit();
				return true;
			}

		}
		else
			return true;
	}
	else
		return true;

}



function validateForm(theForm)
 {	



theForm.Status.disabled = false;			
theForm.StatusReason.disabled = false;
theForm.BrokerCategory.disabled = false;
theForm.BrokerCategoryYear.disabled = false;
theForm.Country.disabled = false;
theForm.State.disabled = false;
theForm.BroadcastMedium.disabled = false;
theForm.BusinessType.disabled = false;	

var errorStatus = false;
var errorFields ="";
  if(theForm.TaxID.value == "")
   {
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.TaxIDRequired")%>'+'\n';
	errorStatus = true;
   }	
  else
   {
   	checkCompleteSetup(theForm.TaxID.name,theForm.TaxID.value)
   }	   
  if(theForm.FirmName.value == "")
   {
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.FirmNameRequired")%>'+'\n';
	errorStatus = true;			
   }
  else
   {
	checkCompleteSetup(theForm.FirmName.name,theForm.FirmName.value);
   }
   
  /*
  if(theForm.Location.value == "")
   {
	errorFields+="Location is a required field \n";
	errorStatus = true;			
   }
  else
   {
	checkCompleteSetup(theForm.Location.name,theForm.Location.value)
   }
   */

if(theForm.Location.value != "")
	checkCompleteSetup(theForm.Location.name,theForm.Location.value)   
   
if(theForm.Line1.value == "")
   {
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.Line1Required")%>'+'\n';
	errorStatus = true;	
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
if(theForm.City.value == "")
   {
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Address.CityRequired")%>'+'\n';
	errorStatus = true;	
   }
else
   {
	checkCompleteSetup(theForm.City.name,theForm.City.value);
   }
if(theForm.County.value != "")
	{
		checkCompleteSetup(theForm.County.name,theForm.County.value);
	}
if(theForm.Province.value != "")
	{
		checkCompleteSetup(theForm.Province.name,theForm.Province.value);
	}
if(theForm.MailStop.value != "")
	{
		checkCompleteSetup(theForm.MailStop.name,theForm.MailStop.value);
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






 if(theForm.EMail.value !="")
   {
	checkCompleteSetup(theForm.EMail.name,theForm.EMail.value);
	checkEmail(theForm.EMail.value);
   }
  if(theForm.EffDate.value =="")
   {
	errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.PaymentAddressEffDate")%>'+'\n';
	errorStatus = true;
   }
  else
   {
   
	var dtSts = chkDateValidation(theForm.EffDate.name,theForm.EffDate.value);	


	if ( dtSts ) {
	
	
     	if(theForm.OrgEffDate.value != theForm.EffDate.value) {

			var ctSts = chkCurrentDate( theForm.EffDate.name, theForm.EffDate.value );
	
			if( !ctSts ) {
				errorStatus = true;	
				errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.EffDateLessthanCurrent")%>'+'\n';
			}
		}       
	}
	else {
		errorStatus = true;	
		errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidEffDate")%>'+'\n';
	
	}
     

   }


	for(var i = 0 ; i <theForm.PhoneList.options.length ; i++)
          {
		theForm.PhoneNumbers.value+= theForm.PhoneList.options[i].value;
		theForm.PhoneNumbers.value+="%";
	  }



for(var count = 0 ; count < category.length ; count++)
	{
		
		var both = category[count]+"-"+categoryYear[count];
		theForm.AllCategory.value+= both +"/"
	}

if (errorStatus==true)
   {
	alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.ErrorMessagePrefix")%>'+'\n'+ errorFields );
	return false;
   }
   else
	return true;


	function chkDateValidation(datename, datevalue){


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



	function chkCurrentDate( datename, datevalue ) {


		var currentDtSts = true;

		var sysDate = document.forms[0].CurrentDate.value;

		var month = sysDate.substring(0, 2);
		var date = sysDate.substring(3, 5);
		var year = sysDate.substring(6, 10);


		//month = month +1 ;
	
		/*
		if ( ( month / 2 ) < 5 )
			month = "0" + month;

		if ( ( date / 2 ) < 5 )
			date = "0" + date;
		*/
		
		
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

					//errorFields += "\n" + datename + "'s day cannot be lesser than today";
					//errorStatus = true;
					currentDtSts = false;
				}
			}
			else {
				currentDtSts = false;
			}

		}
		else {
			currentDtSts = false;
		}
		
		if ( currentDtSts )
			return true;
		else
			return false;

	}



function checkCompleteSetup(name,value)
 {

var TaxID = "1234567890";
var FirmName = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'& " ;	
var Line1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890, ";
var City = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ " ;
var MailStop = "#1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
var EffDate = "1234567890/";
var EMail = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@1234567890.";
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

function checkEmail(email) 
 {
  invalidChars = " /:,;"
   for (i=0; i<invalidChars.length; i++) 
     {    
	badChar = invalidChars.charAt(i)
	if (email.indexOf(badChar,0) > -1) 
         {
       errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+"Email \n";
           errorStatus=true;
	 }
    }
  atPos = email.indexOf("@",1)	
  if (atPos == -1)
   {
       errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+"Email \n";
       errorStatus=true;
	return;
	
   }

  if (email.indexOf("@",atPos+1) != -1)
   {	
		errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+'Email \n';
       errorStatus=true;
	return;
   }

  periodPos = email.indexOf(".",atPos)
  if (periodPos == -1)
   {	  
		errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+'Email \n';
        errorStatus=true;
	return;
   }

  if (periodPos+4 > email.length)	
    {	
		errorFields+='<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+'Email \n';
       errorStatus=true;

    } 
 }

}//End of validateForm function



//Added by Sathish in 12/18/2001

function addToList( theForm ) {

	if ( checkAllValid(theForm.CountryCode.value, theForm.AreaCode.value, theForm.Number.value, theForm.Ext.value) ) {
		if ( checkForDuplication( theForm ) ) {
			if ( validateForm(theForm) ) {
				theForm.StatusIndicator.value = "";
				theForm.PhoneAction.value = "AddPhone";

				if ( theForm.PhoneIK.value == "") 
					theForm.PhoneIK.value = "0";

				setWhereToGo( theForm );
				theForm.submit();
			}
		}
	}

}



function deleteFromList( theForm ) {

	if ( theForm.OldNumberIndicator.value == "true" ) {

		if ( validateForm( theForm ) ) {

				theForm.StatusIndicator.value = "D";
				theForm.PhoneAction.value = "DeletePhone";

				setWhereToGo( theForm );
				theForm.submit();


		}

	}
	else {
		alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.SelectRecordToDelete")%>');
	}

}


function setWhereToGo ( theForm ) {

	if ( parent.destination != undefined )  {
	
			if ( parent.destination.document.forms[0] != undefined ) {
				if ( parent.destination.document.forms[0].name == "AddTypeForm" )
					theForm.WhereToGo.value="AdditionalAddress.jsp";
				if ( parent.destination.document.forms[0].name == "AgreementsForm" )
					theForm.WhereToGo.value="Agreements.jsp";			
				if ( parent.destination.document.forms[0].name == "LicenseForm" )
					theForm.WhereToGo.value="License_DOI.jsp";			
				if ( parent.destination.document.forms[0].name == "PaymentControlsForm" )
					theForm.WhereToGo.value="PaymentControls.jsp";			
				if ( parent.destination.document.forms[0].name == "ContactPerson" )
					theForm.WhereToGo.value="ContactPersonInfo.jsp";			
				if ( parent.destination.document.forms[0].name == "Relationship" )
					theForm.WhereToGo.value="Relationship.jsp";			
					
			}
		
	
	}


}



//Rewrote by Sathish on 11/19/2001

function checkAllValid(iCountryCode,iAreaCode,iNumber,iExtension)
 {	

	var phoneErrorStatus = "false";
	var phoneErrorFields = '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.ErrorMessagePrefix")%>';

	if ( iCountryCode == "" ) {
		phoneErrorFields += "\n"+'<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Phone.CountryCodeRequired")%>';
		phoneErrorStatus = "true";

	}
	else {
			checkChar(iCountryCode);
	}

	if ( iAreaCode == "" ) {
		phoneErrorFields += "\n"+'<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Phone.AreaCodeRequired")%>';
		phoneErrorStatus = "true";

	}
	else {
		if ( iAreaCode.length < 3 ) {
			phoneErrorFields += "\n"+'<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Phone.AreaCodeSize")%>';
			phoneErrorStatus = "true";
		}
		else {
			checkChar(iAreaCode);
		}

	}

	if ( iNumber == "" ) {
		phoneErrorFields += "\n"+'<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Phone.NumberRequired")%>';
		phoneErrorStatus = "true";

	}
	else {
		if ( iNumber.length < 7 ) {
			phoneErrorFields += "\n"+'<%=org.kp.base.web.util.MessageUtil.getInstance().getText("base.Phone.NumberSize")%>';
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
					phoneErrorFields += "\n"+'<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.Invalid")%>'+'Phone Number';
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
       				alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.InvalidChars")%>'+ 'Phone Number' );
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
	
		alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.SelectProperRecord")%>');
	}
	else {	
	
		document.forms[0].PhoneType.value = splitData[0];
		document.forms[0].CountryCode.value = splitData[1];
		document.forms[0].AreaCode.value = splitData[2];
		document.forms[0].Number.value = splitData[3];
		document.forms[0].Ext.value = splitData[4];
		document.forms[0].StatusIndicator.value = splitData[5];
		document.forms[0].PhoneIK.value = splitData[6];
	
		if ( splitData[7] == "Y" )
			document.forms[0].Preference.checked = 1;
		else
			document.forms[0].Preference.checked = 0;
	
		document.forms[0].OldNumberIndicator.value = "true";
	}
   }



   function checkForDuplication(theForm) {

	
	var phntype = 	document.forms[0].PhoneType.value;
	var ccode = document.forms[0].CountryCode.value;
	var acode = document.forms[0].AreaCode.value;
	var num = document.forms[0].Number.value;
	var extn = document.forms[0].Ext.value;
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

				alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.PhoneExists")%>');
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



var oldNo = false;
var phoneIK = "0000";
var disableList = true;
var faxFound = false;

function listHide()			//to hide the list when nophone added to that
 {
//	document.FirmMaintenance.PhoneList.style.visibility = "hidden";	
 }

//--------------------------------------------------------------------
function enableAll(form)	//Enabling all the Fields when Edit clicked
 {
	
   var totalElements = document.FirmMaintenance.elements.length;
   for ( var i = 1 ; i <totalElements ; i++)
    {
	
        if(document.FirmMaintenance.elements[i].name != "bid" && document.FirmMaintenance.elements[i].name != "StatusDate"  && document.FirmMaintenance.elements[i].name != "changeType"  && document.FirmMaintenance.elements[i].type != "button"   && document.FirmMaintenance.elements[i].type != "submit")
		{			
			document.FirmMaintenance.elements[i].style.background = "white";
			document.FirmMaintenance.elements[i].onfocus = null;
		}
    }
   enableDropDowns();
   disableList = false;
}
function checkForFaxInPhoneList()
{	
	
	for(var i=0 ; i < document.FirmMaintenance.PhoneList.options.length; i++) 
		{	
			var listValue = document.FirmMaintenance.PhoneList.options[i].value;
			if(listValue.substring(0,1) == "F")
				{	
					faxFound = true;
					enableFaxInBroadcastMedium();					
					disableList = false;
					document.FirmMaintenance.PhoneList.style.background = "white";
				}		
		}
	if(faxFound !=true && document.FirmMaintenance.EMail.value != "")
		{
			enableEMailInBroadcastMedium();
			faxFound = false;
		}
	else if(faxFound !=true && document.FirmMaintenance.EMail.value == "")
		{
			document.FirmMaintenance.BroadcastMedium.value = "";
			faxFound = false;
		}
	faxFound = false;
}

function enableFaxInBroadcastMedium()
{	
	document.FirmMaintenance.BroadcastMedium.value = "F";
}
function enableEMailInBroadcastMedium()
{	
	document.FirmMaintenance.BroadcastMedium.value = "E";

}
function checkForEMailAndFax(sel)
{
	var canSelect = false;
	if(sel == "F")
	{
	for(var i=0 ; i < document.FirmMaintenance.PhoneList.options.length; i++) 
		{	
			var listValue = document.FirmMaintenance.PhoneList.options[i].value;
			if(sel == listValue.substring(0,1))
				canSelect = true;
		}
	}
	else if (sel =="E")
	{
		if(document.FirmMaintenance.EMail.value != "")
		canSelect = true;
	}
  if(canSelect != true)
	{
		alert('<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.BroadCaseMediumInvalid")%>');
		document.FirmMaintenance.BroadcastMedium.value = document.FirmMaintenance.PreviousBrdcst.value;
	}	
}
function checkEffDateChanged()
{	
	document.FirmMaintenance.EffDateChanged.value = "changed";	
	
}

function disableDropDowns()
{
	document.FirmMaintenance.Status.disabled = true;			
	document.FirmMaintenance.StatusReason.disabled = true;
	document.FirmMaintenance.BrokerCategory.disabled = true;
	document.FirmMaintenance.BrokerCategoryYear.disabled = true;
	document.FirmMaintenance.Country.disabled = true;
	document.FirmMaintenance.BroadcastMedium.disabled = true;
	document.FirmMaintenance.BusinessType.disabled = true;	
	document.FirmMaintenance.changeType[0].disabled = true;
	document.FirmMaintenance.changeType[1].disabled = true;	
	
}
function enableDropDowns()
{
	document.FirmMaintenance.Status.disabled = false;			
	document.FirmMaintenance.StatusReason.disabled = false;
	document.FirmMaintenance.BrokerCategory.disabled = false;
	document.FirmMaintenance.BrokerCategoryYear.disabled = false;
	document.FirmMaintenance.Country.disabled = false;
	document.FirmMaintenance.BroadcastMedium.disabled = false;
	document.FirmMaintenance.BusinessType.disabled = false;	
	document.FirmMaintenance.changeType[0].disabled = false;
	document.FirmMaintenance.changeType[1].disabled = false;	

}
</SCRIPT>


<!-- INCLUDED BY SATHISH 10/03 -->
<Script language="JavaScript">
   function callBrokerTypeChange() {

//	if ( validateForm(FirmMaintenance) ) {
		document.FirmMaintenance.action="ChangeBrokerTypeServlet";
		document.FirmMaintenance.target="_parent";
		document.FirmMaintenance.submit();
//	}
   }

   function callComments() {
   
   		var funType = document.forms[0].FunctionType.value;
   		
   		document.FirmMaintenance.sourceId1.value = document.FirmMaintenance.bid.value;

   		if ( funType == "" )
   			funType = "DMGR";
		
		var url = 'Comments/CommentServlet?sourceId1='+document.FirmMaintenance.sourceId1.value+'&sourceId2=0&sourceId3=0&sourceInd=BKR&funType='+funType;
				
		window.open(url, 'slideWindow',false,500,700);
   }


/*
   function callPrint() {

	document.FirmMaintenance.action="PrintServlet";
	document.FirmMaintenance.submit();

   }
*/

function printFunction() {

	callPrint();
}


   function callSearch() {

		document.FirmMaintenance.action="SearchServlet";
		document.FirmMaintenance.submit();

   }


   function callExit() {

	parent.LeftNav.upTitle(0);

   	// DISABLE ALL Form Elements FROM BrokerMain document
	var leTotal = parent.BrokerMain.document.forms[0].elements.length;
	for ( var i = 0 ; i <leTotal ; i++) {
		parent.BrokerMain.document.forms[0].elements[i].disabled = true;
	}

   	// HIDE ALL BrokerMain Form Elements
	var leTotal = document.FirmMaintenance.elements.length;
	for ( var i = 0 ; i <leTotal ; i++) {
		document.FirmMaintenance.elements[i].style.visibility = 'hidden';
	}

	
	if (document.getElementById) {  // DOM3 = IE5, NS6
		document.getElementById('hidepage2').style.visibility = 'visible';
	}
	else {
		if (document.layers) {  // Netscape 4
			document.hidepage2.visibility = 'visible';
		}
		else {  // IE 4
			document.all.hidepage2.style.visibility = 'visible';
		}
	}

	document.getElementById("theTitle").style.color="#EB0000";

   }


function saveBM(cual) {
		if (cual == "Yes") {
			// hide layer
			hideIT();

			document.FirmMaintenance.SaveExitPage.value = "Yes";
			if ( submitForm( document.FirmMaintenance) ) {
				document.FirmMaintenance.target="_parent";
				document.FirmMaintenance.submit();
			}
		}
		else if (cual == "No") {
			parent.window.close();
		}
		else {
			// hide layer
			hideIT();	
		}

	}


	function hideIT() {
		// HIDE LAYER
		if (document.getElementById) {  // DOM3 = IE5, NS6
			document.getElementById('hidepage2').style.visibility = 'hidden';
		}
		else {
			if (document.layers) {  // Netscape 4
				document.hidepage2.visibility = 'hidden';
			}
			else {  // IE 4
				document.all.hidepage2.style.visibility = 'hidden';
			}
		}
			

	   	// ENABLE ALL Form Elements FROM BrokerMain document
		var leTotal = parent.BrokerMain.document.forms[0].elements.length;
		for ( var i = 0 ; i <leTotal ; i++) {
			parent.BrokerMain.document.forms[0].elements[i].disabled = false;
		}

  		// show ALL BrokerMain Form Elements
		var leTotal = document.FirmMaintenance.elements.length;
		for ( var i = 0 ; i <leTotal ; i++) {
			document.FirmMaintenance.elements[i].style.visibility = 'visible';
		}	
		document.getElementById("theTitle").style.color="#0B5F77";
	}


	function setState( theForm ) {
	
		var country = theForm.Country.value;
		
		
		if ( country == "USA" ) {
			theForm.State.length = 0;		
			for ( var i=0; i<states.length; i++ ) {
				var addstate = new Option();
				addstate.text = states[i];
				addstate.value = states[i];
				theForm.State.options[i] = addstate;				
			}
			theForm.State.disabled = false;	
			theForm.State.value = state;
		}
		else if ( country == "CAN" ) {
			theForm.State.length = 0;		
			for ( var i=0; i<canadianStates.length; i++ ) {
				var addstate = new Option();
				addstate.text = canadianStates[i];
				addstate.value = canadianStates[i];
				theForm.State.options[i] = addstate;				
			}
			theForm.State.disabled = false;
			theForm.State.value = state;			
		}
		else {
				theForm.State.length = 0;		
				theForm.State.disabled = true;
		}

	}
</Script>

<!--Start Additions by drlouie-->

<!-- FOLLOWING SCRIPT COMMUNICATES WITH LEFTNAV SCRIPTS -->
<script language="javascript" src="script/b4dom.js"></script>
<SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function showLayer(leindValue) {

	document.URLer.myindValue.value = leindValue;
	setTimeout('changeToRed()', 500);

   	// HIDE ALL BrokerMain Form Elements
	var leTotal = document.FirmMaintenance.elements.length;
	for ( var i = 0 ; i <leTotal ; i++) {
		document.FirmMaintenance.elements[i].style.visibility = 'hidden';
	}

   	// DISABLE ALL Form Elements FROM Destination document
	var leTotal = parent.destination.document.forms[0].elements.length;
	for ( var i = 0 ; i <leTotal ; i++) {
		parent.destination.document.forms[0].elements[i].disabled = true;
	}
	
	if (document.getElementById) {  // DOM3 = IE5, NS6
		document.getElementById('hidepage').style.visibility = 'visible';
	}
	else {
		if (document.layers) {  // Netscape 4
			document.hidepage.visibility = 'visible';
		}
		else {  // IE 4
			document.all.hidepage.style.visibility = 'visible';
		}
	}
}

function changeToRed() {
	document.getElementById("theTitle").style.color="#EB0000";
}

function hideLayer(cual) {
	var leindValue = document.URLer.myindValue.value;

 	  	// SHOW ALL BrokerMain Form Elements
		var leTotal = document.FirmMaintenance.elements.length;
		for ( var i = 0 ; i <leTotal ; i++) {
			document.FirmMaintenance.elements[i].style.visibility = 'visible';
		}

	   	// ENABLE ALL Form Elements FROM Destination document
		var leTotal = parent.destination.document.forms[0].elements.length;
		for ( var i = 0 ; i <leTotal ; i++) {
			parent.destination.document.forms[0].elements[i].disabled = false;
		}

		// SHOW LAYER
		if (document.getElementById) {  // DOM3 = IE5, NS6
			document.getElementById('hidepage').style.visibility = 'hidden';
		}
		else {
			if (document.layers) {  // Netscape 4
				document.hidepage.visibility = 'hidden';
			}
			else {  // IE 4
				document.all.hidepage.style.visibility = 'hidden';
			}
		}

	parent.LeftNav.runURL(leindValue,cual);
}

//  End -->
</script>
<style type="text/css"> #hidepage {z-index:2000} </style>
<!-- END COMM SCRIPT -->


<!--Dynamic CSS Javascript-->
<script language="javascript" src="script/common_css.js">
</script>

<script language="Javascript">
<!--
//MOUSEOVER IMAGE PRELOAD

//mreset
// // // MOUSE OVER
image1 = new Image();
image1.src = "limages/mreset_ov.gif";
// // // MOUSE OFF
image2 = new Image();
image2.src = "limages/mreset_off.gif";

//medit
image3 = new Image();
image3.src = "limages/medit_ov.gif";
image4 = new Image();
image4.src = "limages/medit_off.gif";
//msearch
image5 = new Image();
image5.src = "limages/msearch_ov.gif";
image6 = new Image();
image6.src = "limages/msearch_off.gif";
//msave
image7 = new Image();
image7.src = "limages/msave_ov.gif";
image8 = new Image();
image8.src = "limages/msave_off.gif";
//mprint
image9 = new Image();
image9.src = "limages/mprint_ov.gif";
image10 = new Image();
image10.src = "limages/mprint_off.gif";
//mexit
image11 = new Image();
image11.src = "limages/mexit_ov.gif";
image12 = new Image();
image12.src = "limages/mexit_off.gif";
//mcomments
image13 = new Image();
image13.src = "limages/mcomments_ov.gif";
image14 = new Image();
image14.src = "limages/mcomments_off.gif";


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


<style type="text/css">
#leTitle {position:absolute; z-index:2001; top:10px; left: 15px; }
</style>

<!--End Additions by drlouie-->

</HEAD>
<BODY bgcolor="#0B5F77" onload="init();disableDropDowns();populatePhoneList();parent.LeftNav.upTitle(0);">
<FORM name="FirmMaintenance" method="post" onsubmit="return submitForm(FirmMaintenance)" action="FirmUpdate"  target="_parent">
  <table width="850" border="0" cellspacing="0" cellpadding="0" align="center">
    <tr> 
      <td width="5" valign="top"><img src="limages/spacer.gif" border="0" width="5" height="5"></td>
      <td width="300" valign="top"><img src="limages/spacer.gif" border="0" width="5" height="5"></td>
      <td width="200"><img src="limages/spacer.gif" border="0" width="5" height="5"></td>
      <td width="300"><img src="limages/spacer.gif" border="0" width="5" height="5"></td>
      <td width="5"><img src="limages/spacer.gif" border="0" width="5" height="5"></td>
    </tr>
    <tr> 
      <td width="5" valign="top">&nbsp;</td>
      <td width="25" valign="top">&nbsp;

        
<div id="leTitle">&nbsp;</div>

      </td>
      <td width="100%" valign="top"><br>
        <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
          <tr> 
            <td bgcolor="#E6E9F0" width="100%"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
        </table>
      </td>
      <td width="300" align="right"> 
        <table width="300" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td bgcolor="#E6E9F0" width="398"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
          <tr> 
            <td width="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td height="37" width="398" align="center"> <a href="#" onMouseOver="javascript:msearch.src = image5.src;" onMouseOut="javascript:msearch.src = image6.src;" onClick="callSearch()"><img src="limages/msearch_off.gif" width="52" height="37" name="msearch" border="0"></a> 
              <input type="image" name="submit" src="limages/msave_off.gif" width="52" height="37" border="0">
              <a href="#" onMouseOver="javascript:mprint.src = image9.src;" onMouseOut="javascript:mprint.src = image10.src;" onClick="printFunction();"><img src="limages/mprint_off.gif" width="52" height="37" name="mprint" border="0"></a> 
              <a href="#" onMouseOver="javascript:mexit.src = image11.src;" onMouseOut="javascript:mexit.src = image12.src;" onClick="callExit()"><img src="limages/mexit_off.gif" width="52" height="37" name="mexit" border="0"></a><a href="#" onMouseOver="javascript:mcomments.src = image13.src;" onMouseOut="javascript:mcomments.src = image14.src;" onClick="callComments()"><img src="limages/mcomments_off.gif" width="66" height="37" name="mcomments" border="0"></a></td>
            <td width="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
          <tr> 
            <td height="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td height="1" bgcolor="#E6E9F0" width="398"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td height="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
        </table>
      </td>
      <td width="5">&nbsp;</td>
    </tr>
    <tr> 
      <td width="5" valign="top">&nbsp;</td>
      <td colspan="3" valign="top" height="35"> 
        <table width="125" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td bgcolor="#E6E9F0" width="398"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
          <tr> 
            <td width="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td height="20" width="198" align="center"> 
              <input type="radio" name="changeType" value="agent"  onClick="callBrokerTypeChange()">
              <font class="ComTitle">Agent</font> 
              <input type="radio" checked name="changeType" value="firm">
              <font class="ComTitle">Firm</font></td>
            <td width="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
          <tr> 
            <td height="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td height="1" bgcolor="#E6E9F0" width="398"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
            <td height="1" bgcolor="#E6E9F0"><img src="limages/spacer.gif" border="0" width="1" height="1"></td>
          </tr>
        </table>
      </td>
      <td width="5">&nbsp;</td>
    </tr>
  </table>
  <table width="850" border="0" cellspacing="0" cellpadding="0" align="center">
    <tr> 
      <td width="5" valign="top">&nbsp;</td>
      <td colspan="3" valign="top"> 
        <table width="840" border="0" cellspacing="0" cellpadding="1">
          <tr align="center"> 
            <td width="48" align="center"><font class="ComTitle">BID</font></td>
            <td width="75"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Tax 
              ID</font></td>
            <td width="192" align="center"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Status</font></td>
            <td width="125" align="center"><font class="ComTitle">Status Reason</font></td>
            <td width="71" align="center"><font class="ComTitle">Date</font></td>
            <td width="154">&nbsp;</td>
            <td width="56" align="center"><font class="ComTitle">BCY</font></td>
            <td width="119" align="center"><font class="ComTitle">Broker Category</font></td>
          </tr>
          <tr align="left" valign="middle" bgcolor="#E6E9F0"> 
            <td width="48" align="center"> 
              <input size="6" type="text" maxlength="12" name="bid" onFocus="this.blur()" value="<%=brokerVO.getBID()%>" class="input1">
            </td>
            <td width="75" align="center"> 
              <input size="11" type="text" maxlength="9" name="TaxID" value="<%=brokerVO.getTaxID()%>" onFocus="this.blur()" class="input1">
            </td>
            <td width="192" align="center"> 
              <select name="Status" onFocus="this.blur()" class="select1" onChange="populateReason(this.value)">
                <%
			java.util.Vector statusText = new java.util.Vector();
			java.util.Vector statusValue = new java.util.Vector();						
			statusText = statusDropDownVO.getStatusText();
			statusValue = statusDropDownVO.getStatusValue();
			for(int i = 0 ; i < statusText.size(); i++)
				{						
		%>
                <option value = '<%=statusValue.elementAt(i)%>'><%=statusText.elementAt(i)%></option>
                <%
				}
		%>
              </select>
            </td>
            <td width="125" align="center"> 
              <select name="StatusReason" class="select1">
                <%
			java.util.Vector statusReasonText = new java.util.Vector();
			java.util.Vector statusReasonValue = new java.util.Vector();	
			java.util.Vector statusReasonCode = new java.util.Vector();						
			statusReasonText = statusDropDownVO.getStatusReasonText();
			statusReasonValue = statusDropDownVO.getStatusReasonValue();
			statusReasonCode = brokerDropDownVO.getStatusReasonCode();
			for(int i = 0 ; i < statusReasonText.size(); i++)
			{
		%>
                <option value = '<%=statusReasonValue.elementAt(i)%>'><%=statusReasonText.elementAt(i)%></option>
                <%
			}
		%>
              </select>
            </td>
            <td width="71" align="center"> 
              <input size="11" type="text" maxlength="10" name="StatusDate" 
value = '<%=statusVO.getStatusDate()%>' onFocus="this.blur()" class="input1">
            </td>
            <td width="154">&nbsp;</td>
            <td width="56" align="center"> 
              <script language="javascript">

function changeCategory(newValue)
	{		
		category[document.FirmMaintenance.BrokerCategoryYear.value]  = newValue;		
	}
function changeCategoryYear(id)
	{	
		document.FirmMaintenance.BrokerCategory.value = category[id];
	}
</script>
              <select name="BrokerCategoryYear" class="select1" onChange="changeCategoryYear(this.value)">
                <%			
			
			brokerCategories = brokerVO.getCategories();
			for(int count = 0 ; count < brokerCategories.size() ; count++)
			{			
				categoryVO = (org.kp.broker.vo.CategoryVO)brokerCategories.elementAt(count);			
			%>
                <option value="<%=count%>"><%=categoryVO.getBrokerCategoryYear()%></option>
                <%								 
			}
		%>
              </select>
              <input type = "hidden" name = "AllCategory" value = "">
            </td>
            <td width="119" align="center"> 
              <select name="BrokerCategory" class="select1" onFocus="this.blur()" onChange="changeCategory(this.value)">
                <% 
			
									java.util.Vector bkrCatText = new java.util.Vector();			
									java.util.Vector bkrCatValue = new java.util.Vector();

									bkrCatText = brokerDropDownVO.getBkrCategoryText();
									bkrCatValue = brokerDropDownVO.getBkrCategoryValue();		
						
									for(int i = 0 ; i < bkrCatText.size(); i++) {
								%>
                <option value="<%=bkrCatValue.elementAt(i)%>"><%=bkrCatText.elementAt(i)%></option>
                <%
									}
						       %>
                <!--                  
                    <OPTION value="R" selected>Regular</OPTION>
                    <OPTION value="P">Prefered</OPTION>
                    -->
              </select>
            </td>
          </tr>
        </table>
      </td>
      <td width="5">&nbsp;</td>
    </tr>
  </table>
  <table width="800" border="0" cellspacing="0" cellpadding="0" align="center">
    <tr> 
      <td width="5" valign="top">&nbsp;</td>
      <td colspan="3" valign="top"> 
        <table width="790" border="0" cellspacing="0" cellpadding="1">
          <tr align="center"> 
            <td><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Name</font></td>
            <td><font class="ComTitle">Location</font></td>
            <td><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Business 
              Type</font></td>
          </tr>
          <tr align="center" bgcolor="#E6E9F0"> 
            <td> 
              <input size="60" type="text" maxlength="80" name="FirmName" value="<%=firmVO.getName()%>" onFocus="this.blur()" class="input1">
            </td>
            <td> 
              <input size="40" type="text" maxlength="40" name="Location" onFocus="this.blur()" class="input1" value="<%=firmVO.getLocation()%>">
            </td>
            <td> 
              <select name="BusinessType" tabindex="1" class="select1">
                <% 
			
			java.util.Vector bsnstypeValue = new java.util.Vector();
			bsnstypeValue = brokerDropDownVO.getBsnsTypeValue();		
			java.util.Vector bsnstypeText = new java.util.Vector();
			bsnstypeText = brokerDropDownVO.getBsnsTypeText();
			for(int i = 0 ; i < bsnstypeValue.size(); i++)
				{
		%>
                <option value = '<%=bsnstypeValue.elementAt(i)%>'><%=bsnstypeText.elementAt(i)%></option>
                <%
				}
		%>
              </select>
            </td>
          </tr>
        </table>
      </td>
      <td width="5">&nbsp;</td>
    </tr>
  </table>
  <table width="850" border="0" cellspacing="0" cellpadding="0" align="center">
    <tr> 
      <td width="5" valign="top">&nbsp;</td>
      <td colspan="3" valign="top"> 
        <table width="840" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td width="355" height="20"><img src="limages/spacer.gif" border="0" width="1" height="5"></td>
            <td align="center" rowspan="2" valign="middle" width="110"><a href="#" onMouseOver="mreset.src = image1.src;" onMouseOut="javascript:mreset.src = image2.src;" onClick="resetForm()"><img src="limages/mreset_off.gif" width="40" height="37" name="mreset" border="0"></a><a href="#" onMouseOver="javascript:medit.src = image3.src;" onMouseOut="javascript:medit.src = image4.src;" onClick="enableAll(this.form)"><br>
              <br>
              <img src="limages/medit_off.gif" width="40" height="37" name="medit" border="0"></a></td>
            <td align="right" width="375" height="20"><img src="limages/spacer.gif" border="0" width="1" height="5"></td>
          </tr>
          <tr> 
            <td valign="top" width="355" align="left"> 
              <table width="355" border="0" cellspacing="0" cellpadding="0">
                <tr> 
                  <td align="left" width="3" height="20"><img src="limages/tleft3.gif" width="3" height="20"></td>
                  <td bgcolor="#E6E9F0" width="349" align="center"><font class="stitle">&nbsp;Primary 
                    Payment Address</font></td>
                  <td align="right" width="3" height="20"><img src="limages/tright3.gif" width="3" height="20"></td>
                </tr>
              </table>
              <table width="355" border="0" cellspacing="0" cellpadding="0">
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
                  <td align="center"> 
                    <table width="353" border="0" cellspacing="0" cellpadding="2">
                      <tr valign="bottom"> 
                        <td align="center" width="176" valign="middle" height="27"><font class="ComTitle">Eff 
                          Date</font> 
                          <input size="10" type="text" maxlength="10" name="EffDate" onFocus="this.blur()" class="input1" value="<%=addressVO.getEffectiveDate()%>">
                          <input type="hidden" name="OrgEffDate" value="<%=session.getAttribute("BkrAddrOrgEffDate")%>">
                        </td>
                        <td align="center" valign="middle"><nobr><font class="ComTitle">Mail 
                          Stop#</font></nobr></td>
                        <td align="left" colspan="3" valign="middle"> 
                          <input size="10" type="text" maxlength="15" name="MailStop" onFocus="this.blur()" value="<%=addressVO.getMailStop()%>" class="input1">
                        </td>
                      </tr>
                      <tr valign="bottom"> 
                        <td align="right" width="176" height="27"><nobr><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Line 
                          1</font>&nbsp; 
                          <input size="20" type="text" maxlength="50" name="Line1" onFocus="this.blur()" value="<%=addressVO.getLine1()%>" class="input1">
                          </nobr> </td>
                        <td width="75" height="27" align="right"><font class="ComTitle">State</font></td>
                        <td width="37" height="27"> <font class="label">
                          <select name="State"  class="select1" onFocus="this.blur()">
                            <option value="">&nbsp;&nbsp;&nbsp;</option>
                          </select>
                          </font></td>
                        <td height="27" valign="bottom" align="right" width="20"><font class="ComTitle">Zip</font></td>
                        <td width="52" height="27"> 
                          <input size="5" type="text" maxlength="10" name="Zip" onFocus="this.blur()" value="<%=addressVO.getZip()%>" class="input1">
                        </td>
                      </tr>
                      <tr valign="bottom"> 
                        <td align="right" width="176"><nobr><font class="ComTitle">Line 
                          2</font>&nbsp; 
                          <input size="20" type="text" maxlength="50" name="Line2" onFocus="this.blur()" value="<%=addressVO.getLine2()%>" class="input1">
                          </nobr></td>
                        <td width="75" align="right"><font class="ComTitle">County</font></td>
                        <td width="187" colspan="3"> 
                          <input size="20" type="text" maxlength="20" name="County" onFocus="this.blur()" value="<%=addressVO.getCounty()%>" class="input1">
                        </td>
                      </tr>
                      <tr valign="bottom"> 
                        <td align="right" width="176"><nobr><font class="ComTitle">Line 
                          3</font>&nbsp; 
                          <input size="20" type="text" maxlength="50" name="Line3" onFocus="this.blur()" class="input1" value="<%=addressVO.getLine3()%>">
                          </nobr> </td>
                        <td width="75" align="right"><font class="ComTitle">Country</font></td>
                        <td width="187" colspan="3"> 
                          <select name="Country" onChange="setState(document.FirmMaintenance)" class="select1">
                            <% 
			
			java.util.Vector country = new java.util.Vector();
			country = brokerDropDownVO.getCountry();		
			
			for(int i = 0 ; i < country.size(); i++)
				{
		%>
                            <option value = '<%=country.elementAt(i)%>'><%=country.elementAt(i)%></option>
                            <%
				}			
		%>
                          </select>
                        </td>
                      </tr>
                      <tr valign="bottom"> 
                        <td align="right" width="176"><nobr><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>City</font>&nbsp; 
                          <input size="20" type="text" maxlength="50" name="City" onFocus="this.blur()" value="<%=addressVO.getCity()%>" class="input1">
                          </nobr> </td>
                        <td width="75" align="right"><font class="ComTitle">Province</font></td>
                        <td width="187" colspan="3"> 
                          <input size="20" type="text" maxlength="20" name="Province" onFocus="this.blur()" class="input1" value="<%=addressVO.getProvince()%>">
                          <input type="hidden" name="CurrentDate" value='<%=session.getAttribute("CurrentDate")%>'>
                          <input type="hidden" name="EffDateChanged" value="<%=addressVO.getEffectiveDate()%>">
                        </td>
                      </tr>
                      <tr valign="bottom"> 
                        <td align="right" width="176"><img src="limages/spacer.gif" border="0" width="5" height="5"></td>
                        <td colspan="4"><img src="limages/spacer.gif" border="0" width="5" height="5"></td>
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
            <td align="right" valign="top" width="375"> 
              <table width="375" border="0" cellspacing="0" cellpadding="0">
                <tr> 
                  <td align="left" width="3" height="20"><img src="limages/tleft3.gif" width="3" height="20"></td>
                  <td bgcolor="#E6E9F0" width="369" align="center"><font class="stitle">Contact 
                    Information</font></td>
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
                      <tr align="center" valign="middle"> 
                        <td width="120"><font class="ComTitle">Email</font></td>
                        <td width="120"><font class="ComTitle">URL</font></td>
                        <td width="133"> <font class="ComTitle">Broadcast Medium</font></td>
                      </tr>
                      <tr align="center" valign="middle" bgcolor="#E6E9F0"> 
                        <td width="120"> 
                          <input size="20" type="text" maxlength="40" name="EMail" tabindex="3" value="<%=brokerVO.getEMailAddress()%>" class="input1" onFocus="this.blur()" onChange = "checkForFaxInPhoneList()" >
                        </td>
                        <td width="120"> 
                          <input size="20" type="text" maxlength="60" name="WebURL" tabindex="4" value="<%=brokerVO.getWebURL()%>" class="input1" onFocus="this.blur()">
                        </td>
                        <td width="133"> 
                          <select name="BroadcastMedium" tabindex="2" class="select1" onChange = "checkForEMailAndFax(this.value)" 
onClick = "document.FirmMaintenance.PreviousBrdcst.value = document.FirmMaintenance.BroadcastMedium.value;">
                            <% 
			
									java.util.Vector broadCastText = new java.util.Vector();			
									java.util.Vector broadCastValue = new java.util.Vector();

									broadCastText = brokerDropDownVO.getBrdcstmdmText();
									broadCastValue = brokerDropDownVO.getBrdcstmdmValue();		
						
									for(int i = 0 ; i < broadCastText.size(); i++) {
								%>
                            <option value="<%=broadCastValue.elementAt(i)%>"><%=broadCastText.elementAt(i)%></option>
                            <%
									}
						       %>
                            <!--
                    <OPTION value="F" selected >Fax</OPTION>
                    <OPTION value="E">EMail</OPTION>
                    -->
                          </select>
                        </td>
                      </tr>
                    </table>
                    <table width="373" border="0" cellspacing="0" cellpadding="2">
                      <tr align="center" valign="bottom"> 
                        <td width="70"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Type</font></td>
                        <td width="25"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Ctry</font></td>
                        <td width="25"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Area</font></td>
                        <td width="30"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Number</font></td>
                        <td width="25"><font class="ComTitle">Ext</font></td>
                        <td width="20"><font class="ComTitle">Pref</font></td>
                        <td width="178" align="center"><font class="ComTitle">&nbsp;</font></td>
                      </tr>
                      <tr align="center" valign="bottom"> 
                        <td width="70" bgcolor="#E6E9F0"> 
                          <select name="select" tabindex="4" class="select1">
                            <% 
			
									java.util.Vector phnTypeText = new java.util.Vector();			
									java.util.Vector phnTypeValue = new java.util.Vector();

									phnTypeText = brokerDropDownVO.getPhoneTypeText();									
									phnTypeValue = brokerDropDownVO.getPhoneTypeValue();		
						
									for(int i = 0 ; i < phnTypeText.size(); i++) {
								%>
                            <option value="<%=phnTypeValue.elementAt(i)%>"><%=phnTypeText.elementAt(i)%></option>
                            <%
									}
						       %>
                          </select>
                        </td>
                        <td width="25" bgcolor="#E6E9F0"> 
                          <input size="3" type="text" maxlength="3" name="CountryCode" tabindex="6"  class="input1" onFocus="this.blur()">
                        </td>
                        <td width="25" bgcolor="#E6E9F0"> 
                          <input size="3" type="text" maxlength="3" name="AreaCode" tabindex="7"  class="input1" onFocus="this.blur()">
                        </td>
                        <td width="30" bgcolor="#E6E9F0"> 
                          <input size="7" type="text" maxlength="7" name="Number" tabindex="8"  class="input1" onFocus="this.blur()">
                        </td>
                        <td width="25" bgcolor="#E6E9F0"> 
                          <input size="5" type="text" maxlength="5" name="Ext" tabindex="9"  class="input1" onFocus="this.blur()">
                        </td>
                        <td width="20" bgcolor="#E6E9F0"> 
                          <input type="checkbox" name="Preference2" tabindex="9">
                        </td>
                        <td width="178" align="center" bgcolor="#E6E9F0"><a href="#" tabindex="29" OnClick="addToList(document.FirmMaintenance);" onMouseOver="javascript:add.src = image15.src;" onMouseOut="javascript:add.src = image16.src;"><img src="limages/add_off.gif" width="50" height="19" border="0" alt="Add" name="add"></a> 
                        </td>
                      </tr>
                      <tr align="center" valign="bottom"> 
                        <td colspan="7" height="50"> 
                          <select size="3" name="PhoneList" onClick="popAgain(PhoneList,this.form.PhoneList.value)" class="multiselect">
                          </select>
                        </td>
                      </tr>
                      <tr align="center" valign="bottom"> 
                        <td colspan="7" height="30"><a href="#" OnClick="deleteFromList(document.FirmMaintenance);" onMouseOver="javascript:delsel.src = image17.src;" onMouseOut="javascript:delsel.src = image18.src;"><img src="limages/delsel_off.gif" width="138" height="19" border="0" alt="Delete Selected" name="delsel" vspace="0"></a> 
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
              <input type="hidden" name="sourceInd" value="BKR">
              <input type="hidden" name="sourceId1" value="">
              <input type="hidden" name="sourceId2" value="0">
              <input type="hidden" name="sourceId3" value="0">
              <input type="hidden" name="GoTo" value="FirmMaintenanceAdminSys.jsp">
              <input type="hidden" name="WhereToGo" value="Blank.htm">
              <input type="hidden" name="SaveExitPage" value="No">
              <input type="hidden" name="FunctionType" value="">
              <input type="hidden" name="PhoneNumbers">
              <input type="hidden" name="StatusIndicator" value="">
              <input type="hidden" name="OldNumberIndicator" value="false">
              <input type="hidden" name="PhoneIK" value="0">
              <input type="hidden" name="PhoneAction" value="">
              <input type="hidden" name="TitleButton" value="">
            </td>
          </tr>
        </table>
      </td>
      <td width="5">&nbsp;</td>
    </tr>
  </table>
  </FORM>


<!-- FOR SAVING DESTINATION -->
<div id="hidepage" style="position: absolute; left:0px; top:0px; background-color: #0B5F77; layer-background-color: #0B5F77; height: 100%; width: 100%;visibility:hidden">
<TABLE align="center" height="100%">
    <TBODY>
        <TR>
            <TD valign="middle" align="center"><img src="limages/alert.gif" border="0" vspace="15"><br><FONT class="stitle2" style="font-size:12px;">Do you want to save any unsaved information for the form named above?</FONT><br><br><form name="URLer"><input type="hidden" name="myindValue" value=""><INPUT type="button" name="Yes" value="Yes" OnClick="hideLayer('Yes');" class="lebotton2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<INPUT type="button" name="No" value="No" OnClick="hideLayer('No');" class="lebotton2" style="font-size:12px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<INPUT type="button" name="Cancel" value="Cancel" OnClick="hideLayer('Cancel');" class="lebotton2" style="font-size:12px;"></form></TD>
        </TR>
    </TBODY>
</TABLE>
</div>


<!-- FOR SAVING BROKERMAIN -->
<div id="hidepage2" style="position: absolute; left:0px; top:0px; background-color: #0B5F77; layer-background-color: #0B5F77; height: 100%; width: 100%;visibility:hidden">
<TABLE align="center" height="100%">
    <TBODY>
        <TR>
            <TD valign="middle" align="center"><img src="limages/alert.gif" border="0" vspace="15"><br><FONT class="stitle2" style="font-size:12px;">Do you want to save any unsaved information for the form named above?</FONT><br><br><form name="URLer2"><INPUT type="button" name="Yes" value="Yes" OnClick="saveBM('Yes');" class="lebotton2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<INPUT type="button" name="No" value="No" OnClick="saveBM('No');" class="lebotton2" style="font-size:12px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<INPUT type="button" name="Cancel" value="Cancel" OnClick="saveBM('Cancel');" class="lebotton2" style="font-size:12px;"></form></TD>
        </TR>
    </TBODY>
</TABLE>
</div> 

</BODY>
</HTML>