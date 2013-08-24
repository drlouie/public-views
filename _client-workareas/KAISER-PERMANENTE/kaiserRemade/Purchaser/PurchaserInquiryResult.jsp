<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<TITLE>Purchaser Inquiry Result</TITLE>
<SCRIPT>
function directTO()
{
	alert("directTo");	
}
</SCRIPT>
<script language="javascript" src="../script/common_css.js"></script>
<script language="javascript" src="../script/mousetable.js"></script>
</HEAD>
<body bgcolor="#0B5F77" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" OnLoad="init();" scroll="yes">
<FORM name = "PurchaserInquiry" method = "post" action = "PurchaserGeneralInfoServlet">
<%@ page import="java.util.*" %> 
<jsp:useBean id="purInquiryVO" class="org.kp.purchaser.vo.PurchaserInquiryVO"/> 
<jsp:useBean id="searchVO" class="org.kp.purchaser.vo.PurchaserInquirySearchVO"/> 
<% String destination = "";%>
<% String noResult = " ";%>
<SCRIPT>
var directTo = '';
function init()
{
	document.PurchaserInquiry.purIK.value = 0;
	<%	
		//String destination = null;
		Vector purInquirys = (Vector)session.getAttribute("PurchaserInquiry");
		searchVO = (org.kp.purchaser.vo.PurchaserInquirySearchVO)session.getAttribute("Search");			
		if(searchVO != null)
		{		
		String directTO = searchVO.getSearchFor();		
		if(directTO.equals("1"))
			destination = "../Purchaser/PurchaserGeneralInfoServlet";
		else if(directTO.equals("2"))
			destination = "../EnrollmentUnit/EUGeneralInfoServlet";
		else if(directTO.equals("3"))
			destination = "../Rollup/AdministerRollupRelationshipsServlet";
	
	%>
	
	directTo = '<%= searchVO.getSearchFor()%>';
	<%
		}
		
		if(searchVO != null)
			{
				if(purInquirys != null)
				{				
				if(purInquirys.size() == 0)
					{
						noResult = org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.inquiry.SearchFoundNoRecord");
					}
				}
				else
					noResult = org.kp.base.web.util.MessageUtil.getInstance().getText("purchaser.inquiry.SearchFoundNoRecord");
			}	
	
	%>
}
function custructHref(purchaserIK)
{	
	var purIK = '';
	var peuIK = '';
	var hypen = '';
	var queryString = '';
	var rollupID = '';
	var counter = 0;
	var hypenArray = new Array();
	for(var count = 0 ; count < purchaserIK.length ; count++)
		{
			if(purchaserIK.substring(count,count+1) == ":")
				{
					hypen = count;
					counter = counter + 1;
					//break;
				}
			hypenArray[counter] = hypen;	
		}
	//purIK = purchaserIK.substring(0,hypen);[ Commented to introduce more than 2 parameters to purchaserIK variable ]
	//peuIK = purchaserIK.substring(hypen+1,purchaserIK.length);
	  purIK = purchaserIK.substring(0,hypenArray[1]);
	  peuIK = purchaserIK.substring(hypenArray[1]+1,hypenArray[2]);
	  rollupID = purchaserIK.substring(hypenArray[2]+1,purchaserIK.length);

	if(directTo == "1")
			queryString = "../Purchaser/PurchaserGeneralInfoServlet?PurIK="+purIK;
	else if(directTo == "2")
			queryString = "../EnrollmentUnit/EUGeneralInfoServlet?PurIK="+purIK+"&PeuIK="+peuIK;
	else if(directTo == "3")
	{
			queryString = "../Rollup/AdministerRollupRelationshipsServlet?SelectedAction=Search&RollupNumber="+rollupID;	
			<% session.setAttribute("sessIDARR","Visited"); %>
	}

//Inserted by drlouie
	parent.window.resizeTo(880,635);
	var windowX = (screen.width/2)-(870/2);
	var windowY = (screen.height/2)-(605/2);
	parent.window.moveTo(windowX, windowY)
// End Insert			

	return queryString;
	
	
}

function callRadio(value)
{	
	document.PurchaserInquiry.purIK.value = value;	
}
</SCRIPT>
<FONT color="#ffff00" size="4"><%= noResult%></FONT>

<INPUT type = "hidden" name="purIK" value = "">
<TABLE border="2" width="100%" cellpadding="5" cellspacing="0" bordercolor="#0B5F77">
    <% if(purInquirys != null)
		{
	%>
        <TR>
            <TD valign="top">
            <TABLE width="100%" border="1" cellpadding="5" cellspacing="0" bordercolor="#E6E9F0" id="ignore">
                <% if(purInquirys != null)
                	{
                	if(purInquirys.size() > 0 )
                    {
                %>
                    <TR>
                    <%
                    	if(destination.indexOf("Rollup") == -1)
                    	{
                    %>
                    	<TD align="center" id="ignore"><FONT class="stitle2">Check</font></TD>
                    <%
                   		}
                    %>
                        <TD align="center" id="ignore"><FONT class="stitle2">Row</font></TD>
                        <TD align="center" id="ignore"><FONT class="stitle2">PID</font></TD>
                        <TD align="center" id="ignore"><FONT class="stitle2">EU</font></TD>
                        <TD align="center" id="ignore"><FONT class="stitle2">Rollup ID</font></TD>
                        <TD align="center" id="ignore"><FONT class="stitle2">Name</font></TD>
                        
                    </TR>
                    <%
                    }
                    }
                    %>
                    <% 
                    if(purInquirys != null )
                    {
                    if(purInquirys.size() > 0 )
                    {
                    for(int count = 0 ; count < purInquirys.size() ; count++)
                    	{
                    	purInquiryVO = (org.kp.purchaser.vo.PurchaserInquiryVO)purInquirys.elementAt(count);
                    %>

                    <TR bgcolor="#E6E9F0" valign="top" style="cursor:hand" onMouseOver="runto(this,'A3ADC7');" onMouseOut="runback(this,'E6E9F0');">
                    <%
                    	if(destination.indexOf("Rollup") == -1)
                    	{
                    %>
                    	<TD align="center" height="15"><INPUT type = "radio" name = "purIK" value = "<%= purInquiryVO.getPurIK()%>" onclick = "callRadio(this.value)" style="height:15px"></TD>                   	
                   	<%
                   		}
                    %>
						<TD align="center" height="15" onclick ="parent.location.href=custructHref(this.id)" id = "<%= purInquiryVO.getPurIK()+":"+purInquiryVO.getPeuIK()+":"+purInquiryVO.getRollUpID()%>"><font class="stitle3"><%= count+1%></font></TD>
                        <TD align="center" height="15" onclick ="parent.location.href=custructHref(this.id)" id = "<%= purInquiryVO.getPurIK()+":"+purInquiryVO.getPeuIK()+":"+purInquiryVO.getRollUpID()%>"><font class="stitle3"><nobr><%= purInquiryVO.getPID()%></nobr></font></TD>
                        <TD class="result" height="15" onclick ="parent.location.href=custructHref(this.id)" id = "<%= purInquiryVO.getPurIK()+":"+purInquiryVO.getPeuIK()+":"+purInquiryVO.getRollUpID()%>"><font class="stitle3"><nobr><%= purInquiryVO.getEU()%>&nbsp;</nobr></font></TD>
                        <TD class="result" height="15" onclick ="parent.location.href=custructHref(this.id)" id = "<%= purInquiryVO.getPurIK()+":"+purInquiryVO.getPeuIK()+":"+purInquiryVO.getRollUpID()%>"><font class="stitle3"><nobr><%= purInquiryVO.getRollUpID()%>&nbsp;</nobr></font></TD>
                        <TD class="result" height="15" onclick ="parent.location.href=custructHref(this.id)" id = "<%= purInquiryVO.getPurIK()+":"+purInquiryVO.getPeuIK()+":"+purInquiryVO.getRollUpID()%>"><font class="stitle3"><nobr><%= purInquiryVO.getName()%></nobr></font></TD>            
                    </TR>
                    <%
                    }
                    }
                    }
                    %>
            </TABLE>
            </TD>
        </TR>
    <%
    }
    %>
</TABLE>
</FORM>
</BODY>
</HTML>

