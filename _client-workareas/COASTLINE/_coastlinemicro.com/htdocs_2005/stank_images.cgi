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

if (($browser =~ "Mozilla/" && $browser =~ "6.") || $browser =~ "Netscape6") { $tablewidth = "100%"; $t1 = "5"; $t2 = "64%"; $t3 = "18%"; $t4 = "18%"; $t5 = "100%"; }	
else { $tablewidth = "470"; $t1 = "5"; $t2 = "339"; $t3 = "79"; $t4 = "42"; $t5 = "470"; }
if ($browser =~ "Mozilla/4.7") { $border = "border=\"1\" bordercolor=\"#333366\""; }

if ($browser =~ "MSIE 5.0" || $browser =~ "MSIE 5.5" || $browser =~ "Mozilla/4.7" || $browser =~ "MSIE 4.0") { $StartURLer="javascript:void(0);\" onClick=\"javascript:window.open"; $EndURLer=",'EMAILIT','width=485,height=590');";}
else { $StartURLer="javascript:trigger"; $EndURLer=");";}

$STANKLEGAL = `cat stank_legal.nsf`;

## ----------------->>> Must Have CMPartNum!
if ($FORM{'CMPartNum'}) {
$CMPartNum = "$FORM{'CMPartNum'}";

if ($FORM{'ThisOne'}) { $ThisOne = "$FORM{'ThisOne'}"; }
else { $ThisOne = "1"; }

## ----------------->>> BACK BUTTON OR NO BACK BUTTON?
$ComingFrom = $FORM{'ComingFrom'};
if ($FORM{'ComingFrom'}) { $GoBack = "<a href=\"javascript:trigger('stank_$ComingFrom\.html?CMPartNum=$CMPartNum');\"><img src=\"images/tables/icon_back_on.gif\" width=\"60\" height=\"20\" name=\"back\" border=\"0\"></a>"; }
else { $GoBack = "<img src=\"images/tables/icon_back_off.gif\" width=\"60\" height=\"20\" name=\"back\" border=\"0\">"; }

##----------->>> Grab PRODUCTS STUFF
use DBI;
my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>coastline</b>\n"; 
$dbh->{RaiseError} = 1; 
my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$CMPartNum'");
$sth->execute or die "Unable to execute query\n";
my @row;
while(@row = $sth->fetchrow_array) { 
	$SavedMediaCode = $row[4];
	$SavedPricingClass = $row[10];
	$SavedItemName = $row[11];
	$SavedTechSpecs = $row[13];
	$SavedLargeLogo = $row[18];
	if ($SavedLargeLogo =~ ",") {
		@Images = split(",", $SavedLargeLogo);
	}
	else { push (@Images, "$SavedLargeLogo"); }
}
$sth->execute or die "Unable to execute query\n"; 
$sth->finish;

## ---------->>> Grab system IMAGE information
$count=0;
foreach $Image (@Images) {
	my $sth = $dbh->prepare("SELECT * FROM Images WHERE ImageID='$Image'");
	$sth->execute or die "Unable to execute query\n";
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$SavedFileName = $row[3];
		$SavedDesc = $row[8];
		push(@LargeImages, "$SavedFileName-----$SavedDesc");
		$count++;
	}
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
}
## ----------->>> here we got the actual count of large images for this product in system
$RealICount = "$count";
$ICount=0;
foreach $LargeImage (@LargeImages) {
	$ICount++;
	@ThyIStuff = split("-----", $LargeImage);
	if ($ThisOne == $ICount) {
		$CurrImage = "<img src=\"/dbimages/prod_common/$ThyIStuff[0]\" border=\"0\" width=\"250\" height=\"250\" alt=\"$SavedItemName\">";
		$CurrDesc = "$SavedItemName";
		if ($ICount ne "1") { $PrevCount = $ICount - 1; $PrevImage = "<font class=\"ctext\">&nbsp;&nbsp;< < < <a href=\"javascript:trigger('stank_images.html?CMPartNum=$CMPartNum&ThisOne=$PrevCount&ComingFrom=$ComingFrom');\"><font class=\"ctext2\">Previous</font></a></font>"; }
		else { $PrevImage = "<font class=\"ctext\">&nbsp;&nbsp;< < < Previous</font>"; }
		if ($ICount ne $RealICount && $RealICount ne "1") { $NextCount = $ICount + 1; $NextImage = "<font class=\"ctext\"><a href=\"javascript:trigger('stank_images.html?CMPartNum=$CMPartNum&ThisOne=$NextCount&ComingFrom=$ComingFrom');\"><font class=\"ctext2\">Next</font></a> > > >&nbsp;&nbsp;</font>"; }
		else { $NextImage = "<font class=\"ctext\">Next > > >&nbsp;&nbsp;</font>"; }
		$WhatofWhat = "<font class=\"ctext\"><b>$ICount&nbsp;&nbsp;of&nbsp;&nbsp;$RealICount</b></font>";		
	}
}


##----------->>> Grab SYSTEMS INFO
my $sth = $dbh->prepare("SELECT * FROM Systems WHERE Parent='$CMPartNum'");
$sth->execute or die "Unable to execute query\n"; 
my @row;
while(@row = $sth->fetchrow_array) { 
	$SavedCMSeries = $row[2];
	$SavedReconfig = $row[3];
}
$sth->execute or die "Unable to execute query\n"; 
$sth->finish;


## MULTIMEDIA
if ($SavedMediaCode ne "") { $SysMedia = "<a href=\"javascript:trigger('stank_media.html?MyCode=$SavedMediaCode&ComingFrom=$ComingFrom');\" onMouseOver=\"javascript:imageOnDHTML('multimedia','ov');\" onMouseOut=\"javascript:imageOffDHTML('multimedia','off');\"><img src=\"images/tables/but_multimedia_off.gif\" width=\"73\" height=\"20\" name=\"multimedia\" border=\"0\"></a>"; }
elsif ($SavedPricingClass ne "Desktop" || $SavedPricingClass ne "Notebook" || $SavedPricingClass ne "Server") { $SysMedia = "<img src=\"images/tables/but_multimedia_dn.gif\" width=\"73\" height=\"20\" name=\"multimedia\" border=\"0\">"; }
else { $SysMedia = "<img src=\"images/tables/but_multimedia_dn.gif\" width=\"73\" height=\"20\" name=\"multimedia\" border=\"0\">"; }

## RECONFIGURABLE?
if ($SavedReconfig eq "Y") { $ConfigIT = "<a href=\"$StartURLer('stank_reconfig.html?CMPartNum=$CMPartNum&ComingFrom=$ComingFrom'$EndURLer\" onMouseOver=\"javascript:imageOnDHTML('configureit','ov');\" onMouseOut=\"javascript:imageOffDHTML('configureit','off');\"><img src=\"images/tables/but_configureit_off.gif\" width=\"81\" height=\"20\" name=\"configureit\" border=\"0\"></a>"; }
elsif ($SavedPricingClass ne "Desktop" || $SavedPricingClass ne "Notebook" || $SavedPricingClass ne "Server") { $ConfigIT = "<img src=\"images/tables/but_configureit_dn.gif\" width=\"81\" height=\"20\" name=\"configureit\" border=\"0\">"; }
else { $ConfigIT = "<img src=\"images/tables/but_configureit_dn.gif\" width=\"81\" height=\"20\" name=\"configureit\" border=\"0\">"; }

## SYSTEM DRIVERS ONLY FOR SYSTEMS AND TECHSPECS ARE DIFFERENT FOR KITS, SYS AND PROD
if ($SavedItemName =~ "mdlschool" || $SavedItemName =~ "MDLSCHOOL") { 
	$LESysDrivers = "<a href=\"javascript:trigger('stank_sysdrivers.html?CMPartNum=$CMPartNum&ComingFrom=$ComingFrom');\" onMouseOver=\"javascript:imageOnDHTML('sysdrivers','ov');\" onMouseOut=\"javascript:imageOffDHTML('sysdrivers','off');\"><img src=\"images/tables/but_sysdrivers_off.gif\" width=\"78\" height=\"20\" name=\"sysdrivers\" border=\"0\"></a>"; 
	$LETechSpecs = "<a href=\"javascript:trigger('stank_techspecs.html?CMPartNum=$CMPartNum&ComingFrom=$ComingFrom');\" onMouseOver=\"javascript:imageOnDHTML('techspecs','ov');\" onMouseOut=\"javascript:imageOffDHTML('techspecs','off');\"><img src=\"images/tables/but_techspecs_off.gif\" width=\"77\" height=\"20\" name=\"techspecs\" border=\"0\"></a>"; 
	$EmailIT = "&nbsp;";
}
elsif ($SavedPricingClass eq "Desktop" || $SavedPricingClass eq "Notebook" || $SavedPricingClass eq "Server") { 
	$LESysDrivers = "<a href=\"javascript:trigger('stank_sysdrivers.html?CMPartNum=$CMPartNum&ComingFrom=$ComingFrom');\" onMouseOver=\"javascript:imageOnDHTML('sysdrivers','ov');\" onMouseOut=\"javascript:imageOffDHTML('sysdrivers','off');\"><img src=\"images/tables/but_sysdrivers_off.gif\" width=\"78\" height=\"20\" name=\"sysdrivers\" border=\"0\"></a>"; 
	$LETechSpecs = "<a href=\"javascript:trigger('stank_techspecs.html?CMPartNum=$CMPartNum&ComingFrom=$ComingFrom');\" onMouseOver=\"javascript:imageOnDHTML('techspecs','ov');\" onMouseOut=\"javascript:imageOffDHTML('techspecs','off');\"><img src=\"images/tables/but_techspecs_off.gif\" width=\"77\" height=\"20\" name=\"techspecs\" border=\"0\"></a>"; 
	$EmailIT = "<a href=\"$StartURLer('stank_emailit.cgi?MySubject=$SavedCMSeries&MyTitle=$SavedCMSeries&MyLoad=loadsys&MyData=$CMPartNum&EmailSubject=$SavedItemName'$EndURLer\" onMouseOver=\"javascript:imageOnDHTML('emailit','ov');\" onMouseOut=\"javascript:imageOffDHTML('emailit','off');\"><img src=\"images/tables/but_emailit_off.gif\" width=\"62\" height=\"21\" name=\"emailit\" border=\"0\"></a>";
}
else { 
	if ($SavedTechSpecs ne "" && $SavedTechSpecs ne "NULL" && $SavedTechSpecs ne "NONE" && $SavedTechSpecs ne "None" && $SavedTechSpecs ne "none") { $LETechSpecs = "<a href=\"javascript:trigger('stank_prodspecs.html?CMPartNum=$CMPartNum&ComingFrom=$ComingFrom');\" onMouseOver=\"javascript:imageOnDHTML('techspecs','ov');\" onMouseOut=\"javascript:imageOffDHTML('techspecs','off');\"><img src=\"images/tables/but_techspecs_off.gif\" width=\"77\" height=\"20\" name=\"techspecs\" border=\"0\"></a>"; } 
	else { 	$LETechSpecs = "<img src=\"images/tables/but_techspecs_off.gif\" width=\"77\" height=\"20\" name=\"techspecs\" border=\"0\">"; }
	$LESysDrivers = "<img src=\"images/tables/but_sysdrivers_dn.gif\" width=\"78\" height=\"20\" border=\"0\">"; 
	$EmailIT = "<a href=\"$StartURLer('stank_emailit.cgi?MySubject=products&MyTitle=products&MyLoad=loadprod&MyData=$CMPartNum&EmailSubject=$SavedItemName'$EndURLer\" onMouseOver=\"javascript:imageOnDHTML('emailit','ov');\" onMouseOut=\"javascript:imageOffDHTML('emailit','off');\"><img src=\"images/tables/but_emailit_off.gif\" width=\"62\" height=\"21\" name=\"emailit\" border=\"0\"></a>";
}

##---------------------------->>> IMAGERY FOR OUTPUT
$MainTitle = "$SavedItemName";

##--->> REFORMAT MAINTITLE
$NCount = "0";
@NameCount = split(//, $MainTitle);
foreach $NameName (@NameCount) { 
$NCount++; 
	if ($NCount >= "30" && $NameName eq " ") { 
		$MainTitle = substr($MainTitle, 0, $NCount); 
	}
}


if ($browser =~ "Mozilla/4.7") { $border = "border=\"1\" bordercolor=\"#333366\""; }

if ($FORM{'NSPRINT'}) { $NSPrinter = "onload=\"javascript:printPageNS();\""; }

print "Content-type: text/html\n\n";
{
print <<EOF

<html>
<head>
<title>Company Name</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<STYLE TYPE="text/css">
body { background-color:#ffffff; scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</STYLE>
<LINK REL="STYLESHEET" HREF="common_css.html?anchor=EB0000&anchorov=EB0000&weight=bold&weightov=bold&decor=underline&decorov=underline" Type="text/css">
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
	this.location.href=myurl;
	}
else if (b=="Netscape") {
	mainFrame = parent.frames.botOne;
	mainFrame.frame.loadpage(''+myurl+'');
}
else {
	this.location.href=myurl;
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
    window.open('stank_sysbrowse.html?CMPartNum=$CMPartNum&NSPRINT=1','PRINT','width=485,height=590');
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
<base href="http://www.rhomberg.com/systemConfigurator/">
</head>
<body bgcolor="#ffffff" text="#8F8FAB" leftmargin="0" topmargin="0" marginwidth="0" scroll="yes" marginheight="0" $NSPrinter>
<table width="$tablewidth" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td align="center" valign="middle" width="$tablewidth" height="25"> 
      <table width="$tablewidth" border="0" cellspacing="0" cellpadding="0" background="images/tables/topbar.jpg" height="24">
        <tr> 
          <td width="$t1"><img src="images/tables/topbar_left.jpg" width="5" height="24"></td>
          <td width="$t2"><nobr><font class="btext">&nbsp;&nbsp;<b>$MainTitle</b></font></nobr></td>
          <td width="$t3" align="center" valign="top">$EmailIT</td>
          <td width="$t4" align="center" valign="top"><a href="javascript:void(0);" onClick="javascript:printPage('stank_images.html','CMPartNum','$CMPartNum');" onMouseOver="javascript:imageOnDHTML('printit','ov');" onMouseOut="javascript:imageOffDHTML('printit','off');"><img src="images/tables/but_printit_off.gif" width="67" height="21" name="printit" border="0"></a></td>
          <td width="$t1" align="left" valign="top"><img src="images/tables/topbar_right.jpg" width="5" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr> 
    <td align="center"> 
      <table width="$tablewidth" border="0" cellspacing="0" cellpadding="0" height="30">
        <tr align="center">
          <td width="20%" align="left">$GoBack</td>
		  <td width="16%">$ConfigIT</td>
          <td width="16%">$LETechSpecs</td>
		  <td width="16%">$LESysDrivers</td>
          <td width="16%"><img src="images/tables/but_lphoto_dn.gif" width="75" height="20" name="lphoto" border="0"></td>
		  <td width="16%">$SysMedia</td>
        </tr>
      </table>
    </td>
  </tr>
  <tr> 
    <td valign="top"> 
      <table width="100%" border="0" cellspacing="1" cellpadding="0" align="center">
        <tr> 
          <td align="center" valign="top" height="150" width="$t5">
<table width="100%" cellspacing="1" cellpadding="0" bgcolor="#FFFFFF">
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="0" bgcolor="#F2F2F7" class="stankth" height="18" $border>
                    <tr>
                      <td align="left" width="25%">&nbsp;</td>
                      <td align="center" width="50%" height="30"><font class="btext"><b>Product Views</b></font></td>
                      <td align="right" width="25%">&nbsp;</td>
                    </tr>
                    <tr> 
                      <td align="left" width="25%">$PrevImage</td>
                      <td align="center" height="25" width="50%">$WhatofWhat</td>
                      <td align="right" width="25%">$NextImage</td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="0" class="stankth" $border>
                    <tr> 
                      <td align="center"><br>
                        $CurrImage<font class="btext3"><br>
                        <br>
                        <b>$CurrDesc</b><br>
                        <br>
                        </font></td>
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

</body>
</html>

EOF
}
exit;
}

## SORRY YALL NO GOOD CALL
else {
$sorry = `cat sorry_nospec.nsf`;

{
print <<EOF

$sorry

EOF
}
exit;
}