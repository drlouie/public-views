<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<%@ page import="java.util.*" %>
<jsp:useBean id="BrokerInquiryVO" class="org.kp.broker.vo.BrokerInquiryVO" />
<%
	// Get the parameters. 
	ArrayList data = (ArrayList) session.getAttribute("BIResults");	
%>
<HTML>
<HEAD>
<TITLE>Display Broker Inquiry Information</TITLE>
<META name="Generator" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<META name="Author" content="Jeff Ritter">
<META name="Description" content="Display Comments from the back end.">
<META http-equiv="Content-Style-Type" content="text/css">
<script language="javascript" src="script/common_css.js"></script>
<script language="javascript" src="script/mousetable.js"></script>
<script language="javascript" src="script/popwindow.js"></script>
<SCRIPT language="javascript">
<!--
function DisplayDetails( Details )
{	

//Inserted by drlouie
	parent.window.resizeTo(880,635);
	var windowX = (screen.width/2)-(870/2);
	var windowY = (screen.height/2)-(605/2);
	parent.window.moveTo(windowX, windowY)
// End Insert

	document.BkrInqMid.BrokerId.value = Details;	
	//alert(document.BkrInqMid.BrokerId.value);
	document.BkrInqMid.submit();
	this.href = "tmpMessage.htm";
	return this.href;
}
//-->
</SCRIPT>
</HEAD>
<body bgcolor="#0B5F77" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">

<FORM name="BkrInqMid" method="post" action="BrokerInquiryServlet" target="_parent">
<INPUT type="hidden" name="BrokerId" value="">
<INPUT type="hidden" name="clicked" value="">
<TABLE border="2" width="100%" cellpadding="5" cellspacing="0" bordercolor="#0B5F77">
    <TR>
      <TD align="top">
            <TABLE width="100%" border="1" cellpadding="5" cellspacing="0" bordercolor="#E6E9F0" id="ignore">
          <%
   int counter = 0;
   int BrokerId = 0;

   for( int i = 0; i < data.size(); i++ )
   {
		//Cast the ArrayList element into a BrokerInquiryVO.
		BrokerInquiryVO  = (org.kp.broker.vo.BrokerInquiryVO) data.get( i );

		//Set the counter once here, instead of twice in the code.
		counter = i + 1;
		BrokerId = BrokerInquiryVO.getBrokerID();		
		
		if ( i==0 ) {
%>

          <TR>
            <TD align="center" id="ignore"><FONT class="stitle2">No</FONT></TD>
            <TD align="center" id="ignore" width="15%"><FONT class="stitle2">Broker Name</FONT></TD>
            <TD align="center" id="ignore"><FONT class="stitle2"><nobr>Broker ID</nobr></FONT></TD>
            <TD align="center" id="ignore"><FONT class="stitle2">IRS Tax ID</FONT></TD>
            <TD align="center" id="ignore"><FONT class="stitle2">License Number</FONT></TD>
            <TD align="center" id="ignore"><FONT class="stitle2">Broker Address</FONT></TD>
          </TR>
		<%
		}
		%>


          <TR bgcolor="#E6E9F0" valign="top" style="cursor:hand" onMouseOver="runto(this,'A3ADC7');" onMouseOut="runback(this,'E6E9F0');" onClick="this.href=DisplayDetails( Details<%= counter%>.value )"> 
            <TD><font class="stitle3"><%= counter%></font><INPUT type="hidden" name="Details<%= counter%>" value="<%= BrokerId%>"></TD>
            <TD><font class="stitle3"><%= BrokerInquiryVO.getBrokerName()%></font></TD>
            <TD><font class="stitle3"><%= BrokerId%></font></TD>
            <TD><font class="stitle3"><%= BrokerInquiryVO.getIRSTaxID()%></font></TD>
            <TD><font class="stitle3"><nobr><%= BrokerInquiryVO.getLicense()%></nobr></font></TD>
            <TD><font class="stitle3"><%= BrokerInquiryVO.getAddress()%></font></TD>
          </TR>

                    <%
   }
   
%>

	<%  
	if ( data.size() < 1 ) {
	%>
          <TR>
            <TD align="center" class="msg" border="0"><FONT class="ComTitle" style="font-size:12px">Can't find a Broker for the 'Search Criteria' you have entered...</FONT></TD>
          </TR>


	<%
	}
	%>
      </TABLE>
            </TD>
    </TR>
</TABLE>
</FORM>

</BODY>
</HTML>