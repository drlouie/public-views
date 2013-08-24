#!/usr/bin/perl5 -s

###########################################################################################################
# Company: �2001 NetMedia Solutions                                                                       #
# Date: Saturday, September 21, 2001                                                                      #
# Location: Los Angeles County, California, United States of America                                      #
# Made By: Luis Rodriguez (drlouie)                                                                       #
# Email: Drlouie@NetMediaSol.com                                                                          #
#                                                                                                         #
# CoastlineMicro.com's GO script which allows to draw framing and scripting for outgoing links.           #
# Dynamically driven by DHTML, HTML, Perl and MySql                                                       #
#                                                                                                         #
# This program cannot be duplicated, distributed or re-used for any other purpose other than its original #
# intended purpose and function. You may request NetMedia Solutions for a copy of the script,             #
# personalized to fit your exact needs for a small re-programming fee.                                    #
###########################################################################################################

require ("referer.nsp"); 
require ("parse_query.nsp");
require ("date.nsp");
## if form is calling for new_url forward to SUB NEW_URL
if ($FORM{'new_url'}) { 
	&new_url;
}
elsif ($FORM{'buyonline'}) { 
	&buyonline;
}
elsif ($FORM{'buyonline2'}) { 
	&buyonline2;
}
elsif ($FORM{'buyonline3'}) { 
	&buyonline3;
}
else {
$sorry = `cat sorry_nospec.nsf`;

print "Content-type: text/html\n\n";
{
print <<EOF

$sorry

EOF
}
}
exit;

sub new_url {
$new_url = "$FORM{'new_url'}";
print "Content-type: text/html\n\n";

{
print <<EOF

<html>
<head>
<title>Coastline Micro Inc. - $date</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>

<frameset rows="35, *" frameborder="NO" border="0" framespacing="0" cols="*">
  <frame name="topOut" noresize scrolling=no src="topout.html">
  <frame name="botOut" noresize src="$new_url">
</frameset>
<noframes>
<body bgcolor="#FFFFFF">
Sorry
</body>
</noframes>
</html>

EOF
}
}
exit;

sub buyonline {
$buyonline = "$FORM{'buyonline'}";
$botOne ="<frame name=\"botOne\" noresize src=\"go.html?buyonline2=1\">";

print "Content-type: text/html\n\n";

{
print <<EOF

<html>
<head>
<title>Coastline Micro Inc. - $date</title>
<meta name="keywords" content="coastlinemicro.com, www.coastlinemicro.com, coastline, micro, irvine, ca, california, about, company, location, businsess, competition, competitors, solutions, irvine, california, technology, ceo, own, partner, fast, reliable, heritage, sophisticated, computer, system, build, custom, sample, guarantee, search, product">
<meta name="description" content="Coastline Micro Inc. is in business to develop hardware solutions that make sense for the small to corporate sized business arena. We have been in business for over a decade and have the knowledge and expertise necessary to be competitive in the market. Our every product carries a 100% Product Satisfaction Guarantee. We are located in Irvine, California at 60 N. Technology Drive. For more information about our company and its what it is in business to do please follow the link above. Our company's Heritage dates back to 1989.">
</head>

<frameset rows="50,*" frameborder="NO" border="0" framespacing="0" cols="*">
  <frame name="topOne" noresize scrolling=no src="top_frame.html">
  $botOne
</frameset>
<noframes>
<body bgcolor="#FFFFFF">
Sorry
</body>
</noframes>
</html>

EOF
}
}
exit;

sub buyonline2 {
$buyonline2 = "$FORM{'buyonline2'}";

print "Content-type: text/html\n\n";

{
print <<EOF
<html>
<head>
<title>Coastline Micro Inc. - $date</title>
</head>
<body bgcolor="#FFFFFF" text="#333366" link="#333366" alink="#333366" vlink="#333366" onLoad="javascript:window.focus()">
<br><br>
<table width=400 align="center" border="0" cellpadding="0" cellspacing="0">
<tr height="100%"><td valign="middle"><br><br><center><img src="sharktank/images/logo_med.jpg" width="161" height="102" border="0"></center><font face="verdana,arial,helvetica" size="2" color="#333366"><br>Our E-Commerce system is currently being re-invented to accommodate our clients' ever changing needs. If you would like to get pricing on our state-of-the-art systems, we urge you to contact your Coastline Micro sales representative at 1-800-729-6809 or contact us online us by following the link below.<br><br><br><br><br><center><font size="1"><b><a href="javascript:history.go(-1);">Go Back</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="cont_temp.html?sub_link=gencomments">Contact Us Online</a></center></b></font></td></tr>
</table>
</body>
</html>
EOF
}
}
exit;

sub buyonline3 {
$buyonline3 = "$FORM{'buyonline3'}";
$botOne ="<frame name=\"botOne\" noresize src=\"http://www.flashecom.com/coastlinemicro/system_dept.asp?dept_id=$buyonline3\">";

print "Content-type: text/html\n\n";

{
print <<EOF

<html>
<head>
<title>Coastline Micro Inc. - $date</title>
<meta name="keywords" content="coastlinemicro.com, www.coastlinemicro.com, coastline, micro, irvine, ca, california, about, company, location, businsess, competition, competitors, solutions, irvine, california, technology, ceo, own, partner, fast, reliable, heritage, sophisticated, computer, system, build, custom, sample, guarantee, search, product">
<meta name="description" content="Coastline Micro Inc. is in business to develop hardware solutions that make sense for the small to corporate sized business arena. We have been in business for over a decade and have the knowledge and expertise necessary to be competitive in the market. Our every product carries a 100% Product Satisfaction Guarantee. We are located in Irvine, California at 60 N. Technology Drive. For more information about our company and its what it is in business to do please follow the link above. Our company's Heritage dates back to 1989.">
</head>

<frameset rows="50,*" frameborder="NO" border="0" framespacing="0" cols="*">
  <frame name="topOne" noresize scrolling=no src="top_frame.html">
  $botOne
</frameset>
<noframes>
<body bgcolor="#FFFFFF">
Sorry
</body>
</noframes>
</html>

EOF
}
}
exit;