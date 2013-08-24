<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<META http-equiv="Content-Style-Type" content="text/css">
<TITLE>Broker Administration System Exchange</TITLE>

<Script language="JavaScript">

   function setTitle() {
	
	if ( parent.BrokerMain.document.forms[0] != undefined )
		parent.BrokerMain.document.AgentCompleteSetup.TitleButton.value = "BKR101 Administer Broker Agent (Complete Setup)";
   }

   function setTabTitle() {

	if ( parent.destination.document.forms[0] != undefined ) {

		var formname = parent.destination.document.forms[0].name;

		if ( parent.BrokerMain.document.forms[0] != undefined ) {		

			if ( formname == "AddTypeForm" ) {
				parent.BrokerMain.document.AgentCompleteSetup.TitleButton.value = "BKR102 Administer Broker Agent (Additional Addresses)";
				parent.BrokerMain.document.AgentCompleteSetup.FunctionType.value = "DMGR";
				setImage(parent.LeftNav.document.forms[0],1);
			}
			else if ( formname == "AgreementsForm" ) {
				parent.BrokerMain.document.AgentCompleteSetup.TitleButton.value = "BKR103 Administer Broker Agent (Agreements)";
				parent.BrokerMain.document.AgentCompleteSetup.FunctionType.value = "AGRMT";
				setImage(parent.LeftNav.document.forms[0],2);
			}
			else if ( formname == "LicenseForm" ) {
				parent.BrokerMain.document.AgentCompleteSetup.TitleButton.value = "BKR104 Administer Broker Agent (License / DOI)";
				parent.BrokerMain.document.AgentCompleteSetup.FunctionType.value = "LIC";
				setImage(parent.LeftNav.document.forms[0],3);
			}
			else if ( formname == "PaymentControlsForm" ) {
				parent.BrokerMain.document.AgentCompleteSetup.TitleButton.value = "BKR105 Administer Broker Agent (Payment Controls)";
				parent.BrokerMain.document.AgentCompleteSetup.FunctionType.value = "PMTCNTL";
				setImage(parent.LeftNav.document.forms[0],4);
			}
			else if ( formname == "ContactPerson" ) {
				parent.BrokerMain.document.AgentCompleteSetup.TitleButton.value = "BKR106 Administer Broker Agent (Contact Person)";
				parent.BrokerMain.document.AgentCompleteSetup.FunctionType.value = "CNTCT";	
				setImage(parent.LeftNav.document.forms[0],5);
			}
			else if ( formname == "Relationship" ) {
				parent.BrokerMain.document.AgentCompleteSetup.TitleButton.value = "BKR107 Administer Broker Agent (Relationships)";
				parent.BrokerMain.document.AgentCompleteSetup.FunctionType.value = "RLSHP";
				setImage(parent.LeftNav.document.forms[0],6);
			}
		}
	}

   }
   
  
	function setImage(theForm,TabIndicator) {
	
	
		if ( TabIndicator == "1" ) {
	
			theForm.Address.src = "../BASEWeb/images/add_z.gif";	
			theForm.Agreement.src = "../BASEWeb/images/agg_y.gif";	
			theForm.License.src = "../BASEWeb/images/lic_y.gif";	
			theForm.Payment.src = "../BASEWeb/images/pay_y.gif";	
			theForm.Contact.src = "../BASEWeb/images/cont_y.gif";	
			theForm.Relation.src = "../BASEWeb/images/rel_y.gif";	
		}
		else if ( TabIndicator == "2" ) {
	
			theForm.Address.src = "../BASEWeb/images/add_y.gif";	
			theForm.Agreement.src = "../BASEWeb/images/agg_z.gif";	
			theForm.License.src = "../BASEWeb/images/lic_y.gif";	
			theForm.Payment.src = "../BASEWeb/images/pay_y.gif";	
			theForm.Contact.src = "../BASEWeb/images/cont_y.gif";	
			theForm.Relation.src = "../BASEWeb/images/rel_y.gif";	
		}
		else if ( TabIndicator == "3" ) {
	
			theForm.Address.src = "../BASEWeb/images/add_y.gif";	
			theForm.Agreement.src = "../BASEWeb/images/agg_y.gif";	
			theForm.License.src = "../BASEWeb/images/lic_z.gif";	
			theForm.Payment.src = "../BASEWeb/images/pay_y.gif";	
			theForm.Contact.src = "../BASEWeb/images/cont_y.gif";	
			theForm.Relation.src = "../BASEWeb/images/rel_y.gif";	
		}
		else if ( TabIndicator == "4" ) {
	
			theForm.Address.src = "../BASEWeb/images/add_y.gif";	
			theForm.Agreement.src = "../BASEWeb/images/agg_y.gif";	
			theForm.License.src = "../BASEWeb/images/lic_y.gif";	
			theForm.Payment.src = "../BASEWeb/images/pay_z.gif";	
			theForm.Contact.src = "../BASEWeb/images/cont_y.gif";	
			theForm.Relation.src = "../BASEWeb/images/rel_y.gif";	
		}
		else if ( TabIndicator == "5" ) {
	
			theForm.Address.src = "../BASEWeb/images/add_y.gif";	
			theForm.Agreement.src = "../BASEWeb/images/agg_y.gif";	
			theForm.License.src = "../BASEWeb/images/lic_y.gif";	
			theForm.Payment.src = "../BASEWeb/images/pay_y.gif";	
			theForm.Contact.src = "../BASEWeb/images/cont_z.gif";	
			theForm.Relation.src = "../BASEWeb/images/rel_y.gif";	
		}
		else if ( TabIndicator == "6" ) {
	
			theForm.Address.src = "../BASEWeb/images/add_y.gif";	
			theForm.Agreement.src = "../BASEWeb/images/agg_y.gif";	
			theForm.License.src = "../BASEWeb/images/lic_y.gif";	
			theForm.Payment.src = "../BASEWeb/images/pay_y.gif";	
			theForm.Contact.src = "../BASEWeb/images/cont_y.gif";	
			theForm.Relation.src = "../BASEWeb/images/rel_z.gif";	
		}

	}
   

</Script>


</HEAD>
<FRAMESET rows="62%,38%" FRAMESPACING="2" frameborder="NO" border="0">
  <FRAME name="BrokerMain" src="AgentCompleteSetup.jsp" OnFocus="setTitle()" scrolling="auto" marginheight="0" marginwidth="0" TOPMARGIN="0">
  <FRAMESET cols="12%,88%" FRAMESPACING="2" frameborder="NO" border="0">
    <FRAME name="LeftNav" src="LeftNav.jsp" scrolling="no" marginheight="0" marginwidth="0" TOPMARGIN="0">
    <FRAME name="destination"  OnFocus="setTabTitle()" scrolling="auto" marginheight="0" marginwidth="0" TOPMARGIN="0" src="Blank.htm">
  </FRAMESET>
  <NOFRAMES>
  <BODY>
  <P>To view this page, you need a browser that supports frames.</P>
  </BODY>
  </NOFRAMES>
</FRAMESET>
</HTML>
