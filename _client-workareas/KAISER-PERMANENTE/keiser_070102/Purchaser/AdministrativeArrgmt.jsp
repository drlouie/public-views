<!-- Sample JSP file --> <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<%@ page import = "org.kp.purchaser.vo.PurchaserDropDownVO" %>
<jsp:useBean id="purchaserAdminVO"  class="org.kp.purchaser.vo.PurchaserAdminVO"  scope="session"></jsp:useBean>
<jsp:useBean id="purchaserInitialVO"  class="org.kp.purchaser.vo.PurchaserInitialVO" 
scope="session"></jsp:useBean>
<jsp:useBean id="purchaserDropDownVO"  class="org.kp.purchaser.vo.PurchaserDropDownVO" 
scope="session"></jsp:useBean>
<HTML>
<HEAD>
<%@ include file="script/validateAdminArrangmtForm.js" %>
<%@ include file="script/validateAdminArrangmt.js" %>
<!-- dfasfda <SCRIPT language="JavaScript1.1" src="/BASEWeb/Purchaser/script/validateAdminArrangmtForm.js"></SCRIPT> -->
<!-- <SCRIPT language="JavaScript1.1" src="/BASEWeb/Purchaser/script/validateAdminArrangmt.js"></SCRIPT> -->
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
.pbttn {
	font-family: arial;
	font-size:13px;
	color:#ffffff;height: 26px;
	text-decoration: none;
	padding-left: 4px;
	padding-right: 4px;
	padding-top:2px;
	padding-bottom: 2px;	
	cursor: hand;
	background-color: #5662af;
	border-top-color: #4A4D7B;
	border-left-style: solid;
	border-left-width: 1px;
	font-weight: bold;
	border-top-style: solid;
	border-left-color: #4A4D7B;
	border-top-width: 1px;
	border-bottom-style: solid;
	border-bottom-width: 1px;
	border-right-style: solid;
	border-right-width: 1px;
	border-bottom-color: #4A4D7B;
	border-right-color: #4A4D7B;
	vertical-align: middle;
	text-align: center;
	} 
-->
</STYLE>
<SCRIPT language="JavaScript">
var oldNo = false;
function addListHide()
 {
        disableform();
    document.AdministrativeArrgmt.CurrentDate.value = "<%=session.getAttribute("CurrentDate").toString()%>";
    document.AdministrativeArrgmt.AddList.style.visibility = "hidden";
	document.AdministrativeArrgmt.administrativeSystem.value = "" ;
	document.AdministrativeArrgmt.administrator.value = " " ;
	document.AdministrativeArrgmt.billingFrequency.value = "";

	var elementsMaxLength = new Array();
	var elementsText = new Array();
	elementsMaxLength[0] =20;
	elementsMaxLength[1] = 30;
	elementsMaxLength[2] = 18;
	elementsMaxLength[3] = 11; 
	elementsMaxLength[4] = 11;
	elementsMaxLength[5] = 1;

	<%
	java.util.Vector adminVec = new java.util.Vector();
	 adminVec = (java.util.Vector) session.getAttribute("ModifiedAdmin");

	java.util.Hashtable adminSystem =  purchaserDropDownVO.getAdminSystem();
	java.util.Hashtable billingFrequency =  purchaserDropDownVO.getBillingFrequency();

	int vecSize =adminVec.size();

	for(int i = vecSize; i > 0 ; i-- ) {
		purchaserAdminVO = ( org.kp.purchaser.vo.PurchaserAdminVO ) adminVec.elementAt(i-1);
			int j =1;
     
	    %>


     		document.AdministrativeArrgmt.AddList.style.visibility = "";

 			elementsText[0] = "<%=adminSystem.get(purchaserAdminVO.getAdminSystem())%>" ;
			elementsText[1] = "<%=purchaserAdminVO.getAdministrator() %>";
			elementsText[2] = "<%=billingFrequency.get(purchaserAdminVO.getBillingFrequency())%>";
			elementsText[3] = "<%=purchaserAdminVO.getEffectiveDate()%>";	
			elementsText[4] = "<%=purchaserAdminVO.getEndDate()%>";
			elementsText[5] = "<%=purchaserAdminVO.getStatusIndicator()%>";
			
		 if( elementsText[5] != "A" && elementsText[5] != "D" ) 
		 {
		  	if( IsThisDateRangeCurrent(elementsText[3],elementsText[4] ) )
		 		elementsText[5] = '***';
		 	else if( <%=purchaserAdminVO.getSortOrder()%> != 0 )
		 		elementsText[5] = "U"; 
		 	else 	 		
		 	   	elementsText[5] = "";
         }   	
	
			
			
	
	for(var i = 0 ; i < elementsMaxLength.length; i++)
		{	
			
			if(elementsText[i].length < elementsMaxLength[i])
				{	
					for(j = elementsText[i].length ; j < elementsMaxLength[i]; j++)
						{			
							elementsText[i]+= " ";							
						}
					
				}
			else
				elementsText[i] = elementsText[i].substring(0,elementsMaxLength[i]);
		}
	



		var addoptions = new Option();
		addoptions.text = elementsText[0] + " " + elementsText[1] + " " + elementsText[2] + " "+ elementsText[3] + " " + elementsText[4] +" " + elementsText[5];  
		addoptions.value = "<%=purchaserAdminVO.getAdminSystem()%>"+ ":" + "<%=purchaserAdminVO.getAdministrator() %>" + ":" + "<%=purchaserAdminVO.getBillingFrequency()%>"+ ":" + "<%=purchaserAdminVO.getEffectiveDate()%>" + ":" + "<%=purchaserAdminVO.getEndDate()%>" + ":" + "<%=purchaserAdminVO.getIdentifier()%>"+":"+"<%=purchaserAdminVO.getStatusIndicator()%>"+":"+"<%=purchaserAdminVO.getSortOrder()%>";
		document.AdministrativeArrgmt.AddList.options[document.AdministrativeArrgmt.AddList.options.length] = addoptions;			
    <%
		}
    String error = (String) session.getAttribute("ERROR");
	if ( ! error.equals("nothing") ) {
	org.kp.purchaser.vo.PurchaserAdminVO padVO = (org.kp.purchaser.vo.PurchaserAdminVO) session.getAttribute("purchaserAdminVO");
	%>
	alert("<%=error %>");
	document.AdministrativeArrgmt.administrativeSystem.value = "<%=padVO.getAdminSystem() %>" ;
	document.AdministrativeArrgmt.administrator.value = "<%=padVO.getAdministrator() %>" ;
	document.AdministrativeArrgmt.billingFrequency.value = "<%=padVO.getBillingFrequency() %>";
	document.AdministrativeArrgmt.effDate.value = "<%=padVO.getEffectiveDate() %>";
	document.AdministrativeArrgmt.endDate.value = "<%=padVO.getEndDate() %>" ;
	document.AdministrativeArrgmt.adminrelId.value = "<%=padVO.getIdentifier() %>" ;
	document.AdministrativeArrgmt.SortOrder.value="<%=padVO.getSortOrder()%>"
	document.AdministrativeArrgmt.statusIndicator.value="<%=padVO.getStatusIndicator()%>" 
	<%
		session.setAttribute("ERROR", "nothing");
	}
	%>	
	document.AdministrativeArrgmt.AddList.disabled = true;
}
function IsThisDateRangeCurrent(EffectiveDate,EndDate)
{
		 var Status = false;
		 var currentdate = document.AdministrativeArrgmt.CurrentDate.value;
		 if(EndDate == "")
		 	EndDate = "12/31/4000";
	
   	     var effmm = EffectiveDate.substring(0, 2);
         var effdd = EffectiveDate.substring(3, 5);
         var effyyyy = EffectiveDate.substring(6, 10);
         
         var endmm = EndDate.substring(0, 2);
         var enddd = EndDate.substring(3, 5);
         var endyyyy = EndDate.substring(6, 10);


   	 	 var curmm = currentdate.substring(0, 2);
         var curdd = currentdate.substring(3, 5);
         var curyyyy = currentdate.substring(6, 10);
 
		if ( endyyyy <= curyyyy ) 
		{
			if( endyyyy == curyyyy )
			{
				if( endmm <= curmm )
				{
					if( endmm == curmm )
					{
						if( enddd >= curdd )
						{
							Status = true;
						}
						else
							Status = false;
					}
					else
						Status = false;
				}
				else 
					Status = true;
			}
			else
				Status = false;
		}
		else
			Status = true;
			
		if(Status == true)
		{
			if( effyyyy >= curyyyy )
			{
				if( effyyyy == curyyyy )
				{
					if( effmm >= curmm )
					{
						if( effmm == curmm )
						{
							if(effdd > curdd )
							{
								Status = false;
							}
							else
								Status = true;
						}
						else
							Status = false;
					}
					else 
						Status = true;
					
				}
				else
					Status = false;
				
			}
			else 
				Status = true;
			
		}
	return Status;
}

</SCRIPT>
<TITLE>PUR100 Administer Purchaser (Administrative Arrangements)</TITLE>
</HEAD>
<BODY bgcolor="#999999" OnLoad="init();addListHide() ">
<FORM name="AdministrativeArrgmt" method="POST" action= "AdminArrangementsServlet" target = "_parent"> 
      	<input type="hidden" name="opmode" value="">
		<input type="hidden" name="adminrelId" value="0">
		<input type="hidden" name="statusIndicator" value="">
		<input type="hidden" name="SelectedAction" value="">
		<input type="hidden" name="message" value="" >
		<input type="hidden" name="SortOrder" value="-10000" >
                 <input type="hidden" name="WhereToGo" value="" >
		  <input type="hidden" name="FromWhere" value="0" >
		    <input type="hidden" name="CurrentDate" value="">
<SCRIPT>
function init()
{	
	// parent.tops.document.PurTop.dynamic.value = "PUR102 Administer Purchaser ( Administrative Arrangements )";
}
</SCRIPT>
<TABLE width="80%">
  <TBODY>
    <TR>
      <TD bgcolor="#999999">
      <TABLE width="100%" cellpadding="0" cellspacing="0">
      </TABLE>
      <TABLE cellpadding="1" cellspacing="1">
        <TBODY>

          <TR>
            <TD class="label" align="center" colspan="4">PID</TD>
            <TD class="label" align="center">TPA ID</TD>
            <TD class="label" align="center" colspan="3">Name</TD>
            <TD align="center"><IMG src="images/edit.gif" width="50" height="22" border="0" onclick="enableform()"></TD>
            <TD align="center"><IMG src="images/reset.gif" width="50" height="22" border="0" onclick="adminReset()"></TD>
                    </TR>
          <TR>
                        <TD align="center" colspan="4">


<INPUT size="15" type="text" maxlength="15" name="PID" value="<%=purchaserInitialVO.getPID() %>" tabindex="1"></TD>
                        <TD align="center"><INPUT size="15" type="text" maxlength="15" name="TPAID" value="<%=purchaserInitialVO.getTPAID() %>" tabindex="2"></TD>
<TD colspan="3" align="center">
<INPUT size="40" type="text" maxlength="40" name="purchaserName" value="<%=purchaserInitialVO.getName() %>" tabindex="3"></TD>
            <TD align="right"></TD>
            <TD align="right"></TD>
                    </TR>
          <TR>
            <TD align="right" colspan="4" class="label">Administration System</TD>
            <TD class="label" align="center">Administrator</TD>
            <TD class="label" align="center">Billing Frequency</TD>
            <TD class="label" align="center">Effective Date</TD>
            <TD class="label" align="center">End Date</TD>
            <TD class="label" align="center"></TD>
            <TD align="center" width="71"><INPUT size="20" type="button" maxlength="20" name="submitDelete" value="Delete" class="pbttn" onclick="return beforeDelete();"></TD>
            <!-- <TD align="left"><INPUT type="image" src="images/delete.gif" name="submitDelete" value="Delete" alt="Delete" onClick="beforeDelete();"></TD> -->
                    </TR>
          <TR>
            <TD align="center" colspan="4"><SELECT name="administrativeSystem" Onchange = "selectAdministartor()" tabindex="4">
          <%  
	 	 java.util.Enumeration enum    = adminSystem.keys();
		while(enum.hasMoreElements())  { 
		String aValue =(String) enum.nextElement();%>
		<OPTION value="<%= aValue %>" ><%= (String) adminSystem.get(aValue) %></OPTION>
		<%
		}
		%>
 
            </SELECT></TD>
            <TD align="center"><INPUT size="20" type="text" maxlength="20" name="administrator"  style="background-color : silver;" onFocus="this.blur()"></TD>
            <TD align="center"><SELECT name="billingFrequency" tabindex="6">
          <%  
	  		   enum    = billingFrequency.keys();
		while(enum.hasMoreElements())  { 
		String aValue =(String) enum.nextElement();			%>
		<OPTION value="<%= aValue %>" ><%= (String) billingFrequency.get(aValue) %></OPTION>
		<%
		}
		%>
            </SELECT></TD>
            <TD align="center"><INPUT size="10" type="text" maxlength="10" name="effDate" tabindex="7"></TD>
            <TD align="center">
            <TABLE cellpadding="1" cellspacing="1">
              <TBODY>
                <TR>
                  <TD align="center"><INPUT size="10" type="text" maxlength="10" name="endDate" tabindex="8"></TD>
                </TR>
              </TBODY>
            </TABLE>
            </TD>
            <TD align="center" class ="label">Indicator</TD>
            <TD align="center" width="71"><INPUT size="20" type="button" maxlength="20" name="submitAdd" value="  Add  " class="pbttn" onclick=" return beforeAdd()" tabindex="9"></TD>
            <!-- <TD><INPUT type = "image" src="images/add.gif" name="submitAdd" value="Add" alt="Add" onClick=" return <B>beforeAdd</B>()" tabindex="9"></TD> -->
 
          </TR>
        </TBODY>
      </TABLE>
      <SELECT size="6" name="AddList"  onclick="return popAgain(AddList,this.form.AddList.value)" style='font-family : "Courier New";' ></SELECT>
 
     <BR>
      </TD>
    </TR>
  </TBODY>
</TABLE>
</FORM>
</BODY>
</HTML>