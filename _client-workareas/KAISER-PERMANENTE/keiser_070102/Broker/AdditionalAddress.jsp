<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



<jsp:useBean id="addr" class="org.kp.broker.vo.AddressVO" />

<jsp:useBean id="brokerDropDownVO" class="org.kp.broker.vo.BrokerDropDownVO" />

<%
	brokerDropDownVO = (org.kp.broker.vo.BrokerDropDownVO)session.getAttribute("DropDowns");
%>


<HTML>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<TITLE>Additional Address</TITLE>


<%@ include file="script/ValidateAddress.js" %>


<Script language="JavaScript">


   var addArray = new Array();
   var adrID = new Array();
   var addArrayLength = 0;

   var oldIndex;
   var adrid;

   var states = new Array() ;
   var canadianStates = new Array();

   var adrtype;
   var state = "";
   
   var OrgEffDate = "";

   function populateValues() {

	OrgEffDate = "<%=session.getAttribute("BkrAddrOrgEffDate")%>";
	addArrayLength = 0;

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


	document.AddTypeForm.BKRBID.value = "<%=session.getAttribute("BIDinSession")%>";


	adrtype = "<%=session.getAttribute("AddType")%>";

	document.AddTypeForm.AddressType.focus();


	<%
	java.util.Vector addVec = (java.util.Vector) session.getAttribute("ModifiedAddress");

	int vecSize = addVec.size();
	
	for( int i=0; i<vecSize; i++ ) {
		addr = ( org.kp.broker.vo.AddressVO ) addVec.elementAt(i);

		
	%>
	
		var line1 = "<%=addr.getLine1()%>";
		var line2 = "<%=addr.getLine2()%>";
		var mstop = "<%=addr.getMailStop()%>";
		var city = "<%=addr.getCity()%>";
		var county = "<%=addr.getCounty()%>";
		state = "<%=addr.getState()%>";
		var zip = "<%=addr.getZip()%>";
		var country = "<%=addr.getCountry()%>";
	
		if ( country == "" || country == "null" ) {
			country = "USA";
		}

		adrid = "<%=addr.getAddressID()%>";

		adrID[addArrayLength] = adrid;



		if ( adrtype == "C" && addArrayLength == 0 ) {


				document.AddTypeForm.AddressType.value = "C";

				document.AddTypeForm.AddressLine1.value = "<%=addr.getLine1()%>";
				document.AddTypeForm.AddressLine2.value = "<%=addr.getLine2()%>";
				document.AddTypeForm.MailStop.value = "<%=addr.getMailStop()%>";
				document.AddTypeForm.City.value = "<%=addr.getCity()%>";
				document.AddTypeForm.County.value = "<%=addr.getCounty()%>";
				document.AddTypeForm.State.value = "<%=addr.getState()%>";
				document.AddTypeForm.Zip.value = "<%=addr.getZip()%>";
				document.AddTypeForm.Country.value = country;
				
				setState( document.AddTypeForm );

				document.AddTypeForm.Province.value = "<%=addr.getProvince()%>";				
				document.AddTypeForm.AddressEffectiveDate.value = "<%=addr.getEffectiveDate()%>";

				document.AddTypeForm.AddressID.value = "<%=addr.getAddressID()%>";
				document.AddTypeForm.TypeChangeKey.value = "0";

				document.AddTypeForm.State.disabled= true;
				document.AddTypeForm.Country.disabled = true;
								
			if ( line1 == "" ) {
				enableAll( document.AddTypeForm );

			}


		}
		else if ( adrtype == "P" && addArrayLength == 1 ) {

				document.AddTypeForm.AddressType.value = "P";

				document.AddTypeForm.AddressLine1.value = "<%=addr.getLine1()%>";
				document.AddTypeForm.AddressLine2.value = "<%=addr.getLine2()%>";
				document.AddTypeForm.MailStop.value = "<%=addr.getMailStop()%>";
				document.AddTypeForm.City.value = "<%=addr.getCity()%>";
				document.AddTypeForm.County.value = "<%=addr.getCounty()%>";
				document.AddTypeForm.State.value = "<%=addr.getState()%>";
				document.AddTypeForm.Zip.value = "<%=addr.getZip()%>";
				document.AddTypeForm.Country.value = country;

				setState( document.AddTypeForm );

				document.AddTypeForm.Province.value = "<%=addr.getProvince()%>";				
				document.AddTypeForm.AddressEffectiveDate.value = "<%=addr.getEffectiveDate()%>";

				document.AddTypeForm.AddressID.value = "<%=addr.getAddressID()%>";
				document.AddTypeForm.TypeChangeKey.value = "1";

				document.AddTypeForm.State.disabled= true;
				document.AddTypeForm.Country.disabled = true;


			if ( line1 == "" ) {
				enableAll( document.AddTypeForm );
			}


		}
		else if ( adrtype == "R"  && addArrayLength == 2 ) {

				document.AddTypeForm.AddressType.value = "R";

				document.AddTypeForm.AddressLine1.value = "<%=addr.getLine1()%>";
				document.AddTypeForm.AddressLine2.value = "<%=addr.getLine2()%>";
				document.AddTypeForm.MailStop.value = "<%=addr.getMailStop()%>";
				document.AddTypeForm.City.value = "<%=addr.getCity()%>";
				document.AddTypeForm.County.value = "<%=addr.getCounty()%>";
				document.AddTypeForm.State.value = "<%=addr.getState()%>";
				document.AddTypeForm.Zip.value = "<%=addr.getZip()%>";
				document.AddTypeForm.Country.value = country;
				
				setState( document.AddTypeForm );
				
				document.AddTypeForm.Province.value = "<%=addr.getProvince()%>";				
				document.AddTypeForm.AddressEffectiveDate.value = "<%=addr.getEffectiveDate()%>";

				document.AddTypeForm.AddressID.value = "<%=addr.getAddressID()%>";
				document.AddTypeForm.TypeChangeKey.value = "2";

				document.AddTypeForm.State.disabled= true;
				document.AddTypeForm.Country.disabled = true;


			if ( line1 == "" ) {
				enableAll( document.AddTypeForm );
			}

		}
		


		if ( line2 == "" )
			line2 = "null";
		if ( mstop == "" )
			mstop = "null";
		if ( county == "" )
			county = "null";


		addArray[addArrayLength] = line1 + "-" + line2 + "-" + mstop + "-" + city + "-" +county + "-" +  state + "-" + zip + "-" + country + "-" + adrid;



		if ( "<%=(String) session.getAttribute("onChangeSession")%>" == "" ) {
			oldIndex = 0;
		}
		else {
			oldIndex = "<%=(String) session.getAttribute("onChangeSession")%>";
		}


		addArrayLength++;

	<%
	}
	%>


	
	if ( "<%=session.getAttribute("AdrErrorMessage")%>" != "null" && "<%=session.getAttribute("AdrErrorMessage")%>" != "" ) {
		alert( "<%=session.getAttribute("AdrErrorMessage")%>" );
	
		if ( parent.LeftNav.document.forms[0]!= undefined )
			parent.LeftNav.document.forms[0].indicator.value = "1";	
			
		<%
			session.setAttribute("AdrErrorMessage","");
		%>
	}


   }



   function enableAll(form) { 

   	var totalElements = document.AddTypeForm.elements.length;
	var enableAdrID = document.AddTypeForm.AddressID.value;

	for ( var i = 0 ; i <totalElements ; i++) {

		if ( enableAdrID != "" && enableAdrID > 0 ) {
		
			if ( document.AddTypeForm.elements[i].type != "button" ) {
				document.AddTypeForm.elements[i].style.background = "white";
				document.AddTypeForm.elements[i].onfocus = null;
			}
			//document.AddTypeForm.AddressEffectiveDate.disabled = false;											
		}
		else {
		
			if ( document.AddTypeForm.elements[i].name != "AddressEffectiveDate" &&
					document.AddTypeForm.elements[i].type != "button" ) {
		
				document.AddTypeForm.elements[i].style.background = "white";
				document.AddTypeForm.elements[i].onfocus = null;
				
			}
		}

		document.AddTypeForm.State.disabled= false;
		document.AddTypeForm.Country.disabled = false;
		
   	}
	//document.AddTypeForm.Country.disabled = false;
   }


   function storeValues() {


	if ( validate(document.AddTypeForm) ) {
		document.AddTypeForm.submit();
	}
	else {
		document.AddTypeForm.AddressType.value = adrtype;
		return false;
	}

   }


   function testValidation() {

	if ( validate(document.AddTypeForm) ) {
		document.AddTypeForm.TypeChangeKey.value = "Submit";
		document.AddTypeForm.submit();
	}
	else
		return false;
   }


   function resetAdrForm(theForm) {


	var StateSts = false;
	var CtrySts = false;

	if ( theForm.State.disabled )
		StateSts = true;
		
	if ( theForm.Country.disabled )
		CtrySts = true;

	theForm.reset();
	populateValues();
	
	theForm.State.disabled = StateSts;
	theForm.Country.disabled = CtrySts;
	
	if ( theForm.Country.value == "USA" || theForm.Country.value == "CAN" ) {
	
		if ( !theForm.Country.disabled )
			theForm.State.disabled = false;
	}

	/*
	var hkey = theForm.TypeChangeKey.value;
	var hind = theForm.indicator.value;
	var hbkrbid = theForm.BKRBID.value;
	var hadrid = theForm.AddressID.value;
	var hadrtype = theForm.AddressType.value;
	var hcountry = theForm.Country.value;
	var effdate = theForm.AddressEffectiveDate.value;

	theForm.reset();
	
	
	theForm.State.value = "";
	theForm.TypeChangeKey.value = hkey;
	theForm.indicator.value = hind;
	theForm.BKRBID.value = hbkrbid;
	theForm.AddressID.value = hadrid;
	theForm.AddressType.value = hadrtype;
	theForm.Country.value = hcountry;
	theForm.AddressEffectiveDate.value = effdate;
	*/	
	
   }

	function setState( theForm ) {
	
		var country = theForm.Country.value;
		
		
		if ( country == "USA" ) {
		
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

<!--Dynamic CSS Javascript-->
<script language="javascript" src="script/common_css.js"></script>



<script language="Javascript">
<!--
//MOUSEOVER IMAGE PRELOAD

//mreset
// // // MOUSE OVER
image1 = new Image();
image1.src = "limages/sreset_ov.gif";
// // // MOUSE OFF
image2 = new Image();
image2.src = "limages/sreset_off.gif";

//medit
image3 = new Image();
image3.src = "limages/sedit_ov.gif";
image4 = new Image();
image4.src = "limages/sedit_off.gif";

//-->
</script>

</HEAD>



<BODY bgcolor="#0B5F77" OnLoad="populateValues()">
<FORM name="AddTypeForm" action="AdditionalAddressServlet" method="POST" OnSubmit="return testValidation()">


  <table width="670" border="0" cellspacing="0" cellpadding="2">
    <tr align="center" valign="middle"> 
      <td width="200"><font class="ComTitle">Choose an Address Type<br>
        <img src="limages/3downarrows.gif" width="86" height="16"><br>
        <select name="AddressType" tabindex="1" onChange="return storeValues()" class="select1">
		<%  
			
			java.util.Vector adrTypeText = new java.util.Vector();
			java.util.Vector adrTypeValue = new java.util.Vector();

			adrTypeText = brokerDropDownVO.getAddressTypeText();		
			adrTypeValue = brokerDropDownVO.getAddressTypeValue();		
			
			for(int i = 0 ; i < adrTypeText.size(); i++) {
			
				String adrType = (String) adrTypeValue.elementAt(i);

				if ( !adrType.equals("M") ) {
				
		%>		
					<option value = '<%=adrTypeValue.elementAt(i)%>'><%=adrTypeText.elementAt(i)%></option>
		<%
				}
			}			
		%>
        </select>
		<INPUT type="hidden" name="TypeChangeKey" value="">
		<INPUT type="hidden" name="indicator" value="0">
		<INPUT type="hidden" name="BKRBID" value="<%=session.getAttribute("BIDinSession")%>">
		<INPUT type="hidden" name="AddressID" value="0">
		<INPUT type="hidden" name="SaveExitPage" value="No">		
        </font></td>
      <td width="470"> 
        <table width="375" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td align="left" width="3" height="20"><img src="limages/tleft3.gif" width="3" height="20"></td>
            <td bgcolor="#E6E9F0" width="184" align="left" height="20"><font class="stitle">&nbsp;&nbsp;&nbsp;Additional 
              Addresses</font></td>
            <td bgcolor="#E6E9F0" align="right" height="20"> 
              <input type="button" value="Edit" name="edit" class="lebotton" OnClick="enableAll(document.AddTypeForm)">
              <input type="button" value="Reset" name="button" class="lebotton" OnClick="resetAdrForm(document.AddTypeForm)">
            </td>
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
            <td width="398" align="center"> 
              <table width="373" border="0" cellspacing="0" cellpadding="2">
                <tr valign="bottom"> 
                  <td align="center" width="120" valign="middle" height="45"><font class="ComTitle">Eff 
                    Date </font><br>
                    <input size="11" type="text" maxlength="10" name="AddressEffectiveDate"  class="input1" tabindex="2">
                  </td>
                  <td width="67" align="center" valign="middle">&nbsp;</td>
                  <td width="66" align="center" valign="middle">&nbsp;</td>
                  <td width="120" align="center" valign="middle"><font class="ComTitle">Mail 
                    Stop# </font><br>
                    <input size="11" type="text" maxlength="10" name="MailStop"  class="input2" tabindex="4">
                  </td>
                </tr>
              </table>
              <table width="373" border="0" cellspacing="0" cellpadding="2">
                <tr valign="bottom"> 
                  <td align="right" width="186" height="27"><nobr><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Line 1</font>&nbsp; 
                    <input size="20" type="text" maxlength="50" name="AddressLine1"  class="input2" tabindex=3">
                    </nobr> </td>
                  <td width="75" height="27" align="right"><font class="ComTitle">State</font></td>
                  <td width="37" height="27"> 
                    <select cname="State"  class="select2" name="State" tabindex="8">
                      <option value="">&nbsp;&nbsp;&nbsp;</option>
                    </select>
                  </td>
                  <td height="27" valign="bottom" align="right" width="20"><font class="ComTitle">Zip</font></td>
                  <td width="62" height="27"> 
                    <input size="5" type="text" maxlength="10" name="Zip"  class="input2" tabindex="9">
                  </td>
                </tr>
                <tr valign="bottom"> 
                  <td align="right" width="186"><nobr><font class="ComTitle">Line 
                    2</font>&nbsp; 
                    <input size="20" type="text" maxlength="50" name="AddressLine2"  value="" class="input2" tabindex="5">
                    </nobr></td>
                  <td width="75" align="right"><font class="ComTitle">County</font></td>
                  <td width="187" colspan="3"> 
                    <input size="20" type="text" maxlength="20" name="County"  class="input2" tabindex="10">
                  </td>
                </tr>
                <tr valign="bottom"> 
                  <td align="right" width="186"><nobr><font class="ComTitle">Line 
                    3</font>&nbsp; 
                    <input size="20" type="text" maxlength="50" name="AddressLine3"  class="input2" value="" tabindex="6">
                    </nobr> </td>
                  <td width="75" align="right"><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>Country</font></td>
                  <td width="187" colspan="3"> 
                    <select name="Country" onChange="setState(document.AgentMaintenance)" class="select2" tabindex="11">
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
                  <td align="right" width="186"><nobr><font class="ComTitle"><font style="color:#eb0000;font-size:11px">*</font>City</font>&nbsp; 
                    <input size="20" type="text" maxlength="25" name="City"  class="input2" tabindex="7">
                    </nobr> </td>
                  <td width="75" align="right"><font class="ComTitle">Province</font></td>
                  <td width="187" colspan="3"> 
                    <input size="20" type="text" maxlength="20" name="Province"  class="input2" value="" tabindex="12">
                  </td>
                </tr>
                <tr valign="bottom"> 
                  <td align="right" width="186"><img src="limages/spacer.gif" border="0" width="5" height="5"></td>
                  <td width="187" colspan="4"><img src="limages/spacer.gif" border="0" width="5" height="5"></td>
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