#!/usr/bin/perl5 -s

###########################################################################################################
# Company: �2001 NetMedia Solutions                                                                             #
# Date: Saturday, September 21, 2001                                                                      #
# Location: Los Angeles County, California, United States of America                                      #
# Made By: Luis Rodriguez (drlouie)                                                                       #
# Email: Drlouie@NetMediaSol.com                                                                          #
#                                                                                                         #
# drlouie's homepage template. Dynamically driven by DHTML, HTML, Perl and MySql               #
###########################################################################################################

print "Content-type: text/html\n\n";

## Snif cookie, if present test for logged in status
require ("cookiesnif.nsp");

$browser = "$ENV{'HTTP_USER_AGENT'}";
$IP = "$ENV{'REMOTE_ADDR'}";

if ($Cookies{'GID'}) {
$leTR = "<tr><td width=\"45%\" align=\"right\"><font class=\"btext_red\">$Cookies{'FiNo'}, You're Logged In!&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<a href=\"newframer.cgi?subject=logoff&title=in\">Log Off</a>&nbsp;&nbsp;&nbsp;</font></td></tr>";
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
$leTR = "<tr><td width=\"45%\" align=\"right\"><font class=\"btext_red\"><a href=\"javascript:void(0)\" onClick=\"javascript:alert('Coming Soon, Please check back...');\">Sign Up Now!</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<a href=\"newframer.cgi?subject=getpass&title=in\">Password Retrieval</a>&nbsp;&nbsp;&nbsp;</font></td></tr>";
$leLogger = "<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\">
  <tr>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td width=\"45%\" align=\"right\">
      <table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" style=\"background-image: url(images/nuevohome/logback.jpg); background-repeat: no-repeat; background-position: right top\" height=\"30\">
        <tr>
<form action=\"login.cgi\" method=\"post\" name=\"login_uno\" onSubmit=\"return checkForm();\">
<input type=\"hidden\" name=\"lasturl\" value=\"index.cgi\">
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
<title>Coastline Micro Inc. - Intel Servers</title>
<!--<title>microsoft windows desktop</title>-->
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<META NAME="Keywords" content="Custom Server, Microsoft Windows, Intel Solution Provider, Personal Computer, cm, coastline micro, thresher, mako, great white, reef, vpn, 3105, 3115, 3125, 1080, shiva, security, intel server, intel workstations, intel desktop, motherboards, nec, seagate, hard drives, hd, kingston, memory, networking, network services, cabling, network attached server, nas, san, lan, wan, SC5200, SC5250E, SR2300, Rackmount Chassis, Server Chassis, Redundant Power, Midtower, Minitower, serial ata, ata, scsi, u320, storage server 2003, windows storage server 2003, microsoft windows storage, windows storage server, wpnas">
<META NAME="Description" content="Coastline Micro - Value Added Distributor and manufacturer of high quality servers, network attached storage, desktops, and notebooks.  Review our site for information on servers, nas, computers, vpn's, security, networking, intel, microsoft, ibm, seagate">
<meta NAME="CLASSIFICATION" CONTENT="Business:Computer Harware and Software Business:Internet Services:Computer Network">
<meta name="GENERATOR" content="NetMedia Solutions (Drlouie Version 2)">
<meta name="ProgId" content="NMS.Editor.Document">
<meta name="robots" content="index,follow">
<meta name="rating" content="General">
<meta name="netinsert" content="0.0.1.12.17.1">
<meta http-equiv="Content-Language" content="en-us">
<meta http-equiv="PICS-Label" content='(PICS-1.1 "http://www.icra.org/ratingsv02.cgi" l gen true r (cz 1 lz 1 nz 1 oz 1 vz 1) "http://www.rsac.org/ratingsv01.cgi" l gen true r (n 0 s 0 v 0 l 0) "http://www.classify.org/safesurf/" l gen true r (SS~~000 1))' />
<META HTTP-EQUIV="title" content="E-Com Store">
<meta name="revisit-after" content="8 days">
<meta name="abstract" content="Coastline Micro, Inc. - The CLM Tiger Series Network Attached Storage is the high-performance standard for storage appliances that provide shared data to clients and other servers on a Local Area Network (LAN) or Wide Area Network (WAN). Driven by the fast Intel Pentium 4 or Intel Xeon processor and can run any Server Platform you like such as Microsoft Windows 2000 XP NT.">
<meta name="security" content="Public">
<meta name="source" content="NMS-DRLv2 Website Developer, Hard-Code 7.16.03">
<meta name="format" content="text/html">
<meta name="charset" content="ISO-8859-1">
<meta name="author" content="admin\@rhomberg.com">
<meta name="owner" content="admin\@rhomberg.com">
<meta name="rights" content="Copyright (c) 2001 by Coastline Micro, Inc.">
<style type="text/css">
body { scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
#overDiv {	filter:alpha(opacity=93); position:absolute; top:0px; left:0px; visibility:hidden; z-index:5000; }
.overDiv {	z-index:5000; }
</style>
<LINK REL="STYLESHEET" HREF="common_css.cgi?anchor=EB0000&anchorov=EB0000&weight=bold&weightov=bold&decor=underline&decorov=none" Type="text/css">
<script language="JavaScript" src="js/b4dom.js"></script>
<script language="Javascript">
///////////////////////////////////////////////////////////////////
// This script and its counterparts are �2001 NetMedia Solutions //
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
	if (document.leImagenSetter.leHref.value.indexOf("newframer.cgi") != -1) {
		parent.location.href(document.leImagenSetter.leHref.value);
	}
	else {
		window.open(document.leImagenSetter.leHref.value,'leImagen');
	}
}

</script>
<SCRIPT LANGUAGE="JavaScript">
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
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions
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
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions
function placeClouds() {
	cualBrowser = "$browser";


	object = new Array;
	object[0] = new Object();
	object[0].src = "certance1";
	object[1] = new Object();
	object[1].src = "thesher2";
	object[2] = new Object();
	object[2].src = "reef1";
	object[3] = new Object();
	object[3].src = "tigernas1";
	object[4] = new Object();
	object[4].src = "tiger1";
	object[5] = new Object();
	object[5].src = "vpn";
	object[6] = new Object();
	object[6].src = "tiger2";
	object[7] = new Object();
	object[7].src = "thresher1";
	object[8] = new Object();
	object[8].src = "tigernas2";
	
// do not edit anything below this line

	var p = object.length;
	var whichOne = Math.round(Math.random()*(p-1));
	var esteHomie = object[whichOne].src;

	if (document.body.clientWidth && cualBrowser.indexOf("etscape") < 0) {
		var currWidth = document.body.clientWidth;
		var fontSize = '11px';
		var marginLeft = '15px';
		// only certance
		var extraBreaker = '<br>';
		if (currWidth <= "800") { 
			// if ('$IP' == '') { alert(currWidth); }		
			fontSize = '9px';
			marginLeft = "0px";
			// only certance
			extraBreaker = "";
		}
		
		// get left:- placement by subtracting the actual size of document upon loadtime from the size of cloudy.jpg
		var negPlacement = (1320 - currWidth);
		document.getElementById("cloudy").style.width = '1320px';
		document.getElementById("cloudy").style.left = '-'+negPlacement+'px';
		document.getElementById("cloudy").style.visibility = 'visible';

		
		// SWF
		document.getElementById("cloudy").innerHTML = '<table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td width="100%"><object ID="CLOUDMOVIE" CLASSID="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" WIDTH="1320" HEIGHT="168" CODEBASE="download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=4,0,2,0"><param NAME="wmode" Value="Transparent"><PARAM NAME="MOVIE" VALUE="images/homepage_all.swf"><param NAME="PLAY" VALUE="true"><param NAME="LOOP" VALUE="false"><param NAME="QUALITY" VALUE="high"><param NAME="MENU" VALUE="false"><embed name="CLOUDMOVIE" SRC="images/homepage_all.swf" style="z-index:-1;" WIDTH="1320" HEIGHT="168" PLAY="true" QUALITY="high" MENU="true" TYPE="application/x-shockwave-flash" PLUGINSPAGE="www.macromedia.com/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash"></embed></object></td></tr></table>';
		var leSpecial = '<table width="250" border="0" cellspacing="0" cellpadding="0"><tr valign="top"><td width="26" rowspan="2"><img src="images/prtbleft_certance.png" width="26" height="156" style="filter:alpha(opacity=55);"></td><td width="198" height="5"><img src="images/prtbtop.png" width="198" height="5" style="filter:alpha(opacity=55);"></td><td width="26" rowspan="2"><img src="images/prtbright_certance.png" width="26" height="156" style="filter:alpha(opacity=55);"></td></tr><tr valign="top"><td width="198" align="center" valign="top"><a href="javascript:void(0);"><img src="images/prtbmain_certance1.png" style="filter:alpha(opacity=55);"  width="198" height="137" border="0"></a><img src="images/prtbbutsC_off.png" width="198" height="25" style="filter:alpha(opacity=80);" name="prtbbuts" usemap="#prtbbuts" border="0"><map name="prtbbuts"><area shape="rect" coords="17,4,87,21" href="javascript:void(0)" onClick="javascript:window.open(\\'http://www.certance.com/\\',\\'CERTANCE\\'); togglePRTB(\\'certance1\\');" onMouseOver="javascript:document.images.prtbbuts.src=\\'images/prtbbutsC_on1.png\\';" onMouseOut="javascript:document.images.prtbbuts.src=\\'images/prtbbutsC_off.png\\';"><area shape="rect" coords="112,4,182,21" href="javascript:void(0)" onClick="javascript:window.open(\\'http://www.certance.com/products/CertanceDrives/ddsDatMain.cgi\\',\\'CERTANCE\\'); togglePRTB(\\'mako2\\');" onMouseOver="javascript:document.images.prtbbuts.src=\\'images/prtbbutsC_on2.png\\';" onMouseOut="javascript:document.images.prtbbuts.src=\\'images/prtbbutsC_off.png\\';"></map></td></tr></table>';

		//SWF CALLERS
		var cualProducto="certance1";
		muaMovie = document.CLOUDMOVIE;


		
		if (esteHomie == "tiger1") {
			document.getElementById("cloudyTable").innerHTML = '<table width="100%" border="0" cellspacing="0" cellpadding="0"><tr valign="top"><td width="275" align="center">'
			+ leSpecial
			+'<img src="images/spacer.gif" width="275" height="1">'
			+'</td><td width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0" height="168"><tr><td align="right" valign="top" width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" valign="bottom" align="center" height="160"><table width="85%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" style="line-height:14px;"><font class="btext" style="font-size:'+fontSize+'";color:#333366"><nobr><b>Tiger Series� DP Xeon&#153; Servers</b>  <span style="margin-left:15px;">( <a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=tiger&loadthis=tiger&PageTitle=Tiger Series DP Xeon Servers" class="btext" style="font-size:9px;color:#333366">Evaluate</a> / <a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=tiger&loadthis=tiger&PageTitle=Tiger Series DP Xeon Servers" class="btext" style="font-size:9px;color:#333366">Configure</a> / <a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=tiger&loadthis=tiger&PageTitle=Tiger Series DP Xeon Servers" class="btext" style="font-size:9px;color:#333366">Print</a> )</span></nobr><br>The Tiger Series&#153; Servers are specifically made for small to mid-sized businesses looking to get the most for their money without compromising scalability or performance.<br><br></font></td></tr></table></td><td width="175" valign="middle" height="160"><img src="images/spacer.gif" width="175" height="1"></td></tr></table></td></tr></table></td></tr></table>';
			// RUN THE MOVIE WITH PROPER IMAGERY
			muaMovie.Rewind();
			muaMovie.SetVariable("cualProducto", "tiger1");
			muaMovie.Play();
		}
		else if (esteHomie == "tiger2") {
			document.getElementById("cloudyTable").innerHTML = '<table width="100%" border="0" cellspacing="0" cellpadding="0"><tr valign="top"><td width="275" align="center">'
			+ leSpecial
			+'<img src="images/spacer.gif" width="275" height="1">'
			+'</td><td width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0" height="168"><tr><td align="right" valign="top" width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" valign="bottom" align="center" height="160"><table width="85%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" style="line-height:14px;"><font class="btext" style="font-size:'+fontSize+'";color:#333366"><nobr><b>Tiger Series� DP Xeon&#153; Servers</b>  <span style="margin-left:15px;">( <a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=tiger&loadthis=tiger&PageTitle=Tiger Series DP Xeon Servers" class="btext" style="font-size:9px;color:#333366">Evaluate</a> / <a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=tiger&loadthis=tiger&PageTitle=Tiger Series DP Xeon Servers" class="btext" style="font-size:9px;color:#333366">Configure</a> / <a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=tiger&loadthis=tiger&PageTitle=Tiger Series DP Xeon Servers" class="btext" style="font-size:9px;color:#333366">Print</a> )</span></nobr><br>The Tiger Series&#153; Servers are specifically made for small to mid-sized businesses looking to get the most for their money without compromising scalability or performance.<br><br></font></td></tr></table></td><td width="175" valign="middle" height="160"><img src="images/spacer.gif" width="175" height="1"></td></tr></table></td></tr></table></td></tr></table>';
			muaMovie.Rewind();
			muaMovie.SetVariable("cualProducto", "tiger2");
			muaMovie.Play();
		}
		else if (esteHomie == "tigernas1") {
			document.getElementById("cloudyTable").innerHTML = '<table width="100%" border="0" cellspacing="0" cellpadding="0"><tr valign="top"><td width="275" align="center">'
			+ leSpecial
			+'<img src="images/spacer.gif" width="275" height="1">'
			+'</td><td width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0" height="168"><tr><td align="right" valign="top" width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" valign="bottom" align="center" height="160"><table width="85%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" style="line-height:14px;"><font class="btext" style="font-size:'+fontSize+';color:#333366"><nobr><b>Tiger Series� Network Attached Storage</b> <span style="margin-left:15px;">( <a href="newframer.cgi?subject=coastlinemicro_services&title=tigerNAS&PageTitle=Tiger%20Series%20NAS%20Solutions" class="btext" style="font-size:9px;color:#333366">Evaluate</a> / <a href="newframer.cgi?subject=coastlinemicro_services&title=tigerNAS&PageTitle=Tiger%20Series%20NAS%20Solutions" class="btext" style="font-size:9px;color:#333366">Configure</a> / <a href="newframer.cgi?subject=coastlinemicro_services&title=tigerNAS&PageTitle=Tiger%20Series%20NAS%20Solutions" class="btext" style="font-size:9px;color:#333366">Print</a> )</span></nobr><br>The Coastline Micro Tiger Series&#153; NAS appliances are perfect for archiving old files, sharing new files, backing up clients, servers and consolidating data storage quickly and efficiently.<br>'+extraBreaker+'</font></td></tr></table></td><td width="175" valign="middle" height="160"><img src="images/spacer.gif" width="175" height="1"></td></tr></table></td></tr></table></td></tr></table>';
			muaMovie.Rewind();
			muaMovie.SetVariable("cualProducto", "tigernas1");
			muaMovie.Play();
		}
		else if (esteHomie == "tigernas2") {
			document.getElementById("cloudyTable").innerHTML = '<table width="100%" border="0" cellspacing="0" cellpadding="0"><tr valign="top"><td width="275" align="center">'
			+ leSpecial
			+'<img src="images/spacer.gif" width="275" height="1">'
			+'</td><td width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0" height="168"><tr><td align="right" valign="top" width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" valign="bottom" align="center" height="160"><table width="85%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" style="line-height:14px;"><font class="btext" style="font-size:'+fontSize+';color:#333366"><nobr><b>Tiger Series� Network Attached Storage</b> <span style="margin-left:15px;">( <a href="newframer.cgi?subject=coastlinemicro_services&title=tigerNAS&PageTitle=Tiger%20Series%20NAS%20Solutions" class="btext" style="font-size:9px;color:#333366">Evaluate</a> / <a href="newframer.cgi?subject=coastlinemicro_services&title=tigerNAS&PageTitle=Tiger%20Series%20NAS%20Solutions" class="btext" style="font-size:9px;color:#333366">Configure</a> / <a href="newframer.cgi?subject=coastlinemicro_services&title=tigerNAS&PageTitle=Tiger%20Series%20NAS%20Solutions" class="btext" style="font-size:9px;color:#333366">Print</a> )</span></nobr><br>The Coastline Micro Tiger Series&#153; NAS appliances are perfect for archiving old files, sharing new files, backing up clients, servers and consolidating data storage quickly and efficiently.<br>'+extraBreaker+'</font></td></tr></table></td><td width="175" valign="middle" height="160"><img src="images/spacer.gif" width="175" height="1"></td></tr></table></td></tr></table></td></tr></table>';
			muaMovie.Rewind();
			muaMovie.SetVariable("cualProducto", "tigernas2");
			muaMovie.Play();
		}
		else if (esteHomie == "reef1") {
			document.getElementById("cloudyTable").innerHTML = '<table width="100%" border="0" cellspacing="0" cellpadding="0"><tr valign="top"><td width="275" align="center">'
			+ leSpecial
			+'<img src="images/spacer.gif" width="275" height="1">'
			+'</td><td width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0" height="168"><tr><td align="right" valign="top" width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" valign="bottom" align="center" height="160"><table width="85%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" style="line-height:14px;"><font class="btext" style="font-size:'+fontSize+';color:#333366"><nobr><b>Reef Series� Notebooks</b>  <span style="margin-left:15px;">( <a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=reef&newIface=true&loadthis=reef&PageTitle=Reef Series Notebooks" class="btext" style="font-size:9px;color:#333366">Evaluate</a> / <a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=reef&newIface=true&loadthis=reef&PageTitle=Reef Series Notebooks" class="btext" style="font-size:9px;color:#333366">Configure</a> / <a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=reef&newIface=true&loadthis=reef&PageTitle=Reef Series Notebooks" class="btext" style="font-size:9px;color:#333366">Print</a> )</span></nobr><br>The reef shark is one of the most visually intruging sharks in the world, as for the Reef Series&#153; Notebook, it stands it\\'s own in the world of mobile computing systems.<br><br></font></td></tr></table></td><td width="175" valign="middle" height="160"><img src="images/spacer.gif" width="175" height="1"></td></tr></table></td></tr></table></td></tr></table>';
			muaMovie.Rewind();
			muaMovie.SetVariable("cualProducto", "reef1");
			muaMovie.Play();
		}
		else if (esteHomie == "thresher1") {
			document.getElementById("cloudyTable").innerHTML = '<table width="100%" border="0" cellspacing="0" cellpadding="0"><tr valign="top"><td width="275" align="center">'
			+ leSpecial
			+'<img src="images/spacer.gif" width="275" height="1">'
			+'</td><td width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0" height="168"><tr><td align="right" valign="top" width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" valign="bottom" align="center" height="160"><table width="85%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" style="line-height:14px;"><font class="btext" style="font-size:'+fontSize+';color:#333366"><nobr><b>Thresher Series� Desktop PCs</b>  <span style="margin-left:15px;">( <a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=thresher&newIface=true&loadthis=thresher&PageTitle=Thresher Series Desktop PCs" class="btext" style="font-size:9px;color:#333366">Evaluate</a> / <a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=thresher&newIface=true&loadthis=thresher&PageTitle=Thresher Series Desktop PCs" class="btext" style="font-size:9px;color:#333366">Configure</a> / <a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=thresher&newIface=true&loadthis=thresher&PageTitle=Thresher Series Desktop PCs" class="btext" style="font-size:9px;color:#333366">Print</a> )</span></nobr><br>The fastest and most reliable value priced Desktop PC in the market today. Fully configurable and fully supported to give you the best possible performance at the lowest possible price.<br><br></font></td></tr></table></td><td width="175" valign="middle" height="160"><img src="images/spacer.gif" width="175" height="1"></td></tr></table></td></tr></table></td></tr></table>';
			muaMovie.Rewind();
			muaMovie.SetVariable("cualProducto", "thresher1");
			muaMovie.Play();
		}
		else if (esteHomie == "thresher2") {
			document.getElementById("cloudyTable").innerHTML = '<table width="100%" border="0" cellspacing="0" cellpadding="0"><tr valign="top"><td width="275" align="center">'
			+ leSpecial
			+'<img src="images/spacer.gif" width="275" height="1">'
			+'</td><td width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0" height="168"><tr><td align="right" valign="top" width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" valign="bottom" align="center" height="160"><table width="85%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" style="line-height:14px;"><font class="btext" style="font-size:'+fontSize+';color:#333366"><nobr><b>Thresher Series� Desktop PCs</b>  <span style="margin-left:15px;">( <a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=thresher&newIface=true&loadthis=thresher&PageTitle=Thresher Series Desktop PCs" class="btext" style="font-size:9px;color:#333366">Evaluate</a> / <a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=thresher&newIface=true&loadthis=thresher&PageTitle=Thresher Series Desktop PCs" class="btext" style="font-size:9px;color:#333366">Configure</a> / <a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=thresher&newIface=true&loadthis=thresher&PageTitle=Thresher Series Desktop PCs" class="btext" style="font-size:9px;color:#333366">Print</a> )</span></nobr><br>The fastest and most reliable value priced Desktop PC in the market today. Fully configurable and fully supported to give you the best possible performance at the lowest possible price.<br><br></font></td></tr></table></td><td width="175" valign="middle" height="160"><img src="images/spacer.gif" width="175" height="1"></td></tr></table></td></tr></table></td></tr></table>';
			muaMovie.Rewind();
			muaMovie.SetVariable("cualProducto", "thresher2");
			muaMovie.Play();
		}
		else if (esteHomie == "vpn") {
			document.getElementById("cloudyTable").innerHTML = '<table width="100%" border="0" cellspacing="0" cellpadding="0"><tr valign="top"><td width="275" align="center">'
			+ leSpecial
			+'<img src="images/spacer.gif" width="275" height="1">'
			+'</td><td width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0" height="168"><tr><td align="right" valign="top" width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" valign="bottom" align="center" height="160"><table width="85%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" style="line-height:14px;"><font class="btext" style="font-size:'+fontSize+';color:#333366"><nobr><b>Shiva&reg; LanRover Security Gateways</b>  <span style="margin-left:15px;">( <a href="newframer.cgi?subject=coastlinemicro_services&title=lanrover3105&PageTitle=LanRover%203105%20Security%20Gateway" class="btext" style="font-size:9px;color:#333366">Evaluate</a> / <a href="newframer.cgi?subject=coastlinemicro_services&title=lanrover3105&PageTitle=LanRover%203105%20Security%20Gateway" class="btext" style="font-size:9px;color:#333366">Configure</a> / <a href="newframer.cgi?subject=coastlinemicro_services&title=lanrover3105&PageTitle=LanRover%203105%20Security%20Gateway" class="btext" style="font-size:9px;color:#333366">Print</a> )</span></nobr><br>The LanRover 3105 enables you to significantly cut the telecommunications costs associated with dial-up, leased-line and frame relay connections by leveraging the Internet to securely provide remote access, LAN-to-LAN and Extranet connectivity.<br><br></font></td></tr></table></td><td width="175" valign="middle" height="160"><img src="images/spacer.gif" width="175" height="1"></td></tr></table></td></tr></table></td></tr></table>';
			muaMovie.Rewind();
			muaMovie.SetVariable("cualProducto", "vpn");
			muaMovie.Play();
		}
		else {
//		else if (esteHomie == "certance1") {
			document.getElementById("cloudyTable").innerHTML = '<table width="100%" border="0" cellspacing="0" cellpadding="0"><tr valign="top"><td width="275" align="center">'
			+ leSpecial
			+'<img src="images/spacer.gif" width="275" height="1">'
			+'</td><td width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0" height="168"><tr><td align="right" valign="top" width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" valign="top" align="center" height="160"><table width="85%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" style="line-height:14px;"><font class="btext" style="font-size:'+fontSize+';color:#145D9C"><nobr>'+extraBreaker+'<br><b>Certance DAT 72</b>  <span style="margin-left:15px;">( <a href="http://www.certance.com/" target="CERTANCE" class="btext" style="font-size:9px;color:#145D9C">Certance Home</a> / <a href="http://www.certance.com/products/CertanceDrives/ddsDatMain.cgi" target="CERTANCE" class="btext" style="font-size:9px;color:#145D9C">More Info</a> )</span></nobr><br>The Certance DAT 72 is the most cost-effective tape solution in its market segment. Total cost of ownership is determined by combining the cost of the tape drive with the minimum number of data cartridges required to perform ongoing backup operations for one and three years.</font></td></tr></table></td><td width="25" valign="middle" height="160"><img src="images/spacer.gif" width="25" height="1"></td></tr></table></td></tr></table></td></tr></table>';
			muaMovie.Rewind();
			muaMovie.SetVariable("cualProducto", "certance1");
			muaMovie.Play();
		}
		// mako 1
//		else {
//			document.getElementById("cloudyTable").innerHTML = '<table width="100%" border="0" cellspacing="0" cellpadding="0"><tr valign="top"><td width="275" align="center">'
//			+ leSpecial
//			+'<img src="images/spacer.gif" width="275" height="1">'
//			+'</td><td width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0" height="168"><tr><td align="right" valign="top" width="100%"><table width="100%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" valign="bottom" align="center" height="160"><table width="85%" border="0" cellspacing="0" cellpadding="0"><tr><td width="100%" style="line-height:14px;"><font class="btext" style="font-size:'+fontSize+';color:#000000"><nobr><b>Mako Series� Workstations</b>  <span style="margin-left:15px;">( <a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=mako&loadthis=mako&PageTitle=Mako Series Workstations" class="btext" style="font-size:9px;color:#000000">Evaluate</a> / <a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=mako&loadthis=mako&PageTitle=Mako Series Workstations" class="btext" style="font-size:9px;color:#000000">Configure</a> / <a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=mako&loadthis=mako&PageTitle=Mako Series Workstations" class="btext" style="font-size:9px;color:#000000">Print</a> )</span></nobr><br>Desktop publishing and CAD/CAM applications were designed to run on our Mako Series� Performance Desktop PCs. These systems will blaze through your process-intensive workloads. Utilizing Rambus memory and the Intel� Pentium� 4 processor each Mako Series� Performance Desktop PC features the latest technological improvements.<br><br></font></td></tr></table></td><td width="175" valign="middle" height="160"><img src="images/spacer.gif" width="175" height="1"></td></tr></table></td></tr></table></td></tr></table>';
//			muaMovie.Rewind();
//			muaMovie.SetVariable("cualProducto", "mako1");
//			muaMovie.Play();
//		}


	}
	else {
		document.getElementById("cloudyTable").innerHTML = '<table height="168" bgcolor="#66698A" style="background-image: url(images/nuevohome/lethresher.jpg); background-repeat: no-repeat; background-position: right top;" width="100%" align="center" cellpadding="0" cellspacing="0"><tr><td width="100%">&nbsp;</td></tr></table>';
		// document.getElementById("careers").style.top = '-150px';
	}


}
function togglePRTB (cual) {

}
</script>
</head>
<BODY bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="placeClouds();wrapIt();makeSearch();timeFlip();" ONRESIZE="placeClouds();" onFocus="wrapIt();">
<!-- Copyright NetMedia Solutions and Coastline Micro, Inc.-->

EOF
}

	print '<script language="Javascript" src="js/newmenu_constructor_home.js"></script>';

{
print <<EOF
<!--
<div style="width:1px;height:1px;visibility:hidden;">
intel server microsoft windows wpnas network attached storage nas coastline micro thresher series great white series mako series tiger series reef series notebook laptop desktop workstation
intel server microsoft windows wpnas network attached storage nas coastline micro thresher series great white series mako series tiger series reef series notebook laptop desktop workstation
intel server microsoft windows wpnas network attached storage nas coastline micro thresher series great white series mako series tiger series reef series notebook laptop desktop workstation
intel server microsoft windows wpnas network attached storage nas coastline micro thresher series great white series mako series tiger series reef series notebook laptop desktop workstation
intel server
microsoft windows wpnas
network attached storage nas
coastline micro
thresher series
great white series
mako series
tiger series
reef series
notebook laptop desktop workstation
intel server
microsoft windows wpnas
network attached storage nas
coastline micro
thresher series
great white series
mako series
tiger series
reef series
notebook laptop desktop workstation
intel server
microsoft windows wpnas
network attached storage nas
coastline micro
thresher series
great white series
mako series
tiger series
reef series
notebook laptop desktop workstation
intel server
microsoft windows wpnas
network attached storage nas
coastline micro
thresher series
great white series
mako series
tiger series
reef series
notebook laptop desktop workstation
intel server
microsoft windows wpnas
network attached storage nas
coastline micro
thresher series
great white series
mako series
tiger series
reef series
notebook laptop desktop workstation
<img src="intel server microsoft windows wpnas network attached storage nas coastline micro thresher series great white series mako series tiger series reef series notebook laptop desktop workstation" width="1" height="1" alt="intel server microsoft windows wpnas network attached storage nas coastline micro thresher series great white series mako series tiger series reef series notebook laptop desktop workstation">
<img src="intel server microsoft windows wpnas network attached storage nas coastline micro thresher series great white series mako series tiger series reef series notebook laptop desktop workstation" width="1" height="1">
<img src="intel server microsoft windows wpnas network attached storage nas coastline micro thresher series great white series mako series tiger series reef series notebook laptop desktop workstation" width="1" height="1">
<img src="intel server microsoft windows wpnas network attached storage nas coastline micro thresher series great white series mako series tiger series reef series notebook laptop desktop workstation" width="1" height="1">
</div>-->
<div id="overDiv"></div>
<div style="position:absolute;left:40%;top:25px;"><a href="#" onClick="javascript:runImagenURL();"><img src="images/nuevohome/hspacer.gif" width="150" height="70" border="0" name="leImagen"></a><form name="leImagenSetter"><input type="hidden" name="leHref" value=""></form></div>
<div style="position:absolute;left:15px;top:5px;"><img src="images/top_cm_logo.jpg" width="220" height="72"></div>

<script language="Javascript" src="js/overlib2.js"></script>
<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td rowspan="2" width="15%" align="center" valign="middle">&nbsp;</td>
    <td rowspan="2" align="right" valign="middle" width="40%"><font face="verdana,arial,helvetica" size="1" color="#333366">&nbsp;</font></td>
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
    <td align="center" height="1"><img src="images/spacer.gif" height="1" width="1" border="0"></td>
  </tr>
  <tr bgcolor="#A6B0CA"> 
    <td align="center" height="20"><img src="images/spacer.gif" height="20" width="100" border="0"></td>
  </tr>
  <tr> 
    <td align="center" height="1"><img src="images/spacer.gif" height="1" width="1" border="0"></td>
  </tr>
</table>

<div id="cloudyTable">&nbsp;</div>
<div id="cloudy" bgcolor="#A6B0CB" style="position:absolute;width:1px;height:168px;left:-1000px;top:122px;z-index:-5;visibility:hidden;">&nbsp;</div>

<!--<div style="position:absolute;top:480px;left:18%;width:339px;height:76px;"><a href="http://www.rhomberg.com/systemConfigurator/Microsoft_Windows_2003.cgi" target="_parent"><img src="images/ms2003serverHome.jpg" width="339" height="76" border="0"></a></div>-->


<!--<table width="100%" border="0" cellspacing="0" cellpadding="0" height="30">
  <tr valign="top"> 
    <td width="50%"><img src="images/nuevohome/serious_servers.jpg" width="325" height="22" vspace="4"></td>
    <td width="50%" valign="top" align="right"><img src="images/nuevohome/serious_service.jpg" width="325" height="22" vspace="4"></td>
  </tr>
</table>
-->

<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr bgcolor="#A6B0CA"> 
    <td bgcolor="#FFFFFF" width="100%" align="right"><img src="images/prtbfinisher.gif" width="35" height="19" border="0"></td>
    <td bgcolor="#E6E9F0" width="1"><img src="images/spacer.gif" width="1" height="10" border="0"></td>
    <td width="141"><font class="newhome1">&nbsp;Profile<br><img src="images/spacer.gif" width="141" height="1" border="0"></font></td>
  </tr>
</table>
<td width="100%">
<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
    <tr> 
      <td align="right" valign="top" width="100%"> 
        <table border="0" cellspacing="0" cellpadding="0" width="100%">
          <tr> 
            <td valign="top" width="100%" align="center">
<center><img src="images/your_value_distributor.jpg" width="316" height="42" border="0" vspace="5"><img src="images/spacer.gif" width="75" height="42" border="0"><a href="http://www.credentrust.com/pbo/nasba/vendorLand1.cfm?salespersonNumber=01000" target="LEASING"><img src="images/leasing_small.gif" width="175" height="67" border="0"  alt="Click to view more information about our system leasing option."></a></center>
<table width="80%" border="0" cellspacing="0" cellpadding="0">
  <tr align="center"> 
    <td colspan="3"><img src="images/prtbbuiltoorder.jpg" width="329" height="26"></td>
  </tr>
  <tr align="center"> 
    <td width="50%">
      <table border="0" cellspacing="0" cellpadding="0" height="329">
        <tr>
          <td><nobr><img src="images/spacer.gif" width="12" height="64"><a href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=reef&newIface=true&loadthis=reef&PageTitle=Reef%20Series%20Notebook%20PCs" target="_parent"><img src="images/prtb1.jpg" width="233" height="73" border="0"></a></nobr></td>
        </tr>
        <tr>
          <td><nobr><img src="images/spacer.gif" width="16" height="64" border="0"><A href="javascript:void(0);"><img src="images/prtb2.jpg" width="230" height="64" border="0"></a></nobr></td>
        </tr>
        <tr>
          <td><A href="newframer.cgi?subject=sharktank&title=thresher&newIface=true&loadthis=thresher&PageTitle=Thresher%20Series%20Desktop%20PCs"><img src="images/prtb3.jpg" width="271" height="65" border="0"></a></td>
        </tr>
      </table>
      <img src="images/spacer.gif" width="195" height="1"></td>
    <td width="30"><img src="images/prtbparter.jpg" width="8" height="329"><br>
      <img src="images/spacer.gif" width="20" height="1"></td>
    <td width="50%">
      <table border="0" cellspacing="0" cellpadding="0" height="329">
        <tr> 
          <td><a href="newframer.cgi?subject=coastlinemicro_services&title=tigerNAS&PageTitle=Tiger%20Series%20NAS%20Solutions" target="_parent"><img src="images/prtb4.jpg" width="318" height="71" border="0"></a></td>
        </tr>
        <tr> 
          <td><img src="images/prtb5.jpg" width="299" height="64" border="0" usemap="#prtb5">

<map name="prtb5"> 
  <area shape="rect" coords="0,13,347,64" href="newframer.cgi?subject=sharktank&title=tiger&loadthis=tiger&PageTitle=Tiger%20Series%20DP%20Xeon%20Servers" target="_parent"> 
  <area shape="rect" coords="0,1,347,14" href="newframer.cgi?subject=sharktank&title=gw&loadthis=gw&PageTitle=Great%20White%20Series%20Servers" target="_parent">
</map>
		  </td>
        </tr>
        <tr> 
          <td><a href="newframer.cgi?subject=coastlinemicro_services&title=lanrover3105&PageTitle=LanRover%203105%20Security%20Gateway" target="_parent"><img src="images/prtb6.jpg" width="256" height="83" border="0"></a></td>
        </tr>
      </table>
    </td>
  </tr>
</table>


<script language="JavaScript">
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions
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
/*
	document.getElementById("PKeywords2").style.visibility = "hidden";
	document.getElementById("SButton2").style.visibility = "hidden";
	var imagen = 	"images/nuevohome/leradiobut_on.gif";
	document.images.Inventory.src = imagen;
*/
}

function wrapIt() {
/*
	if(bw.ns4 || bw.ns6) {
		document.getElementById("PKeywords2").style.top = "-22";
		document.getElementById("SButton2").style.top = "-18";
	}
	else {
		document.getElementById("PKeywords2").style.top = "-42";
		document.getElementById("SButton2").style.top = "-38";	
	}
*/
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
		document.search1.ProductType.focus();
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
		document.search2.keywords.select();
	}
}
//-->
</script>
            </td>
          </tr>
        </table>

      </td>
<!--
      <td bgcolor="#E6E9F0" width="1"><img src="images/spacer.gif" width="1" height="10" border="0"></td>
-->
      <td width="99" valign="top">
<!--
        <table width="99" height="94" border="0" cellspacing="0" cellpadding="0" style="background-image: url(images/nuevohome/hback1.jpg); background-repeat: no-repeat; background-position: right top">
          <tr> 
            <td valign="top"> 
              <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr> 
                  <td height="3"><img src="images/spacer.gif" height="3" width="10" border="0"></td>
                </tr>
                <tr> 
                  <td height="18" valign="middle"><font class="btext">&nbsp;&nbsp;<a href="javascript:void(0)" onClick="toggleSearch('Inventory');" style="color:333366;font-weight:normal">Inventory</a></font></td>
                </tr>
                <tr> 
                  <td height="1" align="left"><img src="images/nuevohome/hspacer.gif" height="1" width="80" border="0"></td>
                </tr>
                <tr> 
                  <td height="18" valign="middle"><font class="btext">&nbsp;&nbsp;<a href="javascript:void(0)" onClick="toggleSearch('Website');" style="color:333366;font-weight:normal">Website</a></font></td>
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
                  <td height="25" valign="middle"><font class="btext">&nbsp;&nbsp;Search Terms</font></td>
                </tr>
              </table>
            </td>
          </tr>
        </table>
-->
      </td>
<!--
      <td bgcolor="#E6E9F0" width="1"><img src="images/spacer.gif" width="1" height="10" border="0"></td>
-->
      <td width="118" valign="top">

<!--
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
                  <td height="12" valign="middle" width="133"><font class="btext"><a style="color:333366;font-weight:normal" href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=thresher&newIface=true&loadthis=thresher&PageTitle=Thresher Series Desktop PCs">Desktop PCs</a></font></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15"><font class="btext">&nbsp;</font></td>
                  <td height="12" valign="middle" width="133"><font class="btext"><a style="color:333366;font-weight:normal" href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=mako&loadthis=mako&PageTitle=Mako Series Workstations">Workstations</a></font></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15"><font class="btext">&nbsp;</font></td>
                  <td height="12" valign="middle" width="133"><font class="btext"><a style="color:333366;font-weight:normal" href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=reef&newIface=true&loadthis=reef&PageTitle=Reef Series Notebooks">Notebooks</a></font></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15"><font class="btext">&nbsp;</font></td>
                  <td height="12" valign="middle" width="133"><font class="btext"><a style="color:333366;font-weight:normal" href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=tiger&loadthis=tiger&PageTitle=Tiger Series DP Xeon Servers">DP Xeon&#153; Servers</a></font></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15"><font class="btext">&nbsp;</font></td>
                  <td height="12" valign="middle" width="133"><font class="btext"><a style="color:333366;font-weight:normal" href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=sharktank&title=gw&loadthis=gw&PageTitle=Great White Series MP Xeon Servers">MP Xeon&#153; Servers</a></font></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15"><font class="btext">&nbsp;</font></td>
                  <td height="12" valign="middle" width="133"><font class="btext"><a style="color:333366;font-weight:normal" href="http://www.rhomberg.com/systemConfigurator/newframer.cgi?subject=services&title=vpn3105&PageTitle=3105 VPN Gateway">VPN/Firewalls</a></font></td>
                </tr>
                <tr> 
                  <td height="5" valign="middle" colspan="2"><img src="images/spacer.gif" width="1" height="5" border="0"></td>
                </tr>
                <tr> 
                  <td height="18" valign="middle" colspan="2"><font class="btext">&nbsp;&nbsp;</font></td>
                </tr>
                <tr> 
                  <td height="12" valign="middle" width="15"><font class="btext">&nbsp;</font></td>
                  <td height="12" valign="middle" width="133"><font class="btext">&nbsp;</font></td>
                </tr>

                <tr> 
                  <td height="24" valign="middle" align="center" colspan="2" bgcolor="#E6E9F0"><font class="btext"><a href="javascript:void(0)" onClick="javascript:alert('Coming Soon, Please check back...');" style="color:333366;font-weight:normal">Testimonials</a></font></td>
                </tr>
                <tr> 
                  <td height="5" colspan="2"><img src="images/spacer.gif" width="1" height="5" border="0"></td>
                </tr>
                <tr> 
                  <td height="24" valign="middle" align="center" colspan="2" bgcolor="#E6E9F0"><font class="btext"><a href="javascript:void(0)" onClick="javascript:alert('Coming Soon, Please check back...');" style="color:333366;font-weight:normal">Monthly Newsletter</a></font></td>
                </tr>

              </table>
            </td>
          </tr>
        </table>
-->
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
                  <td height="12" valign="middle" width="136"><font class="btext">$PressText - <a style="color:#EB0000;font-weight:normal" href="newframer.cgi?subject=press&title=in&viewRel=$PressNum&PageTitle=Press Releases"><b>More Info</b></a></font></td>
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
                  <td height="12" valign="middle" width="136"><font class="btext">Fax<br>(949) 450-9977</font></td>
                </tr>
                <tr> 
                  <td height="15" colspan="2"><img src="images/spacer.gif" width="1" height="15" border="0"></td>
                </tr>
                <tr> 
                  <td height="24" valign="middle" align="center" colspan="2" bgcolor="#E6E9F0"><font class="btext"><a href="javascript:void(0)" onClick="javascript:alert('Coming Soon, Please check back...');" style="color:333366;font-weight:normal">Testimonials</a></font></td>
                </tr>
                <tr> 
                  <td height="5" colspan="2"><img src="images/spacer.gif" width="1" height="5" border="0"></td>
                </tr>
                <tr> 
                  <td height="24" valign="middle" align="center" colspan="2" bgcolor="#E6E9F0"><font class="btext"><a href="javascript:void(0)" onClick="javascript:alert('Coming Soon, Please check back...');" style="color:333366;font-weight:normal">Monthly Newsletter</a></font></td>
                </tr>
                <tr> 
                  <td height="5" colspan="2"><img src="images/spacer.gif" width="1" height="5" border="0"></td>
                </tr>
                <tr> 
                  <td height="24" valign="middle" align="center" colspan="2" bgcolor="#673301"><font class="btext"><a href="newframer.cgi?subject=coastlinemicro_services&title=UPSTools&PageTitle=UPS%20Tools"><img src="images/upsMain.gif" width="135" height="45" border="0"></a></font></td>
                </tr>
                <tr> 
                  <td height="5" colspan="2"><img src="images/spacer.gif" width="1" height="5" border="0"></td>
                </tr>
                <tr> 
                  <td height="24" valign="middle" align="center" colspan="2"><font class="btext"><a href="newframer.cgi?subject=coastlinemicro_services&title=FEDEXTools&PageTitle=FedEx%20Tools"><img src="images/fedexMain.gif" width="135" height="45" border="0"></a></font></td>
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