<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<HEAD>
<META name="GENERATOR" content="IBM WebSphere Page Designer V3.5.3 for Windows">
<META http-equiv="Content-Style-Type" content="text/css">
<TITLE>Broker Administration System Exchange</TITLE>
<SCRIPT LANGUAGE="JavaScript">
function refreshFrame() {
frames['sideLink'].window.location.href = "/BASEWeb/Purchaser/SideLink.jsp";
 // frame 1's page
}
</SCRIPT>
</HEAD>
<FRAMESET rows="142,*" frameborder="NO" border="0" >
  <FRAME name="tops" src="/BASEWeb/Purchaser/PurTop.jsp"  scrolling="no" marginheight="0" marginwidth="0" noresize>
  <FRAMESET cols="165,*" frameborder="NO" border="0" onLoad="refreshFrame();">
    <FRAME name="sideLink" src="/BASEWeb/Purchaser/SideLink.jsp" marginheight="0" marginwidth="0" scrolling="no" noresize>
    <FRAME name="display" src="/BASEWeb/Purchaser/<%=(String)session.getAttribute("Destination")%>" scrolling="auto" marginheight="0" marginwidth="0" >
  </FRAMESET>
  <NOFRAMES>
  <BODY >
  <P>To view this page, you need a browser that supports frames.</P>
  </BODY>
  </NOFRAMES>
</FRAMESET>
</HTML>

