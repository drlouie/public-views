#!/usr/local/bin/perl

require ("referer.hs"); 

require ("parse_query.hs");

require ("date.hs");

print "Content-type: text/html\n\n";

{
print <<EOF


<html>
<head>
<style type="text/css">
a{text-decoration:none;color:#ffffff}
a:hover{text-decoration:underline;color:#ffffff}
</style>
<title>Coastline Micro Inc - Internet Link - $date </title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="keywords" content="coastlinemicro.com, www.coastlinemicro.com, coastline, micro, irvine, ca, california, about, company, location, businsess, competition, competitors, solutions, irvine, california, technology, ceo, own, partner, fast, reliable, heritage, sophisticated, computer, system, build, custom, sample, guarantee, search, product">
<meta name="description" content="Coastline Micro Inc. is in business to develop hardware solutions that make sense for the small to corporate sized business arena. We have been in business for over a decade and have the knowledge and expertise necessary to be competitive in the market. Our every product carries a 100% Product Satisfaction Guarantee. We are located in Irvine, California at 60 N. Technology Drive. For more information about our company and its what it is in business to do please follow the link above. Our company's Heritage dates back to 1989.">
</head>
<body bgcolor="#8f8fab" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<center>
<table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0">
<tr><td align="center"><font face="verdana,arial,helvetica" size="2"><b><a href="#" OnClick="parent.window.close()">>&nbsp;>&nbsp;>&nbsp;You have clicked on a link out of Coastline Micro, to get back Click Here&nbsp;<&nbsp;<&nbsp;<</a></font></b></td></tr>
</table>
<center>
</body>
</noframes>
</html>

EOF
}
