<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<!-- 
	$id$
	Author		Nirav Parikh
	
	Comments	Generic Error page for the base application. 
-->

<%@ page isErrorPage="True" language="java" import="org.kp.base.shared.ExceptionHandler, org.kp.base.web.util.BaseSessionValidator, org.kp.base.web.util.MessageUtil, org.kp.base.shared.BaseException, org.kp.base.shared.BaseValidationException, org.kp.base.shared.MessageInfo, java.util.Date" %>

<%
	/*MessageInfo[]	msgInfo = new MessageInfo[3];
	
	msgInfo[0] = new MessageInfo("invalidUser");
	

	Object[] obj = {new Date() };
	msgInfo[1] = new MessageInfo("invalidDate", obj);
		
	Object[] obj1= {"xyz", new Date(),"osh" }; 
	msgInfo[2] = new MessageInfo("xyzTest", obj1);
	Exception exception =  new BaseException(new NullPointerException());*/
%>
<% String appShortName = MessageUtil.getInstance().getText("appShortName"); %>

<% //if (false) {
if (!BaseSessionValidator.isValidSession(request)) {
       BaseSessionValidator.logoutNow(request); 
%>

<HTML>
<TITLE><%=appShortName%></TITLE>
<META name="GENERATOR" content="IBM WebSphere Studio">
<BODY >
<BR><BR><BR>
<CENTER>
<TABLE WIDTH="400" CELLSPACING=0 BORDER=3>
<TR>
    <TH bgcolor="#000080"><b><FONT color="#ffffff"><%=appShortName%> Session Error</font></b></TH>
</TR>
<TR>
    <TD bgcolor="#cccccc"><BR>
    Your working session is no longer valid due to either
    the session timing out which occurs after 1 hour of non-usage
    OR <%=appShortName%> server being restarted,
    OR a problem with your environment.
    Please click the link below to return back to the <%=appShortName%> Login screen.
    You will need to verify your last action you accessed to make sure your
    changes were saved.<BR>
    Thank you.
    <BR><BR><BR></TD></TR>
    
       <TR ><TD ALIGN="CENTER" bgcolor="#cccccc"><CENTER>
        <A HREF="BaseLoginServlet" TARGET="_top">Click here to Return to the <%=appShortName%> Login Page.</A>
    </CENTER><BR><BR></TD>
</TR>
</TABLE>
</CENTER>
</BODY>
</HTML>

<% } else { %>

<HTML>
<BODY >
<BR><BR><BR>
<CENTER>
<TABLE WIDTH="400" CELLSPACING=0 BORDER=3>
<TR>
    <TH bgcolor="#000080"><b><FONT color="#ffffff"><%=appShortName%> Application Error</font></b></TH>
</TR>
<TR>
    <TD bgcolor="#cccccc"><BR>
    <% 
		String message = ExceptionHandler.getMessage(exception);
		if (message == null) {
			Object[] o = {appShortName};       
			message = MessageUtil.getInstance().getText("contactSupportWithTrace", o);
			message += "\n<BR><BR>\n";
			message += ExceptionHandler.getStackTrace(exception);
       } %>
    <%= message %>
    <BR><BR>
    <CENTER><FORM onSubmit="history.go(-1); return false;"><INPUT TYPE="submit" NAME="submit" value="OK"></FORM></CENTER></TD>
</TR>
</TABLE>
</CENTER>
</BODY>
</HTML>
<% } %>
