#!/usr/bin/perl5 -w

###########################################################
# This CGI Software written by NetMedia Solutions         #
# http://www.netmediasol.com                              #
#                                                         #
# Software Written by:                                    #
# Luis Rodriguez (drlouie)                                #
#                                                         #
# If you have any questions or problems with this script  #
# Please contact me directly for help                     #
# drlouie@hapasol.com                                     #
###########################################################

## test location of request
require ("referer.nsp");

print "Content-type: text/html\n\n";

## Grab User Input
require ("parse_query.nsp");

## get needed cookies
require 'cookie.lib';
&GetCookies('Username');
&GetCookies('UserType');
&GetCookies('FirstName');
&GetCookies('LastName');

{
print <<EOF

<html>
<head>
<title>Coastline Micro Inc.</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<SCRIPT LANGUAGE="JavaScript">
// QUICK CROSS-BROWSER MOUSE-OVER/OFF FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function imageOff(which,thisone) {
	var cual = 	"images/button_"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}
function imageOn(which,thisone) {
	var cual = 	"images/button_"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}
</SCRIPT>
<script language="javascript">
<!--
function trigger(myurl) {
var b = navigator.appName;
if (b=="Netscape") {
	mainFrame = parent.frames.botOne;
	mainFrame.frame.loadpage(''+myurl+'');
	}

else {
	parent.botOne.frame.loadpage(''+myurl+'');
	}
}
//-->
</script>
</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:window.focus()">
<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td rowspan="2" width="15%" align="center" valign="middle"><img src="images/top_cm_logo.jpg" width="116" height="37"></td>
    <td rowspan="2" align="center" valign="middle" width="40%"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Welcome to the Shark Tank&#153; $Cookies{'FirstName'} $Cookies{'LastName'}...</b><br><a href="logoff.cgi" target="_parent">I am not $Cookies{'FirstName'}!</a></font></td>
    <td width="45%" align="right"><img src="images/god_bless_america.gif" width="118" height="35">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
  </tr>
  <tr> 
    <td width="45%" align="right"><a href="./" target="_top" onMouseOver="javascript:imageOn('home','on');" onMouseOut="javascript:imageOff('home','off');"><img src="images/button_home_off.gif" width="61" height="19" name="home" border="0"></a><a href="change_user.cgi?Username=$Cookies{'Username'}&LastName=$Cookies{'LastName'}" target="botOne" onMouseOver="javascript:imageOn('prefs','on');" onMouseOut="javascript:imageOff('prefs','off');"><img src="images/button_prefs_off.gif" width="75" height="19" name="prefs" border="0"></a><a href="logoff.cgi" target="_parent" onMouseOver="javascript:imageOn('logoff','on');" onMouseOut="javascript:imageOff('logoff','off');"><img src="images/button_logoff_off.gif" width="75" height="19" name="logoff" border="0"></a></td>
  </tr>
<tr>
    <td colspan="3" width="100%" bgcolor="#FFFFFF" height="2"><img src="images/spacer.gif" width="2" height="2"></td>
  </tr>
<tr>
    <td colspan="3" width="100%" bgcolor="#8F8FAB" height="2"><img src="images/spacer.gif" width="2" height="2"></td>
  </tr>
<tr>
    <td colspan="3" width="100%" bgcolor="#FFFFFF" height="2"><img src="images/spacer.gif" width="2" height="2"></td>
  </tr>
</table>
<form><input type="hidden" name="ME" value="change_user.cgi?Username=$Cookies{'Username'}&LastName=$Cookies{'LastName'}"></form>
</body>
</html>

EOF
}