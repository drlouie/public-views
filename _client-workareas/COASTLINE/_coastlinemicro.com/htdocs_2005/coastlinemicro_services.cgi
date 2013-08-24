#!/usr/bin/perl5 -s

###########################################################################################################
# Company: ©2001 NetMedia Solutions                                                                       #
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


if ($FORM{'title'}) { 
	print "Content-type: text/html\n\n";
	$pow = `cat pow_products.nsf`;
	## must have command to run search
	$powbutton = "";
	if ($FORM{'title'} ne "UPSTracking" || $FORM{'title'} ne "UPSShipping" || $FORM{'title'} ne "UPSTools" || $FORM{'title'} ne "FEDEXTools" || $FORM{'title'} ne "FEDEXShipping" || $FORM{'title'} ne "FEDEXTracking") {
		$title = "$FORM{'title'}";
		$filename = "content/services/$title.txt";
		$dropme = `cat $filename`;
		$legal = `cat legal.nsf`;
	}

if ($FORM{'title'} eq "tigerNAS" || $FORM{'title'} =~ "tigerNAS") { $myTitle = "title_tigerNAS.jpg"; }
else { $myTitle = "title_services.jpg"; }
	
	
{
print <<EOF
<html>
<head>
<title>Company Name</title>
<SCRIPT LANGUAGE="JavaScript">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

<!-- Begin
function loadScript() {
if (document.getElementById) {  // DOM3 = IE5, NS6
document.getElementById('hidepage').style.visibility = 'hidden';
}
else {
if (document.layers) {  // Netscape 4
document.hidepage.visibility = 'hidden';
}
else {  // IE 4
document.all.hidepage.style.visibility = 'hidden';
      }
   }
}
//  End -->
</script>
<style type="text/css">
#hidepage {z-index:2000}
body { scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</style>
<div id="hidepage" style="position: absolute; left:0px; top:0px; background-color: #FFFFFF; layer-background-color: #FFFFFF; height: 100%; width: 100%;">
<table width=100% cellpadding="0" cellspacing="0">
<tr height="100%"><td align="center" valign="middle"><br><br><img src="sharktank/images/cm_logo_large.jpg" width="166" height="59" border="0"><font face="verdana,arial,helvetica" size="2" color="#333366"><br><br>Loading DHTML interactive user interface, please wait...<br><br><br><br><br><font size="1"><b><u>Compatibility</u></b><br><br>Win/Mac MSIE 4/5/6<br>Win/Mac/Linux Netscape 4/6<br><br><i>Best if viewed on Windows 95/98/2000 platform using MSIE 4+</i></font></font></td></tr>
</table>
</div> 
<script language="JavaScript" src="js/reload.js"></script>

<!--FOLLOWING EXTERNAL SCRIPT IS USED FOR BROWSER TESTING AND IS INTEGRAL PART OF POW-->
<script language="JavaScript" src="js/dynlayer.js"></script>
<!--END-->

<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="keywords" content="coastlinemicro.com, www.coastlinemicro.com, coastline, micro, irvine, ca, california, about, company, location, businsess, competition, competitors, solutions, irvine, california, technology, ceo, own, partner, fast, reliable, heritage, sophisticated, computer, system, build, custom, sample, guarantee, search, product">
<meta name="description" content="Coastline Micro Inc. is in business to develop hardware solutions that make sense for the small to corporate sized business arena. We have been in business for over a decade and have the knowledge and expertise necessary to be competitive in the market. Our every product carries a 100% Product Satisfaction Guarantee. We are located in Irvine, California at 60 N. Technology Drive. For more information about our company and its what it is in business to do please follow the link above. Our company's Heritage dates back to 1989.">
<script language="JavaScript" src="js/menu_config.js"></script>
<LINK REL="STYLESHEET" HREF="common_css.cgi" Type="text/css">

</head>
<body bgcolor="#ffffff" text="#333366" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:loadScript();runSearch();">

<!-- Copyright NetMedia Solutions and Coasltine Micro, Inc.-->
<script language="Javascript" src="js/newmenu_constructor.js"></script>


<table width="100%" border="0" cellspacing="0" cellpadding="0" height="22" bgcolor="#01458E">
  <tr>
    <td width="100%" height="1" bgcolor="#FFFFFF"><img src="images/spacer.gif" width="1" height="1" border="0"></td>
  </tr>
  <tr>
    <td width="100%"><img src="images/spacer.gif" width="1" height="20" border="0"></td>
  </tr>
  <tr>
    <td width="100%" height="1" bgcolor="#FFFFFF"><img src="images/spacer.gif" width="1" height="1" border="0"></td>
  </tr>
</table>

<!-- Start header table -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/newones/2k3/top_tablebg.jpg" height="100">
  <tr> 
    <td width="30%"><img src="images/newones/2k3/illus_services.jpg" width="250" height="100" border="0"></td>
    <td align="right" valign="middle" width="70%"><font size="1" color="#ffffff" face="verdana,arial,helvetica">$date&nbsp;&nbsp;<font size="3">&nbsp;</font></font>
	<center><img src="images/newones/2k3/$myTitle" width="350" height="80" align="bottom"></center></td>
  </tr>
</table>
<!-- End header table -->

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="5"><img src="images/140spacer.gif" width="5" height="8"></td>
    <td width="100%" align="center" valign=top><br>

EOF
}


if ($FORM{'title'} eq "UPSTracking" || $FORM{'title'} eq "UPSShipping" || $FORM{'title'} eq "UPSTools") {
	print '
<table border="1" cellpadding="5" cellspacing="0" bordercolor="#330000">
<tr><td>
	<table border="0" cellpadding="0" cellspacing="0" width="350" bgcolor="#330000">
	<tr>
	<td rowspan="3" align="center"><nobr><img src="images/spacer.gif" width="20" height="133" border="0"><img src="images/upsLarge.gif" width="119" height="133" border="0"></nobr></td>
	<td align="center" width="100%"><font face="verdana,arial,helvetica" size="3" color="#FFC256"><b><nobr>&nbsp;&nbsp;&nbsp;Package Tracking&nbsp;&nbsp;&nbsp;</nobr></b></font></td>
	</tr>
	<tr height="1">
	<td align="center" height="1"><img src="images/spacer_orange.gif" width="120" height="1" border="0"></td>
	</tr>
	<tr>
	<td align="center" width="100%"><font face="verdana,arial,helvetica" size="3" color="#FFC256"><b><nobr>&nbsp;&nbsp;&nbsp;Shipping Calculator&nbsp;&nbsp;&nbsp;</nobr></b></font></td>
	</tr>
	</table>
</td></tr>
</table>
	';

	require("trackUPS.nsp");
}
elsif ($FORM{'title'} eq "UPSTracking" || $FORM{'title'} eq "UPSShipping" || $FORM{'title'} eq "UPSTools" || $FORM{'title'} eq "FEDEXTools" || $FORM{'title'} eq "FEDEXShipping" || $FORM{'title'} eq "FEDEXTracking") {
	print '
<table border="1" cellpadding="0" cellspacing="0" bordercolor="#5C0092">
<tr><td>
	<table border="0" cellpadding="0" cellspacing="0" width="350">
	<tr>
	<td rowspan="3" align="center"><nobr><img src="images/spacer.gif" width="20" height="133" border="0"><img src="images/fedexLarge.gif" width="119" height="133" border="0"></nobr></td>
	<td align="center" width="100%"><font face="verdana,arial,helvetica" size="3" color="#9CA19A"><b><nobr>&nbsp;&nbsp;&nbsp;Package Tracking&nbsp;&nbsp;&nbsp;</nobr></b></font></td>
	</tr>
	<tr height="1">
	<td align="center" height="1"><img src="images/spacer_gray.gif" width="120" height="1" border="0"></td>
	</tr>
	<tr>
	<td align="center" width="100%"><font face="verdana,arial,helvetica" size="3" color="#9CA19A"><b><nobr>&nbsp;&nbsp;&nbsp;Shipping Calculator&nbsp;&nbsp;&nbsp;</nobr></b></font></td>
	</tr>
	</table>
</td></tr>
</table>
	';

	require("trackFEDEX.nsp");
}
else {
	print "$dropme";
}

{
print <<EOF
	</td>
  </tr>
</table>

<!-- Dynamic Moving Layers -->
$pow
</body>
</html>

EOF
}
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