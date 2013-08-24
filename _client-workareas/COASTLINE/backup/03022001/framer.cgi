#!/usr/local/bin/perl

require ("referer.hs"); 

require ("parse_query.hs");

require ("date.hs");

if (($FORM{'new_url'}) && ($FORM{'sub_link'})) { 

####################################
###ACQUIRE SECTION NAME FROM LINK###
####################################
$new_url = "$FORM{'new_url'}";

#######################################
###ACQUIRE SUBSECTION NAME FROM LINK###
#######################################
$sub_link = "$FORM{'sub_link'}";

print "Content-type: text/html\n\n";

###############################################################################
###DETECT IF TITLE IS SPECIFIED WITHIN LINK, IF SO WRITE NEW LINK WITH SPECS###
###############################################################################
if ($FORM{'title'}) { 

$title = "$FORM{'title'}";

$botOne ="<frame name=\"botOne\" noresize src=\"$new_url?sub_link=$sub_link&title=$title\">";

}
#############################################
###ELSE WRITE NEW LINK WITHOUT TITLE SPECS###
#############################################
else {

$botOne ="<frame name=\"botOne\" noresize src=\"$new_url?sub_link=$sub_link\">";
}

{
print <<EOF


<html>
<head>
<title>:::::::::::   Coastline Micro Online   :::::::::::</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
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

######################################
###NO SECTION NAME SPECIFIED SORRY!###
######################################
else {
$sorry = `cat sorry_nospec.hs`;

print "Content-type: text/html\n\n";
{
print <<EOF

$sorry

EOF
}
}
