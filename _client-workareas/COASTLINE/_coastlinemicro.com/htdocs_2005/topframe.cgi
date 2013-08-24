#!/usr/bin/perl5 -s

###########################################################################################################
# Company: ©2001 NetMedia Solutions                                                                             #
# Date: Saturday, September 21, 2001                                                                      #
# Location: Los Angeles County, California, United States of America                                      #
# Made By: Luis Rodriguez (drlouie)                                                                       #
# Email: Drlouie@NetMediaSol.com                                                                          #
#                                                                                                         #
# This program cannot be duplicated, distributed or re-used for any other purpose other than its original #
# intended purpose and function. You may request NetMedia Solutions for a copy of the script,             #
# personalized to fit your exact needs for a small re-programming fee.                                    #
###########################################################################################################

## Test location of request
require ("referer.nsp");

print "Content-type: text/html\n\n";

## Snif cookie, if present test for logged in status
require ("cookiesnif.nsp");

require ("parse_query.nsp");

require ("date.nsp");

if ($Cookies{'GID'} && ($Cookies{'UTipe'} eq "CustAdmin" || $Cookies{'UTipe'} eq "CustUser")) {
	$Welcome = "<b>Ahhh! I see you're back again $Cookies{'FiNo'}...</b><br><a href=\"logoff.cgi\" target=\"_parent\">I am not $Cookies{'FiNo'}!</a>";
	$LoginBut = "<a href=\"logoff.cgi\" onClick=\"document.images.search.src = 'images/spacer.gif';\" target=\"botOne\" onMouseOver=\"javascript:imageOn('logoff','on');\" onMouseOut=\"javascript:imageOff('logoff','off');\"><img src=\"images/dbing/button_logoff_off.gif\" width=\"75\" height=\"19\" name=\"logoff\" border=\"0\"></a>";
	## $CartBut = "<a href=\"products.cgi?title=products&loadcart=1\" target=\"botOne\" onMouseOver=\"javascript:imageOn('mycart','on');\" onMouseOut=\"javascript:imageOff('mycart','off');\"><img src=\"images/dbing/button_mycart_off.gif\" width=\"75\" height=\"19\" name=\"mycart\" border=\"0\"></a>";
}
elsif ($Cookies{'GID'}) { 
	$Welcome = "<b>Welcome to the $Cookies{'FiNo'} $Cookies{'LaNo'}...</b><br><a href=\"logoff.cgi\" target=\"_parent\">I am not $Cookies{'FiNo'}!</a>";
	$LoginBut = "<a href=\"logoff.cgi\" onClick=\"document.images.search.src = 'images/spacer.gif';\" target=\"botOne\" onMouseOver=\"javascript:imageOn('logoff','on');\" onMouseOut=\"javascript:imageOff('logoff','off');\"><img src=\"images/dbing/button_logoff_off.gif\" width=\"75\" height=\"19\" name=\"logoff\" border=\"0\"></a>";
}
else {
	$Welcome = "<b>Welcome to the Store </b><br>Would you like to <a href=\"login.cgi\" onClick=\"document.images.search.src = 'images/spacer.gif';\" target=\"botOne\">Log In?</a>";
	$LoginBut = "<a href=\"login.cgi\" onClick=\"document.images.search.src = 'images/spacer.gif';\" target=\"botOne\" onMouseOver=\"javascript:imageOn('login','on');\" onMouseOut=\"javascript:imageOff('login','off');\"><img src=\"images/dbing/button_login_off.gif\" width=\"75\" height=\"19\" name=\"login\" border=\"0\"></a>";
}

if ($FORM{'noSearch'}) { $noSearch = "<script language=\"Javascript\">function noSoichit() { document.images.search.src = 'images/spacer.gif'; }</script>"; $noSoichit = "noSoichit();"; }

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

<html>
<head>
<title>Company Name</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="http://www.rhomberg.com/systemConfigurator/common_css.cgi" Type="text/css">
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

// QUICK CROSS-BROWSER MOUSE-OVER/OFF FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function imageOff(which,thisone) {
	Test1 = document.images[which].src;
	Test1 = document.images[which].src;
	if (Test1.indexOf('spacer.gif') == -1) {
		var cual = 	"images/dbing/button_"+which+"_"+thisone+".gif";
		document.images[which].src = cual;
	}
}
function imageOn(which,thisone) {
	Test1 = document.images[which].src;
	if (Test1.indexOf('spacer.gif') == -1) {
		var cual = 	"images/dbing/button_"+which+"_"+thisone+".gif";
		document.images[which].src = cual;
	}
}
</SCRIPT>
<script language="javascript">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

<!--
function trigger(myurl) {
var b = navigator.appName;
if (b=="Netscape") {
	mainFrame = parent.frames.botOne;
	mainFrame.frame.loadpage(''+myurl+'');
}

else {
	parent.botOne.frame.loadpage(''+myurl+'');
	}

if (document.getElementById) {  // DOM3 = IE5, NS6
	parent.botOne.document.getElementById('bground').style.visibility = 'visible';
	}
else {
if (document.layers) {  // Netscape 4
	mainFrame.document.bground.visibility = 'visible';
	}
else {  // IE 4
	parent.botOne.document.all.bground.style.visibility = 'visible'; 
	}
}
}

function toggleSearchBox() {
	var b = navigator.appName;
	if (b=="Netscape") { parent.frames.botOne.toggleSearch1(); }
	else { parent.botOne.toggleSearch1(); }
}

//-->
</script>
<style type="text/css">
#divNewsCont {position:absolute; left:275px; top:12px; width:300px; height:80px; clip:rect(0px 300px 80px 0px); visibility:hidden; overflow:hidden;}
#divNews     {position:absolute;} 
.link { line-height:12px; font-family:verdana,arial,helvetica; font-size:10px; text-decoration:none; }
.nolink { line-height:12px; font-family:verdana,arial,helvetica; font-size:10px; text-decoration:none; font-weight:bold; }
.red { color:#EB0000; }
a { text-decoration:none; }
</style>
<script lanagauge="Javascript">
	//How do you want the script to work? 
	//0 = Fade in - Fade out
	//1 = Slide in - Fade out
	//2 = Random 
	nWorks = 2

	//If you use the slide set these variables:
	nSlidespeed = 5 //in px
	nNewsheight = 20 //This is how long down it should start the slide.

	nBetweendelay = 10000 //The delay before fading out.
	nFont = 'verdana,arial,helvetiva' //The font for the news.
	nFontsize = 10 //Font size in pixel.
	nFadespeed = 100 //The speed to fade in, in milliseconds.

	//Set the colors, first color is same as background, last color is the color it stops at:
	//You can have as many colors you want
	nColor=new Array('#FFFFFF', '#EEEEEE','#CCCCCC','#999999','#666666','#333333','#000000')

	//This is the news you wanna have, set the link and the text. If you don't wan't it to link anywhere
	//use a # as the link
	nNews=new Array()
	//Copy there three lines and change the info and numbers to get more news.

EOF
}

if ($Cookies{'GID'} && ($Cookies{'UTipe'} eq "CustAdmin" || $Cookies{'UTipe'} eq "CustUser")) {
	print " 	nNews[0]=new Array()\n";
	print " 	nNews[0][\"text\"]=\"<font class=nolink>Welcome to the Store Front $Cookies{'FiNo'} $Cookies{'LaNo'}...</font><font class=link><br>I am not $Cookies{'FiNo'}, <font class=red>Change User!</font></font>\"\n";
	print " 	nNews[0][\"link\"]=\"#\"\n";
	print " 	nNews[0][\"target\"]=\"_self\"\n";
	print " 	nNews[0][\"script\"]=\"document.images.search.src = \'images/spacer.gif\';\"\n";
	print " 	nNews[1]=new Array()\n";
	print " 	nNews[1][\"text\"]=\"<font class=nolink>Store Front inventory is priced<br>exclusively for <font class=red>$Cookies{'CoNo'}</font></font>\"\n";
	print " 	nNews[1][\"link\"]=\"#\"\n";
	print " 	nNews[1][\"target\"]=\"_self\"\n";
	print " 	nNews[1][\"script\"]=\"void(0);\"\n";
	print " 	nNews[2]=new Array()\n";
	print " 	nNews[2][\"text\"]=\"<font class=nolink><font class=red>Did You Know?</font><br>Coastline Micro offers the highest quality Intel™ network components at the BEST prices? <font class=red>Show me...</font></font>\"\n";
	print " 	nNews[2][\"link\"]=\"http://www.rhomberg.com/systemConfigurator/everything_intel.cgi?title=intel\"\n";
	print " 	nNews[2][\"target\"]=\"botOne\"\n";
	print " 	nNews[2][\"script\"]=\"void(0);\"\n";
	print " 	nNews[3]=new Array()\n";
	print " 	nNews[3][\"text\"]=\"<font class=nolink><font class=red>Press Release</font><br>$PressText <font class=red>- More info</font></font>\"\n";
	print " 	nNews[3][\"link\"]=\"http://www.rhomberg.com/systemConfigurator/press.cgi?viewRel=$PressNum\"\n";
	print " 	nNews[3][\"target\"]=\"botOne\"\n";
	print " 	nNews[3][\"script\"]=\"void(0);\"\n";
}
elsif ($Cookies{'GID'}) { 
	print " 	nNews[0]=new Array()\n";
	print " 	nNews[0][\"text\"]=\"<font class=nolink>Ahhh! I see you're back again $Cookies{'FiNo'}...<br>I am not $Cookies{'FiNo'}, <font class=red>Change User!</font></font>\"\n";
	print " 	nNews[0][\"link\"]=\"logoff.cgi\"\n";
	print " 	nNews[0][\"target\"]=\"botOne\"\n";
	print " 	nNews[0][\"script\"]=\"document.images.search.src = \'images/spacer.gif\';\"\n";
}
else {
	print " 	nNews[0]=new Array()\n";
	print " 	nNews[0][\"text\"]=\"<font class=nolink>Welcome to the Store Front, our online store...<font class=red><br>Would you like to log in?</font></font>\"\n";
	print " 	nNews[0][\"link\"]=\"login.cgi\"\n";
	print " 	nNews[0][\"target\"]=\"botOne\"\n";
	print " 	nNews[0][\"script\"]=\"document.images.search.src = \'images/spacer.gif\';\"\n";
	print " 	nNews[1]=new Array()\n";
	print " 	nNews[1][\"text\"]=\"<font class=nolink>To view <font class=red>your</font> company's price on<br>Store Front inventory please <font class=link>log in</font>...</font>\"\n";
	print " 	nNews[1][\"link\"]=\"login.cgi\"\n";
	print " 	nNews[1][\"target\"]=\"botOne\"\n";
	print " 	nNews[1][\"script\"]=\"document.images.search.src = \'images/spacer.gif\';\"\n";
	print " 	nNews[2]=new Array()\n";
	print " 	nNews[2][\"text\"]=\"<font class=nolink><font class=red>Did You Know?</font><br>Coastline Micro offers the highest quality Intel™ network components at the BEST prices? <font class=red>Show me...</font></font>\"\n";
	print " 	nNews[2][\"link\"]=\"http://www.rhomberg.com/systemConfigurator/everything_intel.cgi?title=intel\"\n";
	print " 	nNews[2][\"target\"]=\"botOne\"\n";
	print " 	nNews[2][\"script\"]=\"void(0);\"\n";
	print " 	nNews[3]=new Array()\n";
	print " 	nNews[3][\"text\"]=\"<font class=nolink><font class=red>Press Release</font><br>$PressText <font class=red>- More info</font></font>\"\n";
	print " 	nNews[3][\"link\"]=\"http://www.rhomberg.com/systemConfigurator/press.cgi?viewRel=$PressNum\"\n";
	print " 	nNews[3][\"target\"]=\"botOne\"\n";
	print " 	nNews[3][\"script\"]=\"void(0);\"\n";
	print " 	nNews[4]=new Array()\n";
	print " 	nNews[4][\"text\"]=\"<font class=nolink><font class=red>*NEW</font> Microsoft Windows Powered Network Attached Solutions (NAS)<br><font class=red>- More info</font></font>\"\n";
	print " 	nNews[4][\"link\"]=\"http://www.rhomberg.com/systemConfigurator/services.cgi?title=tigerNAS\"\n";
	print " 	nNews[4][\"target\"]=\"botOne\"\n";
	print " 	nNews[4][\"script\"]=\"void(0);\"\n";
}

{
print <<EOF
	
</script>
</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:document.images.search.src = 'images/dbing/button_search_off.gif';$noSoichit">
<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td rowspan="2" width="15%" align="center" valign="middle"><img src="images/dbing/top_cm_logo.jpg" width="116" height="37"></td>
    <td rowspan="2" align="center" valign="middle" width="40%"><font face="verdana,arial,helvetica" size="1" color="#333366">&nbsp;</font></td>
    <td width="45%" align="right"><img src="images/dbing/god_bless_america.gif" width="118" height="35">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
  </tr>
<tr><td width="45%" align="right"><a href="http://www.rhomberg.com/systemConfigurator/index.cgi" target="_top" onMouseOver="javascript:imageOn('home','on');" onMouseOut="javascript:imageOff('home','off');"><img src="images/dbing/button_home_off.gif" width="61" height="19" name="home" border="0"></a><a href="http://www.rhomberg.com/systemConfigurator/support.cgi?title=main" onClick="javascript:document.images.search.src = 'images/dbing/button_search_off.gif';" target="botOne" onMouseOver="javascript:imageOn('support','on');" onMouseOut="javascript:imageOff('support','off');"><img src="images/dbing/button_support_off.gif" width="74" height="19" name="support" border="0"></a>$CartBut$LoginBut<a href="#" onClick="javascript:toggleSearchBox();" onMouseOver="javascript:imageOn('search','on');" onMouseOut="javascript:imageOff('search','off');"><img src="images/dbing/button_search_off.gif" name="search" border="0"></a></td></tr>
<tr></tr><td colspan="3" width="100%" bgcolor="#FFFFFF" height="2"><img src="images/spacer.gif" width="2" height="2"></td></tr>
<tr><td colspan="3" width="100%" bgcolor="#8F8FAB" height="2"><img src="images/spacer.gif" width="2" height="2"></td></tr>
<tr><td colspan="3" width="100%" bgcolor="#FFFFFF" height="2"><img src="images/spacer.gif" width="2" height="2"></td></tr>
</table>

$noSearch

<div id="divNewsCont">
	<div id="divNews">
		$Welcome
	</div>
</div>
<script language="Javascript" src="js/ticker.js"></script>
</body>
</html>

EOF
}
exit;