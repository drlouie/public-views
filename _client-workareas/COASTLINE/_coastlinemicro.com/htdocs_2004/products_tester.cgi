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

if ($FORM{'title'}) { 
	$title = "$FORM{'title'}";
	$legal = `cat prod_legal.nsf`;
	$LoadIT = "0";
	if (!$FORM{'loadprod'} && !$FORM{'loadsys'} && !$FORM{'reconfigIt'} && !$FORM{'loadcart'} && !$FORM{'cartit'} && !$FORM{'newConfig'} && !$FORM{'stankCSE'}) {
		require ("whichpow2.nsp");			
		$powerPunch = "runPow();";
		$powbutton = "<a href=\"javascript:checkPosition();\" onMouseOver=\"javascript:mouseOvered();\" onMouseOut=\"javascript:mouseOffed();\"><img src=\"images/newmenu/menuhide_off.gif\" name=\"powbar\" border=\"0\" width=\"192\" height=\"22\"></a><br>";
	}
	else {
		$pow = `cat pow_products.nsf`;
		## must have command to run search
		$powerPunch = "runSearch();";
		$powbutton = "";	
	}

	$browser = "$ENV{'HTTP_USER_AGENT'}";
	## Thresher 2 - MSP (Intel's Model School Program) - Gets a different dynamic frame placement
	if ($browser =~ "MSIE" || $browser =~ "Netscape6" || $browser =~ "netscape6" || $browser =~ "netscape5" || $browser =~ "Netscape5") {
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
		if ($title eq "tpp") { $imagetitle = "products"; }
		else { $imagetitle = "$title"; }
	}

	## PAGELOAD ONBODYLOAD function which works only in IE
	if ($browser) {
		$pageload1 = "<script language=\"JavaScript\" src=\"js/pageload1.js\"></script>";
		$extraspacer = "";

	if ($FORM{'MSP'} eq "1") { $MSP = "&MSP=1"; }
	if ($FORM{'NMUSD'} eq "1") { $NMUSD = "&NMUSD=1"; }
	if ($FORM{'TPP'} eq "1") { $NMUSD = "&TPP=1"; }
	
		if ($FORM{'loadthis'}) {
			## IF SYSTEM, LOAD SYSTEM START PAGE
			if ($FORM{'loadthis'} eq "thresher" || $FORM{'loadthis'} eq "thresher2" || $FORM{'loadthis'} eq "tiger" || $FORM{'loadthis'} eq "gw" || $FORM{'loadthis'} eq "reef" || $FORM{'loadthis'} eq "mako" || $FORM{'loadthis'} eq "nmusd" || $FORM{'loadthis'} eq "nmusdCustCom" || $FORM{'loadthis'} eq "tpp") { 
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
			$loadthis = "stank_cse.html";
			$FORM{'CID'} = $FORM{'cartit'};
		}
	}
	else { 
		if ($title = "thresher2") { $extraspacer = "<table width=\"100%\" align=\"center\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" bgcolor=\"#ffffff\"><tr><td height=\"165\">&nbsp;</td></tr></table>"; }
		else { $extraspacer = "<table width=\"100%\" align=\"center\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" bgcolor=\"#ffffff\"><tr><td height=\"105\">&nbsp;</td></tr></table>"; }
	}
	
	if($title eq "tpp") {
		if ($FORM{'loadthis'}) { 
			$whichdrop = `cat sharktank/$title_drop.nsf`;
		}
		else {
			$whichdrop = `cat sharktank/products_drop.nsf`;
			require ($loadthis);
			$THETABLE = $pageDrop;
			$whichdrop =~ s/!!!MYCONTENT!!!/$THETABLE/;
		}
	}
	else {
		$whichdrop = `cat sharktank/$title_drop.nsf`;
		require ($loadthis);
		$THETABLE = $pageDrop;
		$whichdrop =~ s/!!!MYCONTENT!!!/$THETABLE/;
	}
	
	## IF $loadthis has not produced a $pageHeader (ie: STANK_CSE) then parse common page header
	print "Content-type: text/html\n\n";
	
{
print <<EOF

<html>
<head>
<title>Coastline Micro Inc.</title>
<SCRIPT LANGUAGE="JavaScript">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are �2001 NetMedia Solutions //
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
document.getElementById('bground').style.visibility = 'hidden';
}
else {
if (document.layers) {  // Netscape 4
document.hidepage.visibility = 'hidden';
document.bground.visibility = 'hidden';
}
else {  // IE 4
document.all.hidepage.style.visibility = 'hidden';
document.all.bground.style.visibility = 'hidden';
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
<tr height="100%"><td align="center" valign="middle"><br><br><img src="sharktank/images/logo_med.jpg" width="161" height="102" border="0"><font face="verdana,arial,helvetica" size="2" color="#333366"><br>Loading DHTML interactive user interface, please wait...<br><br><br><br><br><font size="1"><b><u>Compatibility</u></b><br><br>Win/Mac MSIE 4/5/6<br>Win/Mac/Linux Netscape 4/6<br><br><i>Best if viewed on Windows 95/98/2000 platform using MSIE 4+</i></font></font></td></tr>
</table>
</div>
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
<script language="JavaScript" src="js/menu_config.js"></script>
<LINK REL="STYLESHEET" HREF="common_css.html" Type="text/css">

<style type="text/css">
$divcont
$divload
$divBground
#divIEText{position:absolute; left:0; top:0}
$divArrows
#divLinks{position:absolute; left:420; top:220}
</style>

</head>
<body bgcolor="#ffffff" text="#8f8fab" leftmargin="0" topmargin="0" marginwidth="0" scroll="yes" marginheight="0" onLoad="javascript:loadScript();$powerPunch$loadscript">

<!-- Copyright NetMedia Solutions and Coasltine Micro, Inc.-->
<script language="Javascript" src="js/menu_constructor.js"></script>

<!-- Start header table -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/newones/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%"><img src="images/newones/illus_sharktank.jpg" width="250" height="100" border="0"></td>
    <td align="right" valign="middle" width="70%"><font size="1" color="#ffffff" face="verdana,arial,helvetica">$date&nbsp;&nbsp;<font size="3">&nbsp;</font></font>
	<center><img src="images/newones/title_$imagetitle.jpg" width="350" height="80" align="bottom"></center></td>
  </tr>
</table>
<!-- End header table -->

<div id="divLinks"></div>

<!-- THIS DIV IS USED BY ALL BROWSERS EXCEPT IE5.5 AND NS6 FOR DYNAMIC CONTENT WINDOW SCROLLING -->
<div id="divArrows">
<a href="#" onmouseover="frame.scroll=true; frame.up(15);" onmouseout="frame.scroll=false"><img src="images/scrollers/arrowup_1off.gif" border="0" width="17" height="7" name="arrowup1"></a><br>
<a href="#" onmouseover="frame.scroll=true; frame.up(8)" onmouseout="frame.scroll=false"><img src="images/scrollers/arrowup_2off.gif" border="0" width="17" height="11" name="arrowup2"></a><br>
<a href="#" onmouseover="frame.scroll=true; frame.up(3)" onmouseout="frame.scroll=false"><img src="images/scrollers/arrowup_3off.gif" border="0" width="17" height="5" name="arrowup3"></a><br>
<br><br><br>
<a href="#" onmouseover="frame.scroll=true; frame.down(3)" onmouseout="frame.scroll=false"><img src="images/scrollers/arrowdn_1off.gif" border="0" width="17" height="5" name="arrowdn1"></a><br>
<a href="#" onmouseover="frame.scroll=true; frame.down(8)" onmouseout="frame.scroll=false"><img src="images/scrollers/arrowdn_2off.gif" border="0" width="17" height="11" name="arrowdn2"></a><br>
<a href="#" onmouseover="frame.scroll=true; frame.down(15)" onmouseout="frame.scroll=false"><img src="images/scrollers/arrowdn_3off.gif" border="0" width="17" height="7" name="arrowdn3"></a><br>
</div>

$pageload1
<!-- Copyright NetMedia Solutions and Coasltine Micro, Inc.-->
<script language="Javascript" src="js/pageload2.js"></script>

<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr valign="top"> 
    <td width="190" valign="top" align="left">
		<table width="190" border="0" cellpadding="0" cellspacing="0">
			<tr>
				<td width="190" height="150" align="left"><img src="images/newmenu/place_holder.gif" width="190" height="10"></td>
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

<!-- Dynamic Moving Layers -->
$pow

</BODY>
<script langauge="JavaScript" src="js/overlib.js"></script>
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