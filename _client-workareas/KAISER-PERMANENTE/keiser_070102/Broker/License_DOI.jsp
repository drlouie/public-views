<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>


<jsp:useBean id="Lic" class="org.kp.broker.vo.LicenseVO" />

<jsp:useBean id="brokerDropDownVO" class="org.kp.broker.vo.BrokerDropDownVO" />

<%
	brokerDropDownVO = (org.kp.broker.vo.BrokerDropDownVO)session.getAttribute("DropDowns");
%>


<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5 for Windows">
<TITLE>License - DOI Information</TITLE>


<%@ include file="script/ValidateLicense.js" %>

<SCRIPT language="JavaScript">

   var oldNo = false;
   var listIndex = 0;

   var listUILength = 0;
   var listUIValues = new Array();

   var enableList = false;

   var doieff;
   var doiexp;
   var doireq;

   var states = new Array() ;

   // Function to hide list if there is no data to display
   function addListHide() {


	<% 
		java.util.Vector v = new java.util.Vector();
		v = brokerDropDownVO.getState();						
		for(int i = 0 ; i < v.size(); i++){
	%>
			states[<%=i%>] = '<%=v.elementAt(i)%>';
	<%}%>	


//      	document.LicenseForm.AddList.style.visibility = "hidden";

	document.LicenseForm.BKRBID.value = "<%=session.getAttribute("BIDinSession")%>";
	document.LicenseForm.LicID.value = "0";
	document.LicenseForm.DOIRequestedDate.focus();
	document.LicenseForm.LicState.value="";

	doireq = "<%=session.getAttribute("doireq")%>";
	doieff = "<%=session.getAttribute("doieff")%>";
	doiexp = "<%=session.getAttribute("doiexp")%>";

	if ( doireq != "null" )
		document.LicenseForm.DOIRequestedDate.value = "<%=session.getAttribute("doireq")%>";
	if ( doieff != "null" )
		document.LicenseForm.DOIEffectiveDate.value = "<%=session.getAttribute("doieff")%>";
	if ( doiexp != "null" )
		document.LicenseForm.DOIExpirationDate.value = "<%=session.getAttribute("doiexp")%>";


	<%
	java.util.Vector licVec = (java.util.Vector) session.getAttribute("ModifiedLicense");
	int vecSize = licVec.size();
	

	for( int i=0; i<vecSize; i++ ) {
		Lic = ( org.kp.broker.vo.LicenseVO ) licVec.elementAt(i);

		if ( Lic.getState() != null && !Lic.getState().equals("") ) {


	%>
	      	document.LicenseForm.AddList.style.visibility = "";
			var addoptions = new Option();


			var elementsMaxLength = new Array();
			var elementsText = new Array();
			var elementsValue = new Array();

			elementsText[0] = "<%=Lic.getState()%>";
			elementsText[1] = "<%=Lic.getLicenseNo()%>";
			elementsText[2] = "<%=Lic.getMainName()%>";
			elementsText[3] = "<%=Lic.getDBAName()%>";
			elementsText[4] = "<%=Lic.getIssued()%>";
			elementsText[5] = "<%=Lic.getRenewed()%>";
			elementsText[6] = "<%=Lic.getExpiration()%>";
			elementsText[7] = "<%=Lic.getExtension()%>";
			elementsText[8] = "<%=Lic.getIndicator()%>";
			
			if ( elementsText[5] == elementsText[4] )
				elementsText[5] = "";
		
			elementsMaxLength[0] = 3;
			elementsMaxLength[1] = 12;
			elementsMaxLength[2] = 15;
			elementsMaxLength[3] = 15; 
			elementsMaxLength[4] = 10;
			elementsMaxLength[5] = 10;
			elementsMaxLength[6] = 10;
			elementsMaxLength[7] = 10; 
			elementsMaxLength[8] = 3; 
	
			for(var i = 0 ; i < elementsMaxLength.length; i++) {

				if(elementsText[i].length < elementsMaxLength[i]) {

					for(j = elementsText[i].length ; j < elementsMaxLength[i]; j++)
						elementsText[i]+= " ";							
						
				}
				else
					elementsText[i] = elementsText[i].substring(0, elementsMaxLength[i]);
			}

			//addoptions.text = elementsText[0] + "-" + elementsText[1] + "-" + elementsText[2] + "-" + elementsText[3] + "-" + elementsText[4] + "-" + elementsText[5] + "-" + elementsText[6] + "-" + elementsText[7] + "-" + elementsText[8];
			addoptions.text = elementsText[0] + " " + elementsText[1] + " " + elementsText[2] + " " + elementsText[3] + " " + elementsText[4] + " " + elementsText[5] + " " + elementsText[6] + " " + elementsText[7] + " " + elementsText[8];
			addoptions.value = "<%=Lic.getState()%>" + ":" + "<%=Lic.getLicenseNo()%>" + ":" + "<%=Lic.getMainName()%>"+ ":" + "<%=Lic.getDBAName()%>" + ":" + "<%=Lic.getIssued()%>" + ":" + "<%=Lic.getRenewed()%>" + ":" + "<%=Lic.getExpiration()%>" + ":" + "<%=Lic.getExtension()%>" + ":" + "<%=Lic.getLicIdentifier()%>" + ":" + "<%=Lic.getIndicator()%>" + ":" + "<%=Lic.getLipIdentifier()%>";

			document.LicenseForm.AddList.options[document.LicenseForm.AddList.options.length] = addoptions;			

			listUIValues[listUILength] = addoptions.value;
			listUILength++;

		//oldNo = true;



			<%
			if( i == 0 ) {
			%>
				document.LicenseForm.DOIRequestedDate.value="<%= Lic.getApptRequested()%>";
				document.LicenseForm.DOIEffectiveDate.value="<%= Lic.getApptEffective()%>";
				document.LicenseForm.DOIExpirationDate.value="<%= Lic.getApptExpiration()%>";

				doireq = "<%= Lic.getApptRequested()%>";
				doieff = "<%= Lic.getApptEffective()%>";
				doiexp = "<%= Lic.getApptExpiration()%>";

				document.LicenseForm.BKRBID.value = "<%=Lic.getBrokerID()%>";
			
			<%
			}
			%>


			document.LicenseForm.BKRBID.value = "<%=Lic.getBrokerID()%>";

	<%
		}
	}
	%>


	if ( "<%=session.getAttribute("DOIErrorMessage")%>" != "Empty" && "<%=session.getAttribute("DOIErrorMessage")%>" != "null" ) {
			alert("<%=session.getAttribute("DOIErrorMessage")%>");

	}
	
   }



   function validateLicense() {

	if ( validate() ) {

	document.LicenseForm.TypeChangeKey.value = "Submit";
	document.LicenseForm.submit();

	}
   }





   // Function add, modify and manipulate all the functionalities of the list
   function manipulateList( list, state, licno, mname, dbaname, issued, renewed, exp, extn ) {

	var doireq = document.LicenseForm.DOIRequestedDate;
	var doieff = document.LicenseForm.DOIEffectiveDate;
	var doiexp = document.LicenseForm.DOIExpirationDate;


	if ( doireq.value == "" && doieff.value == "" && doiexp.value == "" && state.value == "" &&
		licno.value == "" && mname.value == "" && dbaname.value == "" && issued.value == "" && renewed.value == "" 
			&& exp.value == "" && extn.value == "" ) {

	}
	else {

		if ( validate() ) {

			if ( checkForDuplicateLicense() ) {
				document.LicenseForm.TypeChangeKey.value = "FromList";
				document.LicenseForm.submit(); 
			}
		}

	} //end of else

   }


   function deleteFromList(theForm) {


	if ( theForm.LicState.value == "" && theForm.LicNumber.value == "" && 
		theForm.LicMainName.value == "" && theForm.LicDBAName.value == "" && 
		theForm.LicIssuedDate.value == "" && theForm.LicRenewedDate.value == "" &&
		theForm.LicExtensionDate.value == "" && theForm.LicExpirationDate.value == "" ) {

		//alert( "A record has to be selected first, to be deleted from the list");
		if ( theForm.AddList.length > 0 )
			alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.SelectRecordToDelete")%>' );
		else
			alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.NoRecordToDelete")%>' );		
	}
	else {

		if ( theForm.StatusIndicator.value == "D" ) {
			//alert( "The selected record is already marked for deletion" );
			alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.RecordMarkedDelete")%>' );
			theForm.TypeChangeKey.value = "FromListDelete";
			theForm.submit();

		}
		else {

			theForm.TypeChangeKey.value = "FromListDelete";
			theForm.submit();
		}
	
	}



   }

   function checkForDuplicateLicense() {

	var selectedIndex = "-1";
	var addListLength = document.LicenseForm.AddList.options.length;

	for( var m=0; m < addListLength; m++ ) {
		if ( document.LicenseForm.AddList.options[m].selected == true ) {
			selectedIndex = m;
			break;
		}
	}

	var st = document.LicenseForm.LicState.value;
	st = st.toUpperCase();
	var lic = document.LicenseForm.LicNumber.value;
	lic = lic.toUpperCase();
	var stlic = st + "-" + lic;

	var stLicValues = "";
	var StateLicense = "";
	var licStatus = true;

	var splitData = new Array();
       
	for ( var k=0; k<addListLength; k++ ) {
		
	
		if ( selectedIndex != k )  {

			stLicValues = document.LicenseForm.AddList.options[k].value;

			var j = 0;
			var count = new Array();
			for (var i=0; i < stLicValues.length; i++) {
				temp = "" + stLicValues.substring(i, i+1);

				if ( temp == (":" ) ) {
					count[j] = i;
					j++;
				}
		
			}
			count[j] = stLicValues.length;

			var x = 0;
			for ( i=0; i < count.length; i++ ) {
				splitData[i] = stLicValues.substring( x, count[i] );
				x = count[i]+1;
			}
	
			StateLicense = splitData[0]+ "-" + splitData[1];

			if ( stlic == StateLicense ) {
				//alert( "Cannot duplicate License. A License with the same number and state already exists" );
				alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.license.DuplicateLicense")%>' );
				licStatus = false;
				break;
			}
		}

	}

	if ( licStatus)
		return true;
	else
		return false;

   }


   function popAgain( popList, popValue ) {

	if ( enableList ) {

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


	if ( splitData[1] == undefined ) {
		alert( '<%=org.kp.base.web.util.MessageUtil.getInstance().getText("broker.SelectProperRecord")%>' );
	}
	else {
		document.LicenseForm.LicState.value = splitData[0];
		document.LicenseForm.LicNumber.value = splitData[1];
		document.LicenseForm.LicMainName.value = splitData[2];
		document.LicenseForm.LicDBAName.value = splitData[3];
		document.LicenseForm.LicIssuedDate.value = splitData[4];
		
		if ( splitData[5] == splitData[4] )
			splitData[5] = "";
		document.LicenseForm.LicRenewedDate.value = splitData[5];
		document.LicenseForm.LicExpirationDate.value = splitData[6];
		document.LicenseForm.LicExtensionDate.value = splitData[7];
		document.LicenseForm.LicID.value = splitData[8];
		document.LicenseForm.StatusIndicator.value = splitData[9];
		document.LicenseForm.LipIdentifier.value = splitData[9];	
	
		oldNo = true;
	
	}

	}
   }


   function resetForm(theForm) {

	var hbkrbid = theForm.BKRBID.value;
	var hLicID = theForm.LicID.value;
	var hkey = theForm.TypeChangeKey.value;
	var ind = theForm.indicator.value;
	var stsind = theForm.StatusIndicator.value;
	
	var tempdoireq = "<%=session.getAttribute("doireq")%>";
	var tempdoieff = "<%=session.getAttribute("doieff")%>";
	var tempdoiexp = "<%=session.getAttribute("doiexp")%>";

	theForm.reset();

	theForm.DOIEffectiveDate.value = tempdoieff;
	theForm.DOIExpirationDate.value = tempdoiexp;
	theForm.DOIRequestedDate.value = tempdoireq;
	theForm.BKRBID.value = hbkrbid;
	
	/*
	theForm.LicID.value = hLicID;
	theForm.TypeChangeKey.value = hkey;
	theForm.indicator.value = ind;
	theForm.StatusIndicator.value = stsind;
	*/
	theForm.LicState.value = "";

   }

   function enableLicForm(theForm) {

   	var totalElements = theForm.elements.length;
	var licID = theForm.LicID.value;
	

	for ( var i = 0 ; i <totalElements ; i++) {

		if ( licID != "" && licID > 0 ) {
		
			if ( theForm.elements[i].type != "button" ) {
				theForm.elements[i].style.background = "white";
				theForm.elements[i].onfocus = null;
			}
		}
    	}


	enableList = true;
	theForm.AddList.style.background = "white";

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


<BODY bgcolor="#0B5F77" OnLoad="addListHide()">

<FORM name="LicenseForm" method="POST" action="LicenseServlet" OnSubmit="return validateLicense()">


  <table width="95%" border="0" cellspacing="0" cellpadding="2" align="center">
    <tr align="center" valign="middle"> 
      <td> 
        <table width="670" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td align="left" width="3" height="20"><img src="limages/tleft3.gif" width="3" height="20"></td>
            <td bgcolor="#E6E9F0" width="332" align="left"><font class="stitle">&nbsp;&nbsp;&nbsp;License 
              / DOI</font></td>
            <td bgcolor="#E6E9F0" width="335" align="right"> 
              <input type="button" value="Edit" name="Edit" class="lebotton" onClick="enableLicForm(document.LicenseForm)">
              <input type="button" value="Reset" name="button" onClick="resetForm(document.LicenseForm);" class="lebotton">
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
                  <td class="label" align="center" valign="bottom" width="121" height="25">&nbsp; 
                  </td>
                  <td class="label" width="125" height="25" valign="bottom"></td>
                  <td class="label" align="center" width="100" height="25" valign="bottom"><font class="ComTitle">Requested</font></td>
                  <td class="label" align="center" width="100" height="25" valign="bottom"><font class="ComTitle">Effective</font></td>
                  <td class="label" align="center" width="100" height="25" valign="bottom"><font class="ComTitle">Expiration</font></td>
                  <td class="label" align="center" valign="bottom" width="122" height="25">&nbsp; 
                  </td>
                </tr>
                <tr>
                  <td class="label" bgcolor="#E6E9F0" align="center" valign="bottom" width="121">&nbsp;</td>
                  <td class="title" width="125" bgcolor="#E6E9F0" align="right"><font class="stitle">DOI 
                    Appointment -&gt;</font></td>
                  <td valign="middle" align="center" width="100" bgcolor="#E6E9F0"> 
                    <input size="11" type="text" maxlength="10" name="DOIRequestedDate" class="input2" tabindex="1">
                  </td>
                  <td valign="middle" align="center" width="100" bgcolor="#E6E9F0"> 
                    <input size="11" type="text" maxlength="10" name="DOIEffectiveDate" class="input2" tabindex="2">
                  </td>
                  <td valign="middle" align="center" width="100" bgcolor="#E6E9F0"> 
                    <input size="11" type="text" maxlength="10" name="DOIExpirationDate" class="input2" tabindex="3">
                  </td>
                  <td class="label" bgcolor="#E6E9F0" align="center" valign="bottom" width="122">&nbsp;</td>
                </tr>
                </tbody> 
              </table>
              <table cellpadding="0" cellspacing="0" width="100%" align="center">
                <tbody> 
                <tr align="center" valign="bottom"> 
                  <td class="label" height="25"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>State</font></td>
                  <td class="label" height="25"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>License</font></td>
                  <td class="label" height="25"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Main Name</font></td>
                  <td class="label" height="25"><font class="ComTitle">DBA Name</font></td>
                  <td class="label" height="25"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Issued</font></td>
                  <td class="label" height="25"><font class="ComTitle">Renewed</font></td>
                  <td class="label" height="25"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Expiration</font></td>
                  <td class="label" height="25"><font class="ComTitle">Extension</font></td>
                  <td class="label" height="25">&nbsp;</td>
                </tr>
                <tr align="center"> 
                  <td bgcolor="#E6E9F0"> 
                    <select name="LicState" class="select2" tabindex="4">
                      <option value='AL'>AL</option>
                      <option value='AK'>AK</option>
                      <option value='AS'>AS</option>
                      <option value='AZ'>AZ</option>
                      <option value='AR'>AR</option>
                      <option value='CA'>CA</option>
                      <option value='CZ'>CZ</option>
                      <option value='CO'>CO</option>
                      <option value='CT'>CT</option>
                      <option value='DE'>DE</option>
                      <option value='DC'>DC</option>
                      <option value='FL'>FL</option>
                      <option value='GA'>GA</option>
                      <option value='GU'>GU</option>
                      <option value='HI'>HI</option>
                      <option value='ID'>ID</option>
                      <option value='IL'>IL</option>
                      <option value='IN'>IN</option>
                      <option value='IA'>IA</option>
                      <option value='KS'>KS</option>
                      <option value='KY'>KY</option>
                      <option value='LA'>LA</option>
                      <option value='ME'>ME</option>
                      <option value='MD'>MD</option>
                      <option value='MA'>MA</option>
                      <option value='MI'>MI</option>
                      <option value='MN'>MN</option>
                      <option value='MS'>MS</option>
                      <option value='MO'>MO</option>
                      <option value='MT'>MT</option>
                      <option value='NE'>NE</option>
                      <option value='NV'>NV</option>
                      <option value='NH'>NH</option>
                      <option value='NJ'>NJ</option>
                      <option value='NM'>NM</option>
                      <option value='NY'>NY</option>
                      <option value='NC'>NC</option>
                      <option value='ND'>ND</option>
                      <option value='OH'>OH</option>
                      <option value='OK'>OK</option>
                      <option value='ON'>ON</option>
                      <option value='OR'>OR</option>
                      <option value='PA'>PA</option>
                      <option value='PR'>PR</option>
                      <option value='RI'>RI</option>
                      <option value='SC'>SC</option>
                      <option value='SD'>SD</option>
                      <option value='TN'>TN</option>
                      <option value='TX'>TX</option>
                      <option value='VI'>VI</option>
                      <option value='UT'>UT</option>
                      <option value='VT'>VT</option>
                      <option value='VA'>VA</option>
                      <option value='WA'>WA</option>
                      <option value='WV'>WV</option>
                      <option value='WI'>WI</option>
                      <option value='WY'>WY</option>
                    </select>
                  </td>
                  <td bgcolor="#E6E9F0"> 
                    <input size="11" type="text" maxlength="10" name="LicNumber" class="input2" tabindex="5">
                  </td>
                  <td bgcolor="#E6E9F0"> 
                    <input size="11" type="text" maxlength="30" name="LicMainName" class="input2" tabindex="6">
                  </td>
                  <td bgcolor="#E6E9F0"> 
                    <input size="11" type="text" maxlength="30" name="LicDBAName" class="input2" tabindex="7">
                  </td>
                  <td bgcolor="#E6E9F0"> 
                    <input size="11" type="text" maxlength="10" name="LicIssuedDate" class="input2" tabindex="8">
                  </td>
                  <td bgcolor="#E6E9F0"> 
                    <input size="11" type="text" maxlength="10" name="LicRenewedDate" class="input2" tabindex="9">
                  </td>
                  <td bgcolor="#E6E9F0"> 
                    <input size="11" type="text" maxlength="10" name="LicExpirationDate" class="input2" tabindex="10">
                  </td>
                  <td bgcolor="#E6E9F0"> 
                    <input size="11" type="text" maxlength="10" name="LicExtensionDate" class="input2" tabindex="11">
                  </td>
                  <td bgcolor="#E6E9F0"><a href="#" tabindex="29" OnClick="javascript:return manipulateList(LicenseForm.AddList, LicenseForm.LicState, LicenseForm.LicNumber, LicenseForm.LicMainName, LicenseForm.LicDBAName, LicenseForm.LicIssuedDate, LicenseForm.LicRenewedDate, LicenseForm.LicExpirationDate, LicenseForm.LicExtensionDate)" onMouseOver="javascript:add.src = image15.src;" onMouseOut="javascript:add.src = image16.src;"><img src="limages/add_off.gif" width="50" height="19" border="0" alt="Add" name="add" tabindex="12"></a></td>
                </tr>
                </tbody> 
              </table>
              <table width="100%" border="0" cellspacing="0" cellpadding="2">
                <tr align="center" valign="bottom"> 
                  <td colspan="7"> 
                    <select size="3" name="AddList"  onclick="return popAgain(AddList,this.form.AddList.value)"  OnKeyPress="return popAgain(AddList,this.form.AddList.value)" OnKeyUp="return popAgain(AddList,this.form.AddList.value)" OnKeyDown="return popAgain(AddList,this.form.AddList.value)" class="multiselect2" style="background-color:#ffffff">
                    </select>
                  </td>
                </tr>
                <tr align="center" valign="bottom"> 
                  <td colspan="7"><a href="#" onClick="deleteFromList(document.LicenseForm);" onMouseOver="javascript:delsel.src = image17.src;" onMouseOut="javascript:delsel.src = image18.src;"><img src="limages/delsel_off.gif" width="138" height="19" border="0" alt="Delete Selected" name="delsel" vspace="0"></a> 
			      <INPUT type="hidden" name="BKRBID" value="">
			      <INPUT type="hidden" name="LicID" value="0">
			      <INPUT type="hidden" name="TypeChangeKey">
			      <INPUT type="hidden" name="indicator" value="0">
			      <INPUT type="hidden" name="StatusIndicator" value="">
			      <INPUT type="hidden" name="LipIdentifier" value="-1">			      
			      <INPUT type="hidden" name="SaveExitPage" value="No">	                  
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


</FORM>
</BODY>
</HTML>

