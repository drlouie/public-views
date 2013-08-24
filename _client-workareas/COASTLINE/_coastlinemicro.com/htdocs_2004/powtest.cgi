#!/usr/bin/perl5 -s

#######################################################################################################
# Company: NetMedia Solutions                                                                         #
# Date: Saturday, September 21, 2001                                                                  #
# Location: Los Angeles, California, United States of America                                         #
# Made By: Luis Rodriguez (drlouie)                                                                   #
# Email: drlouie@tstonramp.com                                                                        #
#                                                                                                     #
# CoastlineMicro.com's products main page. Dynamically driven by DHTML, HTML, Perl and MySql          #
#                                                                                                     #
#######################################################################################################

require ("referer.nsp"); 
require ("parse_query.nsp");
require ("date.nsp");
require ("whichpow.nsp");
$powbutton = "<a href=\"javascript:checkPosition();\" onMouseOver=\"javascript:mouseOvered();\" onMouseOut=\"javascript:mouseOffed();\"><img src=\"images/newmenu/menuhide_off.gif\" name=\"powbar\"  border=0 width=172 height=22></a><br>";
$checkposition = "javascript:checkPosition();";
print "Content-type: text/html\n\n";
{
print <<EOF

<html><head>
<title>
</title>
</head>
<body bgcolor="#ffffff" text="#8f8fab" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="$checkposition">

$powbutton

$pow

</body>
</html>

EOF
}
exit;