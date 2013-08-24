<%@ page import="java.util.*" %>
<% if(request.getMethod().equals("GET")){%>
<HTML>
<HEAD>
<script language = "javascript">
<!--
function setFlashVars()
{
  //initialize the variables of the Flash form
  emailForm.SetVariable("name", "<%= getVar("name", "", session) %>");
  emailForm.SetVariable("email","<%= getVar("email", "", session) %>");
  emailForm.SetVariable("subject", "<%= getVar("subject", "", session) %>");
  emailForm.SetVariable("message", "<%= getVar("message", "", session) %>");
  emailForm.SetVariable("url", document.location);
}
//-->
</script>

<TITLE>email_form</TITLE>
</HEAD>
<BODY bgcolor="#FFFFFF" onLoad="setFlashVars()">
<!-- URL's used in the movie-->
<!-- text used in the movie-->
<!--Email: Message: Name: Please Fill in Your Infomation --><OBJECT classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"
 codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=5,0,0,0"
 ID="emailForm"
 WIDTH=550 HEIGHT=400>
 <PARAM NAME=movie VALUE="email_form.swf"> <PARAM NAME=quality VALUE=high> <PARAM NAME=bgcolor VALUE=#FFFFFF> <EMBED src="email_form.swf" quality=high bgcolor=#FFFFFF  WIDTH=550 HEIGHT=400 TYPE="application/x-shockwave-flash" PLUGINSPAGE="http://www.macromedia.com/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash"></EMBED>
</OBJECT>
</BODY>
</HTML>

<% }else{%>
<HTML>
<HEAD>
<TITLE>Email Submit</TITLE>
<BODY>
<H1>You Submitted the following info!</H1>

<B>Name:</B> <%=request.getParameter("name") %><BR>
<B>Email:</B> <%=request.getParameter("email") %><BR>
<B>Subject:</B> <%=request.getParameter("subject") %><BR>
<B>Message:</B> <%=request.getParameter("message") %><BR>

<%
   //Save the submitted variables in the HttpSession
   //so that the form can remember what was entered.
   session.setAttribute("name", request.getParameter("name"));
   session.setAttribute("email", request.getParameter("email"));
   session.setAttribute("subject", request.getParameter("subject"));
   session.setAttribute("message", request.getParameter("message"));
  
   //dump out all of the submitted variables as an HTML comment
   //to help debug the final values in the form.
   out.println("<!-----Debug output all vars: ------");
   Enumeration pNames = request.getParameterNames();
   while(pNames.hasMoreElements()){
      String pName = (String)pNames.nextElement();
      out.println(pName + ": " + request.getParameter(pName));
   }
   out.println("-->");
%>
</BODY>
</HTML>
<%}%>


<%! 
//Extract a variable from the session or return the default value if
//the variable is not defined in the session.
String getVar(String name, String defaultVal, HttpSession session){
   Object obj = session.getAttribute(name);
   if(obj == null){
      obj = defaultVal;
   }
   return obj.toString();
}
%>
