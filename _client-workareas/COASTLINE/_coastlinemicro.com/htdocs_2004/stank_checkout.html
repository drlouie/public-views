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

## Snif cookie, if present test for logged in status
require ("cookiesnif.nsp");

## ----------------->>> Must Be Logged In!
if ($Cookies{'Echado'} eq "YES") {

##----------->>> CONNECT TO DB
use DBI;
my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
$dbh->{RaiseError} = 1; 

$count=0;
if ($Cookies{'CNFIGS'} ne "") {

	@EstosCNFIGS = split(/,/, $Cookies{'CNFIGS'});
	foreach $EsteCNFIG (@EstosCNFIGS) {
		@muaCF = split(/-----/, $EsteCNFIG);
		$ConfigID = "$muaCF[0]";
		$laCuenta = "$muaCF[1]";

		## GET CONFIGURATION INFORMATION
		my $sth = $dbh->prepare("SELECT * FROM Configs WHERE ConfigID='$ConfigID'");
		$sth->execute or die "Unable to execute query\n";
		my @row;
		while(@row = $sth->fetchrow_array) {
			$Parent = $row[1];
			$CMSeries = $row[3];
			$ProductIDs = $row[4];
			$TotalPrice = $row[7];
			$TotalWeight = $row[8];
			$CreatedOn = $row[9];
			push(@Configs,"$Parent=====$CMSeries=====$ProductIDs=====$TotalPrice=====$TotalWeight=====$CreatedOn=====$ConfigID=====$laCuenta");
			## how many calls for this config? IF more than one tally in as many as there are specified
			if ($laCuenta eq "1") { push(@losPrecios,$TotalPrice); }
			else {
				foreach (1 .. $laCuenta) {
					push(@losPrecios,$TotalPrice);
				}
			}
			$count++;
		}
		$sth->finish;
	}
}

## add cart totals
$PCount=0;
foreach $elPrecio (@losPrecios) {
$PCount++;
	if ($PCount eq "1") { $EntireTotal = $elPrecio; }
	else { $EntireTotal = $EntireTotal + $elPrecio; }
	$EntireTotal = sprintf("%.2f", $EntireTotal);
}

## NS PRINT FUNCTION
if ($FORM{'NSPRINT'}) { $NSPrinter = "onload=\"javascript:printPageNS();\""; }

$MainTitle = "Shark Tank&#153; Checkout Counter";

print "Content-type: text/html\n\n";

{
print <<EOF

<html>
<head>
<title>Coastline Micro Inc.</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="common_css.html?anchor=333366&anchorov=EB0000&weight=normal&weightov=normal&decor=underline&decorov=underline" Type="text/css">
<STYLE TYPE="text/css">
body { background-color:#ffffff; scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</STYLE>
<script language="Javascript" src="js/mousetable.js"></script>
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


//Called from search1.swf from all browsers except for NS4
function pushIt() {
	document.leCOut.submit();
}
//-->
</script>
<!--FOLLOWING EXTERNAL SCRIPT IS USED FOR BROWSER TESTING AND IS INTEGRAL PART OF FLASH COMPONENTS-->
<script language="JavaScript" src="js/dynlayer.js"></script>
<!--END-->
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
function abrete(me) {
	parent.window.open(me,'VCONFIG','width=600,height=600');
}

//-->
</script>
<base href="http://www.coastlinemicro.com/">
</head>
<body bgcolor="#ffffff" text="#8F8FAB" leftmargin="0" topmargin="0" marginwidth="0" scroll="yes" marginheight="0" onLoad="javascript:runShip();">
<table width="$tablewidth" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td align="center" valign="middle" width="$tablewidth" height="25"> 
      <table width="$tablewidth" border="0" cellspacing="0" cellpadding="0" background="images/tables/topbar.jpg" height="24">
        <tr> 
          <td width="$t1"><img src="images/tables/topbar_left.jpg" width="5" height="24"></td>
          <td width="$t2"><nobr><font class="btext">&nbsp;&nbsp;<b>$MainTitle</b></font></nobr></td>
          <td width="$t3" align="center" valign="top">&nbsp;</td>
          <td width="$t4" align="center" valign="top">&nbsp;</td>
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
          <td valign="top" width="$t5"> 
            <table width="95%" align="center" cellspacing="1" cellpadding="0" bgcolor="#FFFFFF">
              <tr> 
                <td> 
                  			<table width="100%" cellspacing="0" cellpadding="1" bgcolor="#FFFFFF" class="stankth" height="25" $border>
                    			<tr> 
	                      		<td width="100%" align="right">
<SCRIPT language="Javascript">
//Calling for search1.swf for all browsers except for NS4, it gets a submit image button
if (is.ns4) {
document.write('<input type=\"image\" name=\"Submit\" border=\"0\" src=\"images/newones/ns4_submitorder.jpg\" width=\"423\" height=\"25\">');
}
else {
document.write('<object classid=\"clsid:D27CDB6E-AE6D-11cf-96B8-444553540000\" width=\"423\" height=\"25\" codebase=\"http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=4,0,2,0\">');
document.write('<param name=\"MOVIE\" value=\"flash/submitorder_line.swf\"><param name=\"PLAY\" value=\"true\"><param name=\"LOOP\" value=\"false\"><param name=\"QUALITY\" value=\"high\"><param name=\"MENU\" value=\"false\">');
document.write('<embed src=\"flash/submitorder_line.swf\" width=\"423\" height=\"25\" play=\"true\" loop=\"false\" quality=\"high\" menu=\"false\" type=\"application/x-shockwave-flash\" pluginspage=\"http://www.macromedia.com/shockwave/download/index.html?P1_Prod_Version=ShockwaveFlash\"></embed>');
document.write('</object>');
}
</SCRIPT>
								</td>
    	                		</tr>
        	          		</table>
                </td>
              </tr>
              <tr> 
                <td> 
                  <table width="100%" align="center" cellspacing="0" cellpadding="5" class="stankth" $border>
                    <tr> 
                      <td valign="top">


					  <font class=\"btext\"><b>Please review and submit your order</b><br>Your company's default Shipping and Payment information is being used to process this order. To change any of this information simply use the links and/or buttons to do so. <b>Keep in mind:</b> Shipping information is controlled by <b>$Cookies{'CoNo'}'s</b> administrative user, your company's master user.<br></font>
					</td></tr>
                    <tr> 
                      <td valign="top">					  
<form name="leCOut" method="Post" action="">

EOF
}

if (@Configs) {

## Get list of Shipping Addresses for this company
$Cuentame = 0;
my $sth = $dbh->prepare("SELECT * FROM ShipDests WHERE CMCustNum='$Cookies{'CeeEmmNo'}' ORDER BY AddedOn ASC");
$sth->execute or die "Unable to execute query\n"; 
my @row;
while(@row = $sth->fetchrow_array) { 
	$Cuentame++;
	$ShipID = $row[0];
	$Courier = $row[2];
	$ShipType = $row[3];
	$Contact = $row[5];
	$Address1 = $row[10];
	$Address2 = $row[11];
	$City = $row[12];
	$State = $row[13];
	$Zip = $row[14];
	$AddedOn = $row[15];
	
	if ($ShipType eq "1DM") { $ShipTipo = "Next Day Air Early AM"; }
	elsif ($ShipType eq "1DA") { $ShipTipo = "Next Day Air"; }
	elsif ($ShipType eq "2DA") { $ShipTipo = "2nd Day Air"; }
	elsif ($ShipType eq "GNDRES") { $ShipTipo = "Ground Residential"; }
	elsif ($ShipType eq "GNDCOM") { $ShipTipo = "Ground Commercial"; }

	require ("ups_perpound.nsp");
	
	push(@allShips, "$Courier-----$ShipType-----$ShipTipo-----$Contact-----$Address1-----$Address2-----$City-----$State-----$Zip-----$ShipPrice-----$ShipID");
}
$sth->finish;

## ----------------->>> MAKE Shipping fields...
if ($Cuentame eq "1") {
	@myShip = split(/-----/, $allShips[0]);
	$Courier = "$myShip[0]<br>";
	$ShipType = "$myShip[1]";
	$ShipTipo = "$myShip[2]<br>";
	$Contact = "$myShip[3]<br>";
	$Address1 = "$myShip[4]<br>";
	if ($myShip[5] ne "" && $myShip[5] ne " ") { $Address2 = "$myShip[5]<br>"; }
	$City = "$myShip[6]";
	$State = "$myShip[7]";
	$Zip = "$myShip[8]";
	$ShipPrice = "\$$myShip[9]/lb.";
	$PPP = "<input type=\"hidden\" name=\"theWeight\" value=\"\"><input type=\"hidden\" name=\"PPP\" value=\"$myShip[9]\">";
	$MuaID = "$myShip[10]";
}

else {
	print "<script language=\"Javascript\">";	
	print "function runShip() {\n";
	print "var formindex = document.leCOut.ShipDests.selectedIndex; var thisone = document.leCOut.ShipDests.options[formindex].value;\n";
	$ShipSelStart = "<font class=\"btext\"><b>Shipping Destinations --> </b>&nbsp;<select name=\"ShipDests\" size=\"1\" class=\"inputtext\" onChange=\"javascript:runShip();\"></font>";
	$ShipperC = 0;
	$ShipType = "";
	$Zip = "";
	foreach $thyShip (@allShips) {
		$ShipperC++;
		@myShip2 = split(/-----/, $thyShip);
		$Courier = $myShip2[0];
		$ShipType = $myShip2[1];
		$ShipTipo = $myShip2[2];
		$Contact = $myShip2[3];
		$Address1 = $myShip2[4];
		$Address2 = $myShip2[5];
		$City = $myShip2[6];
		$State = $myShip2[7];
		$Zip = $myShip2[8];
		$MuaID = $myShip2[10];

		use lib '.';
		use Business::UPS;
		my $type = "$ShipType";
		my $to = "$Zip";
		my $wgt = "1";
		my ($from,$co) = qw/92618/;
		my ($shipping,$ups_zone,$error) = getUPS($type,$from,$to,$wgt,$co,'', '', '', '', '');
		$error and die "ERROR: $error\n";
		$ShipPrice = "$shipping";
		$UPSZone = "$ups_zone";

		push(@selectShip, "$MuaID-----$City-----$Address1");
		print "if (thisone == \"$MuaID\") {\n";
		print "		document.leCOut.ShipContact.value = \"$Contact\";\n";
		print "		document.leCOut.ShipAddress1.value = \"$Address1\";\n";
		print "		document.leCOut.ShipAddress2.value = \"$Address2\";\n";
		print "		document.leCOut.ShipCity.value = \"$City\";\n";
		print "		document.leCOut.ShipState.value = \"$State\";\n";
		print "		document.leCOut.ShipZip.value = \"$Zip\";\n";
		print "		document.leCOut.ShipCourier.value = \"$Courier\";\n";
		print "		document.leCOut.ShipType.value = \"$ShipTipo\";\n";
		print "		document.leCOut.ShipPrice.value = \"\$$ShipPrice/lb.\";\n";
		print "		document.leCOut.PPP.value = \"$ShipPrice\";\n";
		print "		document.leCOut.SPrice.value = \"\$$ShipPrice\";\n";
		print "		document.leCOut.Tax.value = \"\$0.00\";\n";
		print "		theWeight = document.leCOut.theWeight.value;\n";
		print "		ShipTotal = $ShipPrice * theWeight;\n";
		print "		ShipTotal = round(ShipTotal,2);\n";
		print "		document.leCOut.SPrice.value = \"\$$ShipPrice\";\n";
		print "		document.leCOut.STotal.value = \"\$\"+ShipTotal+\"\";\n";
		print "		PTTotal1 = ShipTotal + $EntireTotal;\n";
		print "		PTTotal = round(PTTotal1,2);\n";
		print "		document.leCOut.OTotalNoTax.value = \"\$\"+PTTotal+\"\";\n";
		print "		document.leCOut.FinalTotal1.value = \"Order Total: \$\"+PTTotal+\"\";\n";
		print "		document.leCOut.FinalTotal2.value = \"Order Total: \$\"+PTTotal+\"\";\n";
		print "}\n";
		if ($ShipperC eq "1") {
			$ShipInputs1 = "<input type=\"text\" name=\"ShipContact\" value=\"$Contact\" size=\"15\" class=\"inputtext15\" onFocus=\"javascript:noChange2();\"><br><input type=\"text\" name=\"ShipAddress1\" value=\"$Address1\" size=\"15\" class=\"inputtext15\" onFocus=\"javascript:noChange2();\"><br><input type=\"text\" name=\"ShipAddress2\" value=\"$Address2\" size=\"15\" class=\"inputtext15\" onFocus=\"javascript:noChange2();\"><br><input type=\"text\" name=\"ShipCity\" value=\"$City\" size=\"15\" class=\"inputtext15\" onFocus=\"javascript:noChange2();\"><br><input type=\"text\" name=\"ShipState\" value=\"$State\" size=\"3\" class=\"inputtext3\" onFocus=\"javascript:noChange2();\"><input type=\"text\" name=\"ShipZip\" value=\"$Zip\" size=\"7\" class=\"inputtext7\" onFocus=\"javascript:noChange2();\"><br>";
			$ShipInputs2 = "<input type=\"hidden\" name=\"PPP\" value=\"$ShipPrice\"><input type=\"hidden\" name=\"theWeight\" value=\"\"><input type=\"text\" name=\"ShipCourier\" value=\"$Courier\" size=\"7\" class=\"inputtext7\" onFocus=\"javascript:noChange2();\"><br><input type=\"text\" name=\"ShipType\" value=\"$ShipTipo\" size=\"15\" class=\"inputtext15\" onFocus=\"javascript:noChange2();\"><br><input type=\"text\" name=\"ShipPrice\" value=\"\$$ShipPrice/lb.\" size=\"15\" class=\"inputtext15\" onFocus=\"javascript:noChange2();\"><br>";
		}
	}
	$ShipSelEnd = "</select>";
	print "}\n";
	print "</script>";
}

## ----------------->>> GET CUSTOMER INFO
my $sth = $dbh->prepare("SELECT * FROM Customers WHERE CMCustNum='$Cookies{'CeeEmmNo'}'");
$sth->execute or die "Unable to execute query\n"; 
my @row;
while(@row = $sth->fetchrow_array) { 
		$AdminID = $row[4];
		$PayOption = $row[15];
			$CCVisaName = $row[16];
			$CCVisa = $row[17];
			$CCVisaExp = $row[18];
			$CCMasterName = $row[19];
			$CCMaster = $row[20];
			$CCMasterExp = $row[21];
			$CCAmexName = $row[22];
			$CCAmex = $row[23];
			$CCAmexExp = $row[24];
}
$sth->finish;

$CardCount=0;
if ($PayOption =~ "Cash") { push(@PayOptions, "Cash-----Cash"); }
if ($PayOption =~ "Check") { push(@PayOptions, "Check-----Check"); }
if ($PayOption =~ "CCVisa" && $CCVisa ne "" && $CCVisa ne " " && $CCVisaExp ne "" && $CCVisaExp ne " ") { push(@PayOptions, "Visa-----CCVisa"); $CardCount++; }
if ($PayOption =~ "CCMaster" && $CCMaster ne "" && $CCMaster ne " " && $CCMasterExp ne "" && $CCMasterExp ne " ") { push(@PayOptions, "Master Card-----CCMaster"); $CardCount++; }
if ($PayOption =~ "CCAmex" && $CCAmex ne "" && $CCAmex ne " " && $CCAmexExp ne "" && $CCAmexExp ne " ") { push(@PayOptions, "American Express-----CCAmex"); $CardCount++; }
if ($PayOption =~ "Net5") { push(@PayOptions, "Net5-----Net5"); }
if ($PayOption =~ "Net10") { push(@PayOptions, "Net10-----Net10"); }
if ($PayOption =~ "Net30") { push(@PayOptions, "Net30-----Net30"); }

if ($CardCount ne "0") {
	print "<script language=\"Javascript\">";
	if ($CCVisa ne "" && $CCVisa ne " " && $CCVisaExp ne "" && $CCVisaExp ne " ") { 
    	$CCVisa = substr($CCVisa, 12, 16);     # ONLY last 4 numbers, Characters
		$CCVisa = "****-****-****-" . "$CCVisa"; 
		print "function visaIt() {\n document.leCOut.CeeCeeNa.value = \"$CCVisaName\";\n document.leCOut.SeaSeaNo.value = \"$CCVisa\";\n document.leCOut.SiSiEx.value = \"$CCVisaExp\";\n }\n";			   
	}
	if ($CCMaster ne "" && $CCMaster ne " " && $CCMasterExp ne "" && $CCMasterExp ne " ") { 
    	$CCMaster = substr($CCMaster, 12, 16);     # ONLY last 4 numbers, Characters
		$CCMaster = "****-****-****-" . "$CCMaster"; 
		print "function masterIt() {\n document.leCOut.CeeCeeNa.value = \"$CCMasterName\";\n document.leCOut.SeaSeaNo.value = \"$CCMaster\";\n document.leCOut.SiSiEx.value = \"$CCMasterExp\";\n }\n";			   
	}
	if ($CCAmex ne "" && $CCAmex ne " " && $CCAmexExp ne "" && $CCAmexExp ne " ") { 
    	$CCAmex = substr($CCAmex, 12, 16);     # ONLY last 4 numbers, Characters
		$CCAmex = "****-****-****-" . "$CCAmex"; 
		print "function amexIt() {\n document.leCOut.CeeCeeNa.value = \"$CCAmexName\";\n document.leCOut.SeaSeaNo.value = \"$CCAmex\";\n document.leCOut.SiSiEx.value = \"$CCAmexExp\";\n }\n";			   
	}
	$CCInstruct = "<br>The fields below are filled in automatically if you choose a Credit Card from the Payment Option(s) list above. <b>Keep in mind:</b> Only your company's admin user can change payment option information.<br><br>";
	$CCName = "Name on Credit Card<br><input type=\"text\" name=\"CeeCeeNa\" value=\"\" size=\"15\" class=\"inputtext15\" onFocus=\"javascript:noChange();\"><br>";
	$CCNumber = "Credit Card Number<br><input type=\"text\" name=\"SeaSeaNo\" value=\"\" size=\"15\" class=\"inputtext15\" onFocus=\"javascript:noChange();\"><br>";
	$CCExp = "Expiration Date<br><input type=\"text\" name=\"SiSiEx\" value=\"\" size=\"15\" class=\"inputtext15\" onFocus=\"javascript:noChange();\"><br>";
	print "</script>";
}

print "
<table width=\"100%\" align=\"center\" cellpadding=\"2\" cellspacing=\"0\" border=\"0\">
<tr> 
<td width=\"65%\" valign=\"top\">";

## if no shipping info, print shipping error.
if ($Cuentame ne "0") {

print "
<!--START Ship Location and Method -->

<table width=\"100%\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\" class=\"stankth\" height=\"18\" $border>
<tr height=\"25\" bgcolor=\"#ffffff\"><td align=\"right\" width=\"100%\">
$ShipSelStart
";

foreach $thisShip (@selectShip) {
	@mioShip = split(/-----/, $thisShip);
	print "<option value=\"$mioShip[0]\">$mioShip[1] / $mioShip[2]</option>";
}

print "
$ShipSelEnd
</td></tr>
</table>

<table width=\"100%\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\" border=\"0\" height=\"1\">
<tr height=\"1\"><td width=\"100%\"><img src=\"images/spacer.gif\" border=\"0\" height=\"1\" width=\"1\"></td></tr>
</table>

<table width=\"100%\" align=\"center\" cellspacing=\"0\" cellpadding=\"5\" class=\"stankth\" height=\"18\" $border>
<tr height=\"25\" bgcolor=\"#F2F2F7\"><td align=\"left\" width=\"50%\"><font class=\"btext\"><b>Shipping Location</b></font></td><td align=\"left\" width=\"50%\"><font class=\"btext\"><b>Shipping Method</b></font></td></tr>
</table>";

if ($Cuentame ne "1") {
print "
<table width=\"100%\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\" border=\"0\" height=\"1\">
<tr height=\"1\"><td width=\"100%\"><img src=\"images/spacer.gif\" border=\"0\" height=\"1\" width=\"1\"></td></tr>
</table>

<table width=\"100%\" align=\"center\" cellspacing=\"0\" cellpadding=\"10\" class=\"stankth\" height=\"18\" $border>
<tr height=\"10\"><td width=\"50%\"><font class=\"btext\">$ShipInputs1<br>United States</font></td><td width=\"50%\" valign=\"top\"><font class=\"btext\">$ShipInputs2<br><br><center><input type=\"text\" name=\"FinalTotal1\" value=\"\" size=\"22\" class=\"inputtext22red\"></center></font></td></tr>
<table>
<br>
<!--END Ship Location and Method -->
";
}

else {
print "<table width=\"100%\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\" border=\"0\" height=\"1\">
<tr height=\"1\"><td width=\"100%\"><img src=\"images/spacer.gif\" border=\"0\" height=\"1\" width=\"1\"></td></tr>
</table>

<table width=\"100%\" align=\"center\" cellspacing=\"0\" cellpadding=\"10\" class=\"stankth\" height=\"18\" $border>
<tr height=\"10\"><td width=\"50%\"><font class=\"btext\"><b>$Contact</b> $Address1 $Address2 $City $State $Zip<br>United States</font></td><td width=\"50%\" valign=\"top\"><font class=\"btext\"><b>$Courier</b> $ShipTipo $ShipPrice $PPP</font></td></tr>
<table>
<br>
<!--END Ship Location and Method -->
";
}

}
else {
print "
<table width=\"100%\" align=\"center\" cellspacing=\"0\" cellpadding=\"5\" class=\"stankth\" height=\"18\" $border>
<tr height=\"12\" bgcolor=\"#F2F2F7\"><td align=\"left\" width=\"100%\"><font class=\"btext\"><b>Shipping Location</b></font></td></tr>
<tr height=\"10\" bgcolor=\"#FFFFFF\"><td width=\"50%\"><font class=\"btext\"><b>No Shipping Information Found</b><br>Our system did not find any preset shipping information for your company. Please let the Shark Tank&#153; alert your company's chosen 'Administrative User' about this problem by clicking the 'Email It' icon at the top of this screen to email him/her a message regarding this issue. We cannot process this order without a shipping address attached to it.<br>United States</font></td><td width=\"50%\" valign=\"top\"><font class=\"btext\"><b>$Courier</b> $ShipTipo $\$ShipPrice/lb.</font></td></tr>
<table>
<br>
";
}

print "<table width=\"100%\" align=\"center\" cellspacing=\"0\" cellpadding=\"5\" class=\"stankth\" height=\"18\" $border>
<tr height=\"12\" bgcolor=\"#F2F2F7\"><td align=\"left\" width=\"100%\"><font class=\"btext\"><b>Order Summary</b></font></td></tr>
</table>

<table width=\"100%\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\" border=\"0\" height=\"1\">
<tr height=\"1\"><td width=\"100%\"><img src=\"images/spacer.gif\" border=\"0\" height=\"1\" width=\"1\"></td></tr>
</table>

<table width=\"100%\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\" class=\"stankth\" height=\"18\" $border>
<tr height=\"12\" bgcolor=\"#ffffff\"><td align=\"center\" width=\"17%\"><font class=\"btext\"><i>CFGID</i></font></td><td width=\"49%\"><font class=\"btext\"><i>System's Name</i></font></td><td width=\"18%\" align=\"center\"><font class=\"btext\"><i>Price</i></font></td><td width=\"4%\" align=\"center\"><font class=\"btext\"><i>Qty.</i></font></td><td width=\"12%\" align=\"center\"><font class=\"btext\"><i>Weight</i></font></td></tr>
</table>

<table width=\"100%\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\" border=\"0\" height=\"1\">
<tr height=\"1\"><td width=\"100%\"><img src=\"images/spacer.gif\" border=\"0\" height=\"1\" width=\"1\"></td></tr>
</table>

<table width=\"100%\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\" class=\"stankth\" height=\"18\" $border>
<tr height=\"10\"><td width=\"100%\" colspan=\"5\"><img src=\"images/spacer.gif\" border=\"0\" height=\"10\" width=\"1\"></td></tr>
";
	$CFGCount=0;
	foreach $Config (@Configs) {
	$CFGCount++;
		@leConfig = split(/=====/, $Config);
		$leParent = "$leConfig[0]";
		$leCMSeries = "$leConfig[1]";
		$leProductIDs = "$leConfig[2]";
		$leTotalPrice = "$leConfig[3]";
		$leTotalWeight = "$leConfig[4]";
		$leCreatedOn = "$leConfig[5]";
		$leConfigID = "$leConfig[6]";
		$leCuenta = "$leConfig[7]";
		$leCuenta = $leCuenta;
		if ($leCuenta > 1) {
			foreach (1 .. $leCuenta) {
				push(@muaWeight, $leTotalWeight);
			}
		}
		else {
			push(@muaWeight, $leTotalWeight);
		}
		my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$leParent'");
		$sth->execute or die "Unable to execute query\n";
		my @row;
		while(@row = $sth->fetchrow_array) {
			$MuaNombre = $row[11];
			$MuaSPhoto = $row[17];
			$MuaWarr = $row[19];
			$MuaAccessories = $row[24];
		}
		$sth->finish;
		print "<tr height=\"35\"><td valign=\"top\" align=\"center\" width=\"17%\"><font class=\"btext\"><a href=\"javascript:abrete('http://www.coastlinemicro.com/stank_vconfig.html?CID=$leConfigID&InnerLink=1');\">$leConfigID</a></font></td><td valign=\"top\" width=\"49%\"><font class=\"btext\">$MuaNombre</font></td><td width=\"18%\" valign=\"top\" align=\"center\"><font class=\"btext_red\">$leTotalPrice</font></td><td valign=\"top\" width=\"4%\" align=\"center\"><font class=\"btext\">$leCuenta</font></td><td valign=\"top\" width=\"12%\" align=\"center\"><font class=\"btext\">$leTotalWeight</font></td></tr>";
	}

	## tally weight
	$pesoCount=0;
	foreach $muaPeso (@muaWeight) {
		$pesoCount++;
		if ($pesoCount eq "1") { $theWeight = $muaPeso; }
		else { $theWeight = $theWeight + $muaPeso; }
	}
	print "<tr height=\"20\" bgcolor=\"#F2F2F7\"><td valign=\"middle\" width=\"66%\" align=\"right\" colspan=\"2\"><font class=\"btext\"><b>Cart Total</b> (No shipping included) &nbsp;</font></td><td valign=\"middle\" width=\"18%\" align=\"center\"><font class=\"btext_red\"><b>\$$EntireTotal</b></font></td><td width=\"4%\"><font class=\"btext\">&nbsp;</font></td><td width=\"12%\" align=\"center\"><font class=\"btext\">$theWeight</font></td></tr></table>";
	
}

## if nothing in cart
else {

print "<table width=\"85%\" align=\"center\" cellpadding=\"3\" cellspacing=\"0\" border=\"0\">
<tr> 
<td width=\"100%\" valign=\"top\"><center><font class=\"stankprice\"><b>Your Cart's Total \$0</b></font><br><font class=\"btext\"><br><b>Your Shark Tank&#153; Shopping Cart is currently empty...</b><br><br><br></font></center></td>
</tr>
</table>";

}

{
print <<EOF
<br>
                      </td>
                    </tr>
                  </table>
<table width="100%" align="center" cellspacing="0" cellpadding="5" class="stankth" height="18" $border>
<tr height="12" bgcolor="#F2F2F7"><td align="left" width="50%"><font class="btext"><b>Order Overview</b></font></td><td align="left" width="50%"><font class="btext"><b>Payment Option(s)</b></font></td></tr>
</table>

<table width="100%" align="center" cellspacing="0" cellpadding="0" border="0" height="1">
<tr height="1"><td width="100%"><img src="images/spacer.gif" border="0" height="1" width="1"></td></tr>
</table>

<table width="100%" align="center" cellspacing="0" cellpadding="10" class="stankth" height="18" $border>

<tr height="10"><td width="65%" valign="top">

<!--START ORDER TALLY-->

<table width="100%" align="center" cellspacing="0" cellpadding="0" border="0" height="1">
<tr height="30">
<td width="50%" valign="middle"><font class="btext">Cart Total:</font></td>
<td width="50%" valign="middle"><input type="text" name="CTotal" value="\$$EntireTotal" size="7" class="inputtext7"></td>
</tr>
<tr height="30">
<td width="50%" valign="middle"><nobr><font class="btext"><b>$theWeight</b> lbs. @ <input type="text" name="SPrice" value="" size="7" class="inputtext7">/lb. = </nobr></font></td>
<td width="50%" valign="middle"><input type="text" name="STotal" value="" size="7" class="inputtext7"></td>
</tr>
<tr height="30">
<td width="50%" valign="middle"><font class="btext"><nobr>Total w/Ship & Handle</nobr></font></td>
<td width="50%" valign="middle"><input type="text" name="OTotalNoTax" value="" size="7" class="inputtext7"></td>
</tr>
<tr height="30">
<td width="50%" valign="middle"><font class="btext">Total Tax</font></td>
<td width="50%" valign="middle"><input type="text" name="Tax" value="" size="7" class="inputtext7"></td>
</tr>
<tr height="40">
<td width="100%" valign="middle" align="center" colspan="2"><input type="text" name="FinalTotal2" value="" size="22" class="inputtext22red"></td>
</tr>
</table>

<!--END ORDER TALLY-->

</td><td width="35%" valign="top"><font class="btext">

<script language="Javascript">
function testCC() {
var formindex = document.leCOut.PayClass.selectedIndex;
var thisone = document.leCOut.PayClass.options[formindex].value;
if (thisone == "CCVisa") { visaIt(); }
else if (thisone == "CCMaster") { masterIt(); }
else if (thisone == "CCAmex") { amexIt(); }
// clear cc fields if none of the above...
else { 
	document.leCOut.CeeCeeNa.value = ""; 
	document.leCOut.SeaSeaNo.value = "";
	document.leCOut.SiSiEx.value = "";
}
}

function noChange() {
	alert('Sorry, you cannot directly edit the contents of this field. This information is controlled solely by your company\\'s administrative user. \\n\\nTo automatically set these fields, select a Credit Card type from the \\'Payment Option(s)\\' list.');
	document.leCOut.PayClass.focus();
}

function noChange2() {
	alert('Sorry, you cannot directly edit the contents of this field. This information is controlled solely by your company\\'s administrative user. \\n\\nTo automatically set these fields, select a Location from the \\'Shipping Destinations\\' list.');
	document.leCOut.ShipDests.focus();
}

// math round function
function round(number,X) {
// rounds number to X decimal places, defaults to 2
X = (!X ? 2 : X);
return Math.round(number*Math.pow(10,X))/Math.pow(10,X);
}

// SET TOTAL WEIGHT
document.leCOut.theWeight.value = "$theWeight";

</SCRIPT>

<select name="PayClass" size="1" class="inputtext" onChange="javascript:testCC();">
EOF
}

foreach $laOpcion (@PayOptions) {
	@splitOpcion = split(/-----/, $laOpcion);
	print "<option value=\"$splitOpcion[1]\">$splitOpcion[0]</option>";
}

{ 
print <<EOF
</select><br>

$CCInstruct
$CCName
$CCNumber
$CCExp

</font></td></tr>
<table>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
              <tr> 
                <td> 
                  			<table width="100%" cellspacing="0" cellpadding="1" bgcolor="#FFFFFF" class="stankth" height="25" $border>
                    			<tr> 
	                      		<td width="100%" align="right">
<SCRIPT language="Javascript">
//Calling for search1.swf for all browsers except for NS4, it gets a submit image button
if (is.ns4) {
document.write('<input type=\"image\" name=\"Submit\" border=\"0\" src=\"images/newones/ns4_submitorder.jpg\" width=\"423\" height=\"25\">');
}
else {
document.write('<object classid=\"clsid:D27CDB6E-AE6D-11cf-96B8-444553540000\" width=\"423\" height=\"25\" codebase=\"http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=4,0,2,0\">');
document.write('<param name=\"MOVIE\" value=\"flash/submitorder_line.swf\"><param name=\"PLAY\" value=\"true\"><param name=\"LOOP\" value=\"false\"><param name=\"QUALITY\" value=\"high\"><param name=\"MENU\" value=\"false\">');
document.write('<embed src=\"flash/submitorder_line.swf\" width=\"423\" height=\"25\" play=\"true\" loop=\"false\" quality=\"high\" menu=\"false\" type=\"application/x-shockwave-flash\" pluginspage=\"http://www.macromedia.com/shockwave/download/index.html?P1_Prod_Version=ShockwaveFlash\"></embed>');
document.write('</object>');
}
</SCRIPT>
								</td>
    	                		</tr>
        	          		</table>
                </td>
              </tr>

      </table>

    </td>
  </tr>
</table>

<br>
<table width="$tablewidth" border="0" cellspacing="0" cellpadding="0"><tr><td align="center" width="$tablewidth"> 
$STANKLEGAL
</td></tr></table>


</form>
</body>
</html>

EOF
}

## DISCONNECT DB 
$dbh->disconnect; 

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