<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<META http-equiv="Content-Style-Type" content="text/css">
<TITLE>Broker Administration System Exchange</TITLE>

<Script language="JavaScript">

   function setTitle() {
	if ( parent.BrokerMain.document.forms[0] != undefined )
		setTimeout('parent.LeftNav.upTitle(7)',2000);
   }

   function setTabTitle() {

	if ( parent.destination.document.forms[0] != undefined ) {

		var formname = parent.destination.document.forms[0].name;

		if ( parent.BrokerMain.document.forms[0] != undefined ) {		

			if ( formname == "AddTypeForm" ) {
				setTimeout('parent.LeftNav.upTitle(1)',2000);
				parent.BrokerMain.document.FirmMaintenance.FunctionType.value = "DMGR";
				setImage(parent.LeftNav.document.forms[0],1);
			}
			else if ( formname == "AgreementsForm" ) {
				setTimeout('parent.LeftNav.upTitle(2)',2000);
				parent.BrokerMain.document.FirmMaintenance.FunctionType.value = "AGRMT";
				setImage(parent.LeftNav.document.forms[0],2);
			}
			else if ( formname == "LicenseForm" ) {
				setTimeout('parent.LeftNav.upTitle(3)',2000);
				parent.BrokerMain.document.FirmMaintenance.FunctionType.value = "LIC";
				setImage(parent.LeftNav.document.forms[0],3);				
			}
			else if ( formname == "PaymentControlsForm" ) {
				setTimeout('parent.LeftNav.upTitle(4)',2000);
				parent.BrokerMain.document.FirmMaintenance.FunctionType.value = "PMTCNTL";
				setImage(parent.LeftNav.document.forms[0],4);				
			}				
			else if ( formname == "ContactPerson" ) {
				setTimeout('parent.LeftNav.upTitle(5)',2000);
				parent.BrokerMain.document.FirmMaintenance.FunctionType.value = "CNTCT";
				setImage(parent.LeftNav.document.forms[0],5);
			}
			else if ( formname == "Relationship" ) {
				setTimeout('parent.LeftNav.upTitle(6)',2000);
				parent.BrokerMain.document.FirmMaintenance.FunctionType.value = "RLSHP";
				setImage(parent.LeftNav.document.forms[0],6);
			}				
		}

	}

   }
	
	function setDestination() {

		<%
			if ( session.getAttribute("Destination") == null ) {
		%>
			frames['destination'].window.location.href = "Blank.htm";
		<%	}
			else {
		%>
			frames['destination'].window.location.href = "<%=session.getAttribute("Destination").toString()%>";
		<%
			}
		%>
	}
	
	function setImage(theForm,TabIndicator) {
	

//MOUSEOVER IMAGE PRELOAD
menu1 = new Image();
menu1.src = "limages/menu_arrow_on.gif";
menu2 = new Image();
menu2.src = "limages/menu_arrow_off.gif";

		if ( TabIndicator == "1" ) {
			parent.LeftNav.resetMenu();
			parent.LeftNav.document.images.Address.src = menu1.src;
		}
		else if ( TabIndicator == "2" ) {
	
			parent.LeftNav.resetMenu();
			parent.LeftNav.document.images.Agreement.src = menu1.src;
		}
		else if ( TabIndicator == "3" ) {
	
			parent.LeftNav.resetMenu();
			parent.LeftNav.document.images.License.src = menu1.src;
		}
		else if ( TabIndicator == "4" ) {
	
			parent.LeftNav.resetMenu();
			parent.LeftNav.document.images.Payment.src = menu1.src;
		}
		else if ( TabIndicator == "5" ) {
	
			parent.LeftNav.resetMenu();
			parent.LeftNav.document.images.Contact.src = menu1.src;
		}
		else if ( TabIndicator == "6" ) {

			parent.LeftNav.resetMenu();
			parent.LeftNav.document.images.Relation.src = menu1.src;
		}
	}



</Script>

</HEAD>

<FRAMESET rows="375,*" FRAMESPACING="0" frameborder="1" border="3">
  <FRAME name="BrokerMain" src="FirmMaintenance.jsp" OnFocus="setTitle()" noresize scrolling="No" marginheight="0" marginwidth="0" TOPMARGIN="0">
  <FRAMESET cols="165,*" FRAMESPACING="0" frameborder="1" border="3" OnLoad="setDestination()">
    <FRAME name="LeftNav" src="LeftNav.jsp" noresize scrolling="No" marginheight="0" marginwidth="0" TOPMARGIN="0">
    <FRAME name="destination" src="Blank.htm" OnFocus="setTabTitle()" noresize scrolling="No" marginheight="0" marginwidth="0" TOPMARGIN="0">
  </FRAMESET>
  <NOFRAMES>
  <BODY>
  <P>To view this page, you need a browser that supports frames.</P>
  </BODY>
  </NOFRAMES>
</FRAMESET>


</HTML>
