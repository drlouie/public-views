<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"><!-- Sample JSP file -->

<HTML><META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<META http-equiv="Content-Style-Type" content="text/css">
<TITLE></TITLE>


<BODY  bgcolor="#999999">

<%@  page isErrorPage="true" autoFlush="false" %> 
<hr color=blue>
<center> <font color=Red size=8.5>  Error </font> </center>
<hr color=blue>
		
		  <font face="Arial, Helvetica, sans-serif" size="2" color=red>

	<%
		if(session.getAttribute("ERROR") != null)
		{
			out.println("<B> <FONT COLOR=RED> Error: &nbsp;&nbsp; </B>");
			out.println(session.getAttribute("ERROR")+"</FONT><br><br>" );
			session.removeAttribute("ERROR");
		}
	%>
</font>
<BR>
<BR>
<BR>


Note:- Please report this error to the Business Analyst

</BODY>
</HTML> 