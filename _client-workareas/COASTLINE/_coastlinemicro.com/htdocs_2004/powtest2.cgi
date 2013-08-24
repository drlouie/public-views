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
require ("whichpow2.nsp");
$powbutton = "<a href=\"javascript:checkPosition();\" onMouseOver=\"javascript:mouseOvered();\" onMouseOut=\"javascript:mouseOffed();\"><img src=\"images/newmenu/menuhide_off.gif\" name=\"powbar\"  border=0 width=172 height=22></a><br>";
print "Content-type: text/html\n\n";
{
print <<EOF

<html><head>
<title>
</title>
</head>  
<body bgcolor="#ffffff" onLoad="runPow();">

$powbutton

$pow

</body>
</html>

EOF
}
exit;