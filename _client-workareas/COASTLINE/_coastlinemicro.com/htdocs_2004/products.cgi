#!/usr/bin/perl5 -s

###########################################################################################################
# Company: �2001 NetMedia Solutions                                                                       #
# Date: Saturday, September 21, 2001                                                                      #
# Location: Los Angeles County, California, United States of America                                      #
# Made By: Luis Rodriguez (drlouie)                                                                       #
# Email: Drlouie@NetMediaSol.com                                                                          #
#                                                                                                         #
# CoastlineMicro.com's DB product table parsing script. Dynamically driven by DHTML, HTML, Perl and MySql #
#                                                                                                         #
# This program cannot be duplicated, distributed or re-used for any other purpose other than its original #
# intended purpose and function. You may request NetMedia Solutions for a copy of the script,             #
# personalized to fit your exact needs for a small re-programming fee.                                    #
###########################################################################################################

require ("referer.nsp"); 
require ("parse_query.nsp");
require ("date.nsp");

## Snif cookie, if present test for logged in status
require ("cookiesnif.nsp");


if ($FORM{'SEAGATE'} eq "1") { $light1 = "C3D6D5"; $dark1 = "000000"; $dark2 = "387675"; }
elsif ($FORM{'QUEST'} eq "1") { $light1 = "CAD8E8"; $dark1 = "01458E"; $dark2 = "01458E"; }
else { $light1 = "F2F2F7"; $dark1 = "000000"; $dark2 = "$dark2"; }

if ($FORM{'title'}) { 
	$title = "$FORM{'title'}";
	if ($title eq "quest") { $legal = `cat quest_legal.nsf`; }
	else { $legal = `cat prod_legal.nsf`; }
	$LoadIT = "0";
##	if (!$FORM{'loadprod'} && !$FORM{'loadsys'} && !$FORM{'reconfigIt'} && !$FORM{'loadcart'} && !$FORM{'cartit'} && !$FORM{'newConfig'} && !$FORM{'stankCSE'}) {
##		require ("whichpow2.nsp");
##		$powerPunch = "runPow();";
##		$powbutton = "<a href=\"javascript:checkPosition();\" onMouseOver=\"javascript:mouseOvered();\" onMouseOut=\"javascript:mouseOffed();\"><img src=\"images/newmenu/menuhide_off.gif\" name=\"powbar\" border=\"0\" width=\"192\" height=\"22\"></a><br>";
##	}
##	else {
		$pow = `cat pow_products.nsf`;
		## must have command to run search
		$powerPunch = "runSearch();";
		$powbutton = "";	
##	}

	$browser = "$ENV{'HTTP_USER_AGENT'}";
	## Thresher 2 - MSP (Intel's Model School Program) - Gets a different dynamic frame placement
	if ($browser =~ "MSIE" || $browser =~ "Netscape") {
		$zindex = "";
	}
	else {
		$zindex = "z-index:5";
	}
	if($title eq "thresher2") {
		$divcont = "#divCont{position:absolute; overflow:hidden; left:375; top:243; clip:rect(0,470,450,0); height:450; width:470;}";
		$divload = "#divLoad{position:absolute; left:375; top:243; clip:rect(0,470,450,0); height:450; width:470; visibility:hidden;}";
		$divArrows = "#divArrows{position:absolute; left:850; top:310; z-index:25; visibility:hidden}";
		$divBground = "#bground{position:absolute; left:374; top:242; clip:rect(0,472,452,0); height:452; width:472;$zindex}";
		## blank title image 
		$imagetitle = "blank";
	}
	## All other product calls come with the same dynamic frame placement
	else {
		$divcont = "#divCont{position:absolute; overflow:hidden; left:375; top:180; clip:rect(0,470,450,0); height:450; width:470;}";
		$divload = "#divLoad{position:absolute; left:375; top:180; clip:rect(0,470,450,0); height:450; width:470; visibility:hidden;}";	
		$divArrows = "#divArrows{position:absolute; left:850; top:250; z-index:25; visibility:hidden}";
		$divBground = "#bground{position:absolute; left:374; top:179; clip:rect(0,472,452,0); height:452; width:472;$zindex}";
		## dynamic title image
		if ($title eq "tpp" || $title eq "seagate" || $title eq "quest") { $imagetitle = "products"; }
		else { $imagetitle = "$title"; }
	}

	
	###CUAL MAIN HEADER?
	if ($title eq "seagate" || $title eq "quest") {
		if ($title eq "seagate") { 
			if ($FORM{'loadthis'} eq "seagate") { $cualMainHeader = "<a href=\"products.html?title=seagate&loadthis=seagate&SEAGATE=1\"><img src=\"images/seagate_headerL.jpg\" width=\"343\" height=\"107\" border=\"0\">"; }
			else { $cualMainHeader = "<a href=\"products.html?title=seagate&loadthis=seagate&SEAGATE=1\"><img src=\"images/seagate_header.jpg\" width=\"240\" height=\"107\" border=\"0\"></a>"; }
			$cualCSS = "<LINK REL=\"STYLESHEET\" HREF=\"common_css.html?SEAGATE=1\" Type=\"text/css\">";
			$cualIllus = "illus_sharktank_seagate.jpg";
			$cualIllusBG = "top_tablebg_seagate.jpg";
			$imagetitle = $imagetitle . "_seagate";
		}
		elsif ($title eq "quest") { 
			if ($FORM{'loadthis'} eq "quest") { $cualMainHeader = "<br><a href=\"products.html?title=quest&loadthis=quest&QUEST=1\"><img src=\"images/quest_headerL.jpg\" width=\"255\" height=\"49\" border=\"0\">"; }
			else { $cualMainHeader = "<a href=\"products.html?title=quest&loadthis=quest&QUEST=1\"><img src=\"images/quest_headerL.jpg\" width=\"255\" height=\"49\" border=\"0\"></a>"; }
			$cualCSS = "<LINK REL=\"STYLESHEET\" HREF=\"common_css.html?QUEST=1\" Type=\"text/css\">";
			$cualIllus = "illus_sharktank_quest.jpg";
			$cualIllusBG = "top_tablebg_quest.jpg";
			$imagetitle = $imagetitle . "_quest";
		}
	}
	else { 
		$cualMainHeader = "<img src=\"images/newmenu/place_holder.gif\" width=\"190\" height=\"10\">"; 
		$cualCSS = "<LINK REL=\"STYLESHEET\" HREF=\"common_css.html\" Type=\"text/css\">";
		$cualIllus = "illus_sharktank.jpg";
		$cualIllusBG = "top_tablebg_main.jpg";
	}
	
	## PAGELOAD ONBODYLOAD function which works only in IE
	if ($browser) {
		$extraspacer = "";

	if ($FORM{'MSP'} eq "1") { $MSP = "&MSP=1"; }
	if ($FORM{'NMUSD'} eq "1") { $NMUSD = "&NMUSD=1"; }

	if ($FORM{'TPP'} eq "1") { 
		$NMUSD = "&TPP=1";
		$menu1 = "";	
		$menu2 = "";
	}
	elsif ($FORM{'SEAGATE'} eq "1") { 
		$NMUSD = "&SEAGATE=1";
		$menu1 = "";	
		$menu2 = "";
	}
	elsif ($FORM{'QUEST'} eq "1") { 
		$NMUSD = "&QUEST=1";
		$menu1 = "";	
		$menu2 = "";
	}
	elsif ($FORM{'title'} eq "tpp") {
		$menu1 = "";	
		$menu2 = "";	
	}
	else {
		$menu1 = "<script language=\"JavaScript\" src=\"js/menu_config.js\"></script>";
		$menu2 = "<script language=\"Javascript\" src=\"js/menu_constructor.js\"></script>";
	}	
		if ($FORM{'loadthis'}) {
			## IF SYSTEM, LOAD SYSTEM START PAGE
			if ($FORM{'loadthis'} eq "thresher" || $FORM{'loadthis'} eq "thresher2" || $FORM{'loadthis'} eq "tiger" || $FORM{'loadthis'} eq "gw" || $FORM{'loadthis'} eq "reef" || $FORM{'loadthis'} eq "mako" || $FORM{'loadthis'} eq "nmusd" || $FORM{'loadthis'} eq "nmusdCustCom" || $FORM{'loadthis'} eq "tpp" || $FORM{'loadthis'} eq "seagate" || $FORM{'loadthis'} eq "quest") { 
				$loadthis = "stank_startpage_real.nsp";
				$FORM{'Series'} = $FORM{'loadthis'};
			}
			## ELSE MUST BE A PRODUCT CALL
			else { 
				$loadthis = "stank_startpage_real.nsp";
				$FORM{'CMPartNum'} = $FORM{'loadthis'}; 
			}
		}
		elsif ($FORM{'loadprod'}) {
			$loadthis = "stank_viewprod_real.nsp";
			$FORM{'CMPartNum'} = $FORM{'loadprod'};
		}
		elsif ($FORM{'loadsys'}) {
			$loadthis = "stank_sysbrowse_real.nsp";
			$FORM{'CMPartNum'} = $FORM{'loadsys'};
		}
		elsif ($FORM{'reconfigIt'}) {
			$loadthis = "stank_reconfig_real.nsp";
			$FORM{'CMPartNum'} = $FORM{'reconfigIt'};
			$loadscript = "feedAllParts();";
		}
		elsif ($FORM{'newConfig'}) {
			$loadthis = "stank_newconfig_real.nsp";
			$FORM{'CMPartNum'} = $FORM{'CMPartNum'};
			$loadscript = "";
		}
		elsif ($FORM{'CartSaveEQuote'}) {
			if ($FORM{'CartSaveEQuote'} eq "SAVE") { $loadthis = "stank_save_real.nsp"; } 
			elsif ($FORM{'CartSaveEQuote'} eq "EQUOTE") { $loadthis = "stank_equote_real.nsp"; } 
			elsif ($FORM{'CartSaveEQuote'} eq "CART") { $loadthis = "stank_cartit_real.nsp"; } 			
			## $FORM{'CMPartNum'} is already available...
			$loadscript = "";
		}
		elsif ($FORM{'specIt'}) {
			$loadthis = "stank_techspecs_real.nsp";
			$FORM{'CMPartNum'} = $FORM{'specIt'};
		}
		elsif ($FORM{'sysdrivers'}) {
			$loadthis = "stank_sysdrivers_real.nsp";
			$FORM{'CMPartNum'} = $FORM{'sysdrivers'};
		}
		elsif ($FORM{'images'}) {
			$loadthis = "stank_images_real.nsp";
			$FORM{'CMPartNum'} = $FORM{'images'};
		}
		elsif ($FORM{'loadcart'}) {
			$loadthis = "stank_mycart_real.nsp";
		}
		elsif ($FORM{'checkout'}) {
			$loadthis = "stank_checkout_real.nsp";
			$loadscript = "runShip();";
		}
		elsif ($FORM{'CO'}) {
			$loadthis = "stank_CO_real.nsp";
			$loadscript = "";
		}
		elsif ($FORM{'cartit'}) {
			$loadthis = "stank_cse.cgi";
			$FORM{'CID'} = $FORM{'cartit'};
		}
	}
	else { 
		if ($title = "thresher2") { $extraspacer = "<table width=\"100%\" align=\"center\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" bgcolor=\"#ffffff\"><tr><td height=\"165\">&nbsp;</td></tr></table>"; }
		else { $extraspacer = "<table width=\"100%\" align=\"center\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" bgcolor=\"#ffffff\"><tr><td height=\"105\">&nbsp;</td></tr></table>"; }
	}
	
	if($title eq "tpp" || $title eq "seagate" || $title eq "quest") {
		if ($FORM{'loadthis'}) { 
			$whichdrop = `cat sharktank/$title\_drop.nsf`;
		}
		else {
			if ($FORM{'SEAGATE'} eq "1") { $whichdrop = `cat sharktank/seagate_gui.nsf`; }
			elsif ($FORM{'QUEST'} eq "1") { $whichdrop = `cat sharktank/quest_gui.nsf`; }
			else { $whichdrop = `cat sharktank/products_drop.nsf`; }
			require ($loadthis);
			$THETABLE = $pageDrop;
			$whichdrop =~ s/!!!MYCONTENT!!!/$THETABLE/;
		}
	}
	else {
		$whichdrop = `cat sharktank/$title\_drop.nsf`;
		require ($loadthis);
		$THETABLE = $pageDrop;
		$whichdrop =~ s/!!!MYCONTENT!!!/$THETABLE/;
	}
	
	## IF $loadthis has not produced a $pageHeader (ie: STANK_CSE) then parse common page header
	if (!$pageHeader) { print "Content-type: text/html\n\n"; }
	
{
print <<EOF

<html>
<head>
<title>Coastline Micro Inc.</title>
<script langauge="JavaScript" src="js/overlib.js"></script>
<script language="JavaScript" src="js/reload.js"></script>
<SCRIPT LANGUAGE="JavaScript">
// QUICK CROSS-BROWSER MOUSE-OVER/OFF FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function imageOff(which,thisone) {
	var cual = 	"images/tables/but_"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}
function imageOn(which,thisone) {
	var cual = 	"images/tables/but_"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}
</SCRIPT>

<SCRIPT LANGUAGE=\"JavaScript\">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are �2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

// QUICK CROSS-BROWSER MOUSE-OVER/OFF FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

// Specific Mouseover for DHTML window, must be placed on main document in order to work for
// MSIE 4 & 5

function imageOffDHTML(which,thisone) {
	var cual = 	"images/tables/but_"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}
function imageOnDHTML(which,thisone) {
	var cual = 	"images/tables/but_"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}

EOF
}

###>>> START CGI <<<###
if ($FORM{'newConfig'}) {
{
print <<EOF
function imageOffDHTML2(daobject,which,thisone) {
	var cual = 	"images/newones/"+which+"_"+thisone+".gif";
	daobject.src = cual;
}
function imageOnDHTML2(daobject,which,thisone) {
	var cual = 	"images/newones/"+which+"_"+thisone+".gif";
	daobject.src = cual;
}
EOF
}

}
else {
{
print <<EOF
function imageOffDHTML2(which,thei,thisone) {
	var cual = 	"images/db/but_"+thei+"_"+thisone+".gif";
	document.images[which].src = cual;
}
function imageOnDHTML2(which,thei,thisone) {
	var cual = 	"images/db/but_"+thei+"_"+thisone+".gif";
	document.images[which].src = cual;
}

EOF
}

}

{
print <<EOF

function imageOffDHTML3(which,thisone) {
	var cual = 	"images/newones/"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}
function imageOnDHTML3(which,thisone) {
	var cual = 	"images/newones/"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}

function imageOffDHTML4(me,which,thisone) {
	var cual = 	"images/newones/"+which+"_"+thisone+".gif";
	me.src = cual;
}
function imageOnDHTML4(me,which,thisone) {
	var cual = 	"images/newones/"+which+"_"+thisone+".gif";
	me.src = cual;
}

function trigger(myurl) {
	location.href=myurl;
}
</script>

<!--START PRINT-->

<SCRIPT LANGUAGE=\"JavaScript\">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are �2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

<!--
function runTemplate(script,direction,type) {
    window.open(script+'?'+direction+'='+type+'&NSPRINT=1','PRINT','width=485,height=590');
  	return false;
}

function toggleEmailer(url) {
    window.open(url,'EMAILER','width=485,height=590');
}
// -->
</SCRIPT>
<!--END PRINT-->
<script language="Javascript" src="js/mousetable.js"></script>
<script language="Javascript" src="js/b4dom.js"></script>

<script language="javascript">
function abrete(me) {
	parent.window.open(me);
}
</script>

<!--FOLLOWING EXTERNAL SCRIPT IS USED FOR BROWSER TESTING AND IS INTEGRAL PART OF POW-->
<script language="JavaScript" src="js/dynlayer.js"></script>
<!--END-->
<script language="JavaScript" src="js/mousetable.js"></script>

<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="keywords" content="coastlinemicro.com, www.coastlinemicro.com, coastline, micro, irvine, ca, california, about, company, location, businsess, competition, competitors, solutions, irvine, california, technology, ceo, own, partner, fast, reliable, heritage, sophisticated, computer, system, build, custom, sample, guarantee, search, product">
<meta name="description" content="Coastline Micro Inc. is in business to develop hardware solutions that make sense for the small to corporate sized business arena. We have been in business for over a decade and have the knowledge and expertise necessary to be competitive in the market. Our every product carries a 100% Product Satisfaction Guarantee. We are located in Irvine, California at 60 N. Technology Drive. For more information about our company and its what it is in business to do please follow the link above. Our company's Heritage dates back to 1989.">
$menu1
$cualCSS
<style type="text/css">
body { scrollbar-face-color:#$light1; scrollbar-highlight-color:#$light1; scrollbar-shadow-color:#$dark1; scrollbar-3dlight-color: #$dark1; scrollbar-arrow-color:#$dark1; scrollbar-track-color:#$light1; scrollbar-darkshadow-color:#$dark1; }
</style>
</head>
<body bgcolor="#ffffff" text="#8f8fab" leftmargin="0" topmargin="0" marginwidth="0" scroll="yes" marginheight="0" onLoad="javascript:$powerPunch$loadscript">

<!-- Copyright NetMedia Solutions and Coasltine Micro, Inc.-->
$menu2

<!-- Dynamic Moving Layers -->
$pow

<!-- Start header table -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/newones/$cualIllusBG" height="100">
  <tr> 
    <td width="30%"><img src="images/newones/$cualIllus" width="250" height="100" border="0"></td>
    <td align="right" valign="middle" width="70%"><font size="1" color="#ffffff" face="verdana,arial,helvetica">$date&nbsp;&nbsp;<font size="3">&nbsp;</font></font>
	<center><img src="images/newones/title_$imagetitle.jpg" width="350" height="80" align="bottom"></center></td>
  </tr>
</table>
<!-- End header table -->

<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr valign="top"> 
    <td width="190" valign="top" align="left">
		<table width="190" border="0" cellpadding="0" cellspacing="0">
			<tr>
				<td width="190" height="150" align="left">$cualMainHeader</td>
			</tr>
			<tr>
				<td width="190" align="left"><img src="images/spacer.gif" width="190" height="20" border="0">$powbutton $legal</td>
			</tr>
		</table>
	</td>
    <td width="100%">$whichdrop</td>
  </tr>
</table>

<div id="overDiv"></div>

</BODY>

</HTML>

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