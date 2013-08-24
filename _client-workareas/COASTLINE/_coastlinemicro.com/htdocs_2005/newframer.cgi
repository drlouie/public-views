#!/usr/bin/perl5 -s


###########################################################################################################
# Company: ©2001 NetMedia Solutions                                                                       #
# Date: Saturday, September 21, 2001                                                                      #
# Location: Los Angeles County, California, United States of America                                      #
# Made By: Luis Rodriguez (drlouie)                                                                       #
# Email: Drlouie@NetMediaSol.com                                                                          #
#                                                                                                         #
# drlouie's GO script which allows to draw framing and scripting for outgoing links.           #
# Dynamically driven by DHTML, HTML, Perl and MySql                                                       #
#                                                                                                         #
# This program cannot be duplicated, distributed or re-used for any other purpose other than its original #
# intended purpose and function. You may request NetMedia Solutions for a copy of the script,             #
# personalized to fit your exact needs for a small re-programming fee.                                    #
###########################################################################################################

require ("parse_query.nsp");
require ("date.nsp");

if (($FORM{'subject'} && $FORM{'title'}) || $FORM{'PKeywords'} || $FORM{'keywords'} ) { 
	$subject = "$FORM{'subject'}";
	$title = "$FORM{'title'}";

	if ($FORM{'newIface'} eq "true") { $NIF = "&newIface=true"; }

	if ($FORM{'MSP'} eq "1") { $MSP = "&MSP=1"; }
	elsif ($FORM{'NMUSD'} eq "1") { $NMUSD = "&NMUSD=1"; }
	elsif ($FORM{'SEAGATE'} eq "1") { $NMUSD = "&SEAGATE=1"; }
	elsif ($FORM{'QUEST'} eq "1") { $NMUSD = "&QUEST=1"; }
	
	### IF COMES WITH PRODUCT THEN MUST BE A SHARKTANK CALL - A DB CALL - MAKE FRAME BY CALLING PRODUCTS SCRIPT
	if ($FORM{'loadthis'} || $FORM{'loadprod'} || $FORM{'loadsys'} || $FORM{'loadkit'} || $FORM{'cartit'}) {
		### NEW SHARKTANK ADDITION - IE ONLY
		if ($FORM{'loadthis'}) { $loadthis = "&loadthis=$FORM{'loadthis'}"; }
		elsif ($FORM{'loadprod'}) { $loadprod = "&loadprod=$FORM{'loadprod'}"; }
		elsif ($FORM{'loadkit'}) { $loadkit = "&loadkit=$FORM{'loadkit'}"; }
		elsif ($FORM{'loadsys'}) { $loadsys = "&loadsys=$FORM{'loadsys'}"; }
		elsif ($FORM{'cartit'}) { $cartit = "&cartit=$FORM{'cartit'}"; }
		$botOne ="<frame name=\"botOne\" noresize src=\"sharktank.cgi?title=$title$loadthis$loadprod$loadkit$loadsys$cartit$MSP$NMUSD$NIF\">";
	}

	### IF PRESS RELEASE CALL PRESENT MAKE - MAKE A FRAME AND CALL THE PRESS RELEASE AS NECESSARY
	elsif ($FORM{'viewRel'}) {
		$viewrel = "&viewRel=$FORM{'viewRel'}";
		$botOne ="<frame name=\"botOne\" noresize scrolling=\"Yes\" src=\"$subject.cgi?press.cgi&viewRel=$viewrel\">";
	}

	### IF HOMEPAGE SEARCH CALL
	elsif ($FORM{'PKeywords'}) {
		$botOne ="<frame name=\"botOne\" noresize scrolling=\"Yes\" src=\"Ns_prod.cgi?PKeywords=$FORM{'PKeywords'}&ProductType=All\">";
	}

	### IF HOMEPAGE SEARCH CALL
	elsif ($FORM{'keywords'}) {
		$botOne ="<frame name=\"botOne\" noresize scrolling=\"Yes\" src=\"Ns.cgi?keywords=$FORM{'keywords'}\">";
	}
	
	### IF RECONFIG SYSTEM CALL
	elsif ($FORM{'reconfigIt'}) {
		$botOne ="<frame name=\"botOne\" noresize scrolling=\"Yes\" src=\"$subject.cgi?title=$title&reconfigIt=$FORM{'reconfigIt'}$NIF\">";
	}

	### IF HOMEPAGE SEARCH CALL
	elsif ($FORM{'getpass'}) {
		$FORM{'PageTitle'} = "Secure Password Retrieval";
	}
	
	###MUST BE A COMMON WEBSITE CALL - GRAB NECESSARY###
	else { $botOne ="<frame name=\"botOne\" noresize scrolling=\"Yes\" src=\"$subject.cgi?title=$title$NIF\">"; }

	if ($FORM{'PageTitle'}) { $Pagetitle = "Coastline Micro, Inc. - $FORM{'PageTitle'}"; }
	else { $Pagetitle = "Coastline Micro, Inc. - Welcome to the Store Front"; }

print "Content-type: text/html\n\n";
{
print <<EOF


<html>
<head>
<title>$Pagetitle</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="keywords" content="coastlinemicro.com, www.coastlinemicro.com, coastline, micro, irvine, ca, california, about, company, location, businsess, competition, competitors, solutions, irvine, california, technology, ceo, own, partner, fast, reliable, heritage, sophisticated, computer, system, build, custom, sample, guarantee, search, product">
<meta name="description" content="Coastline Micro Inc. is in business to develop hardware solutions that make sense for the small to corporate sized business arena. We have been in business for over a decade and have the knowledge and expertise necessary to be competitive in the market. Our every product carries a 100% Product Satisfaction Guarantee. We are located in Irvine, California at 60 N. Technology Drive. For more information about our company and its what it is in business to do please follow the link above. Our company's Heritage dates back to 1989.">
</head>

<frameset rows="64,*" frameborder="NO" border="0" framespacing="0" cols="*">
  <frame name="topOne" noresize scrolling="No" src="http://www.rhomberg.com/systemConfigurator/newtopframe.cgi">
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
$sorry = `cat sorry_nospec.nsf`;

print "Content-type: text/html\n\n";
{
print <<EOF

$sorry

EOF
}
}
exit;