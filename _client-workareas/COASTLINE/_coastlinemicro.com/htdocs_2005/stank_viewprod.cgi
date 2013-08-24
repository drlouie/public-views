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

## ----------------->>> Must Have CMPartNum!
if ($FORM{'CMPartNum'}) {
$CMPartNum = "$FORM{'CMPartNum'}";

## ----------------->>> BACK BUTTON OR NO BACK BUTTON?
$ComingFrom = $FORM{'ComingFrom'};
if ($FORM{'ComingFrom'} eq "sysbrowse" || $FORM{'ComingFrom'} eq "viewkit") { $GoBack = "<a href=\"javascript:trigger('stank_$FORM{'ComingFrom'}\.html?CMPartNum=$FORM{'OGPart'}\');\"><img src=\"images/tables/icon_back_on.gif\" width=\"60\" height=\"20\" name=\"back\" border=\"0\"></a>"; }
elsif ($FORM{'ComingFrom'} eq "vconfig") { 
	if ($FORM{'InnerLink'} eq "1") { $InnerLink = "&InnerLink=1"; }
	$topVCONFIG = "<br><table width=\"95%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" align=\"center\"><tr height=\"40\"><td rowspan=\"2\" width=\"15%\" align=\"left\" valign=\"top\"><a href=\"http://www.rhomberg.com/systemConfigurator/\"><img src=\"http://www.rhomberg.com/systemConfigurator/Mailbox/images/top_cm_logo.jpg\" width=\"116\" height=\"37\" border=\"0\"></a></td><td rowspan=\"2\" align=\"center\" valign=\"bottom\" width=\"30%\">&nbsp;</td><td width=\"55%\" align=\"right\" valign=\"bottom\"><img src=\"http://www.rhomberg.com/systemConfigurator/Mailbox/images/god_bless_america.gif\" width=\"118\" height=\"35\"></td></tr><tr><td colspan=\"3\" width=\"100%\" bgcolor=\"#FFFFFF\" height=\"5\"><img src=\"http://www.rhomberg.com/systemConfigurator/Mailbox/images/spacer.gif\" width=\"2\" height=\"5\"></td></tr><tr><td colspan=\"3\" width=\"100%\" bgcolor=\"#8F8FAB\" height=\"2\"><img src=\"http://www.rhomberg.com/systemConfigurator/Mailbox/images/spacer.gif\" width=\"2\" height=\"2\"></td></tr><tr><td colspan=\"3\" width=\"100%\" bgcolor=\"#FFFFFF\" height=\"2\"><img src=\"http://www.rhomberg.com/systemConfigurator/Mailbox/images/spacer.gif\" width=\"2\" height=\"2\"></td></tr></table><table width=\"95%\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\" border=\"1\" bordercolor=\"#8F8FAB\" class=\"comtableborder\"><tr><td width=\"100%\" valign=\"top\">";
	$GoBack = "<a href=\"javascript:trigger('stank_$FORM{'ComingFrom'}\.html?CID=$FORM{'OGPart'}$InnerLink\');\"><img src=\"images/tables/icon_back_on.gif\" width=\"60\" height=\"20\" name=\"back\" border=\"0\"></a>"; 
	$botVCONFIG = "</td></tr></table>";
	## remove the CM logo since this page has a different layout with CM in it already...
	$STANKLEGAL =~ s/cm_logo_small.jpg/spacer.gif/g;
	$STANKLEGAL =~ s/142/1/g;
	$STANKLEGAL =~ s/51/1/g;	
}
else { $GoBack = "<img src=\"images/tables/icon_back_off.gif\" width=\"60\" height=\"20\" name=\"back\" border=\"0\">"; }

##----------->>> Grab PRODUCTS STUFF
use DBI;
my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>coastline</b>\n"; 
$dbh->{RaiseError} = 1; 
$count=0;
my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$CMPartNum'");
$sth->execute or die "Unable to execute query\n";
my @row;
while(@row = $sth->fetchrow_array) { 
	$SavedProductID = $row[0];
	$SavedCMPartNum = $row[1];
	$SavedSYSCode = $row[2];
	$SavedKITCode = $row[3];
	$SavedMediaCode = $row[4];
	$SavedDISTCode = $row[5];
	$SavedMFGCode = $row[6];
	$SavedMFGPartNum = $row[7];
	$SavedMFGProdURL = $row[8];
	$SavedMFGDriverURL = $row[9];
	$SavedPricingClass = $row[10];
	$SavedItemName = $row[11];
	$SavedDescription = $row[12];
	$SavedTechSpecs = $row[13];
	$SavedKeywords = $row[14];
	$SavedSneakPeak = $row[15];
	push(@Emblems, "$row[16]-----EMBLEM");
	push(@Images, "$row[17]-----SMALL");
	$SavedLargeLogo = $row[18];
	$SavedWarranty = $row[19];
	$SavedWeight = $row[20];
	$SavedCost = $row[21];
	$SavedCompPrice = $row[22];
	$SavedRelatedProd = $row[23];
	$SavedAccessories = $row[24];
	$SavedAddedBy = $row[25];
	$SavedAddedOn = $row[26];
	$SavedModifiedBy = $row[27];
	$SavedModifiedBy = $row[28];
	$SavedIngramPartNum = $row[29];
	$SavedTechDataPartNum = $row[30];
	$SavedSynnexPartNum = $row[31];
	## Re-Structure data as necessary
	$AddYear = substr($SavedAddedOn, 0, 2);
	$AddMonth = substr($SavedAddedOn, 2, 2);
	$AddDay = substr($SavedAddedOn, 4, 2);
	$ModYear = substr($SavedModifiedOn, 0, 2);
	$ModMonth = substr($SavedModifiedOn, 2, 2);
	$ModDay = substr($SavedModifiedOn, 4, 2);
	$count++;
}
$sth->execute or die "Unable to execute query\n"; 
$sth->finish;

##----------->>> Grab system IMAGE information
foreach $Image (@Images) {
	@Estos = split(/-----/, $Image);
	$count=0;
	my $sth = $dbh->prepare("SELECT * FROM Images WHERE ImageID='$Estos[0]'");
	$sth->execute or die "Unable to execute query\n";
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$SavedFileName = $row[3];
		$SavedDesc = $row[8];
		if ($Estos[1] eq "LARGE") { push(@LargeImages, "$SavedFileName-----$SavedDesc"); }
		else { $SmallImageN = "$SavedFileName"; $SmallImageD= "$SavedDesc";  }
		$count++;
	}
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
}

##----------->>> GET MFG INFO
my $sth = $dbh->prepare("SELECT * FROM MFGs WHERE ManufacturerID='$SavedMFGCode'");
$sth->execute or die "Unable to execute query\n";
my @row;
while(@row = $sth->fetchrow_array) { 
	$MFGName = $row[1];
	$MFGURL = $row[2];
	$MFGMPhoto = $row[19];
}
$sth->execute or die "Unable to execute query\n"; 
$sth->finish;

##----------->>> Grab system EMBLEM information
foreach $Emblem (@Emblems) {
	@Estas = split(/-----/, $Emblem);
	$count=0;
	my $sth = $dbh->prepare("SELECT * FROM Images WHERE ImageID='$Estas[0]'");
	$sth->execute or die "Unable to execute query\n";
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$InnerURL = $row[6];
		if ($Estas[1] eq "EMBLEM") { push(@LosEmblems, "$InnerURL"); }
		$count++;
	}
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
}

##------------------>>> MEDIUM MFG LOGO
if ($MFGMPhoto ne "") {  

	my $sth = $dbh->prepare("SELECT * FROM Images WHERE ImageID='$MFGMPhoto'");
	$sth->execute or die "Unable to execute query\n";
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$URL = $row[6];
	}
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;

	if ($FORM{'ComingFrom'} ne "vconfig") { $MFGMEDP = "<center><a href=\"javascript:abrete('$MFGURL');\"><img src=\"/$URL\" border=\"0\" vspace=\"5\"></a></center>" }
	else { $MFGMEDP = "<center><img src=\"/$URL\" border=\"0\" vspace=\"5\"></center>" }
}

##------------------>>> MFG PRODUCT URL
if ($SavedMFGProdURL ne "") {
	$MFGPRODURL = "<tr><td width=\"100%\" height=\"15\"><font class=\"btext3\"><b>Product URL<br></b><font class=\"btext\"><a href=\"javascript:abrete('$SavedMFGProdURL');\">$SavedItemName</a></font><br></font></td></tr>";
}

##------------------>>> PRODUCT DRIVER URL
if ($SavedMFGDriverURL ne "") { $MFGDRIVURL = "<tr><td width=\"100%\" height=\"15\"><font class=\"btext3\"><b>Driver Update URL<br></b><font class=\"btext\"><a href=\"javascript:abrete('$SavedMFGDriverURL');\">$SavedItemName</a></font><br></font></td></tr>"; }

if ($SavedTechSpecs ne "" && $SavedTechSpecs ne "NULL" && $SavedTechSpecs ne "NONE" && $SavedTechSpecs ne "None" && $SavedTechSpecs ne "none" && $FORM{'ComingFrom'} ne "sysbrowse" && $FORM{'ComingFrom'} ne "viewkit" && $FORM{'ComingFrom'} ne "vconfig") { $LETechSpecs = "<a href=\"javascript:trigger('stank_prodspecs.html?CMPartNum=$CMPartNum&ComingFrom=viewprod');\" onMouseOver=\"javascript:imageOnDHTML('techspecs','ov');\" onMouseOut=\"javascript:imageOffDHTML('techspecs','off');\"><img src=\"images/tables/but_techspecs_off.gif\" width=\"77\" height=\"20\" name=\"techspecs\" border=\"0\"></a>"; }
else { $LETechSpecs = "<img src=\"images/tables/but_techspecs_dn.gif\" width=\"77\" height=\"20\">"; }

##---------------------------->>> CONFIGURE SYSTEM INFORMATION AND IMAGERY FOR OUTPUT
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

## SMALL/LARGE PHOTO
if ($FORM{'ComingFrom'} eq "vconfig") {
	$LPhoto = "<img src=\"images/tables/but_lphoto_dn.gif\" width=\"75\" height=\"20\" name=\"lphoto\" border=\"0\">"; 	
}

elsif (@LargeImages ne "" && $FORM{'ComingFrom'} ne "sysbrowse" && $FORM{'ComingFrom'} ne "viewkit") { 
	$LPhoto = "<a href=\"javascript:trigger('stank_images.html?CMPartNum=$CMPartNum&ComingFrom=viewprod');\" onMouseOver=\"javascript:imageOnDHTML('lphoto','ov');\" onMouseOut=\"javascript:imageOffDHTML('lphoto','off');\"><img src=\"images/tables/but_lphoto_off.gif\" width=\"75\" height=\"20\" name=\"lphoto\" border=\"0\"></a>"; $TriggerPhoto = "javascript:trigger('stank_images.html?CMPartNum=$CMPartNum&ComingFrom=viewprod');"; 
}
elsif ($FORM{'ComingFrom'} ne "sysbrowse" && $FORM{'ComingFrom'} ne "viewkit") { 
	$LPhoto = "<a href=\"javascript:trigger('stank_images.html?CMPartNum=$CMPartNum&ComingFrom=viewprod');\" onMouseOver=\"javascript:imageOnDHTML('lphoto','ov');\" onMouseOut=\"javascript:imageOffDHTML('lphoto','off');\"><img src=\"images/tables/but_lphoto_off.gif\" width=\"75\" height=\"20\" name=\"lphoto\" border=\"0\"></a>"; $TriggerPhoto = "javascript:trigger('stank_images.html?CMPartNum=$CMPartNum&ComingFrom=viewprod');"; 
}
else { 
	$LPhoto = "<img src=\"images/tables/but_lphoto_dn.gif\" width=\"75\" height=\"20\">"; 
}

if ($SmallImageN ne "") { }
else { $SmallImageN = ""; $SmallImageD = ""; }

## is there a small photo available if not give sorry image
if ($SmallImageN ne "") { $SmallPHOTO = "<img src=\"/dbimages/prod_common/$SmallImageN\" width=\"165\" height=\"100\" vspace=\"20\" border=\"0\" alt=\"Click to view large photo(s) of this product.\">"; }
else { $SmallPHOTO = "<img src=\"images/noimage_small.gif\" width=\"165\" height=\"100\" vspace=\"20\" border=\"0\" alt=\"Click to view large photo(s) of this product.\">"; }

if ($FORM{'NSPRINT'}) { $NSPrinter = "onload=\"javascript:printPageNS();\""; }

	$EntireTotal = sprintf("%.2f", $SavedCost);

	## Snif cookie, if present test for logged in status
	require ("cookiesnif.nsp");
	
	if ($Cookies{'Echado'} eq "YES") {

		if ($SavedPricingClass eq "Monitor") { $MyTypo = "$Cookies{'MOV'}"; }
		elsif ($SavedPricingClass eq "Memory") { $MyTypo = "$Cookies{'MYV'}"; }
		elsif ($SavedPricingClass eq "HardDrive") { $MyTypo = "$Cookies{'HDV'}"; }
		elsif ($SavedPricingClass eq "VideoCard") { $MyTypo = "$Cookies{'VDV'}"; }
		elsif ($SavedPricingClass eq "Printer") { $MyTypo = "$Cookies{'PTV'}"; }
		else { $MyTypo = "$Cookies{'PHV'}"; }
		$MyTypo = 100 - $MyTypo;
		if ($MyTypo < 10) { $MyTypo = "." . "0" . "$MyTypo"; }
		else { $MyTypo = ".$MyTypo"; }
		$Markup = ($EntireTotal / $MyTypo);
		$Markup = sprintf("%.2f", $Markup);
		$EntireTotal = $Markup;
	}
	elsif ($Cookies{'UserType'} eq "CMManage" || $Cookies{'UserType'} eq "CMAdmin" || $Cookies{'UserType'} eq "CMSales" || $Cookies{'UserType'} eq "CMUser") {
		$EntireTotal = $EntireTotal;
	}
	else {
		$Markup = ($EntireTotal / .75);
		$Markup = sprintf("%.2f", $Markup);
		$EntireTotal = $Markup;
	}

	$EntireTotal = sprintf("%.2f", $EntireTotal);

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
    window.open('stank_viewprod.html?CMPartNum=$CMPartNum&NSPRINT=1','PRINT','width=470,height=590');
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

function abrete(me) {
	parent.window.open(me);
}
</script>
<base href="http://www.rhomberg.com/systemConfigurator/">
</head>
<body bgcolor="#ffffff" text="#8F8FAB" leftmargin="0" topmargin="0" marginwidth="0" scroll="yes" marginheight="0" $NSPrinter>

$topVCONFIG

<table width="$tablewidth" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td align="center" valign="middle" width="$tablewidth" height="25"> 
      <table width="$tablewidth" border="0" cellspacing="0" cellpadding="0" background="images/tables/topbar.jpg" height="24">
        <tr> 
          <td width="$t1"><img src="images/tables/topbar_left.jpg" width="5" height="24"></td>
          <td width="$t2"><nobr><font class="btext">&nbsp;&nbsp;<b>$MainTitle</b></font></nobr></td>
          <td width="$t3" align="center" valign="top"><a href="$StartURLer('stank_emailit.cgi?MySubject=products&MyTitle=products&MyLoad=loadprod&MyData=$CMPartNum&EmailSubject=$MainTitle'$EndURLer" onMouseOver="javascript:imageOnDHTML('emailit','ov');" onMouseOut="javascript:imageOffDHTML('emailit','off');"><img src="images/tables/but_emailit_off.gif" width="62" height="21" name="emailit" border="0"></a></td>
          <td width="$t4" align="center" valign="top"><a href="javascript:void(0);" onClick="javascript:printPage('stank_viewprod.html','CMPartNum','$CMPartNum');" onMouseOver="javascript:imageOnDHTML('printit','ov');" onMouseOut="javascript:imageOffDHTML('printit','off');"><img src="images/tables/but_printit_off.gif" width="67" height="21" name="printit" border="0"></a></td>
          <td width="$t1" align="right" valign="top"><img src="images/tables/topbar_right.jpg" width="5" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr> 
    <td align="center"> 
      <table width="$tablewidth" border="0" cellspacing="0" cellpadding="0" height="30">
        <tr align="center"> 
          <td width="20%" align="left">$GoBack</td>
		  <td width="16%"><img src="images/tables/but_configureit_dn.gif" width="81" height="20" border="0"></td>
          <td width="16%">$LETechSpecs</td>
          <td width="16%"><img src="images/tables/but_sysdrivers_dn.gif" width="78" height="20" border="0"></td>
          <td width="16%">$LPhoto</td>
          <td width="16%"><img src="images/tables/but_multimedia_dn.gif" width="73" height="20" border="0"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr> 
    <td valign="top"> 
      <table width="$tablewidth" border="0" cellspacing="1" cellpadding="0" align="center">
        <tr> 
          <td align="center" valign="top" height="150" width="$t5"><font class="stankprice"><br>$SmallPHOTO
            <table width="100%" cellspacing="1" cellpadding="0" bgcolor="#FFFFFF">
              <tr> 
                <td align="center"> 
	

EOF
}

foreach $InnerURL (@LosEmblems) {

	if ($MFGPRODURL && $FORM{'ComingFrom'} ne "vconfig") { print "<br><a href=\"javascript:abrete('$SavedMFGProdURL');\"><img src=\"/$InnerURL\" border=\"0\"></a><br><br>"; }
	else { print "<br><img src=\"/$InnerURL\" border=\"0\"><br><br>"; }
}
                        
{
print <<EOF

                </td>
              </tr>
            </table>
          </td>
          <td valign="top" width="$t6"> 
$MFGMEDP
            <table width="100%" cellspacing="1" cellpadding="0" bgcolor="#FFFFFF">
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="0" bgcolor="#F2F2F7" class="stankth" height="18" $border>
                    <tr> 
                      <td align="center"><font class="btext"><b>Product Description</b></font></td>
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

	print "<table width=\"100%\" border=\"0\" bordercolor=\"#FFFFFF\" cellspacing=\"0\" cellpadding=\"0\" bgcolor=\"#F2F2F7\">";
	print "<tr>";
	print "<td colspan=\"2\" height=\"5\"><font face=\"verdana,arial,helvetica\" size=\"-4\">&nbsp;</font></td>";
	print "<td rowspan=\"2\" width=\"10%\" align=\"center\" valign=\"top\">&nbsp;</td>";
	print "</tr><tr><td width=\"90%\" align=\"right\">";
	print "<table width=\"95%\" border=\"0\" cellspacing=\"0\" cellpadding=\"10\" bgcolor=\"#FFFFFF\"><tr><td width=\"100%\" height=\"15\"><font class=\"btext3\"><b>Type<br></b>$SavedPricingClass<br></font></td></tr><tr><td width=\"100%\" height=\"15\"><font class=\"btext3\"><b>Manufacturer<br></b><font class=\"btext\"><a href=\"javascript:abrete('$MFGURL');\">$MFGName</a></font><br></font></td></tr>$MFGPRODURL$MFGDRIVURL<tr><td width=\"100%\"><font class=\"btext3\"><b>Description<br></b>$SavedDescription</font></td></tr></table>";
	print "</td></tr></table>";

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

$botVCONFIG

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