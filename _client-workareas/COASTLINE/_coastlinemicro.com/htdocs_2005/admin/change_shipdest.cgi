#!/usr/bin/perl5 -w

## Test location of request
require ("referer.nsp");

print "Content-type: text/html\n\n";
## Snif thisurl, in case user needs to login you have somewhere to send em back to
$lasturl = "$ENV{'SCRIPT_NAME'}";
## Snif cookie, if present test for logged in status
require ("cookiesnif.nsp");
## If comes back dead a login prompt was called, kill current process
if ($exit eq '1') { exit; }
## else continue with process

## Check to see if the logged user is granted rights to this action script
if (($Cookies{'UserType'} eq "COManage") || ($Cookies{'UserType'} eq "WEBAdmin")) { $nextone = "1"; }
else {
	$noaccess = `cat noaccess.nsf`;
	print "$noaccess";	
	exit;
}

## Grab User Input
require ("parse_query.nsp");

## script's name
$script = "$ENV{'SCRIPT_NAME'}";
## grab admin date format
require ("date.nsp");

## get perl built dynamic DHTML menu js
my $MenuConfig = `cat js/menu_config.js`;
my $MenuConstructor = `cat js/menu_constructor.js`;
my $MenuConfig = "<script langauage=\"Javascript\">\n$MenuConfig\n</script>";
my $MenuConstructor = "<script langauage=\"Javascript\">\n$MenuConstructor\n</script>";

## get CM legal piece
$legal = `cat legal.nsf`;

## If SAVING
if (($FORM{'DROPIN'}) && ($FORM{'CMCustNum'}) && ($FORM{'CompanyName'}) && ($FORM{'ShippingID'})) {

## TOP HTML TEMPLATE
&topper;

	## Crumble Form Input to Variables
	my $CMCustNum = "$FORM{'CMCustNum'}";
	my $ShippingID = "$FORM{'ShippingID'}";
	my $CompanyName = "$FORM{'CompanyName'}";
	my $AdminUser = "$FORM{'AdminUser'}";
	my $Courier = "$FORM{'Courier'}";
	my $ShipType = "$FORM{'Package'}";
	my $ShipPrice = "$FORM{'ShipPrice'}";
	my $Contact = "$FORM{'LastName'},$FORM{'FirstName'}";
	my $Instructions = "$FORM{'Instructions'}";
	my $Phone = "$FORM{'Phone'}";
	my $Extension = "$FORM{'Extension'}";
	my $Fax = "$FORM{'Fax'}";
	my $ShipAdd = "$FORM{'ShipAdd'}";
	my $ShipAdd2 = "$FORM{'ShipAdd2'}";
	my $ShipCity = "$FORM{'ShipCity'}";
	my $ShipState = "$FORM{'ShipState'}";
	my $ShipZip = "$FORM{'ShipZip'}";
	my $ActionUser = "$Cookies{'Username'}";

	
## --------------------->>>> UPDATE SHIPDESTS WITH NEW INPUT
use DBI;
my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
$dbh->{RaiseError} = 1;
my $sth = $dbh->prepare("UPDATE LOW_PRIORITY ShipDests 
						 SET Courier='$Courier', 
						 ShipType='$ShipType', 
						 ShipPrice='$ShipPrice', 
						 Contact='$Contact', 
						 Instructions='$Instructions', 
						 Phone='$Phone', 
						 Extension='$Extension', 
						 Fax='$Fax', 
						 Address1 ='$ShipAdd', 
						 Address2 ='$ShipAdd2', 
						 City='$ShipCity', 
						 State='$ShipState', 
						 Zip='$ShipZip', 
						 ModifiedBy='$ActionUser', 
						 ModifiedOn=Null 
						 WHERE ShippingID='$ShippingID'");
$sth->execute or die "Unable to execute query\n"; 
$sth->finish; 
$dbh->disconnect; 	


## ----------------------->>> SEND EMAIL START
$AdminUser = "$FORM{'AdminUser'}";
use DBI;
my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
$dbh->{RaiseError} = 1;
## ----------------------->>> GATHER USER'S INFORMATION (SECOND USER/NOT USER MAKING CHANGES)
my $sth = $dbh->prepare("SELECT * FROM Users WHERE Username='$AdminUser'");
$sth->execute or die "Unable to execute query\n"; 
my @row;
while(@row = $sth->fetchrow_array) { 
	$EmailType = $row[2];
	$AdminEmail = $row[5];
	
}
$sth->finish;
$dbh->disconnect;

## ----------------------->>> PREPARE VARIABLES FOR OUTER SEND EMAIL PROGRZM
$TO = "$AdminEmail";
$FROM = "admin\@rhomberg.com";
$SUBJECT = "Administration System - Shipping Location Updated";
$GREETING = "Concerned,\n\n";
$BODY = "A shipping location has been updated for $CompanyName within our E-Com store. Below you will find the specifics of the affected shipping location.\n\nCM Customer Number - $CMCustNum\nCompany Name - $CompanyName\nSelected Courier - $Courier\nSelected Courier Package - $ShipType\nPackage Destination - From Our Location (92618) to $ShipCity ($ShipZip)\nCourier's Price per/lb. for this location - \$$ShipPrice\n\n\n";
$ATTACHMENTS = "";
$FOOTER = "";
$MYHTMLTITLE = "<title>Shipping Locations</title>";
$MYHTMLSTAMP = "<table width=\"450\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" align=\"center\"><tr><td width=\"100%\" valign=\"top\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#333366\">Concerned,<br><br>A new shipping location has been updated for $CompanyName within the E-Com store. Below you will find the specifics of the affected shipping location.<br><br><b>CM Customer Number</b> - $CMCustNum<br><b>Company Name</b> - $CompanyName<br><b>Selected Courier</b> - $Courier<br><b>Selected Courier Package</b> - $ShipType<br><b>Package Destination</b> - From Our Location (92618) to $ShipCity ($ShipZip)<br><b>Courier's Price per/lb. for this location</b> - \$$ShipPrice<br><br><ul><li>Shark Tank&#153; Administration System<br><a href=\"http://www.rhomberg.com/systemConfigurator/admin/\">http://www.rhomberg.com/systemConfigurator/admin/</a></li><li>Did not request this info?<br><a href=\"mailto:security\@rhomberg.com?Subject=Shipping Location Update (Shark Tank Admin)\">Report It</a></li></ul></font></td></tr></table>";
$MYHTMLATTACH = "";
## ----------------------->>> EXECUTE OUTER EMAIL PROGRAM
require("mailer_2nd.nsp");
## ----------------------->>> END EMAILINGS

{
print <<EOF

<font face="verdana,arial,helvetica" size="1" color="#333366"><center><br><b>Update Shipping Location</b><br><br>The shipping location for <b>$CompanyName</b> has been updated successfully.<br><br><form><input type="button" value="Back to $CompanyName\'s Profile" onClick="javascript:location.href='change_customer.cgi?CMCustNum=$CMCustNum&CompanyName=$CompanyName'" class="inputbut"><br></center></font>
					  
EOF
}
	
## END PAGE TEMPLATE
&bottom;

exit;
}

## ------------->>> If trying to delete a current Shipping Location
elsif (($FORM{'DELETEIT'}) && ($FORM{'ShippingID'})) {
## TOP HTML TEMPLATE
&topper;

	## Crumble Form Input to Variables
	my $ShippingID = "$FORM{'ShippingID'}";
	my $CMCustNum = "$FORM{'CMCustNum'}";
	my $CompanyName = "$FORM{'CompanyName'}";
	my $ActionUser = "$Cookies{'Username'}";

	print "<br><center><b>Delete Shipping Location</b><br><br>The shipping location you requested to be deleted has been successfully deleted from the system effective immediately.<br><br><form><input type=\"button\" value=\"Back to $CompanyName's Profile\" onClick=\"javascript:location.href='change_customer.cgi?CMCustNum=$CMCustNum&CompanyName=$CompanyName'\" class=\"inputbut\"></form></center>";
	print "<br></font>";
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("DELETE FROM ShipDests WHERE ShippingID=$ShippingID");
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
	$dbh->disconnect;
	
	
## END PAGE TEMPLATE
&bottom;

exit;
}

## ------------->>> If we need the very small bottom blank frame
elsif ($FORM{'blank'}) {
print "<html><head><title></title></head><body></body></html>";
exit;
}

## ------------->>> If no resident form processing calls are given continue
elsif (($FORM{'enformthee'}) && ($FORM{'CMCustNum'}) && ($FORM{'CompanyName'}) && ($FORM{'ShippingID'})) {

my $ShippingID = "$FORM{'ShippingID'}";
my $CMCustNum = "$FORM{'CMCustNum'}";
my $CompanyName = "$FORM{'CompanyName'}";
my $AdminUser = "$FORM{'AdminUser'}";


## ------------->>> GET SHIPDEST CONFIG
	use DBI;
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("SELECT * FROM ShipDests WHERE ShippingID='$ShippingID' AND CMCustNum='$CMCustNum'");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
	my $SavedShippingID = $row[0];
	my $SavedCMCustNum = $row[1];
	my $SavedCourier = $row[2];
	my $SavedShipType = $row[3];	
	my $SavedShipPrice = $row[4];
	my $SavedContact = $row[5];
	my $SavedInstructions = $row[6];
	my $SavedPhone = $row[7];
	my $SavedExtension = $row[8];
	my $SavedFax = $row[9];
	my $SavedAddress1 = $row[10];
	my $SavedAddress2 = $row[11];
	my $SavedCity = $row[12];
	my $SavedState = $row[13];
	my $SavedZip = $row[14];
	my $SavedAddedBy = $row[15];
	my $SavedAddedOn = $row[16];
	my $SavedModifiedBy = $row[17];
	my $SavedModifiedOn = $row[18];
	## Re-Structure data as necessary
   	local($SavedLastName, $SavedFirstName) = split(/,/, $SavedContact);
	my $TelArea = substr($SavedPhone, 0, 3);
	my $TelNum = substr($SavedPhone, 3, 7);
	my $FaxArea = substr($SavedFax, 0, 3);
	my $FaxNum = substr($SavedFax, 3, 7);
	my $AddYear = substr($SavedAddedOn, 0, 2);
	my $AddMonth = substr($SavedAddedOn, 2, 2);
	my $AddDay = substr($SavedAddedOn, 4, 2);
	my $ModYear = substr($SavedModifiedOn, 0, 2);
	my $ModMonth = substr($SavedModifiedOn, 2, 2);
	my $ModDay = substr($SavedModifiedOn, 4, 2);
	my $DelYear = substr($SavedDeletedOn, 0, 2);
	my $DelMonth = substr($SavedDeletedOn, 2, 2);
	my $DelDay = substr($SavedDeletedOn, 4, 2);
	
{
print <<EOF

<html>
<head>
<title>Shark Tank Admin System - Shipping Locations</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<script language="Javascript">
// QUICK CROSS-BROWSER MOUSE-OVER/OFF FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function imageOff(which,thisone) {
	var cual = 	"images/button_"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}
function imageOn(which,thisone) {
	var cual = 	"images/button_"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}

// FORM FEEDER FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function getPackages() {
var formindex = document.add.Courier.selectedIndex;
var thisone = document.add.Courier.options[formindex].value;
var b = navigator.appName;
if (b=="Netscape") { parent.frames.xtraOne.location.href='courier.cgi?Courier='+thisone+''; }
else { parent.xtraOne.location.href='courier.cgi?Courier='+thisone+''; }
}

function getPrice() {
var formindex = document.add.Courier.selectedIndex;
var thisone = document.add.Courier.options[formindex].value;
var formindex2 = document.add.Package.selectedIndex;
var thisone2 = document.add.Package.options[formindex2].value;
var shipzip = document.add.ShipZip.value;
if (shipzip == null || shipzip == "" || shipzip == " ") {
	alert ('You must type in a 5 digit zip code for this shipping location before trying to calculate the shipping price per pound for this location. Once you type this number in just re-select your choice for Courier Package and the price will automatically be generated for you.');
	document.add.ShipZip.focus();
}
else {
	var b = navigator.appName;
	if (b=="Netscape") { parent.frames.xtraOne.location.href='ups_perpound.cgi?Courier='+thisone+'&Package='+thisone2+'&ShipZip='+shipzip+''; }
	else { parent.xtraOne.location.href='ups_perpound.cgi?Courier='+thisone+'&Package='+thisone2+'&ShipZip='+shipzip+''; }
}
}

// FORM CHECKER FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function checkForm() {
var missingdrop = "";
var thefirst = "";

// Check Common form fields
if (document.add.FirstName.value == "" || document.add.FirstName.value == " ") {
    missingdrop += "\\n     - First Name";
	thefirst = "FirstName";
}

if (document.add.ShipAdd.value == "" || document.add.ShipAdd.value == " ") {
    missingdrop += "\\n     - Shipping Address";
	if (thefirst == "") { thefirst = "ShipAdd"; }
}

if (document.add.ShipCity.value == "" || document.add.ShipCity.value == " ") {
    missingdrop += "\\n     - Shipping Address City";
	if (thefirst == "") { thefirst = "ShipCity"; }
}

if (isNaN(document.add.ShipZip.value) || (document.add.ShipZip.value == "") || (document.add.ShipZip.value == " ") || (document.add.ShipZip.value.length != 5)) {
    missingdrop += "\\n     - Shipping Address Zip must be a 5 digit number";
	if (thefirst == "") { thefirst = "ShipZip"; }
}

// Check Phone number and format if it is there get the area code and num and feed the Phone field
if (isNaN(document.add.TelArea.value) || (document.add.TelArea.value == "") || (document.add.TelArea.value == " ") || (document.add.TelArea.value.length != 3)) {
    missingdrop += "\\n     - Phone's Area Code must be a 3 digit number";
	if (thefirst == "") { thefirst = "TelArea"; }
}
else if (isNaN(document.add.TelNum.value) || (document.add.TelNum.value == "") || (document.add.TelNum.value == " ") || (document.add.TelNum.value.indexOf('-') != -1) || (document.add.TelNum.value.length != 7)) {
    missingdrop += "\\n     - Phone Number must be a 7 digit number\\n        *No hyphen (-) necessary";
	if (thefirst == "") { thefirst = "TelNum"; }
}
else {
	PhoneValues = document.add.TelArea.value + document.add.TelNum.value;
	document.add.Phone.value = PhoneValues;
}

// Check Fax number and format if it is there get the area code and num and feed the Fax field
if (isNaN(document.add.FaxArea.value) || (document.add.FaxArea.value == "") || (document.add.FaxArea.value == " ") || (document.add.FaxArea.value.length != 3)) {
    missingdrop += "\\n     - Fax's Area Code must be a 3 digit number";
	if (thefirst == "") { thefirst = "FaxArea"; }
}
else if (isNaN(document.add.FaxNum.value) || (document.add.FaxNum.value == "") || (document.add.FaxNum.value == " ") || (document.add.FaxNum.value.indexOf('-') != -1) || (document.add.FaxNum.value.length != 7)) {
    missingdrop += "\\n     - Fax Number must be a 7 digit number\\n        *No hyphen (-) necessary";
	if (thefirst == "") { thefirst = "FaxNum"; }
}
else {
	FaxValues = document.add.FaxArea.value + document.add.FaxNum.value;
	document.add.Fax.value = FaxValues;
}

// CHECK COURIER PRICE
if ((document.add.ShipPrice.value == "") || (document.add.ShipPrice.value == " ") || (document.add.ShipPrice.value < 0)) {
    missingdrop += "\\n     - Courier Price has not been calculated for this location.\\n        *You must select a Courier Package to dynamically fill\\n           this field in with a real-time shipping price for this\\n           specific shipping location.";
	if (thefirst == "") { thefirst = "ShipPrice"; }
}

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    missingdrop ="___________________________________________                   \\n\\n" + "  Sorry, I cannot process your request because the\\n  following fields are either blank or filled incorrectly:\\n" + "___________________________________________                   \\n\\n" +
    missingdrop + "\\n\\n___________________________________________                   " + "\\n\\n   To continue, check fields and submit form again!" + "\\n___________________________________________";
    alert(missingdrop);
	document.add(thefirst).focus();
    return false;
} 
else {
return true;
}
}
</SCRIPT>
$MenuConfig
</head>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
$MenuConstructor
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%" valign="top"><img src="images/illus_main.jpg" width="250" height="100"></td>
    <td width="25%">&nbsp;</td>
    <td align="left" valign="top"><img src="images/title_main.jpg" width="300" height="100"></td>
  </tr>
</table>
<form method="post" action="$script" name="add" onSubmit="return checkForm();">
<table width="100%" border="0" height="100%" cellpadding="0" cellspacing="0">
  <tr valign="top"> 
    <td width="20%">$legal</td>
    <td align="center" width="80%"> 
      <table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
            <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>Create 
              New Shipping Location</b></font></td>
          <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
              <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER" bordercolor="#333366">
                <tr bordercolor="#333366" valign="middle"> 
                  <td width="100%" align="center" height="50" class="tableBG"><font face="verdana,arial,helvetica" size="1" color="#EB0000">*If 
                    you have any questions please ask your Supervisor or Manager 
                    for help using the system or updating it's information.</font> 
                    <font face="verdana,arial,helvetica" size="1" color="#333366"></font><font face="verdana,arial,helvetica" size="1" color="#333366"></font><font face="verdana,arial,helvetica" size="1" color="#333366"></font></td>
              </tr>
              <tr bordercolor="#333366"> 
                  <td width="100%" align="center" valign="top" height="250" bordercolor="#333366"> 
                    <table width="100%" border="0" cellspacing="0" cellpadding="5">
                      <tr valign="top" align="center"> 
                        <td bordercolor="#333366" class="tableBORDER"><br>
                          <table width="300" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="348" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Parent 
                                      Company </font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" bgcolor="#F2F2F7" align="center"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"> <font face="verdana,arial,helvetica" size="1" color="#333366">$CompanyName</font> 
                                      <input type="hidden" name="CMCustNum" value="$CMCustNum">
                                      <input type="hidden" name="CompanyName" value="$CompanyName">
                                      <input type="hidden" name="ShippingID" value="$ShippingID">
                                      <input type="hidden" name="AdminUser" value="$AdminUser">
                                      <input type="hidden" name="DROPIN" value="1">
                                    </td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                </table>
                              </td>
                              <td bgcolor="#8F8FAB" width="1" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="300" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="348" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">First 
                                      Name</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" bgcolor="#F2F2F7" align="center"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"> 
                                      <input type="text" name="FirstName" size="15" class="inputtext15" value="$SavedFirstName">
                                    </td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                </table>
                              </td>
                              <td bgcolor="#8F8FAB" width="1" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="300" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="348" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Last 
                                      Name</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" bgcolor="#F2F2F7" align="center"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"> 
                                      <input type="text" name="LastName" size="15" class="inputtext15" value="$SavedLastName">
                                    </td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                </table>
                              </td>
                              <td bgcolor="#8F8FAB" width="1" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="300" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="348" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Physical 
                                      Address</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" bgcolor="#F2F2F7" align="center" valign="middle"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="65" align="center"><nobr><font face="verdana,arial,helvetica" size="1" color="#333366">Line 
                                      1:</font> 
                                      <input type="text" name="ShipAdd" size="15" class="inputtext15" value="$SavedAddress1">
                                      </nobr><br>
                                      <nobr><font face="verdana,arial,helvetica" size="1" color="#333366">Line 
                                      2:</font> 
                                      <input type="text" name="ShipAdd2" size="15" class="inputtext15" value="$SavedAddress2">
                                      </nobr></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                </table>
                              </td>
                              <td bgcolor="#8F8FAB" width="1" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="300" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="348" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">City</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" bgcolor="#F2F2F7" align="center"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"> 
                                      <input type="text" name="ShipCity" size="15" class="inputtext15" value="$SavedCity">
                                    </td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                </table>
                              </td>
                              <td bgcolor="#8F8FAB" width="1" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="300" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="348" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">State</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" bgcolor="#F2F2F7" align="center"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"> 
                                      <select name="ShipState" class="inputtext">
EOF
}

## WHICH STATE IS CHOSEN?
@States = ("AK","AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","HI","IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VA","VT","WA","WI","WV","WY");
foreach $State (@States) {
	if ($State eq "$SavedState") { print "<option value=\"$State\" SELECTED>$State</option>"; }
	else { print "<option value=\"$State\">$State</option>"; }
}

{
print <<EOF
                                      </select>
                                    </td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                </table>
                              </td>
                              <td bgcolor="#8F8FAB" width="1" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="300" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="348" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Zip 
                                      Code </font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="55" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">Type 
                                      a zip code for this company's mailing address. 
                                      Must be only a 5 digit number in order to 
                                      calculate a shipping rate for this location.</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="45" align="center"> 
                                      <input type="text" name="ShipZip" size="7" class="inputtext7" value="$SavedZip">
                                    </td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                </table>
                              </td>
                              <td bgcolor="#8F8FAB" width="1" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                        </td>
                        <td> <br>
                          <table width="300" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="348" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Location 
                                      Phone Number</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="45" bgcolor="#F2F2F7" align="center" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366"><font color="#EB0000">Area 
                                      Code - 3 digits<br>
                                      Phone Number - 7 digits</font> </font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="55" align="center"> <nobr> 
                                      <input type="text" name="TelArea" size="3" class="inputtext3" value="$TelArea">
                                      <input type="text" name="TelNum" size="7" class="inputtext7" value="$TelNum">
                                      <input type="text" name="Extension" size="3" class="inputtext3" value="$SavedExtension">
                                      <input type="hidden" name="Phone" value="">
                                      </nobr> <font face="verdana,arial,helvetica" size="1" color="#333366"><br>
                                      <nobr>Area&nbsp;&nbsp;&nbsp; Number &nbsp;&nbsp;&nbsp;&nbsp;Ext.<nobr></font> 
                                    </td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                </table>
                              </td>
                              <td bgcolor="#8F8FAB" width="1" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="300" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="348" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Location Fax 
                                      Number</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="45" bgcolor="#F2F2F7" align="center" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366"><font color="#EB0000">Area 
                                      Code - 3 digits<br>
                                      Fax Number - 7 digits</font> </font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="55" align="center"> <nobr> 
                                      <input type="hidden" name="Fax">
                                      <nobr> 
                                      <input type="text" name="FaxArea" size="3" class="inputtext3" value="$FaxArea">
                                      <input type="text" name="FaxNum" size="7" class="inputtext7" value="$FaxNum">
                                      </nobr> <font face="verdana,arial,helvetica" size="1" color="#333366"><br>
                                      Area &nbsp;&nbsp;Number</font> </nobr></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                </table>
                              </td>
                              <td bgcolor="#8F8FAB" width="1" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="300" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="348" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Special 
                                      Instructions </font></b><font color="#FFFFFF">(To 
                                      Recipient)</font></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" bgcolor="#F2F2F7" align="center"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="125" align="center"> 
                                      <textarea name="Instructions" cols="25" class="textarea1" rows="5">$SavedInstructions</textarea>
                                    </td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                </table>
                              </td>
                              <td bgcolor="#8F8FAB" width="1" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="300" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="348" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Courier</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="65" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">Select 
                                      the courier to use for this specific shipping 
                                      location. Everytimea different option is 
                                      chosen, the 'Courier Package' list below 
                                      is re-generated accordingly.</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="45" align="center"> 
                                      <select name="Courier" class="inputtext" onChange="getPackages();">
EOF
}

## WHICH STATE IS CHOSEN?
@Couriers = ("FEDEX","UPS");
foreach $Courier (@Couriers) {
	if ($Courier eq "$SavedCourier") { print "<option value=\"$Courier\" SELECTED>$Courier</option>"; }
	else { print "<option value=\"$Courier\">$Courier</option>"; }
}

{
print <<EOF
                                      </select>
                                    </td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                </table>
                              </td>
                              <td bgcolor="#8F8FAB" width="1" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="300" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="348" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Courier 
                                      Ship Package </font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="65" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">Select 
                                      the Courier Package that suits your needs. 
                                      If you have not yet typed in a 'Shipping 
                                      Address Zip', you will receive a prompt 
                                      to do so when you select an option from 
                                      this list.</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="45" align="center"> 
                                      <select name="Package" class="inputtext" onChange="getPrice();">
EOF
}

if ($SavedCourier eq "UPS") {
	## WHICH ExtraAccess rights are granted?
	$count=0;
	@Packages = ("1DM,Next Day Air Early AM","1DA,Next Day Air","2DA,2nd Day Air","3DS,3 Day Select","GNDCOM,Ground Commercial","GNDRES,Ground Residential");
	foreach $Type (@Packages) {
		$count++;
   		# Split the pair up into individual variables.
   		local($value, $name) = split(/,/, $Type);
		if ($SavedShipType =~ "$value") { 
			print "<option value=\"$value\" SELECTED>$name</option>"; 
		}
		else { 
			print "<option value=\"$value\">$name</option>"; 
		}
	}
}
else {

}

{
print <<EOF
                                      </select>
                                    </td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                </table>
                              </td>
                              <td bgcolor="#8F8FAB" width="1" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="300" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="348" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Price 
                                      Per Pound</font></b><font color="#FFFFFF"> 
                                      (from CM to Destination)</font></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="45" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">This 
                                      field will be filled in automatically when 
                                      you select a 'Courier Package' from the 
                                      previous list.</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"> <nobr> <font face="verdana,arial,helvetica" size="1" color="#333366">\$</font> 
                                      <input type="text" name="ShipPrice" size="7" class="inputtext7" value="$SavedShipPrice">
                                      <font face="verdana,arial,helvetica" size="1" color="#333366">per/lb.</font></nobr></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                </table>
                              </td>
                              <td bgcolor="#8F8FAB" width="1" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                        </td>
                      </tr>
                    </table>
                </td>
              </tr>
              <tr bordercolor="#333366" bgcolor="#F2F2F7"> 
                  <td align="center" valign="middle" height="45" bordercolor="#333366" bgcolor="#F2F2F7"> 
                    <input type="submit" value="Save Shipping Location" name="submit" class="inputbut">
                    <input type="reset" value="Reset Form" name="reset" class="inputbut">
                    &nbsp;&nbsp;</td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
        <br>
    </td>
  </tr>
</table>
<table width="100%" background="images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0"><tr><td width="55%" align="left" height="56">&nbsp;</td></tr></table>
</form>
</body>
</html>

EOF
}

}
$sth->finish;
$dbh->disconnect;


exit;
}

## ------------->>> if no useful calls present frameset
else {
$CMCustNum = "$FORM{'CMCustNum'}";
$ShippingID = "$FORM{'ShippingID'}";
if (($CMCustNum eq "") || ($CMCustNum eq " ") || ($CMCustNum < 0)) {
	print "Sorry, you must have a CM Customer Number attached to your call to this script...";
	exit;
}
else {

{
print <<EOF

<html>
<head>
<title>Shark Tank Admin System - Shipping Locations</title>
</head>
<frameset rows="64,*,5" rows="*" border="0" framespacing="0"> 
<frame name="topOne" scrolling="NO" noresize src="topper.cgi" marginwidth="0" marginheight="0" frameborder="NO">


EOF
}

use DBI;
my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
$dbh->{RaiseError} = 1; 
## get company name for this CMCustNum
my $sth = $dbh->prepare("SELECT * FROM Customers WHERE CMCustNum='$CMCustNum'");
$sth->execute or die "Unable to execute query\n"; 
my @row;
while(@row = $sth->fetchrow_array) { 
	my $AdminUser = $row[4];
	my $CompanyName = $row[6];
	print "<frame name=\"botOne\" src=\"$script?enformthee=1&CMCustNum=$CMCustNum&CompanyName=$CompanyName&ShippingID=$ShippingID&AdminUser=$AdminUser\" frameborder=\"NO\" marginheight=\"0\" marginwidth=\"0\" scrolling=\"AUTO\">";
}
$sth->finish;
$dbh->disconnect;

{
print <<EOF

<frame name="xtraOne" src="$script?blank=1" frameborder="NO" marginheight="0" marginwidth="0" scrolling="AUTO">
</frameset>
<noframes><body bgcolor="#FFFFFF">
</body></noframes>
</html>

EOF
}

}
exit;
}


sub topper {
{
print <<EOF

<html>
<head>
<title>Shark Tank Admin System - Shipping Locations</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<SCRIPT LANGUAGE="JavaScript">
// QUICK CROSS-BROWSER MOUSE-OVER/OFF FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function imageOff(which,thisone) {
	var cual = 	"images/button_"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}
function imageOn(which,thisone) {
	var cual = 	"images/button_"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}
</script>
$MenuConfig
</head>

<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
$MenuConstructor
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%" valign="top"><img src="images/illus_main.jpg" width="250" height="100"></td>
    <td width="25%">&nbsp;</td>
    <td align="left" valign="top"><img src="images/title_main.jpg" width="300" height="100"></td>
  </tr>
</table>
<table width="100%" border="0" height="100%" cellpadding="0" cellspacing="0">
  <tr valign="top"> 
    <td width="20%"><br>$legal</td>
    <td align="center" width="80%"> 
      <table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="50%"><font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update Shipping Location</b></font></td>
          <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
              <tr bordercolor="#333366"> 
                <td width="50%" align="center" valign="top" height="250"><font face="verdana,arial,helvetica" size="1" color="#333366"> 
EOF
}
}
exit;

sub bottom {
{
print <<EOF

</font>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
      <br>
    </td>
  </tr>
</table>
</body>
</html>

EOF
}
}
exit;