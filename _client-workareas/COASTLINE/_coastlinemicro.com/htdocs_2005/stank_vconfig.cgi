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

require ("referer.nsp"); 
require ("parse_query.nsp");
require ("date.nsp");

$browser = "$ENV{'HTTP_USER_AGENT'}";
if (($browser =~ "Mozilla/" && $browser =~ "6.") || $browser =~ "Netscape6") { $tablewidth = "100%"; $t1 = "5"; $t2 = "64%"; $t3 = "18%"; $t4 = "18%"; $t5 = "25%"; $t6 = "75%"; }	
else { $tablewidth = "470"; $t1 = "5"; $t2 = "339"; $t3 = "79"; $t4 = "42"; $t5 = "170"; $t6 = "300"; }
if ($browser =~ "Mozilla/4.7") { $border = "border=\"1\" bordercolor=\"#333366\""; }

if ($browser =~ "MSIE 5.0" || $browser =~ "MSIE 5.5" || $browser =~ "Mozilla/4.7" || $browser =~ "MSIE 4.0") { $StartURLer="javascript:void(0);\" onClick=\"javascript:window.open"; $EndURLer=",'EMAILIT','width=485,height=590');";}
else { $StartURLer="javascript:trigger"; $EndURLer=");";}

$STANKLEGAL = `cat stank_legal.nsf`;

## remove the CM logo since this page has a different layout with CM in it already...
$STANKLEGAL =~ s/cm_logo_small.jpg/spacer.gif/g;
$STANKLEGAL =~ s/142/1/g;
$STANKLEGAL =~ s/51/1/g;

## Snif cookie, if present test for logged in status
require ("cookiesnif.nsp");

## ----------------->>> Must Be Logged In!
if ($Cookies{'Echado'} eq "YES") {

##----------->>> CONNECT TO DB
	use DBI;
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 

	$count=0;
	if ($FORM{'CID'} ne "" || $FORM{'CID'} ne " " || $FORM{'CID'} > 0) {
		$CID = "$FORM{'CID'}";
		## GET CONFIGURATION INFORMATION
		my $sth = $dbh->prepare("SELECT * FROM Configs WHERE ConfigID='$CID'");
		$sth->execute or die "Unable to execute query\n";
		my @row;
		while(@row = $sth->fetchrow_array) {
			$Parent = $row[1];
			$Username = $row[2];
			$CMCustNum = $row[3];
			$OrderIDs = $row[4];
			$CMSeries = $row[5];
			$ProductIDs = $row[6];
			$TotalPrice = $row[7];
			$TotalWeight = $row[8];
			$CreatedOn = $row[9];
			push(@elConfig,"$Parent=-=-=$Username=-=-=$CMCustNum=-=-=$OrderIDs=-=-=$CMSeries=-=-=$ProductIDs=-=-=$TotalPrice=-=-=$TotalWeight=-=-=$CreatedOn=-=-=$CID");
		}
		$sth->finish;

		## check to make sure user is from the company owning this configuration
		if (($Cookies{'CeeEmmNo'} eq "$CMCustNum") && (@elConfig)) { &goodone; }
		## if not user for comapny owning this CID
		else { &baduser; }
	}

	## ---------- >>> if no CID
	else {
		$sorry = `cat sorry_nospec.nsf`;
		print "Content-type: text/html\n\n";
		print "$sorry";
		exit;
	}

	## disconnect DB
	$dbh->disconnect;
}

## SORRY YOU MUST BE LOGGED IN...
else {
	print "Content-type: text/html\n\n";
	print "<script language=\"Javascript\">parent.location.href=\"login.cgi?lasturl=stank_vconfig.cgi&CID=$FORM{'CID'}\";</script>";
exit;
}

## =-=-=--------->>> IF USER IS GOOD AND CID IS PASSED
sub goodone {
$MainTitle = "Configuration Viewer";

use DBI;
my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>coastline</b>\n"; 
$dbh->{RaiseError} = 1; 
	
@splitConfig = split(/=-=-=/, $elConfig[0]);
$leParent = $splitConfig[0];
$leUser = $splitConfig[1];
$leCMC = $splitConfig[2];
$leOIDs = $splitConfig[3];
$leCMS = $splitConfig[4];
$lePIDs = $splitConfig[5];
$lePrice = $splitConfig[6];
$leWeight = $splitConfig[7];
$leCreated = $splitConfig[8];
$leCID = $splitConfig[9];

my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$leParent'");
$sth->execute or die "Unable to execute query\n";
my @row;
while(@row = $sth->fetchrow_array) {
	$ProductNombre = $row[11];
	$SmallPhoto = $row[17];
}
$sth->finish;

my $sth = $dbh->prepare("SELECT * FROM Images WHERE ImageID='$SmallPhoto'");
$sth->execute or die "Unable to execute query\n";
my @row;
while(@row = $sth->fetchrow_array) { 
	$SavedFileName = $row[3];
	$SavedDesc = $row[8];
	$SmallImageN = "$SavedFileName"; 
	$SmallImageD= "$SavedDesc";
}
$sth->execute or die "Unable to execute query\n"; 
$sth->finish;

if ($leCMS eq "GreatWhite") { $leCMS = "gw"; }
elsif ($leCMS eq "Mako") { $leCMS = "mako"; }
elsif ($leCMS eq "Reef") { $leCMS = "reef"; }
elsif ($leCMS eq "Thresher") { $leCMS = "thresher"; }
else { $leCMS = "tiger"; }

if ($FORM{'NSPRINT'}) { $NSPrinter = "onload=\"javascript:printPageNS();\""; }


if ($FORM{'InnerLink'} eq "1") {
	$CARTITLink = "&nbsp;"; 
	$RECONFIGLink = "&nbsp;";
	$LayerCSS = "#divNewsCont {position:absolute; left:150; top:12px; width:300px; height:80px; clip:rect(0px 300px 80px 0px); visibility:hidden; overflow:hidden;}\n";
	$LayerCSS2 = "#divNews     {position:absolute;}\n";
}
else { 
	$CARTITLink = "<a href=\"javascript:location.href = 'framer.html?subject=$leCMS&title=$leCMS&cartit=$leCID';\" onMouseOver=\"javascript:imageOnDHTML3('cartit','ov');\" onMouseOut=\"javascript:imageOffDHTML3('cartit','off');\"><img src=\"images/newones/cartit_off.gif\" border=\"0\" name=\"cartit\"></a>"; 
	$RECONFIGLink = "<a href=\"javascript:location.href = 'framer.html?subject=$leCMS&title=$leCMS&loadsys=$leParent';\" onMouseOver=\"javascript:imageOnDHTML3('reconfigit','ov');\" onMouseOut=\"javascript:imageOffDHTML3('reconfigit','off');\"><img src=\"images/newones/reconfigit_off.gif\" border=\"0\" name=\"reconfigit\"></a>";
	$LayerCSS = "#divNewsCont {position:absolute; top:12px; width:300px; height:80px; clip:rect(0px 300px 80px 0px); visibility:hidden; overflow:hidden;}\n";
	$LayerCSS2 = "#divNews     {position:absolute;}\n";
}

print "Content-type: text/html\n\n";

{
print <<EOF

<html>
<head>
<title>Company Name</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="common_css.html?anchor=333366&anchorov=EB0000&weight=normal&weightov=normal&decor=underline&decorov=underline" Type="text/css">
<STYLE TYPE="text/css">
body { background-color:#ffffff; scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</STYLE>
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

function imageOffDHTML(which,thisone) {
	var cual = 	"images/tables/but_"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}
function imageOnDHTML(which,thisone) {
	var cual = 	"images/tables/but_"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}

function imageOffDHTML2(which,thei,thisone) {
	var cual = 	"images/db/but_"+thei+"_"+thisone+".gif";
	document.images[which].src = cual;
}
function imageOnDHTML2(which,thei,thisone) {
	var cual = 	"images/db/but_"+thei+"_"+thisone+".gif";
	document.images[which].src = cual;
}

function imageOffDHTML3(which,thisone) {
	var cual = 	"images/newones/"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}
function imageOnDHTML3(which,thisone) {
	var cual = 	"images/newones/"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
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
if (b=="Netscape" && navigator.userAgent.indexOf("6.")) {
	parent.frames.botOne.frame.location.href=myurl;
	}
else if (b=="Netscape") {
	mainFrame = parent.frames.botOne;
	mainFrame.frame.loadpage(''+myurl+'');
}
else {
	parent.frames.botOne.frame.location.href=myurl;
	}
}
//-->
</script>
<!--START PRINT-->

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

<!--

var da = (document.all) ? 1 : 0;
var pr = (window.print) ? 1 : 0;
var mac = (navigator.userAgent.indexOf("Mac") != -1); 
var ns4 = ((navigator.userAgent.indexOf("Mozilla") != -1) && (navigator.userAgent.indexOf("4.") != -1)  && (navigator.userAgent.indexOf("MSIE") == -1));
var ns6 = ((navigator.userAgent.indexOf("Netscape") != -1) && (navigator.userAgent.indexOf("6.") != -1));

function printPageNS() {
    window.print()
}

function printPage() {
  if (ns4) // NS4
    window.open('stank_vconfig.html?CID=$leCID&NSPRINT=1','PRINT','width=485,height=590');
  else if (pr) // IE5+
    window.print()
  else if (ns6) // NS6
    window.document.print()
  else if (da && !mac) // IE4 (Windows)
    lePrint()
  else // other browsers
    alert("Sorry, your browser doesn't support this feature.");
  return false;
}

if (da && !pr && !mac) with (document) {
  writeln('<OBJECT ID="wbp" CLASSID="CLSID:778C58A9-81B6-11D3-BB8F-00C04FA3471C">');
  writeln('<' + 'SCRIPT LANGUAGE="VBScript">');
  writeln('    Sub lePrint()');
  writeln('        If Len(wbp.DefaultPrinterName) = 0 Then');
  writeln('            MsgBox "No default printer!"');
  writeln('            Exit Sub');
  writeln('        End If');
  writeln('        wbp.Print');
  writeln('    End Sub');
  writeln('<' + '/SCRIPT>');
}
// -->
</SCRIPT>
<!--END PRINT-->
<style type="text/css">
$LayerCSS
$LayerCSS2
.link { line-height:12px; font-family:verdana,arial,helvetica; font-size:10px; text-decoration:none; }
.nolink { line-height:12px; font-family:verdana,arial,helvetica; font-size:10px; text-decoration:none; font-weight:bold; }
.red { color:#EB0000; }
a { text-decoration:underline; }
a:hover { text-decoration:none; }
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

if ($FORM{'InnerLink'} eq "1") {
	$Welcome = "<a href=\"#\" onClick=\"javascript:window.close();\"><b><font class=nolink><font class=red>** NOTE **</font><br>To close this window and return to your Store Front Cart, click here at anytime...</font></b></a>";
	print " 	nNews[0]=new Array()\n";
	print " 	nNews[0][\"text\"]=\"<font class=nolink><font class=red>** Keep in Mind **</font><br>You cannot re-configure this system, yet you can always re-configure any system in our inventory...</font>\"\n";
	print " 	nNews[0][\"link\"]=\"javascript:void(0);\"\n";
	print " 	nNews[0][\"target\"]=\"_self\"\n";
	print " 	nNews[0][\"script\"]=\"void(0);\"\n";
	print " 	nNews[1]=new Array()\n";
	print " 	nNews[1][\"text\"]=\"<font class=nolink><font class=red>** NOTE **</font><br>To close this window and return to your Store Front Cart, click here at anytime...</font>\"\n";
	print " 	nNews[1][\"link\"]=\"#\"\n";
	print " 	nNews[1][\"target\"]=\"_self\"\n";
	print " 	nNews[1][\"script\"]=\"window.close();\"\n";

}
else {
	$Welcome = "<font class=nolink><font class=red>Welcome to the Store Front Configuration Viewer</font><br>We hope you enjoy your stay and we welcome you, your friends and collegues to our site...</font></font>";
	print " 	nNews[0]=new Array()\n";
	print " 	nNews[0][\"text\"]=\"<font class=nolink><font class=red>** Keep in Mind **</font><br>You cannot re-configure this system, yet you can always re-configure any system in our inventory...</font>\"\n";
	print " 	nNews[0][\"link\"]=\"javascript:void(0);\"\n";
	print " 	nNews[0][\"target\"]=\"_self\"\n";
	print " 	nNews[0][\"script\"]=\"void(0);\"\n";
	print " 	nNews[1]=new Array()\n";
	print " 	nNews[1][\"text\"]=\"<font class=nolink><font class=red>Welcome to the Store Front Configuration Viewer</font><br>We hope you enjoy your stay and we welcome you, your friends and collegues to our site...</font></font>\"\n";
	print " 	nNews[1][\"link\"]=\"javascript:void(0);\"\n";
	print " 	nNews[1][\"target\"]=\"_self\"\n";
	print " 	nNews[1][\"script\"]=\"void(0);\"\n";
}

{
print <<EOF

</script>
<base href="http://www.rhomberg.com/systemConfigurator/">
</head>
<body bgcolor="#ffffff" text="#8F8FAB" leftmargin="0" topmargin="0" marginwidth="0" scroll="yes" marginheight="0" $NSPrinter>
<br>
<table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
<tr height="40">
<td rowspan="2" width="15%" align="left" valign="top"><a href="http://www.rhomberg.com/systemConfigurator/"><img src="http://www.rhomberg.com/systemConfigurator/Mailbox/images/top_cm_logo.jpg" width="116" height="37" border="0"></a></td>
<td rowspan="2" align="center" valign="bottom" width="30%"><div id="divNewsCont"><div id="divNews">$Welcome</div></div></td>
<td width="55%" align="right" valign="bottom"><img src="http://www.rhomberg.com/systemConfigurator/Mailbox/images/god_bless_america.gif" width="118" height="35"></td>
</tr>
<tr><td colspan="3" width="100%" bgcolor="#FFFFFF" height="5"><img src="http://www.rhomberg.com/systemConfigurator/Mailbox/images/spacer.gif" width="2" height="5"></td></tr>
<tr><td colspan="3" width="100%" bgcolor="#8F8FAB" height="2"><img src="http://www.rhomberg.com/systemConfigurator/Mailbox/images/spacer.gif" width="2" height="2"></td></tr>
<tr><td colspan="3" width="100%" bgcolor="#FFFFFF" height="2"><img src="http://www.rhomberg.com/systemConfigurator/Mailbox/images/spacer.gif" width="2" height="2"></td></tr>
</table>
<table width="95%" align="center" cellspacing="0" cellpadding="0" border="1" bordercolor="#8F8FAB" class="comtableborder"><tr><td width="100%" valign="top">

<table width="$tablewidth" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td align="center" valign="middle" width="$tablewidth" height="25"> 
      <table width="$tablewidth" border="0" cellspacing="0" cellpadding="0" background="images/tables/topbar.jpg" height="24">
        <tr> 
          <td width="$t1"><img src="images/tables/topbar_left.jpg" width="5" height="24"></td>
          <td width="$t2"><nobr><font class="btext">&nbsp;&nbsp;<b>$MainTitle</b></font></nobr></td>
          <td width="$t3" align="center" valign="top">&nbsp;</td>
          <td width="$t4" align="center" valign="top"><a href="javascript:void(0);" onClick="javascript:printPage('stank_vconfig.html','CID','$CID');" onMouseOver="javascript:imageOnDHTML('printit','ov');" onMouseOut="javascript:imageOffDHTML('printit','off');"><img src="images/tables/but_printit_off.gif" width="67" height="21" name="printit" border="0"></a></td>
          <td width="$t1" align="left" valign="top"><img src="images/tables/topbar_right.jpg" width="5" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr> 
    <td align="center"> 
      <table width="$tablewidth" border="0" cellspacing="0" cellpadding="0" height="30">
        <tr align="center"> 
          <td width="20%" align="left"><img src="images/tables/icon_back_off.gif" width="60" height="20" name="back" border="0"></td>
          <td width="16%"><img src="images/tables/but_configureit_dn.gif" width="81" height="20" name="configureit" border="0"></td>
          <td width="16%"><img src="images/tables/but_techspecs_dn.gif" width="77" height="20" name="techspecs" border="0"></td>
          <td width="16%"><img src="images/tables/but_sysdrivers_dn.gif" width="78" height="20" name="sysdrivers" border="0"></td>
          <td width="16%"><img src="images/tables/but_lphoto_dn.gif" width="75" height="20" name="lphoto" border="0"></td>
          <td width="16%"><img src="images/tables/but_multimedia_dn.gif" width="73" height="20" name="sysmedia" border="0"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr> 
    <td valign="top"> 
      <table width="$tablewidth" border="0" cellspacing="1" cellpadding="0" align="center">
        <tr> 
          <td align="center" valign="top" height="150" width="$t5">
		  <table width="100%" align="center" border="0" cellpadding="0" cellspacing="0">
		  <tr>
		  <td width="40%" align="right" valign="middle">$CARTITLink</td>
		  <td width="20%" align="center" valign="middle">&nbsp;</td>
		  <td width="40%" align="left" valign="middle">$RECONFIGLink</td>
		  </tr>
		  </table>
		  <font class="stankprice"><br><font class=\"stankprice\"><center>System's Price<br><b>\$$TotalPrice</b></center></font><img src="/dbimages/prod_common/$SmallImageN" width="165" height="100" vspace="20" border="0" alt="$SmallImageD"></font>
            <table width="100%" cellspacing="1" cellpadding="0" bgcolor="#FFFFFF">
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="0" bgcolor="#F2F2F7" class="stankth" height="18" $border>
                    <tr> 
                      <td align="center"><font class="btext"><b>Trusted Performance By</b></font></td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="0" class="stankth" $border>
                    <tr> 
                      <td width="5%">&nbsp;</td><td align="center" width="90%"><font class="btext">
					  
EOF
}

@losProductos = split(/,,,,,/, $lePIDs);
foreach $elProducto (@losProductos) {
	@splitItem = split(/-----/, $elProducto);	
	$MiCate = $splitItem[0];
	$MiNume = $splitItem[1];
	my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$MiNume'");
	$sth->execute or die "Unable to execute query\n";
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$Compania = $row[6];
		$ItemName = $row[11];
		$Description = $row[12];
		if ($Compania ne "" && $Compania ne " " && $Compania ne "NONE") { push(@Companias,"$Compania"); }
		if ($row[16] ne "" && $row[16] ne " ") { push(@emblems, "$row[16]"); }
		push(@theItems, "$MiCate-----$MiNume-----$ItemName-----$Description");
	}
	$sth->finish;
}

foreach $Company (@Companias) {
	my $sth = $dbh->prepare("SELECT * FROM MFGs WHERE ManufacturerID='$Company'");
	$sth->execute or die "Unable to execute query\n";
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$MuaName = $row[1];
		$SImage = $row[18];
		if ($Company ne "" && $Company ne $LastCompany) { push(@Emblems,"$Company,,,,,$MuaName,,,,,$SImage"); $LastCompany = $Company; }
	}
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
}

foreach $EmblemIt (@Emblems) {
	@EsteEmb = split(/,,,,,/, $EmblemIt);
	$MuaCompany = $EsteEmb[0];
	$MuaName = $EsteEmb[1];
	$MuaSImage = $EsteEmb[2];
	
	my $sth = $dbh->prepare("SELECT * FROM Images WHERE ImageID='$MuaSImage'");
	$sth->execute or die "Unable to execute query\n";
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$InnerURL = $row[6];
		if ($lastImage ne "$InnerURL") { print "<br><img src=\"/$InnerURL\" border=\"0\"><br>$MuaName\<br><br><br>"; }
		$lastImage = $InnerURL;
	}
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
}
                   
{
print <<EOF

						<br></font></td><td width="5%">&nbsp;</td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
          <td valign="top" width="$t6"> 
            <table width="100%" cellspacing="1" cellpadding="0" bgcolor="#FFFFFF">
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="0" bgcolor="#F2F2F7" class="stankth" height="18" $border>
                    <tr> 
                      <td align="center"><font class="btext"><b>System Specifications</b></font></td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="2" class="stankth" $border>
                    <tr> 
                      <td> 

EOF
}

$SCuenta=0;
foreach $anItem (@theItems) {
	@splitCosas = split(/-----/, $anItem);	
	$Category = $splitCosas[0];
	$MiNume = $splitCosas[1];
	$MiEsteNombre = $splitCosas[2];
	$ItsDesc = $splitCosas[3];

	##--->> REFORMAT INCOMING DATA FOR PARSING
	$DCount = "0";
	@DescCount = split(//, $ItsDesc);
	foreach $DescDesc (@DescCount) { 
	$DCount++; 
		if ($DCount >= "50" && ($DescDesc eq "." || $DescDesc eq "!")) { 
			$ItsDesc = substr($ItsDesc, 0, $DCount); 
		} 
	}
	##--->> REFORMAT INCOMING DATA FOR PARSING
	$NCount = "0";
	@NameCount = split(//, $MiName);
	foreach $NameName (@NameCount) { 
	$NCount++; 
		if ($NCount >= "35" && $NameName eq " ") { 
			$MiEsteNombre = substr($MiEsteNombre, 0, $NCount); 
		} 
	}

	if ($SCuenta ne "0" && $lastCate ne "$Category") { print "<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" bgcolor=\"#F2F2F7\"><tr><tr><td width=\"100%\" height=\"10\"><font size=\"-4\" face=\"verdana,arial,helvetica\">&nbsp;</font></td></tr></table><hr width=\"65%\" align=\"center\" size=\"1\" color=\"#333366\">"; }
	
	## check categories
	if ($lastCate ne "$Category") { 
		print "<table width=\"100%\" border=\"0\" bordercolor=\"#FFFFFF\" cellspacing=\"0\" cellpadding=\"0\" bgcolor=\"#F2F2F7\"><tr><td height=\"20\" width=\"90%\" ><font class=\"btext4\">&nbsp;<b>$Category</b></font></td></tr><tr><td width=\"90%\" align=\"right\"><table width=\"95%\" border=\"0\" cellspacing=\"0\" cellpadding=\"3\"><tr><td colspan=\"2\" width=\"95%\" height=\"15\" bgcolor=\"#FFFFFF\"><font class=\"btext3\"><a href=\"stank_viewprod.html?CMPartNum=$MiNume&ComingFrom=vconfig&OGPart=$leCID&InnerLink=1\" onMouseOver=\"javascript:imageOnDHTML2('I_$SCuenta','info','ov');\" onMouseOut=\"javascript:imageOffDHTML2('I_$SCuenta','info','off');\">$MiEsteNombre</a></font></td><td rowspan=\"2\" width=\"5%\" height=\"15\" align=\"center\" valign=\"top\"><a href=\"stank_viewprod.html?CMPartNum=$MiNume&ComingFrom=vconfig&OGPart=$leCID\" onMouseOver=\"javascript:imageOnDHTML2('I_$SCuenta','info','ov');\" onMouseOut=\"javascript:imageOffDHTML2('I_$SCuenta','info','off');\"><img src=\"images/db/but_info_off.gif\" width=\"12\" height=\"12\" vspace=\"5\" border=\"0\" name=\"I_$SCuenta\"></a></td></tr><tr><td width=\"4%\" bgcolor=\"#FFFFFF\">&nbsp;</td><td width=\"91%\" bgcolor=\"#FFFFFF\"><font class=\"btext3\">$ItsDesc</font></td></tr></table></td></tr></table>"; 
	}
	else {
		print "<table width=\"100%\" border=\"0\" bordercolor=\"#FFFFFF\" cellspacing=\"0\" cellpadding=\"0\" bgcolor=\"#F2F2F7\"><tr><td height=\"1\" width=\"90%\"><img src=\"images/spacer.gif\" width=\"1\" height=\"1\"></td></tr><tr><td width=\"90%\" align=\"right\"><table width=\"95%\" border=\"0\" cellspacing=\"0\" cellpadding=\"3\"><tr><td colspan=\"2\" width=\"95%\" height=\"15\" bgcolor=\"#FFFFFF\"><a href=\"stank_viewprod.html?CMPartNum=$MiNume&ComingFrom=vconfig&OGPart=$leCID&InnerLink=1\" onMouseOver=\"javascript:imageOnDHTML2('I_$SCuenta','info','ov');\" onMouseOut=\"javascript:imageOffDHTML2('I_$SCuenta','info','off');\"><font class=\"btext3\">$MiEsteNombre</font></a></td><td rowspan=\"2\" width=\"5%\" height=\"15\" align=\"center\" valign=\"top\"><a href=\"stank_viewprod.html?CMPartNum=$MiNume&ComingFrom=vconfig&OGPart=$leCID\" onMouseOver=\"javascript:imageOnDHTML2('I_$SCuenta','info','ov');\" onMouseOut=\"javascript:imageOffDHTML2('I_$SCuenta','info','off');\"><img src=\"images/db/but_info_off.gif\" width=\"12\" height=\"12\" vspace=\"5\" border=\"0\" name=\"I_$SCuenta\"></a></td></tr><tr><td width=\"4%\" bgcolor=\"#FFFFFF\">&nbsp;</td><td width=\"91%\" bgcolor=\"#FFFFFF\"><font class=\"btext3\">$ItsDesc</font></td></tr></table></td></tr></table>"; 
	}
	$lastCate = "$Category";

$SCuenta++;
}

{
print <<EOF

<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" bgcolor=\"#F2F2F7\"><tr><tr><td width=\"100%\" height=\"10\"><font size=\"-4\" face=\"verdana,arial,helvetica\">&nbsp;</font></td></tr></table>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>

    </td>
  </tr>
</table>

<table width="$tablewidth" border="0" cellspacing="0" cellpadding="0"><tr><td align="center" width="$tablewidth"> 
$STANKLEGAL
</td></tr></table>

<script language="Javascript" src="js/ticker.js"></script>

</body>
</html>

EOF
}
exit;
}

## -------------->>> IF USER IS GOOD AND CID IS PASSED
sub baduser {
	print "Content-type: text/html\n\n";
	print "<script language=\"Javascript\">alert('Sorry, you cannot view that configuration...');location.href=\"index.html\";</script>";	
exit;
}