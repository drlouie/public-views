#!/usr/bin/perl5 -s

###########################################################################################################
# Company: ©2001 NetMedia Solutions                                                                             #
# Date: Saturday, September 21, 2001                                                                      #
# Location: Los Angeles County, California, United States of America                                      #
# Made By: Luis Rodriguez (drlouie)                                                                       #
# Email: Drlouie@NetMediaSol.com                                                                          #
#                                                                                                         #
# This program cannot be duplicated, distributed or re-used for any other purpose other than its original #
# intended purpose and function. You may request NetMedia Solutions for a copy of the script,             #
# personalized to fit your exact needs for a small re-programming fee.                                    #
###########################################################################################################

require ("referer.nsp"); 

require ("parse_query.nsp");

require ("date.nsp");

if ($FORM{'from_url'}) { $backme = "<a href=\"javascript:void(0)\" OnClick=\"parent.history.go(-1)\">"; }
else { $backme = "<a href=\"javascript:void(0)\" OnClick=\"parent.history.go(-1)\">"; }

print "Content-type: text/html\n\n";

{
print <<EOF


<html>
<head>
<style type="text/css">
a{text-decoration:underline;color:#ffffff;font-weight:bold}
a:hover{text-decoration:none;color:#ffffff;font-weight:bold}
</style>
<title>Coastline Micro Inc - Internet Link - $date </title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="keywords" content="coastlinemicro.com, www.coastlinemicro.com, coastline, micro, irvine, ca, california, about, company, location, businsess, competition, competitors, solutions, irvine, california, technology, ceo, own, partner, fast, reliable, heritage, sophisticated, computer, system, build, custom, sample, guarantee, search, product">
<meta name="description" content="Coastline Micro Inc. is in business to develop hardware solutions that make sense for the small to corporate sized business arena. We have been in business for over a decade and have the knowledge and expertise necessary to be competitive in the market. Our every product carries a 100% Product Satisfaction Guarantee. We are located in Irvine, California at 60 N. Technology Drive. For more information about our company and its what it is in business to do please follow the link above. Our company's Heritage dates back to 1989.">
</head>
<body bgcolor="#8f8fab" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<table width="100%" border="0" cellpadding="0" cellspacing="0" align="center">
<tr><td width="25%" align="left" height="35">&nbsp;&nbsp;&nbsp;$backme<img src="images/il_back_off.gif" border="0"></a></td><td align="center" width="50%" height="35"><font face="verdana,arial,helvetica" size="1" color="#ffffff"><b>You have clicked on a link out of CoastlineMicro.com<br>Use the BACK button to return to where you left off</font></b></td><td width="25%" align="right" height="35"><a href="#" OnClick="parent.history.go(1)"><img src="images/il_fwd_off.gif" border="0"></a>&nbsp;&nbsp;&nbsp;</td></tr>
</table>
</body>
</html>

EOF
}
exit;