#!/usr/bin/perl5 -s

###########################################################################################################
# Company: ©2001 NetMedia Solutions                                                                             #
# Date: Saturday, September 21, 2001                                                                      #
# Location: Los Angeles County, California, United States of America                                      #
# Made By: Luis Rodriguez (drlouie)                                                                       #
# Email: Drlouie@NetMediaSol.com                                                                          #
#                                                                                                         #
# CoastlineMicro.com's homepage template. Dynamically driven by DHTML, HTML, Perl and MySql               #
###########################################################################################################

print "Content-type: text/html\n\n";

## Snif cookie, if present test for logged in status
require ("cookiesnif.nsp");

$browser = "$ENV{'HTTP_USER_AGENT'}";
$IP = "$ENV{'REMOTE_ADDR'}";

if ($Cookies{'GID'}) {
$leTR = "<tr><td width=\"45%\" align=\"right\"><font class=\"btext_red\">$Cookies{'FiNo'}, You're Logged In!&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<a href=\"https://www.coastlinemicro.com/framer.cgi?subject=logoff&title=in\">Log Off</a>&nbsp;&nbsp;&nbsp;</font></td></tr>";
$leLogger = "<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\">
  <tr>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td width=\"45%\" align=\"right\">
      <table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" style=\"background-image: url(images/nuevohome/logback.jpg); background-repeat: no-repeat; background-position: right top\" height=\"30\">
        <tr>
            <td align=\"right\" valign=\"bottom\" width=\"372\">&nbsp;</td>
        </tr>
      </table>
    </td>
  </tr>
</table>";
}
else {
$leTR = "<tr><td width=\"45%\" align=\"right\"><font class=\"btext_red\"><a href=\"#\">Sign Up Now!</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<a href=\"https://www.coastlinemicro.com/framer.cgi?subject=getpass&title=in\">Password Retrieval</a>&nbsp;&nbsp;&nbsp;</font></td></tr>";
$leLogger = "<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\">
  <tr>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td width=\"45%\" align=\"right\">
      <table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" style=\"background-image: url(images/nuevohome/logback.jpg); background-repeat: no-repeat; background-position: right top\" height=\"30\">
        <tr>
<form action=\"https://www.coastlinemicro.com/login.cgi\" method=\"post\" name=\"login_uno\" onSubmit=\"return checkForm();\">
<input type=\"hidden\" name=\"lasturl\" value=\"starter.cgi\">
            <td align=right valign=\"bottom\" width=\"100%\"><nobr>
<input type=\"text\" name=\"Username\" size=\"13\" class=\"search1\" style=\"height:18;margin-bottom:4px\"><font class=\"btext_red\">&nbsp;&nbsp;</font><input type=\"Password\" name=\"Password\" size=\"13\" class=\"search1\" style=\"height:18;margin-bottom:4px\"><font class=\"btext_red\">&nbsp;&nbsp;</font><input type=\"image\" name=\"submit\" onMouseOver=\"javascript:imageOn2(this,'login','on');\" onMouseOut=\"javascript:imageOff2(this,'login','off');\" src=\"images/dbing/button_login_off.gif\" width=\"75\" height=\"19\" border=\"0\">
              <font class=\"btext_red\">&nbsp;&nbsp;</font></nobr></td>
</form>
        </tr>
      </table>
    </td>
  </tr>
</table>";
}

## Capture saved PRESS RELEASES
$cstuff = "admin/press/releases/releases.dat";
$thestuff = `cat $cstuff`;

@lines = split(/:end\n/, $thestuff);


$count=0;
foreach $line (@lines) { $count++; }

$random = int( rand($count));
## random chosen image from the sharktank/pow/ directory
$thisfile = @lines[$random];

@pairs = split(/&&&/, $thisfile);
foreach $pair (@pairs) {
	local($name, $value) = split(/===/, $pair);
	$name =~ tr/+/ /;
   	$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$value =~ s/<!--(.|\n)*-->//g;
	$Saved{$name} = $value;
}
$PressNum = "$Saved{'file'}";
$PressText = "$Saved{'title'}";

{
print <<EOF
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
<title>Coastline Micro, Inc.</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<style type="text/css">
body { scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</style>
<LINK REL="STYLESHEET" HREF="common_css.html?anchor=EB0000&anchorov=EB0000&weight=bold&weightov=bold&decor=underline&decorov=none" Type="text/css">
<script language="JavaScript" src="js/b4dom.js"></script>
<script language="Javascript">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

function timeFlip() {
	object = new Array;
	object[0] = new Object();
	object[0].src = "images/nuevohome/p4p_graphic.gif";	
	object[0].href = "http://www.intel.com/intelinside/weblinks/english/p4p.htm";
	
// do not edit anything below this line

var j = 0
var p = object.length;
var preBuffer = new Array()
for (i = 0; i < p; i++){
   preBuffer[i] = new Image()
   preBuffer[i].src = object[i]
}
	var whichImage = Math.round(Math.random()*(p-1));

	document.leImagen.src = object[whichImage].src;
	document.leImagenSetter.leHref.value = object[whichImage].href;
	
	setTimeout("timeFlip()", 7500);
}

function runImagenURL() {
	if (document.leImagenSetter.leHref.value.indexOf("framer.cgi") != -1) {
		parent.location.href(document.leImagenSetter.leHref.value);
	}
	else {
		window.open(document.leImagenSetter.leHref.value,'leImagen');
	}
}

</script>
<SCRIPT LANGUAGE="JavaScript">
// QUICK CROSS-BROWSER MOUSE-OVER/OFF FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function imageOff2(daobject,which,thisone) {
	var cual = 	"images/dbing/button_"+which+"_"+thisone+".gif";
	daobject.src = cual;
}
function imageOn2(daobject,which,thisone) {
	var cual = 	"images/dbing/button_"+which+"_"+thisone+".gif";
	daobject.src = cual;
}
</SCRIPT>
<script language="Javascript">
<!--
function checkForm() {
	if ((document.login_uno.Username.value == "") || (document.login_uno.Username.value == "0") || (document.login_uno.Username.value == " ")) {
	alert('Before you can login you must type in your account username.')
	document.login_uno.Username.focus();
	return false;
	}	
	if ((document.login_uno.Password.value == "") || (document.login.Password.value == "0") || (document.login_uno.Password.value == " ")) {
	alert('Before you can login you must type in your account password.')
	document.login_uno.Password.focus();
	return false;
	}	
	else {
	return true;
	}	
}
//-->
</script>
<script language="JavaScript" src="js/menu_config.js"></script>
<script language="Javascript">
function placeClouds() {
	cualBrowser = "$browser";


	object = new Array;
	object[0] = new Object();
	object[0].src = "tiger1";
	object[1] = new Object();
	object[1].src = "reef1";
	object[2] = new Object();
	object[2].src = "thresher1";
	object[3] = new Object();
	object[3].src = "tigerNAS";
	object[4] = new Object();
	object[4].src = "tigerNAS";	
	object[5] = new Object();
	object[5].src = "tigerNAS";	
	
// do not edit anything below this line

	var p = object.length;
	var whichOne = Math.round(Math.random()*(p-1));
	var esteHomie = object[whichOne].src;

	if (document.body.clientWidth && cualBrowser.indexOf("etscape") < 0) {
		var currWidth = document.body.clientWidth;
		var fontSize = '11px';
		var marginLeft = '15px';
		var extraBreaker = '<br><br><br><br><br>';
		if (currWidth <= "800") { 
			// if ('$IP' == '') { alert(currWidth); }		
			fontSize = '9px';
			marginLeft = "0px";

		}
		
		// get left:- placement by subtracting the actual size of document upon loadtime from the size of cloudy.jpg
		var negPlacement = (1320 - currWidth);
		document.getElementById("cloudy").style.width = '1320px';
		document.getElementById("cloudy").style.left = '-'+negPlacement+'px';
		document.getElementById("cloudy").style.visibility = 'visible';
		if (esteHomie == "tiger1") {
			document.getElementById("cloudyTable").innerHTML = '<table width="100%" border="0" cellspacing="0" cellpadding="0"><tr valign="top"><td width="152"><img src="images/spacer.gif" width="152" height="1"></td><td width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0" height="176"><tr><td align="right" valign="top" width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0"><tr><td width="85%" valign="bottom" align="center" height="160"><table width="75%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" style="line-height:16px;"><font class="btext" style="font-size:'+fontSize+'";color:#333366"><nobr><b>Tiger Series™ DP Xeon&#153; Servers</b>  <span style="margin-left:15px;">( <a href="http://www.coastlinemicro.com/framer.cgi?subject=products&title=tiger&loadthis=tiger&PageTitle=Tiger Series DP Xeon Servers" class="btext" style="font-size:9px;color:#333366">Evaluate</a> / <a href="http://www.coastlinemicro.com/framer.cgi?subject=products&title=tiger&loadthis=tiger&PageTitle=Tiger Series DP Xeon Servers" class="btext" style="font-size:9px;color:#333366">Configure</a> / <a href="http://www.coastlinemicro.com/framer.cgi?subject=products&title=tiger&loadthis=tiger&PageTitle=Tiger Series DP Xeon Servers" class="btext" style="font-size:9px;color:#333366">Print</a> )</span></nobr><br>The Tiger Series&#153; Servers are specifically made for small to mid-sized businesses looking to get the most for their money without compromising scalability or performance.<br><br></font></td></tr></table></td><td width="200" valign="middle" height="160">&nbsp;</td></tr></table></td></tr></table></td></tr></table>';
			document.getElementById("cloudy").innerHTML = '<table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td width="100%"><object CLASSID="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" WIDTH="1320" HEIGHT="168" CODEBASE="download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=4,0,2,0"><param NAME="wmode" Value="Transparent"><PARAM NAME="MOVIE" VALUE="images/homepage_tiger1.swf"><param NAME="PLAY" VALUE="true"><param NAME="LOOP" VALUE="false"><param NAME="QUALITY" VALUE="high"><param NAME="MENU" VALUE="false"><embed SRC="images/homepage_tiger1.swf" style="z-index:-1;" WIDTH="1320" HEIGHT="168" PLAY="true" QUALITY="high" MENU="true" TYPE="application/x-shockwave-flash" PLUGINSPAGE="www.macromedia.com/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash"></embed></object></td></tr></table>';
		}
		else if (esteHomie == "tigerNAS") {
			document.getElementById("cloudyTable").innerHTML = '<table width="100%" border="0" cellspacing="0" cellpadding="0"><tr valign="top"><td width="152"><img src="images/spacer.gif" width="152" height="1"></td><td width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0" height="176"><tr><td align="right" valign="top" width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0"><tr><td width="85%" valign="bottom" align="center" height="160"><table width="75%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" style="line-height:16px;"><font class="btext" style="font-size:'+fontSize+';color:#333366"><nobr><b>Tiger Series™ Network Attached Storage</b> <span style="margin-left:15px;">( <a href="http://www.coastlinemicro.com/nas/" class="btext" style="font-size:9px;color:#333366">Evaluate</a> / <a href="http://www.coastlinemicro.com/nas/" class="btext" style="font-size:9px;color:#333366">Configure</a> / <a href="http://www.coastlinemicro.com/nas/" class="btext" style="font-size:9px;color:#333366">Print</a> )</span></nobr><br>The Coastline Micro Tiger Series&#153; NAS appliances are perfect for archiving old files, sharing new files, backing up clients, servers and consolidating data storage quickly and efficiently.<br><br>'+extraBreaker+'</font></td></tr></table></td><td width="200" valign="middle" height="160">&nbsp;</td></tr></table></td></tr></table></td></tr></table>';
			document.getElementById("cloudy").innerHTML = '<table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td width="100%"><object CLASSID="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" WIDTH="1320" HEIGHT="168" CODEBASE="download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=4,0,2,0"><param NAME="wmode" Value="Transparent"><PARAM NAME="MOVIE" VALUE="images/homepage_tigerNAS.swf"><param NAME="PLAY" VALUE="true"><param NAME="LOOP" VALUE="false"><param NAME="QUALITY" VALUE="high"><param NAME="MENU" VALUE="false"><embed SRC="images/homepage_tigerNAS.swf" style="z-index:-1;" WIDTH="1320" HEIGHT="168" PLAY="true" QUALITY="high" MENU="true" TYPE="application/x-shockwave-flash" PLUGINSPAGE="www.macromedia.com/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash"></embed></object></td></tr></table>';
		}
		else if (esteHomie == "reef1") {
			document.getElementById("cloudyTable").innerHTML = '<table width="100%" border="0" cellspacing="0" cellpadding="0"><tr valign="top"><td width="152"><img src="images/spacer.gif" width="152" height="1"></td><td width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0" height="176"><tr><td align="right" valign="top" width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0"><tr><td width="85%" valign="bottom" align="center" height="160"><table width="75%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" style="line-height:16px;"><font class="btext" style="font-size:'+fontSize+';color:#333366"><nobr><b>Reef Series™ Notebooks</b>  <span style="margin-left:15px;">( <a href="http://www.coastlinemicro.com/framer.cgi?subject=products&title=reef&loadthis=reef&PageTitle=Reef Series Notebooks" class="btext" style="font-size:9px;color:#333366">Evaluate</a> / <a href="http://www.coastlinemicro.com/framer.cgi?subject=products&title=reef&loadthis=reef&PageTitle=Reef Series Notebooks" class="btext" style="font-size:9px;color:#333366">Configure</a> / <a href="http://www.coastlinemicro.com/framer.cgi?subject=products&title=reef&loadthis=reef&PageTitle=Reef Series Notebooks" class="btext" style="font-size:9px;color:#333366">Print</a> )</span></nobr><br>The reef shark is one of the most visually intruging sharks in the world, as for the Reef Series&#153; Notebook, it stands it\\'s own in the world of mobile computing systems.<br><br></font></td></tr></table></td><td width="200" valign="middle" height="160">&nbsp;</td></tr></table></td></tr></table></td></tr></table>';
			document.getElementById("cloudy").innerHTML = '<table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td width="100%"><object CLASSID="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" WIDTH="1320" HEIGHT="168" CODEBASE="download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=4,0,2,0"><param NAME="wmode" Value="Transparent"><PARAM NAME="MOVIE" VALUE="images/homepage_reef1.swf"><param NAME="PLAY" VALUE="true"><param NAME="LOOP" VALUE="false"><param NAME="QUALITY" VALUE="high"><param NAME="MENU" VALUE="false"><embed SRC="images/homepage_reef1.swf" style="z-index:-1;" WIDTH="1320" HEIGHT="168" PLAY="true" QUALITY="high" MENU="true" TYPE="application/x-shockwave-flash" PLUGINSPAGE="www.macromedia.com/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash"></embed></object></td></tr></table>';
		}
		// thresher 1
		else {
			document.getElementById("cloudyTable").innerHTML = '<table width="100%" border="0" cellspacing="0" cellpadding="0"><tr valign="top"><td width="152"><img src="images/spacer.gif" width="152" height="1"></td><td width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0" height="176"><tr><td align="right" valign="top" width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0"><tr><td width="85%" valign="bottom" align="center" height="160"><table width="75%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" style="line-height:16px;"><font class="btext" style="font-size:'+fontSize+';color:#333366"><nobr><b>Thresher Series™ Desktop PCs</b>  <span style="margin-left:15px;">( <a href="http://www.coastlinemicro.com/framer.cgi?subject=products&title=thresher&loadthis=thresher&PageTitle=Thresher Series Desktop PCs" class="btext" style="font-size:9px;color:#333366">Evaluate</a> / <a href="http://www.coastlinemicro.com/framer.cgi?subject=products&title=thresher&loadthis=thresher&PageTitle=Thresher Series Desktop PCs" class="btext" style="font-size:9px;color:#333366">Configure</a> / <a href="http://www.coastlinemicro.com/framer.cgi?subject=products&title=thresher&loadthis=thresher&PageTitle=Thresher Series Desktop PCs" class="btext" style="font-size:9px;color:#333366">Print</a> )</span></nobr><br>The fastest and most reliable value priced Desktop PC in the market today. Fully configurable and fully supported to give you the best possible performance at the lowest possible price.<br><br></font></td></tr></table></td><td width="200" valign="middle" height="160">&nbsp;</td></tr></table></td></tr></table></td></tr></table>';
			document.getElementById("cloudy").innerHTML = '<table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td width="100%"><object CLASSID="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" WIDTH="1320" HEIGHT="168" CODEBASE="download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=4,0,2,0"><param NAME="wmode" Value="Transparent"><PARAM NAME="MOVIE" VALUE="images/homepage_thresher1.swf"><param NAME="PLAY" VALUE="true"><param NAME="LOOP" VALUE="false"><param NAME="QUALITY" VALUE="high"><param NAME="MENU" VALUE="false"><embed SRC="images/homepage_thresher1.swf" style="z-index:-1;" WIDTH="1320" HEIGHT="168" PLAY="true" QUALITY="high" MENU="true" TYPE="application/x-shockwave-flash" PLUGINSPAGE="www.macromedia.com/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash"></embed></object></td></tr></table>';
		}
	}
	else {
		document.getElementById("cloudyTable").innerHTML = '<table height="168" bgcolor="#66698A" style="background-image: url(images/nuevohome/lethresher.jpg); background-repeat: no-repeat; background-position: right top;" width="100%" align="center" cellpadding="0" cellspacing="0"><tr><td width="100%">&nbsp;</td></tr></table>';
		document.getElementById("careers").style.top = '-150px';
	}
}

</script>
</head>
<BODY bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="placeClouds();wrapIt();makeSearch();timeFlip();" ONRESIZE="placeClouds();" onFocus="wrapIt();">
<!-- Copyright NetMedia Solutions and Coastline Micro, Inc.-->
<script language="Javascript" src="js/menu_constructor.js"></script>
<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td rowspan="2" width="15%" align="center" valign="middle"><img src="images/dbing/top_cm_logo.jpg" width="116" height="37"></td>
    <td rowspan="2" align="center" valign="middle" width="40%"><font face="verdana,arial,helvetica" size="1" color="#333366">&nbsp;</font></td>
    <td width="45%" align="right" height="55"><img src="images/dbing/god_bless_america.gif" width="118" height="35">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
  </tr>
$leTR
</table>
<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td align="right" height="3"><img src="images/spacer.gif" height="3" width="3" border="0"></td>
  </tr>
</table>

$leLogger

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td align="right" height="1"><img src="images/spacer.gif" height="1" width="1" border="0"></td>
  </tr>
</table>

<div id="cloudyTable">&nbsp;</div>
<div id="cloudy" bgcolor="#A6B0CB" style="position:absolute;width:1px;height:168px;left:-1000px;top:101px;z-index:-5;visibility:hidden;">&nbsp;</div>

<div style="position:absolute;top:480px;left:18%;width:339px;height:76px;"><a href="http://www.coastlinemicro.com/Microsoft_Windows_2003.html" target="_parent"><img src="images/ms2003serverHome.jpg" width="339" height="76" border="0"></a></div>
<table width="100%" border="0" cellspacing="0" cellpadding="0" height="30">
  <tr valign="top"> 
    <td width="50%"><img src="images/nuevohome/serious_servers.jpg" width="325" height="22" vspace="4"></td>
    <td width="50%" valign="top" align="right"><img src="images/nuevohome/serious_service.jpg" width="325" height="22" vspace="4"></td>
  </tr>
</table>
<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr bgcolor="#A6B0CA"> 
    <td>&nbsp;</td>
    <td bgcolor="#E6E9F0" width="1"><img src="images/spacer.gif" width="1" height="10" border="0"></td>
    <td width="99"><font class="newhome1">&nbsp;Search</font></td>
    <td bgcolor="#E6E9F0" width="1"><img src="images/spacer.gif" width="1" height="10" border="0"></td>
    <td width="118"><font class="newhome1">&nbsp;Offerings</font></td>
    <td bgcolor="#E6E9F0" width="1"><img src="images/spacer.gif" width="1" height="10" border="0"></td>
    <td width="141"><font class="newhome1">&nbsp;Profile</font></td>
  </tr>
</table>
<td width="100%">
<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
    <tr> 
      <td align="right" valign="top" width="100%"> 
        <table border="0" cellspacing="0" cellpadding="0" width="100%">
          <tr> 
            <td valign="top" width="100%"> 
<table width="100%" align="center" border="0" cellpadding="0" cellspacing="0">
<tr>
<td width="100%" align="center" valign="top"><br><a href="#" onClick="javascript:runImagenURL();"><img src="images/nuevohome/hspacer.gif" width="207" height="98" border="0" name="leImagen" style="margin-top:10px;"></a><form name="leImagenSetter"><input type="hidden" name="leHref" value=""></form></td>
<td width="300" align="right">
              <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <script language="JavaScript">
<!--
//Check Search field for completion
function checkSearch1() {
	// SPECIAL FORM HANDLING
		if (document.search1.ProductType.value == "NULL" || document.search1.ProductType.value == " " || document.search1.ProductType.value == "") {
		alert ('Inventory search has detected that you have selected an invalid Product Type list item, please select a different one.');
		document.search1.ProductType.focus();
		return false;
		}	
		if (document.search1.PKeywords.value == " " || document.search1.PKeywords.value == "") {
			alert ('Inventory search cannot continue with the Search Terms field blank.');
			document.search1.PKeywords.focus();
			return false;	
		}
		else { return true; }
}

function checkSearch2() {
	if (document.search2.keywords.value == " " || document.search2.keywords.value == "") {
		alert ('Website search cannot continue with the Search Terms field blank.');
		document.search2.keywords.focus();
		return false; 
	}
	else { return true; }
}

	var da = (document.all) ? 1 : 0;
	var ns4 = ((navigator.userAgent.indexOf("Mozilla") != -1) && (navigator.userAgent.indexOf("4.") != -1)  && (navigator.userAgent.indexOf("MSIE") == -1));
	var ns6 = ((navigator.userAgent.indexOf("Netscape") != -1) && (navigator.userAgent.indexOf("6.") != -1));
	
function makeSearch() {
	document.getElementById("PKeywords2").style.visibility = "hidden";
	document.getElementById("SButton2").style.visibility = "hidden";
	var imagen = 	"images/nuevohome/leradiobut_on.gif";
	document.images.Inventory.src = imagen;
}

function wrapIt() {
	if(bw.ns4 || bw.ns6) {
		document.getElementById("PKeywords2").style.top = "-22";
		document.getElementById("SButton2").style.top = "-18";
	}
	else {
		document.getElementById("PKeywords2").style.top = "-42";
		document.getElementById("SButton2").style.top = "-38";	
	}
}

function toggleSearch(cual) {
	if (cual == "Inventory") {
		// SHOW INVENTORY
		document.getElementById("ProductType").style.visibility = "visible";
		document.getElementById("PTypeTXT").style.visibility = "visible";
		document.getElementById("PKeywords").style.visibility = "visible";
		document.getElementById("SButton").style.visibility = "visible";
		var imagen = 	"images/nuevohome/leradiobut_on.gif";
		document.images.Inventory.src = imagen;
		var imagen2 = 	"images/nuevohome/hspacer.gif";
		document.images.SSpacer.src = imagen2;
		document.images.SSpacer2.src = imagen2;
		// HIDE WEBSITE
		document.getElementById("PKeywords2").style.visibility = "hidden";
		document.getElementById("SButton2").style.visibility = "hidden";
		var imagen = 	"images/nuevohome/leradiobut_off.gif";
		document.images.Website.src = imagen;
	}
	if (cual == "Website") {
		// SHOW WEBSITE
		document.getElementById("PKeywords2").style.visibility = "visible";
		document.getElementById("SButton2").style.visibility = "visible";
		var imagen = 	"images/nuevohome/leradiobut_on.gif";
		document.images.Website.src = imagen;
		// HIDE INVENTORY
		document.getElementById("ProductType").style.visibility = "hidden";
		document.getElementById("PTypeTXT").style.visibility = "hidden";
		document.getElementById("PKeywords").style.visibility = "hidden";
		document.getElementById("SButton").style.visibility = "hidden";
		var imagen = 	"images/nuevohome/leradiobut_off.gif";
		document.images.Inventory.src = imagen;
		var imagen2 = 	"images/spacer.gif";
		document.images.SSpacer.src = imagen2;
		document.images.SSpacer2.src = imagen2;
	}
}
//-->
</script>
                <form name="search1" method="GET" action="framer.cgi" onSubmit="return checkSearch1();">
                  <tr> 
                    <td height="3"><img src="images/spacer.gif" height="3" width="10" border="0"></td>
                  </tr>
                  <tr> 
                    <td height="18" valign="middle" align="right"><a href="#" onClick="toggleSearch('Inventory');"><img src="images/nuevohome/leradiobut_off.gif" width="16" height="18" name="Inventory" border="0"></a><img src="images/spacer.gif" height="10" width="5" border="0"></td>
                  </tr>
                  <tr> 
                    <td height="1" valign="middle" align="right"><img src="images/nuevohome/hspacer.gif" height="1" width="20" border="0"></td>
                  </tr>
                  <tr> 
                    <td height="18" valign="middle" align="right"><a href="#" onClick="toggleSearch('Website');"><img src="images/nuevohome/leradiobut_off.gif" width="16" height="18" name="Website" border="0"></a><img src="images/spacer.gif" height="10" width="5" border="0"></td>
                  </tr>
                  <tr> 
                    <td height="20" align="right"><img src="images/spacer.gif" height="1" width="20" border="0"></td>
                  </tr>
                  <tr> 
                    <td height="25" valign="middle" align="right"><nobr> 
                      <select name="ProductType" size="1" class="search1" id="ProductType">
                        <option value="All" selected>All Product Types</option>
                        <option value="NULL"></option>
                        <option value="NULL">---- Pre-Configured ---- </option>
                        <option value="Desktop">Desktop PCs</option>
                        <option value="Notebook">Notebook Computers</option>
                        <option value="Server">Net Servers</option>
                        <option value="NULL"></option>
                        <option value="NULL">---- Miscellaneous ---- </option>
                        <option value="Audio">Audio Equipment</option>
                        <option value="CDROM">CD-ROM Drives</option>
                        <option value="CDRW">CD-RW Drives</option>
                        <option value="DigitalCam">Digital Cameras</option>
                        <option value="DVDROM">DVD-ROM Drives</option>
                        <option value="Floppy">Floppy Drives</option>
                        <option value="HardDrive">Hard Drives</option>
                        <option value="InternetCam">Internet Cameras</option>
                        <option value="Joystick">Joysticks</option>
                        <option value="Keyboard">Keyboards</option>
                        <option value="Memory">Memory</option>
                        <option value="Modem">Modems</option>
                        <option value="Monitor">Monitors</option>
                        <option value="Networking">Networking</option>
                        <option value="NIC">Network Cards</option>
                        <option value="NoteExtra">Notebooks Extras</option>
                        <option value="Pointer">Pointer Devices</option>
                        <option value="UPS">Power Protection</option>
                        <option value="Printer">Printers</option>
                        <option value="Processor">Processors</option>
                        <option value="Scanner">Scanners</option>
                        <option value="Software">Software</option>
                        <option value="Speaker">Speakers</option>
                        <option value="Storage">Storage Devices</option>
                        <option value="SystemBoard">System Boards</option>
                        <option value="SystemChassis">System Chassis</option>
                        <option value="VideoCard">Video Cards</option>
                        <option value="WirelessNet">Wireless Networking</option>
                        <option value="ZipDrive">Zip Drives</option>
                        <option value="NULL"></option>
                        <option value="NULL">---- All Others ---- </option>
                        <option value="Peripheral">Peripherals (Catchall)</option>
                      </select>
                      <img src="images/spacer.gif" height="10" width="5" border="0"></nobr></td>
                  </tr>
                  <tr> 
                    <td height="1" valign="middle" align="right"><img src="images/nuevohome/hspacer.gif" height="1" width="125" border="0" name="SSpacer"></td>
                  </tr>
                  <tr> 
                    <td height="25" valign="middle" align="right"><nobr> 
                      <!--Search1-->
                      <input type="text" name="PKeywords" id="PKeywords" size="13" class="search1" style="position:relative;top:1px;left:-9px;">
                      <input type="image" name="submit2" id="SButton" onMouseOver="javascript:imageOn2(this,'search','on');" onMouseOut="javascript:imageOff2(this,'search','off');" src="images/dbing/button_search_off.gif" border="0" width="65" height="19" style="position:relative;top:5px;left:-9px;">
                </form>
                <!--Search2-->
                <form name="search2" method="GET" action="framer.cgi" onSubmit="return checkSearch2();">
                  <input type="text" name="keywords" id="PKeywords2" size="13" class="search1" style="position:relative;top:-42px;left:-9px;">
                  <input type="image" name="submit2" id="SButton2" onMouseOver="javascript:imageOn2(this,'search','on');" onMouseOut="javascript:imageOff2(this,'search','off');" src="images/dbing/button_search_off.gif" border="0" width="65" height="19" style="position:relative;top:-38px;left:-9px;">
                </form>
                <img src="images/spacer.gif" height="10" width="5" border="0"></nobr>
				<div id="careers" style="position:relative;top:-190px;left:-70px;" class="btext"><i><u><a href="http://www.coastlinemicro.com/framer.cgi?subject=aboutus&title=careers&PageTitle=Careers%20at%20Coastline%20Micro" class="btext" style="font-size:14px;"><nobr>Careers at Coastline Micro</nobr></a></u></i></div>
              </table>

</td>
</tr>
</table>

            </td>
          </tr>
        </table>
      </td>
      <td bgcolor="#E6E9F0" width="1"><img src="images/spacer.gif" width="1" height="10" border="0"></td>
      <td width="99" valign="top">
        <table width="99" height="94" border="0" cellspacing="0" cellpadding="0" style="background-image: url(images/nuevohome/hback1.jpg); background-repeat: no-repeat; background-position: right top">
          <tr> 
            <td valign="top"> 
              <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr> 
                  <td height="3"><img src="images/spacer.gif" height="3" width="10" border="0"></td>
                </tr>
                <tr> 
                  <td height="18" valign="middle"><font class="btext">&nbsp;&nbsp;Inventory</font></td>
                </tr>
                <tr> 
                  <td height="1" align="left"><img src="images/nuevohome/hspacer.gif" height="1" width="80" border="0"></td>
                </tr>
                <tr> 
                  <td height="18" valign="middle"><font class="btext">&nbsp;&nbsp;Website</font></td>
                </tr>
                <tr> 
                  <td height="20"><img src="images/spacer.gif" height="1" width="10" border="0"></td>
                </tr>
                <tr> 
                  <td height="25" valign="middle"><font class="btext" id="PTypeTXT">&nbsp;&nbsp;Product 
                    Type</font></td>
                </tr>
                <tr> 
                  <td height="1" align="left"><img src="images/nuevohome/hspacer.gif" height="1" width="80" border="0" name="SSpacer2"></td>
                </tr>
                <tr> 
                  <td height="25" valign="middle"><font class="btext">&nbsp;&nbsp;Search 
                    Terms</font></td>
                </tr>
              </table>
            </td>
          </tr>
        </table>
      </td>
      <td bgcolor="#E6E9F0" width="1"><img src="images/spacer.gif" width="1" height="10" border="0"></td>
      <td width="118" valign="top">
        <table width="118" height="113" border="0" cellspacing="0" cellpadding="0" style="background-image: url(images/nuevohome/hback2.jpg); background-repeat: no-repeat; background-position: right top">
          <tr> 
            <td valign="top"> 
              <table border="0" cellspacing="0" cellpadding="0">
                <tr> 
                  <td height="3" colspan="2"><img src="images/spacer.gif" height="3" width="10" border="0"></td>
                </tr>
                <tr> 
                  <td height="18" valign="middle" colspan="2"><font class="btext">&nbsp;&nbsp;<b>Custom Products</b></font></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15"><font class="btext">&nbsp;</font></td>
                  <td height="12" valign="middle" width="133"><font class="btext"><a style="color:333366;font-weight:normal" href="http://www.coastlinemicro.com/framer.cgi?subject=products&title=thresher&loadthis=thresher&PageTitle=Thresher Series Desktop PCs">Desktop PCs</a></font></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15"><font class="btext">&nbsp;</font></td>
                  <td height="12" valign="middle" width="133"><font class="btext"><a style="color:333366;font-weight:normal" href="http://www.coastlinemicro.com/framer.cgi?subject=products&title=mako&loadthis=mako&PageTitle=Mako Series Workstations">Workstations</a></font></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15"><font class="btext">&nbsp;</font></td>
                  <td height="12" valign="middle" width="133"><font class="btext"><a style="color:333366;font-weight:normal" href="http://www.coastlinemicro.com/framer.cgi?subject=products&title=reef&loadthis=reef&PageTitle=Reef Series Notebooks">Notebooks</a></font></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15"><font class="btext">&nbsp;</font></td>
                  <td height="12" valign="middle" width="133"><font class="btext"><a style="color:333366;font-weight:normal" href="http://www.coastlinemicro.com/framer.cgi?subject=products&title=tiger&loadthis=tiger&PageTitle=Tiger Series DP Xeon Servers">DP Xeon&#153; Servers</a></font></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15"><font class="btext">&nbsp;</font></td>
                  <td height="12" valign="middle" width="133"><font class="btext"><a style="color:333366;font-weight:normal" href="http://www.coastlinemicro.com/framer.cgi?subject=products&title=gw&loadthis=gw&PageTitle=Great White Series MP Xeon Servers">MP Xeon&#153; Servers</a></font></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15"><font class="btext">&nbsp;</font></td>
                  <td height="12" valign="middle" width="133"><font class="btext"><a style="color:333366;font-weight:normal" href="http://www.coastlinemicro.com/framer.cgi?subject=services&title=vpn3105&PageTitle=3105 VPN Gateway">VPN/Firewalls</a></font></td>
                </tr>
                <tr> 
                  <td height="5" valign="middle" colspan="2"><img src="images/spacer.gif" width="1" height="5" border="0"></td>
                </tr>
                <tr> 
                  <td height="18" valign="middle" colspan="2"><font class="btext">&nbsp;&nbsp;<b>Special Offers</b></font></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15"><font class="btext">&nbsp;</font></td>
                  <td height="12" valign="middle" width="133"><font class="btext"><a style="color:333366;font-weight:normal" href="http://www.coastlinemicro.com/msp/">Intel&reg; Model School Program</a></font></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15"><font class="btext">&nbsp;</font></td>
                  <td height="12" valign="middle" width="133"><font class="btext"><a style="color:333366;font-weight:normal" href="http://www.coastlinemicro.com/nmusd.html">NMUSD Program</a></font></td>
                </tr>
              </table>
            </td>
          </tr>
        </table>
      </td>
      <td bgcolor="#E6E9F0" width="1"><img src="images/spacer.gif" width="1" height="10" border="0"></td>
      <td width="141" valign="top">
        <table width="141" height="160" border="0" cellspacing="0" cellpadding="0" style="background-image: url(images/nuevohome/hback3.jpg); background-repeat: no-repeat; background-position: right top">
          <tr> 
            <td valign="top"> 
              <table border="0" cellspacing="0" cellpadding="0">
                <tr> 
                  <td height="3" colspan="2"><img src="images/spacer.gif" height="3" width="10" border="0"></td>
                </tr>

                 <tr> 
                  <td height="18" valign="middle" colspan="2"><font class="btext">&nbsp;&nbsp;<b>Press Release</b></font></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15"><font class="btext">&nbsp;</font></td>
                  <td height="12" valign="middle" width="136"><font class="btext">$PressText - <a style="color:#EB0000;font-weight:normal" href="framer.cgi?subject=press&title=in&viewRel=$PressNum&PageTitle=Press Releases"><b>More Info</b></a></font></td>
                </tr>

                <tr> 
                  <td height="5" valign="middle" colspan="2"><img src="images/spacer.gif" width="1" height="5" border="0"></td>
                </tr>
				
                <tr> 
                  <td height="18" valign="middle" colspan="2"><font class="btext">&nbsp;&nbsp;<b>Contact Info</b></font></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15"><font class="btext">&nbsp;</font></td>
                  <td height="12" valign="middle" width="136"><font class="btext">Coastline Micro, Inc.<br>60 Technology Drive<br>Irvine, CA 92618</font></td>
                </tr>
                <tr> 
                  <td height="5" valign="middle" colspan="2"><img src="images/spacer.gif" width="1" height="5" border="0"></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15"><font class="btext">&nbsp;</font></td>
                  <td height="12" valign="middle" width="136"><font class="btext">Toll 
                    Free<br>
                    (800) 729-6809</font></td>
                </tr>
                <tr> 
                  <td height="5" valign="middle" colspan="2"><img src="images/spacer.gif" width="1" height="5" border="0"></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15">&nbsp;</td>
                  <td height="12" valign="middle" width="136"><font class="btext">Phone<br>
                    (949) 450-9966</font></td>
                </tr>
                <tr> 
                  <td height="5" valign="middle" colspan="2"><img src="images/spacer.gif" width="1" height="5" border="0"></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15">&nbsp;</td>
                  <td height="12" valign="middle" width="136"><font class="btext">Fax<br>
                    (949) 450-9977</font></td>
                </tr>
              </table>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</td>
    <td width="1"><img src="images/spacer.gif" width="1" height="10" border="0"></td>
    
<td width="118" align="left">&nbsp; </td>
    <td width="1"><img src="images/spacer.gif" width="1" height="10" border="0"></td>
    
<td width="141" align="left">&nbsp; </td>
</table>
</body>
</html>


EOF
}
exit;