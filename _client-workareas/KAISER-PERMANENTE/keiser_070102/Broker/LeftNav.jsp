<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<TITLE></TITLE>

<jsp:useBean id="brokerDropDownVO" class="org.kp.broker.vo.BrokerDropDownVO" />

<%
	brokerDropDownVO = (org.kp.broker.vo.BrokerDropDownVO)session.getAttribute("DropDowns");
%>

<%@ include file="script/ValidateAddress.js" %>

<Script src="script/ValidateDOI.js">
</Script>


<%@ include file="script/ContactRequiredFields.js" %>




<!-- START JAVSCRIPT REDOS BY DRLOUIE -->

<Script language="JavaScript">

   var states = new Array() ;
   var canadianStates = new Array();
   var BRKBIDValue = "<%=session.getAttribute("BIDinSession")%>";


   function formURL(este) {

	if ( BRKBIDValue == "" || BRKBIDValue == null ) {
		alert( "Well! Where is the broker ID?" );
		return this.href = "/funny.htm";
	}
	else {

		if ( parent.destination.document.forms[0] != undefined ) {

			var indValue = document.LeftNavForm.indicator.value;
			if ( indValue != este ) {
				parent.BrokerMain.showLayer(este);
			}

		}
		else {
			document.LeftNavForm.UserVisitIndicator.value = este;

			document.LeftNavForm.BKRBID.value = BRKBIDValue;
			document.LeftNavForm.indicator.value = este;
			if (este == "1") { document.LeftNavForm.TypeChangeKey.value = "UnLoad"; }
			else { document.LeftNavForm.TypeChangeKey.value = ""; }

			if (este == "1") { document.forms[0].action = "AdditionalAddressServlet"; }
			else if (este == "2") { document.forms[0].action = "AgreementsServlet"; }
			else if (este == "3") { document.forms[0].action = "LicenseServlet"; }
			else if (este == "4") { document.forms[0].action = "PaymentControlsServlet"; }
			else if (este == "5") { document.forms[0].action = "ContactPersonServlet"; }
			else if (este == "6") { document.forms[0].action = "RelationshipServlet"; }
			
			document.forms[0].target="destination";
			document.forms[0].submit();

	   		resetMenu();
			if (este == "1") { document.images.Address.src = menu1.src; setTimeout('upTitle(1)',1000); }
			else if (este == "2") { document.images.Agreement.src = menu1.src; setTimeout('upTitle(2)',1000); }
			else if (este == "3") { document.images.License.src = menu1.src; setTimeout('upTitle(3)',1000); }
			else if (este == "4") { document.images.Payment.src = menu1.src; setTimeout('upTitle(4)',1000); }
			else if (este == "5") { document.images.Contact.src = menu1.src; setTimeout('upTitle(5)',1000); }
			else if (este == "6") { document.images.Relation.src = menu1.src; setTimeout('upTitle(6)',1000); }
		}
	}


}
</script>


<script language="javascript">
function runURL(myindValue,cual) {

		var retValue = cual;
		
			if ( retValue == "Yes" ) {
				if ( validateDestinationForm( parent.destination.document.forms[0] ) ) {
					document.LeftNavForm.indicator.value = myindValue;
					parent.destination.document.forms[0].indicator.value = myindValue;
					parent.destination.document.forms[0].TypeChangeKey.value = "Submit";
					setFormValues();
					parent.destination.document.forms[0].submit();
                        
				}
			}
			else if ( retValue == "No" ) {
				// only for 1
				if (myindValue == "1") { document.LeftNavForm.UserVisitIndicator.value = "1"; }
		
				if (myindValue == "5" || myindValue == "6") { document.LeftNavForm.bid.value = BRKBIDValue; }
				else { document.LeftNavForm.BKRBID.value = BRKBIDValue; }


				document.LeftNavForm.indicator.value = myindValue;

				// Unload only for 1
				if (myindValue == "1") { document.LeftNavForm.TypeChangeKey.value = "UnLoad"; }
				else { document.LeftNavForm.TypeChangeKey.value = ""; }

				if (myindValue == "1") { var nextURL = "AdditionalAddressServlet"; }
				else if (myindValue == "2") { var nextURL = "AgreementsServlet"; }
				else if (myindValue == "3") { var nextURL = "LicenseServlet"; }
				else if (myindValue == "4") { var nextURL = "PaymentControlsServlet"; }
				else if (myindValue == "5") { var nextURL = "ContactPersonServlet"; }
				else if (myindValue == "6") { var nextURL = "RelationshipServlet"; }

				document.forms[0].action = nextURL;
				document.forms[0].target="destination";
				document.forms[0].submit();

			}


	///////////////////////////////////////////////
	/// ADDED BY DRLOUIE -> Menu Image Controls ///
	///////////////////////////////////////////////
	if ( retValue != "Cancel") {
   		resetMenu();

		if (myindValue == "1") { document.images.Address.src = menu1.src; setTimeout('upTitle(1)',2000); }
		else if (myindValue == "2") { document.images.Agreement.src = menu1.src; setTimeout('upTitle(2)',2000); }
		else if (myindValue == "3") { document.images.License.src = menu1.src; setTimeout('upTitle(3)',2000); }
		else if (myindValue == "4") { document.images.Payment.src = menu1.src; setTimeout('upTitle(4)',2000); }
		else if (myindValue == "5") { document.images.Contact.src = menu1.src; setTimeout('upTitle(5)',2000); }
		else if (myindValue == "6") { document.images.Relation.src = menu1.src; setTimeout('upTitle(6)',2000); }
	}

}
</script>
<script language="javascript">
function upTitle(cual) {

	startStuff = "<table width='380' border='0' cellspacing='0' cellpadding='0'><tr><td align='left' width='3' height='20'><img src='limages/tleft4.gif' width='3' height='24'></td><td bgcolor='#E6E9F0' width='374'><font class='maintitle' id='theTitle'><nobr>";
	endStuff = "</nobr></font></td><td 'align='right' width='3' height='20'><img src='limages/tright4.gif' width='3' height='24'></td></tr></table>";

	leSrc= parent.BrokerMain.location.href;

	if (leSrc.indexOf('AgentMaintenance') != -1) {
		if (cual == "0") { parent.BrokerMain.document.getElementById("leTitle").innerHTML = startStuff+"BKR101 Administer Broker Agent"+endStuff; }
		else if (cual == "1") { parent.BrokerMain.document.getElementById("leTitle").innerHTML = startStuff+"BKR102 Administer Broker Agent - <font style=\"font-size:9px;font-weight:normal;\">Additional Addresses</font>"+endStuff; }
		else if (cual == "2") { parent.BrokerMain.document.getElementById("leTitle").innerHTML = startStuff+"BKR103 Administer Broker Agent - <font style=\"font-size:9px;font-weight:normal;\">Agreements</font>"+endStuff; }
		else if (cual == "3") { parent.BrokerMain.document.getElementById("leTitle").innerHTML = startStuff+"BKR104 Administer Broker Agent - <font style=\"font-size:9px;font-weight:normal;\">License / DOI</font>"+endStuff; }
		else if (cual == "4") { parent.BrokerMain.document.getElementById("leTitle").innerHTML = startStuff+"BKR105 Administer Broker Agent - <font style=\"font-size:9px;font-weight:normal;\">Payment Controls</font>"+endStuff; }
		else if (cual == "5") { parent.BrokerMain.document.getElementById("leTitle").innerHTML = startStuff+"BKR106 Administer Broker Agent - <font style=\"font-size:9px;font-weight:normal;\">Contact Person</font>"+endStuff; }
		else if (cual == "6") { parent.BrokerMain.document.getElementById("leTitle").innerHTML = startStuff+"BKR107 Administer Broker Agent - <font style=\"font-size:9px;font-weight:normal;\">Relationships</font>"+endStuff; }
	}
	else {
		if (cual == "0") { parent.BrokerMain.document.getElementById("leTitle").innerHTML = startStuff+"BKR201 Administer Broker Firm"+endStuff; }
		else if (cual == "1") { parent.BrokerMain.document.getElementById("leTitle").innerHTML = startStuff+"BKR202 Administer Broker Firm - <font style=\"font-size:9px;font-weight:normal;\">Additional Addresses</font>"+endStuff; }
		else if (cual == "2") { parent.BrokerMain.document.getElementById("leTitle").innerHTML = startStuff+"BKR203 Administer Broker Firm - <font style=\"font-size:9px;font-weight:normal;\">Agreements</font>"+endStuff; }
		else if (cual == "3") { parent.BrokerMain.document.getElementById("leTitle").innerHTML = startStuff+"BKR204 Administer Broker Firm - <font style=\"font-size:9px;font-weight:normal;\">License / DOI</font>"+endStuff; }
		else if (cual == "4") { parent.BrokerMain.document.getElementById("leTitle").innerHTML = startStuff+"BKR205 Administer Broker Firm - <font style=\"font-size:9px;font-weight:normal;\">Payment Controls</font>"+endStuff; }
		else if (cual == "5") { parent.BrokerMain.document.getElementById("leTitle").innerHTML = startStuff+"BKR206 Administer Broker Firm - <font style=\"font-size:9px;font-weight:normal;\">Contact Person</font>"+endStuff; }
		else if (cual == "6") { parent.BrokerMain.document.getElementById("leTitle").innerHTML = startStuff+"BKR207 Administer Broker Firm - <font style=\"font-size:9px;font-weight:normal;\">Relationships</font>"+endStuff; }
	}
}
</script>

<!-- END JAVSCRIPT REDOS BY DRLOUIE -->




<!-- START JAVASCRIPT ADDITIONS BY DRLOUIE -->

<!--Dynamic CSS Javascript-->
<script language="javascript" src="script/common_css.js">
</script>

<script language="Javascript">
<!--
//MOUSEOVER IMAGE PRELOAD
menu1 = new Image();
menu1.src = "limages/menu_arrow_on.gif";
menu2 = new Image();
menu2.src = "limages/menu_arrow_off.gif";
//RESETS MENU ITEMS TO NON-ACTIVE STATUS -> Called from original JS ie: formURL()
function resetMenu() {
     document.images.Address.src = menu2.src;
     document.images.Agreement.src = menu2.src;
     document.images.License.src = menu2.src;
     document.images.Payment.src = menu2.src;
     document.images.Contact.src = menu2.src;
     document.images.Relation.src = menu2.src;
}
//-->
</script>

<!-- END JAVASCRIPT ADDITIONS BY DRLOUIE -->




<Script language="JavaScript">

   function setFormValues() {

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

	if ( parent.destination.document.forms[0].name == "Relationship" ) {
		parent.destination.document.forms[0].opmode.value="save";
		parent.destination.document.forms[0].submitField.value="submit";
	}


   }


   function validateDestinationForm(theForm) {

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



	if ( theForm.name == "AddTypeForm" ) {

		if ( validate(theForm) ) {
			return true;
		}
		else
			return false;
	}
	else if ( theForm.name == "ContactPerson" ) {
		if ( validateContactForm(theForm) )
			return true;
		else
			return false;
	}
	else if ( theForm.name == "LicenseForm" ) {
		if ( validateDOIValues(theForm) )
			return true;
		else
			return false;
	}
	else
		return true;



   }



</Script>



</HEAD>
<BODY bgcolor="#0B5F77" vlink="#333366" alink="#333366" link="#333366">

<table width="165" border="0" cellspacing="0" cellpadding="0">
<tr><td width="165" height="31"><img name="Address" src="limages/menu_arrow_off.gif" alt="Address" width="165" height="31" border="0" vspace="0"></td></tr>
<tr><td width="165" height="31"><img name="Agreement" src="limages/menu_arrow_off.gif" alt="Agreement" width="165" height="31" border="0" vspace="0"></td></tr>
<tr><td width="165" height="31"><img name="License" src="limages/menu_arrow_off.gif" alt="License" width="165" height="31" border="0" vspace="0"></td></tr>
<tr><td width="165" height="31"><img name="Payment" src="limages/menu_arrow_off.gif" alt="Payment" width="165" height="31" border="0" vspace="0"></td></tr>
<tr><td width="165" height="31"><img name="Contact" src="limages/menu_arrow_off.gif" alt="Contact" width="165" height="31" border="0" vspace="0"></td></tr>
<tr><td width="165" height="31"><img name="Relation" src="limages/menu_arrow_off.gif" alt="Relation" width="165" height="31" border="0" vspace="0"></td></tr>
</table>




<FORM name="LeftNavForm" method="post" action="LeftNav.jsp">
<INPUT type="hidden" name="bid" value="">
<INPUT type="hidden" name="BKRBID" value="">
<INPUT type="hidden" name="TypeChangeKey" value="">
<INPUT type="hidden" name="queryurl" value="">
<INPUT type="hidden" name="indicator" value="0">
<INPUT type="hidden" name="UserVisitIndicator" value="">
<INPUT type="hidden" name="ImageIndicator" value="">


<div style="position:absolute; z-index:15; left:5px; top:3px;" class="menu1"><a href="#" OnClick="formURL('1');" class="menulinks">Additional Addresses</a></div>
<div style="position:absolute; z-index:15; left:5px; top:34px;" class="menu2"><a href="#" OnClick="formURL('2');" class="menulinks">Agreements</a></div>
<div style="position:absolute; z-index:15; left:5px; top:65px;" class="menu3"><a href="#" OnClick="formURL('3');" class="menulinks">License / DOI</a></div>
<div style="position:absolute; z-index:15; left:5px; top:96px;" class="menu4"><a href="#" OnClick="formURL('4');" class="menulinks">Payment Controls</a></div>
<div style="position:absolute; z-index:15; left:5px; top:127px;" class="menu5"><a href="#" OnClick="formURL('5');" class="menulinks">Contact Person Info</a></div>
<div style="position:absolute; z-index:15; left:5px; top:158px;" class="menu6"><a href="#" OnClick="formURL('6');" class="menulinks">Relationships</a></div>

</FORM>


</BODY>
</HTML>
