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

## destroy all cookies as of now, log browser off
require 'cookie.lib';
print "Content-type: text/html\n";
## Set cookie date to now to kill it immediately
## Wdy, DD-Mon-YYYY HH:MM:SS GMT
&SetCookies('Logged','NO');
&SetCookies('Username','');
&SetCookies('Password','');
&SetCookies('FirstName','');
&SetCookies('LastName','');
&SetCookies('UserType','');
print "\n";


## Grab User Input
require ("parse_query.nsp");

{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - Get My Password</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<form method="post">
<table width="100%" border="0" height="100%" cellpadding="0" cellspacing="0">
  <tr>
    <td width="25%" height="50">&nbsp;</td>
    <td width="50%" height="50">&nbsp;</td>
    <td width="25%" height="50">&nbsp;</td>
  </tr>
  <tr>
    <td width="25%">&nbsp;</td>
      <td align="center" width="50%" valign="middle"><img src="images/splash_logos.jpg" width="166" height="164"><br>
        <br>
        <font face="verdana,arial,helvetica" size="1" color="#333366"><b>Logged Off Successfully</b><br>
        <br>
        </font> 
        <table width="350" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td width="100%"><font face="verdana,arial,helvetica" size="1" color="#333366">You have been successfully logged off the system. Any reports of bugs or suggestions for functionality are greatly appreciated by the Coastline Micro Management.<br><br><center><form><input type="button" value="Re-Login" onClick="javascript:parent.location.href='login.cgi?lasturl=index.cgi'"></form></center></font></td>
          </tr>
        </table>
    </td>
      <td width="25%">&nbsp;</td>
  </tr>
  <tr>
    <td width="25%" height="50">&nbsp;</td>
    <td width="50%" height="50">&nbsp;</td>
    <td width="25%" height="50">&nbsp;</td>
  </tr>
</table>
</form>
</body>
</html>

EOF
}

exit;