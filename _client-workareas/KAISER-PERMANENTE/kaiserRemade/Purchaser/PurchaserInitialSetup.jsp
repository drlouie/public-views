<!-- Sample JSP file -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<%@ page import = "org.kp.purchaser.vo.PurchaserDropDownVO,org.kp.base.util.BaseUtil" %>
<jsp:useBean id="purchaserAdminVO"  class="org.kp.purchaser.vo.PurchaserAdminVO"  scope="session"></jsp:useBean>
<jsp:useBean id="purchaserInitialVO"  class="org.kp.purchaser.vo.PurchaserInitialVO" 
scope="session"></jsp:useBean>
<jsp:useBean id="purchaserDropDownVO"  class="org.kp.purchaser.vo.PurchaserDropDownVO" 
scope="session"></jsp:useBean><HTML>
<HEAD>
<%@ include file="script/ValidatePurchaserInitial.js" %>
<!--f sdfasf <SCRIPT language="JavaScript1.1" src="/BASEWeb/Purchaser/script/ValidatePurchaserInitial.js"></SCRIPT> -->
<Script src="/BASEWeb/script/PrintScript.js">
</Script>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<META http-equiv="Content-Style-Type" content="text/css">
<STYLE>
<!--
.label {
	COLOR : #0033FF; 
	font-family: arial,verdana,sans-serif;
	font-size : 13px;
	font-weight : bold;
	font-style: normal;	
	}
.title
	{
	COLOR : #FFFFFF; 
	font-family: arial,verdana,sans-serif;
	font-size : 14px;
	font-weight : bold;
	font-style: normal;	

	}
IMG{
  color : olive;
}


-->
</STYLE>
<SCRIPT language="JavaScript">
var oldNo = false;
var states = new Array() ;
var canadianStates = new Array();
var state = "<%=BaseUtil.asString(purchaserInitialVO.getAddress().getState()) %>";
function addListHide() {
<% 
			java.util.Vector stateV = new java.util.Vector();
			stateV = purchaserDropDownVO.getStatesValue();						
			for(int i = 0 ; i < stateV.size(); i++)
				{
		%>
					states[<%=i%>] = '<%=stateV.elementAt(i)%>';
		<%
				}
		%>	

	<% 
		java.util.Vector canSt = new java.util.Vector();
		canSt = purchaserDropDownVO.getCanadianStates();	 					
		for(int i = 0 ; i < canSt.size(); i++){
	%>
			canadianStates[<%=i%>] = '<%=canSt.elementAt(i)%>';
	<%}%>	
		
	
	document.PurchaserInitialSetup.regionDivision.value = "<%=BaseUtil.asString(purchaserInitialVO.getRegion()) %>";
	document.PurchaserInitialSetup.size.value = "<%=BaseUtil.asString(purchaserInitialVO.getSize()) %>";
	document.PurchaserInitialSetup.directSale.value = "<%=BaseUtil.asString(purchaserInitialVO.getDirectSale()) %>";
	document.PurchaserInitialSetup.administrativeSystem.value = "<%=BaseUtil.asString(purchaserInitialVO.getAdminArrangements().getAdminSystem()) %>" ;
	document.PurchaserInitialSetup.administrator.value = "<%=BaseUtil.asString(purchaserInitialVO.getAdminArrangements().getAdministrator()) %>" ;
	document.PurchaserInitialSetup.billingFrequency.value = "<%=BaseUtil.asString(purchaserInitialVO.getAdminArrangements().getBillingFrequency())%>";
	document.PurchaserInitialSetup.country.value = "<%=BaseUtil.asString(purchaserInitialVO.getAddress().getCountry()) %>";
	document.PurchaserInitialSetup.state.value = "<%=BaseUtil.asString(purchaserInitialVO.getAddress().getState()) %>";
	document.PurchaserInitialSetup.country.value = "USA";
	setState( document.PurchaserInitialSetup );	
<%
	
String error = (String) session.getAttribute("ERROR");
	 	if ( ! error.equals("nothing") ) {
%>
	alert("<%=error %>");


	<%
		session.setAttribute("ERROR", "nothing");
	}
	%>

}

  function changeMode()
{
if ( validate(document.PurchaserInitialSetup) )
{
 document.PurchaserInitialSetup.administrator.disabled=false;
 document.PurchaserInitialSetup.opmode.value="save" ;
//alert(document.PurchaserInitialSetup.opmode.value);
}
else{
return false;

}
}

function selectAdministartor()

{
    var count=0;	
    var adsysValue =  document.PurchaserInitialSetup.administrativeSystem.value  ;   
	var adminid = new Array();
	var adminds = new Array();
   

		<%  	
		int count =0;
		java.util.Vector adminidV = new java.util.Vector();
		java.util.Vector admindsV = new java.util.Vector();
	 	java.util.Hashtable administrator =  purchaserDropDownVO.getAdministrators();
		 java.util.Enumeration enum    = administrator.keys();
		int i =0;
		while(enum.hasMoreElements())  { 
		String aValue =(String) enum.nextElement();
		%>
	adminid["<%=i%>"] = "<%=aValue %>";
	adminds["<%=i%>"] = "<%=(String)administrator.get(aValue) %>";
		<%
		   i++;
		 } 
		%>
		 for(var j = 0 ; j < adminid.length ; j++)
		{
			 
 	        if(adsysValue ==adminid[j])
		 {
		  count = j;
		  break;		
		 }			
		}
		  document.PurchaserInitialSetup.administrator.value=adminds[count] ;
 }

function purchaserReset()
{

	document.PurchaserInitialSetup.PID.value ="";
     document.PurchaserInitialSetup.TPAID.value = "";
	document.PurchaserInitialSetup.purchaserName.value = "";
	document.PurchaserInitialSetup.regionDivision.value = "";
	document.PurchaserInitialSetup.size.value = "";
	document.PurchaserInitialSetup.origEffectiveDate.value = "";
	document.PurchaserInitialSetup.terminationDate.value = "";
	document.PurchaserInitialSetup.administrativeSystem.value = "";
	document.PurchaserInitialSetup.administrator.value = "";
	document.PurchaserInitialSetup.billingFrequency.value = "";
	document.PurchaserInitialSetup.effDate.value = "";
	document.PurchaserInitialSetup.endDate.value = "";
	document.PurchaserInitialSetup.adminrelId.value = ""; 
	document.PurchaserInitialSetup.directSale.value = ""; 
	document.PurchaserInitialSetup.country.value = ""; 
	document.PurchaserInitialSetup.state.value="";

}

	function setState( theForm ) {
	
		var country = theForm.country.value;
		if ( country == "USA" ) {
		
			for ( var i=0; i<states.length; i++ ) {
				var addstate = new Option();
				addstate.text = states[i];
				addstate.value = states[i];
				theForm.state.options[i] = addstate;				
			}
			theForm.state.disabled = false;	
			theForm.state.value = state;
		}

		else if ( country == "CAN" ) {

			theForm.state.length = 0;

			for ( var i=0; i<canadianStates.length; i++ ) {
				var addstate = new Option();
				addstate.text = canadianStates[i];
				addstate.value = canadianStates[i];
				theForm.state.options[i] = addstate;				
			}
			theForm.state.disabled = false;
			theForm.state.value = state;			
		}
		else {

			theForm.state.length = 0;				
			theForm.state.disabled = true;
		}

	}





</SCRIPT>


<TITLE>
PUR100 Administer Purchaser (Initial Setup)
</TITLE>
</HEAD>

<BODY BGCOLOR="#999999" OnLoad="addListHide() ">
<FORM name="PurchaserInitialSetup" method="POST" action= "PurchaserInitialServlet">
<TABLE>
  <TBODY>
    <TR>
      <TD bgcolor="#999999" width="778" height="365">
      <TABLE width="100%" cellpadding="0" cellspacing="0">
        <TBODY>
          <TR>
            <TD class="title" bgcolor="#ffcc00"><FONT color="#0033cc">PUR 100 Administer Purchaser ( Initial Setup )</FONT></TD>
            <TD class="title" align="right" bgcolor="#ffcc00"><A href="/BASEWeb/Purchaser/PurchaserInquiry.jsp" target="_parent"><IMG src="images/search.gif" width="72" height="22" border="0"></A><INPUT type="image" name="submit" value="save" src="images/save.gif" onclick="return changeMode()"><IMG src="images/print.gif" width="50" height="22" border="0" OnClick="callPrint()"><IMG src="images/exit.gif" width="50" height="22" border="0"><IMG src="images/comments.gif" width="86" height="22" border="0"></TD>
	          
</TR>
        </TBODY>
      </TABLE>
      <TABLE cellpadding="1" cellspacing="1" width="814">
        <TBODY>
          <TR>
                        <TD align="right" class="label" width="147">Orig Effective Date<FONT color="#ff0033"><FONT size="+1">*</FONT></FONT></TD>
                        <TD align="left" width="141">
		<input type="hidden" name="opmode" value="">
		<input type="hidden" name="adminrelId" value="0">
		<input type="hidden" name="statusIndicator" value="">
            <INPUT size="10" type="text" maxlength="10" name="origEffectiveDate" value="<%=BaseUtil.asString(purchaserInitialVO.getOrigEffectiveDate() )%>" tabindex="1">
            </TD>
                        <TD class="label" align="right" width="123">Termination Date</TD>
            <TD align="left" width="86">
            <INPUT size="9" type="text" maxlength="10" name="terminationDate" value="<%=BaseUtil.asString(purchaserInitialVO.getTerminationDate() )%>">
            </TD>
            <TD class="label" align="right" width="65"></TD>
            <TD align="left" width="55"></TD>
            <TD align="right"></TD>
            <TD align="right"></TD>
          </TR>
          <TR>
                        <TD class="label" align="right" width="147">Region / Division<FONT color="#ff0033"><FONT size="+1">*</FONT></FONT></TD>
                        <TD align="left" width="141">
            <SELECT name="regionDivision" tabindex="2">
          <%  
	 	java.util.Hashtable regionDivision =  purchaserDropDownVO.getRegionDivision();
		   enum    = regionDivision.keys();
		while(enum.hasMoreElements())  { 
		String aValue =(String) enum.nextElement();			%>
		<OPTION value="<%= aValue %>" ><%= (String) regionDivision.get(aValue) %></OPTION>
		<%
		}
		%>

           </SELECT>
            </TD>
                        <TD class="label" align="right" width="123">Sales Unit<FONT color="#ff0033"><FONT size="+1">*</FONT></FONT></TD>
            <TD align="left" width="86">
            <SELECT name="size" tabindex="3">
          <%  
	 	java.util.Hashtable salesUnit=  purchaserDropDownVO.getSalesUnit();
		   enum    = salesUnit.keys();
		while(enum.hasMoreElements())  { 
		String aValue =(String) enum.nextElement();			%>
		<OPTION value="<%= aValue %>" ><%= (String) salesUnit.get(aValue) %></OPTION>
		<%
		}
		%>

		 </SELECT>
            </TD>
            <TD class="label" align="right" width="65"></TD>
            <TD align="left" width="55"></TD>
            <TD align="right"></TD>
            <TD align="right"></TD>
          </TR>
          <TR>
                        <TD class="label" align="right" width="147">Direct Sale<FONT color="#ff0033"><FONT size="+1">*</FONT></FONT></TD>
                        <TD width="141"><SELECT name="directSale" tabindex="4">
                            <OPTION value="Y">Yes</OPTION>
                            <OPTION value="N" selected>No</OPTION>
                        </SELECT></TD>
                        <TD class="label" align="right" width="123">Tax ID/SSN<FONT color="#ff0033"><FONT size="+1">*</FONT></FONT></TD>
            <TD width="86"><INPUT size="9" type="text" name="taxId" maxlength="9" value="<%=BaseUtil.asString(purchaserInitialVO.getTaxId()) %>" tabindex="5"></TD>
            <TD class="label" width="65"></TD>
            <TD width="55"></TD>
            <TD></TD>
            <TD><IMG src="images/reset.gif" width="62" height="22" border="0" onclick="document.PurchaserInitialSetup.reset();purchaserReset()
"></TD>
          </TR>
          <TR>
                        <TD class="label" align="center" width="147">PID</TD>
                        <TD class="label" align="center" width="141">TPA ID</TD>
                        <TD class="label" align="left" colspan="3">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name<FONT color="#ff0033"><FONT size="+1">*</FONT></FONT></TD>
            <TD align="right" width="55"></TD>
            <TD align="right"></TD>
            <TD align="right"></TD>
          </TR>
          <TR>
                        <TD align="center" width="147">
             <INPUT size="20" type="text" maxlength="15" name="PID" value="<%=BaseUtil.asString(purchaserInitialVO.getPID() )%>" tabindex="6"> 
            </TD>
                        <TD align="center" width="141">
              <INPUT size="20" type="text" maxlength="15" name="TPAID" value="<%=BaseUtil.asString(purchaserInitialVO.getTPAID() )%>" tabindex="7">
            </TD>
                        <TD colspan="3" align="left">
             <INPUT size="40" type="text" maxlength="40" name="purchaserName" value="<%=BaseUtil.asString(purchaserInitialVO.getName() )%>" tabindex="8">
            </TD>
            <TD align="right" width="55"></TD>
            <TD align="right"></TD>
            <TD align="right"></TD>
          </TR>
        </TBODY>
      </TABLE>
      <TABLE cellpadding="1" cellspacing="1" width="80%">
        <TBODY>
          <TR>
            <TD align="center" class = "label">Administration System</TD>
            <TD align="center" class = "label">Administrator</TD>
            <TD align="center" class = "label">Billing Frequency</TD>
            <TD align="center" class = "label">Effective Date</TD>
            <TD align="center" class = "label">End Date</TD>
            <TD><!--<INPUT type="image" src="/BASEWeb/Purchaser/images/delete.gif" width="58" height="22" border="0" disabled>--></TD>
          </TR>
          <TR>
            <TD align="center"><SELECT name="administrativeSystem" Onchange = "selectAdministartor()" tabindex="9">
          <%  
	 	 java.util.Hashtable adminSystem =  purchaserDropDownVO.getAdminSystem();
		   enum    = adminSystem.keys();
		while(enum.hasMoreElements())  { 
		String aValue =(String) enum.nextElement();			%>
		<OPTION value="<%= aValue %>" ><%= (String) adminSystem.get(aValue) %></OPTION>
		<%
		}
		%>
            </SELECT></TD>
            <TD align="center">
		<INPUT size="20" type="text" maxlength="20" name="administrator" readOnly style="background-color : silver;" onFocus="this.blur()">
          </TD>
            <TD align="center"><SELECT name="billingFrequency" tabindex="10">
          <%  
	 	java.util.Hashtable billingFrequency =  purchaserDropDownVO.getBillingFrequency();
		   enum    = billingFrequency.keys();
		while(enum.hasMoreElements())  { 
		String aValue =(String) enum.nextElement();			%>
		<OPTION value="<%= aValue %>" ><%= (String) billingFrequency.get(aValue) %></OPTION>
		<%
		}
		%>
            </SELECT></TD>
            <TD align="center"><INPUT size="10" type="text" maxlength="10" name="effDate" value="<%=BaseUtil.asString(purchaserInitialVO.getAdminArrangements() .getEffectiveDate() )%>" tabindex="11"></TD>
            <TD align="center"><INPUT size="10" type="text" maxlength="10" name="endDate" value="<%=BaseUtil.asString(purchaserInitialVO.getAdminArrangements() .getEndDate() )%>" tabindex="12"></TD>
            <TD><!-- <INPUT type="image" src="/BASEWeb/Purchaser/images/add.gif" width="50" height="22" border="0" disabled> --></TD>
          </TR>
        </TBODY>
      </TABLE>
      <TABLE width="675" cellpadding="1" cellspacing="1">
        <TBODY>
          <TR>
                        <TD class="label" height="23" width="46">Line1<FONT color="#ff0033"><FONT size="+1">*</FONT></FONT></TD>
                        <TD height="23" align="left" width="288"><INPUT size="33" type="text" name="line1" value="<%=BaseUtil.asString(purchaserInitialVO.getAddress() .getLine1() )%>" tabindex="13"></TD>
                        <TD height="23" width="33" class="label">M/S</TD>
            <TD height="23" width="86"><INPUT size="8" type="text" name="mailStop" value="<%=BaseUtil.asString(purchaserInitialVO.getAddress() .getMailStop()) %>" tabindex="14"></TD>
            <TD class="label" width="194">Phone</TD>
          </TR>
          <TR>
                        <TD class="label" height="23" width="46">Line2</TD>
                        <TD height="23" align="left" width="288"><INPUT size="33" type="text" name="line2" value="<%=BaseUtil.asString(purchaserInitialVO.getAddress() .getLine2() )%>" tabindex="15"></TD>
                        <TD height="23" width="33"></TD>
            <TD height="23" width="86"></TD>
            <TD rowspan="2" height="1" width="194">
            <TABLE>
              <TBODY>
                <TR>
                  <TD class="label">Cntry</TD>
                                    <TD class="label" width="41">Area<FONT color="#ff0033"><FONT size="+1">*</FONT></FONT></TD>
                                    <TD class="label" width="61">Number<FONT color="#ff0033"><FONT size="+1">*</FONT></FONT></TD>
                                    <TD class="label" width="19">Ext</TD>
                                </TR>
                <TR>
                  <TD><INPUT size="4" type="text" value=1 name="countryCode" style="background-color : silver;" onFocus="this.blur()" readonly></TD>
                                    <TD width="41"><INPUT size="3" type="text" name="areaCode" maxlength="3" tabindex="21" value='<%=purchaserInitialVO.getPhone() .getAreaCode()==0?"":Integer.toString(purchaserInitialVO.getPhone() .getAreaCode())%>'></TD>
                                    <TD width="61"><INPUT size="7" type="text" name="phoneNumber"  maxlength="7" tabindex="22" value='<%=purchaserInitialVO.getPhone() .getNumber()==0?"":Integer.toString( purchaserInitialVO.getPhone() .getNumber())%>'></TD>
                                    <TD width="19"><INPUT size="3" type="text" name="extension"  maxlength="3" tabindex="23" value='<%=purchaserInitialVO.getPhone() .getExtension()==0?"":Integer.toString(purchaserInitialVO.getPhone() .getExtension())%>'></TD>
                                </TR>
              </TBODY>
            </TABLE>
            </TD>
          </TR>
          <TR>
                        <TD class="label" height="23" width="46">Line3</TD>
                        <TD align="left" height="23" width="288"><INPUT size="33" type="text" name="line3" value="<%=BaseUtil.asString(purchaserInitialVO.getAddress() .getLine3()) %>" tabindex="16"></TD>
                        <TD height="23" width="33"></TD>
            <TD height="23" width="86"></TD>
          </TR>
          <TR>
                        <TD class="label" height="13" width="46">City<FONT color="#ff0033"><FONT size="+1">*</FONT></FONT></TD>
                        <TD align="left" height="13" width="288"><INPUT size="33" type="text" name="city" value="<%=BaseUtil.asString(purchaserInitialVO.getAddress() .getCity() )%>" tabindex="17"></TD>
                        <TD height="13" width="33"></TD>
            <TD height="13" width="86"></TD>
            <TD width="194"></TD>
          </TR>
          <TR>
                        <TD class="label" width="46">State<FONT color="#ff0033"><FONT size="+1">*</FONT></FONT></TD>
                        <TD width="288">
            <TABLE cellpadding="1" cellspacing="1">
              <TBODY>
                <TR>
                  <TD width="48"><SELECT name="state" tabindex="18">
                                        <OPTION>&nbsp;&nbsp;&nbsp;</OPTION>
                                    </SELECT></TD>
                  <TD class="label" width="31">Zip<FONT color="#ff0033"><FONT size="+1">*</FONT></FONT></TD>
                  <TD width="67"><INPUT size="10" type="text" name="zip" value="<%=BaseUtil.asString(purchaserInitialVO.getAddress() .getZip() )%>" maxlength="10" tabindex="19"></TD>
                                    <TD class="label" width="58">Country<FONT color="#ff0033"><FONT size="+1">*</FONT></FONT></TD>
                                    <TD width="32"><SELECT name="country" OnChange="setState(document.PurchaserInitialSetup)" tabindex="20">
					<%  
	 				java.util.Vector countryValue =  purchaserDropDownVO.getCountryValue();
	 				java.util.Vector countryName =  purchaserDropDownVO.getCountryText();
					int length   = countryValue.size();
				for(int k=0;k< length; k++)  { %>
				<OPTION value="<%= (String)countryValue.elementAt(k) %>" ><%= (String)countryValue.elementAt(k) %></OPTION>
				
					<%
					}
					%>
                    
                  </SELECT></TD>
                                </TR>
              </TBODY>
            </TABLE>
            </TD>
                        <TD width="33"></TD>
            <TD width="86"></TD>
            <TD width="194"></TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
  </TBODY>
</TABLE>
</FORM>
</BODY>
</HTML>
