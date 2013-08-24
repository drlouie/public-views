<!-- Sample JSP file -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<META http-equiv="Content-Style-Type" content="text/css">
<STYLE>
<!--
.label {
	COLOR: #0033FF;
	font-family: arial, verdana, sans-serif;
	font-size: 13px;
	font-weight: bold;
	font-style: normal;
}
.result {
	COLOR: #000000;
	font-family: courier-new;
	font-size: 14px;
	font-weight: normal;
	font-style: normal;
}
.title {
	COLOR: #FFFFFF;
	font-family: arial, verdana, sans-serif;
	font-size: 14px;
	font-weight: bold;
	font-style: normal;
}
.error {
	COLOR: #FFFF66;
	font-family: arial, verdana, sans-serif;
	font-size: 18px;
	font-weight: bold;
	font-style: normal;
}
IMG {
	color: olive;
}
-->
</STYLE>
<TITLE>Administer Purchaser ( PID / PID_EU Relationships )</TITLE>
</HEAD>
<BODY bgcolor="#999999" onload="init()">
<FORM name="PurchaserEURelationship" method = "post" action = "PurchaserEURelationshipServlet" target="_parent">
<%@ page import="java.util.*" %> 
<input type="hidden" name="WhereToGo" value="" >
<input type="hidden" name="FromWhere" value="0" >
<jsp:useBean id="purEURelVO" class="org.kp.purchaser.vo.PurchaserEURelationshipVO"/> <SCRIPT>
<%! String noEUFound = "";%>
function init()
{
	//parent.tops.document.PurTop.dynamic.value = "PUR108 Administer Purchaser ( PID / PID_EU Relationships )";
	<%
		Vector purEURels = (Vector)session.getAttribute("PurchaserEURelationships");
		if(purEURels != null )
			{			
				if(purEURels.size() == 0)
					noEUFound = "No Enrollment Unit Relationships found for this Purchaser";
			}
		else
				noEUFound = "No Enrollment Unit Relationships found for this Purchaser";
		String destination = "Search.jsp";
		System.out.println("EU:"+noEUFound);
	%>
}
</SCRIPT>
<FONT color="#ffff00" size="5"><%= noEUFound%></FONT>
<TABLE border="1" width = "100%">

    <% if(purEURels != null)
		{
		if(purEURels.size() > 0 )
		{
	%>
    <TBODY>
        <TR>
            <TD>            
            <TABLE width="100%" cellpadding="1" cellspacing="1">
                <TBODY>
                    <TR bgcolor="#006f6f">
                        <TH align="center"><FONT color="#fffff">Row</font></TH>
                        <TH align="center"><FONT color="#fffff">PID</font></TH>
                        <TH align="center"><FONT color="#fffff">EU</font></TH>
                        <TH align="center"><FONT color="#fffff"><nobr>Enrollment Unit Name</nobr></font></TH>
                        <TH align="center"><FONT color="#fffff"><nobr>Effective Date</nobr></font></TH>
                        <TH align="center"><FONT color="#fffff"><nobr>End Date</nobr></font></TH>
                    </TR>
                    <% for(int count = 0 ; count < purEURels.size() ; count++)
                    	{
                    	purEURelVO = (org.kp.purchaser.vo.PurchaserEURelationshipVO)purEURels.elementAt(count);
                    %>

                    <TR bgcolor="#FFFFEC">
                        <TD class ="result" align="center"><%= count+1%></TD>
                        <TD class ="result" align="center"><nobr><A href="../EnrollmentUnit/EUGeneralInfoServlet?UserVisited=1&PurIK=<%=purEURelVO.getPurIK()%>&PeuIK=<%=purEURelVO.getPeuIK()%>" target="_parent"><%= purEURelVO.getPID()%></A></nobr></TD>
                        <TD class ="result"><nobr><%= purEURelVO.getEU()%></nobr></TD>
                        <TD class ="result"><nobr><%= purEURelVO.getEUName()%></nobr></TD>
                        <TD class ="result"><nobr><%= purEURelVO.getEffDate()%></nobr></TD>
                        <TD class ="result"><nobr><%= purEURelVO.getEndDate()%></nobr></TD>
                    </TR>
                    <%
                    }
                    %>
                </TBODY>
            </TABLE>
            </TD>
        </TR>
    </TBODY>
    <%
    }
    }
    %>
</TABLE>
</FORM>
</BODY>
</HTML>
