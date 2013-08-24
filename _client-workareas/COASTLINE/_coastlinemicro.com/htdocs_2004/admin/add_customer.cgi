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
if (($Cookies{'UserType'} eq "CMManage") || ($Cookies{'UserType'} eq "CMAdmin") || ($Cookies{'UserType'} eq "CMSales") || ($Cookies{'ExtraAccess'} =~ "AdminCust")) { $nextone = "1"; }
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
$MenuConfig = `cat js/menu_config.js`;
$MenuConstructor = `cat js/menu_constructor.js`;
$MenuConfig = "<script langauage=\"Javascript\">\n$MenuConfig\n</script>";
$MenuConstructor = "<script langauage=\"Javascript\">\n$MenuConstructor\n</script>";

## get CM legal piece
$legal = `cat legal.nsf`;

## If data present scan it...
if (($FORM{'CMCustNum'}) && ($FORM{'CompanyName'}) && ($FORM{'RepID'}) && ($FORM{'CompanyType'})) {

## TOP HTML TEMPLATE
&topper;

	## Crumble Form Input to Variables
	my $CMCustNum = "$FORM{'CMCustNum'}";
	my $CompanyName = "$FORM{'CompanyName'}";
	my $RepID = "$FORM{'RepID'}";
	my $CompanyType = "$FORM{'CompanyType'}";
	my $Phone = "$FORM{'Phone'}";
	my $Fax = "$FORM{'Fax'}";
	my $MailAdd = "$FORM{'MailAdd'}";
	my $MailAdd2 = "$FORM{'MailAdd2'}";
	my $MailCity = "$FORM{'MailCity'}";
	my $MailState = "$FORM{'MailState'}";
	my $MailZip = "$FORM{'MailZip'}";
	my $PayOption = "$FORM{'PayTypes'}";	
	my $DesktopValue = "$FORM{'DesktopValue'}";
	my $ServerValue = "$FORM{'ServerValue'}";
	my $NotebookValue = "$FORM{'NotebookValue'}";
	my $MonitorValue = "$FORM{'MonitorValue'}";
	my $MemoryValue = "$FORM{'MemoryValue'}";
	my $HDriveValue = "$FORM{'HDriveValue'}";
	my $VideoValue = "$FORM{'VideoValue'}";
	my $PeriphValue = "$FORM{'PeriphValue'}";
	my $PrinterValue = "$FORM{'PrinterValue'}";
	my $SoftwareValue = "$FORM{'SoftwareValue'}";
	my $ActionUser = "$Cookies{'Username'}";

##----------->>> Start Customer Account Check, make sure no dupes are made
	use DBI;
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $count=0;
	my $sth = $dbh->prepare("SELECT * FROM Customers");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		my $SavedCMCustNum = $row[1];
		my $SavedAdminID = $row[4];
		my $SavedCompanyName = $row[6];
		my $SavedPhone = $row[8];
		my $SavedMailCity = $row[12];
		my $SavedMailState = $row[13];
		my $SavedAddedBy = $row[35];
		## Re-Structure data as necessary
		my $Zip4 = substr($SavedMailZip, 0, 5);
		my $ZipMore = substr($SavedMailZip, 5, 8);
		my $AreaCode = substr($SavedPhone, 0, 3);
		my $PhoneNum3 = substr($SavedPhone, 3, 3);
		my $PhoneNum4 = substr($SavedPhone, 6, 4);
		
## ---------->>> IF EXISTS DIE PRINT OUT RECORD(s) THAT MATCH REQUEST
		if (($SavedCMCustNum eq $CMCustNum) || ($SavedCompanyName eq $CompanyName)) {
{
print <<EOF

            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
              <tr bordercolor="#333366"> 
                <td width="50%" align="center" valign="top" height="250"> 
                  <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr> 
                      <td width="100%"><font face="verdana,arial,helvetica" size="1" color="#333366"><br><b>Error Description</b><br><br>
                        While trying to complete your addition request we found 
                        a Company record that mathces the information you are 
                        submitting. Following is the record that matches your 
                        request's parameters: </font><font face="verdana,arial,helvetica" size="1" color="#333366"><br>
                        <br>
                        <center><font color="#EB0000">*The red text denotes the record's 
                        matching field(s).</font></center>
                        </font><br>
                        <table width="100%" border="1" bordercolor="#333366" cellspacing="0" cellpadding="0" align="center" bgcolor="#F2F2F7">
						<tr><td width="100%">
                        <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                          <tr> 
                            <td width="35%" height="20"><font class="stextbig"><b>Matching Customer Record(s)</b></font></td>
                            <td align="right" width="65%"><font class="stext2"><b></b></font></td>
                          </tr>
                          <tr> 
                            <td colspan="2" height="1" bgcolor="#333366"><img src="images/spacer.gif" width="1" height="1"></td>
                          </tr>
                          <tr> 
                            <td colspan="2" height="15"><img src="images/spacer.gif" width="1" height="15"></td>
                          </tr>
                          <tr> 
                            <td colspan="2" align="left" width="100%"> 
	<table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
<tr width="100%"><td width="100%">
<table width="100%" height="35" border="1" bordercolor="#333366" cellspacing="1" cellpadding="3" align="center" bgcolor="#ffffff">
<tr height="20" width="100%" bgcolor=\"#F2F2F7\">
<td align="center" width="15%"><font class="sresults1"><b>CM #</b><br></font></td>
<td align="center" width="25%"><font class="sresults1"><b>Company Name</b></font></td>
<td align="center" width="15%"><font class="sresults1"><b>Admin ID</b></font></td>
<td align="center" width="15%"><font class="sresults1"><b>City</b></font></td>
<td align="center" width="15%"><font class="sresults1"><b>State</b></font></td>
<td align="center" width="15%"><font class="sresults1"><b>Phone</b></font></td>
</tr>

EOF
}

			if ($SavedCMCustNum eq $CMCustNum) { $SavedCMCustNum = "<font color=\"red\">$SavedCMCustNum</font>"}
			if ($SavedCompanyName eq $CompanyName) { $SavedCompanyName = "<font color=\"red\">$SavedCompanyName</font>"}
			if ($ZipMore > 0) { $ZipMore = "-$ZipMore"}
			$count++;
			print "<tr width=\"100%\">";
			print "<td><font class=\"stextbig\" width=\"15%\"><b>$SavedCMCustNum&nbsp;</b></font></td>";
			print "<td><font class=\"stextbig\" width=\"25%\">$SavedCompanyName&nbsp;</font></td>";
			print "<td><font class=\"stextbig\" width=\"15%\">$SavedAdminID&nbsp;</font></td>";
			print "<td><font class=\"stextbig\" width=\"15%\">$SavedMailCity&nbsp;</font></td>";
			print "<td><font class=\"stextbig\" width=\"15%\">$SavedMailState&nbsp;</font></td>";
			print "<td><font class=\"stextbig\" width=\"15%\">($AreaCode) $PhoneNum3-$PhoneNum4&nbsp;</font></td>";
			print "</tr>";
			$dbh->disconnect;
			$sth->finish;
			print "</table>";
			print "<center><form><input type=\"button\" value=\"Try Again\" onClick=\"javascript:history.go(-1)\" class=\"inputbut\"><br><br><input type=\"button\" value=\"Cancel Account Addition\" onClick=\"javascript:parent.location.href='index.cgi'\" class=\"inputbut\"></form></center>";
			print "</td></tr>";
			print "</table>";
			
## END PAGE TEMPLATE
&bottom;

			exit;
		}
	}
	$sth->finish;
	$dbh->disconnect;
## ---------->>> IF EXISTS SCRIPT IS DEAD BY NOW
	
## ---------->>> IF NOT EXIST ADD IT
{
print <<EOF

            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
              <tr bordercolor="#333366"> 
                <td width="50%" align="center" valign="top" height="250"> 
                  <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr> 
                      <td width="100%"><font face="verdana,arial,helvetica" size="1" color="#333366">
					  
EOF
}
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("INSERT INTO Customers (CustomerID, CMCustNum, ShippingID, 
							 RepID, AdminID, MessageID, CompanyName, CompanyType, 
							 Phone, Fax, MailAdd, MailAdd2, MailCity, MailState, MailZip, 
							 PayOption, CCVisaName, CCVisa, CCVisaExp, CCMasterName, 
							 CCMaster, CCMasterExp, CCAmexName, CCAmex, CCAmexExp, 
							 DesktopValue, ServerValue, NotebookValue, MonitorValue, 
							 MemoryValue, HDriveValue, VideoValue, PeriphValue, 
							 PrinterValue, SoftwareValue, AddedBy, AddedOn, ModifiedBy, 
							 ModifiedOn, DeletedBy, DeletedOn)

							 VALUES (Null, '$CMCustNum', Null, '$RepID', Null, Null, 
							 '$CompanyName', '$CompanyType', '$Phone', '$Fax', 
							 '$MailAdd', '$MailAdd2', '$MailCity', '$MailState', '$MailZip', 
							 '$PayOption', '', '', '', '', '', '', '', '', '', 
							 '$DesktopValue', '$ServerValue', '$NotebookValue', 
							 '$MonitorValue', '$MemoryValue', '$HDriveValue', 
							 '$VideoValue', '$PeriphValue', '$PrinterValue', 
							 '$SoftwareValue', '$ActionUser', Null, '', '', '', 
							 '')");

	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish; 
	print "<b><br>Create Customer Account</b><br><br>The account for <b>$CompanyName</b> has been created successfully. Now you must create a User Account for the administrator of this new company account's users and profile configurations. This account will control the entire configuration and administration for the company account. Either a CM Manager or Admin and/or the company admin can change this setting in the future.<br>";
	print "<br><br>";
	print "<center><form><input type=\"button\" value=\"Create Admin Account\" onClick=\"javascript:location.href='add_user.cgi?enformthee=1&AddAdmin=1&CMCustNum=$CMCustNum&CompanyName=$CompanyName'\" class=\"inputbut\"></form></center></font>";
	$dbh->disconnect; 

## END PAGE TEMPLATE
&bottom;

exit;
}

## If no resident form processing calls are given continue
elsif ($FORM{'enformthee'}) {

{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - Shark Tank Admin System - Customer Accounts</title>
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

function checkForm() {
var missingdrop = "";
var thefirst = "";

// Check Common form fields
if (document.add.CompanyName.value == "" || document.add.CompanyName.value == " ") {
    missingdrop += "\\n     - Company Name";
	thefirst = "CompanyName";
}

if (document.add.CMCustNum.value == "" || document.add.CMCustNum.value == " ") {
    missingdrop += "\\n     - CM Customer Number";
	if (thefirst == "") { thefirst = "CMCustNum"; }
}

if (document.add.MailAdd.value == "" || document.add.MailAdd.value == " ") {
    missingdrop += "\\n     - Mailing Address";
	if (thefirst == "") { thefirst = "MailAdd"; }
}

if (document.add.MailCity.value == "" || document.add.MailCity.value == " ") {
    missingdrop += "\\n     - City";
	if (thefirst == "") { thefirst = "MailCity"; }
}

if (isNaN(document.add.MailZip.value) || (document.add.MailZip.value == "") || (document.add.MailZip.value == " ") || (document.add.MailZip.value.length != 5)) {
    missingdrop += "\\n     - Zip Code must be a 5 digit number";
	if (thefirst == "") { thefirst = "MailZip"; }
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

// -------------------------->>> PERL STARTS 
EOF
}
## -------------------------->>> WITH JAVASCRIPT FORM CHECK FOR PayOption CONFIGURATION - FOR THOSE WITH PayOption ADMIN RIGHTS
if (($Cookies{'UserType'} eq "CMManage") || ($Cookies{'UserType'} eq "CMAdmin")  || ($Cookies{'ExtraAccess'} =~ "PayOptions")) {

{
print <<EOF
// -------------------------->>> PERL ENDS

// Check GRANTED PayOptions
var strValues = "";
	var boxLength = document.add.PayOption.length;
	var count = 0;
if (boxLength != 0) {
	for (i = 0; i < boxLength; i++) {
		if (count == 0) {
			strValues = document.add.PayOption.options[i].value;
		}
		else {
			strValues = strValues + "," + document.add.PayOption.options[i].value;
		}
	count++;
   }
}
else {
    missingdrop += "\\n     - Payment Options\\n        *Select at least one option";
	if (thefirst == "") { thefirst = "PayOption"; }
}
if (strValues.length == 0) {
}
else {
	// Grab selected fields from PayOption and make PayTypes form field for processing
	document.add.PayTypes.value = strValues;
}

// -------------------------->>> PERL STARTS
EOF
}
}

{
print <<EOF
// -------------------------->>> PERL ENDS

// Check markup values if one is missing add error message tp MissingValues variable
var missingvalue = "";
if (isNaN(document.add.DesktopValue.value) || document.add.DesktopValue.value <= 0 || document.add.DesktopValue.value >= 100) {
    missingvalue += "\\n           - Desktop PCs";
	if (thefirst == "") { thefirst = "DesktopValue"; }
}
if (isNaN(document.add.ServerValue.value) || document.add.ServerValue.value <= 0 || document.add.DesktopValue.value >= 100) {
    missingvalue += "\\n           - Servers";
	if (thefirst == "") { thefirst = "ServerValue"; }
}
if (isNaN(document.add.NotebookValue.value) || document.add.NotebookValue.value <= 0 || document.add.NotebookValue.value >= 100) {
    missingvalue += "\\n           - Notebooks";
	if (thefirst == "") { thefirst = "NotebookValue"; }
}
if (isNaN(document.add.MonitorValue.value) || document.add.MonitorValue.value <= 0 || document.add.MonitorValue.value >= 100) {
    missingvalue += "\\n           - Monitors";
	if (thefirst == "") { thefirst = "MonitorValue"; }
}
if (isNaN(document.add.MemoryValue.value) || document.add.MemoryValue.value <= 0 || document.add.MemoryValue.value >= 100) {
    missingvalue += "\\n           - Memory";
	if (thefirst == "") { thefirst = "MemoryValue"; }
}
if (isNaN(document.add.HDriveValue.value) || document.add.HDriveValue.value <= 0 || document.add.HDriveValue.value >= 100) {
    missingvalue += "\\n           - Hard Drives";
	if (thefirst == "") { thefirst = "HDriveValue"; }
}
if (isNaN(document.add.VideoValue.value) || document.add.VideoValue.value <= 0 || document.add.VideoValue.value >= 100) {
    missingvalue += "\\n           - Video Cards";
	if (thefirst == "") { thefirst = "VideoValue"; }
}
if (isNaN(document.add.PeriphValue.value) || document.add.PeriphValue.value <= 0 || document.add.PeriphValue.value >= 100) {
    missingvalue += "\\n           - Peripherals";
	if (thefirst == "") { thefirst = "PeriphValue"; }
}
if (isNaN(document.add.PrinterValue.value) || document.add.PrinterValue.value <= 0 || document.add.PrinterValue.value >= 100) {
    missingvalue += "\\n           - Printers";
	if (thefirst == "") { thefirst = "PrinterValue"; }
}
if (isNaN(document.add.SoftwareValue.value) || document.add.SoftwareValue.value <= 0 || document.add.SoftwareValue.value >= 100) {
    missingvalue += "\\n           - Software";
	if (thefirst == "") { thefirst = "SoftwareValue"; }
}

// Whatever markup values are missing get printed out along with the Payment Options title
if (missingvalue != "") {
    missingdrop += "\\n     - Markup Values must be (1-99) only";
    missingdrop += missingvalue;
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

function jumpOption() {
PayOption = document.forms[0].PayOption;
PayOptions = document.forms[0].PayOptions; 
var sizer = PayOption.length;
for(var i = 0; i < PayOptions.length; i++) {
if ((PayOptions.options[i] != null) && (PayOptions.options[i].selected)) {
var there = false;
for(var count = 0; count < sizer; count++) {
if (PayOption.options[count] != null) {
if (PayOptions.options[i].text == PayOption.options[count].text) {
there = true;
break;
      }
   }
}
if (there != true) {
PayOption.options[sizer] = new Option(PayOptions.options[i].text); 
PayOption.options[sizer].value = PayOptions.options[i].value;
sizer++;
         }
      }
   }
}

function killOption() {
var PayOption  = document.forms[0].PayOption;
var sizer = PayOption.options.length;
for(var i = (sizer-1); i >= 0; i--) {
if ((PayOption.options[i] != null) && (PayOption.options[i].selected == true)) {
PayOption.options[i] = null;
      }
   }
}

function checkOptions() {
CompanyType = document.forms[0].CompanyType; 
RepID = document.forms[0].RepID; 
PayOption = document.forms[0].PayOption;
PayOptions = document.forms[0].PayOptions; 
var sizer = PayOption.length;
for(var i = 0; i < PayOptions.length; i++) {
for(var count = 0; count < sizer; count++) {
if (PayOptions.options[i] != null) {
if (PayOption.options[count] != null) {
if (PayOption.options[count].text == PayOptions.options[i].value) {
PayOption.options[count] = new Option(PayOptions.options[i].text); 
PayOption.options[count].value = PayOptions.options[i].value;
sizer++;
      		}
   		  }
		}
      }
   }
// CLEARS DEFAULT DATA FOR SECONDARY SELECT
if (CompanyType.options[0].value == "BIGNULL") { CompanyType.options[0] = null; }
if (RepID.options[0].value == "BIGNULL") { RepID.options[0] = null; }
if (PayOption.options[0].value == "BIGNULL") { PayOption.options[0] = null; }
if (PayOptions.options[0].value == "BIGNULL") { PayOptions.options[0] = null; }
}

// -------------------------->>> PERL STARTS 
EOF
}

## -------------------------->>> WITHOUT ONLOAD JAVASCRIPT PROMPT - FOR THOSE WITH PayOption ADMIN RIGHTS
if (($Cookies{'UserType'} eq "CMManage") || ($Cookies{'UserType'} eq "CMAdmin") || ($Cookies{'ExtraAccess'} =~ "PayOptions")) { $next=1; }
## -------------------------->>> WITH ONLOAD JAVASCRIPT PROMPT - FOR THOSE WITHOUT PayOption ADMIN RIGHTS
else {
{
print <<EOF
// -------------------------->>> PERL ENDS

var selectoption = "";
selectoption = "______________________________________________________________________________________                   " + "\\nYou have access to add customers to the system, yet you do not have access to grant Payment Options to customers in the system. Please make sure a CM Manager or Accounting Rep can configure the Payment Options for this account for you as soon as you are finished with the customer addition process. All CM Accounting Staff will recieve a reminder to do so everytime they log on to the system until the request is fulfilled." + "\\n______________________________________________________________________________________";
alert(selectoption);

// -------------------------->>> PERL STARTS
EOF
}
}

{
print <<EOF
// -------------------------->>> PERL ENDS
</SCRIPT>
$MenuConfig
</head>

EOF
}

## -------------------------->>> WITH ONLOAD JAVASCRIPT CHECK - FOR THOSE WITH PayOption ADMIN RIGHTS
if (($Cookies{'UserType'} eq "CMManage") || ($Cookies{'UserType'} eq "CMAdmin") || ($Cookies{'ExtraAccess'} =~ "PayOptions")) { print "<body TEXT=\"#333366\" LINK=\"#8F8FAB\" VLINK=\"#8F8FAB\" ALINK=\"#8F8FAB\" BGCOLOR=\"#ffffff\" leftmargin=\"0\" topmargin=\"0\" marginwidth=\"0\" marginheight=\"0\"  onLoad=\"javascript:checkOptions();\">"; }
## -------------------------->>> WITHOUT
else { print "<body TEXT=\"#333366\" LINK=\"#8F8FAB\" VLINK=\"#8F8FAB\" ALINK=\"#8F8FAB\" BGCOLOR=\"#ffffff\" leftmargin=\"0\" topmargin=\"0\" marginwidth=\"0\" marginheight=\"0\">"; }

{
print <<EOF

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
              Customer Account</b></font></td>
            <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
              <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER" bordercolor="#333366">
                <tr bordercolor="#333366" valign="middle"> 
                  <td width="50%" align="center" height="50" class="tableBG"><font face="verdana,arial,helvetica" size="1" color="#EB0000">*If 
                    you have any questions please ask your Supervisor or Manager 
                    for help using the system or updating it's information.</font> 
                    <font face="verdana,arial,helvetica" size="1" color="#333366"></font><font face="verdana,arial,helvetica" size="1" color="#333366"></font></td>
              </tr>
              <tr bordercolor="#333366"> 
                  <td width="50%" align="center" valign="top" bordercolor="#333366"> 
                    <table width="100%" border="0" cellspacing="0" cellpadding="5">
                      <tr> 
                        <td width="100%" align="center" height="25" bgcolor="#F2F2F7" class="tableBG" colspan="2"><font face="verdana,arial,helvetica" size="2" color="#333366"><b>Company 
                          Contact Information</b></font></td>
                      </tr>
                      <tr> 
                        <td align="center" valign="top"> <br>
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Company 
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
                                      <input type="text" name="CompanyName" size="15" class="inputtext15">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">CM 
                                      Customer Number</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="65" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">Type 
                                      in the CM Customer Number for the Company 
                                      being added to the system.<br>
                                      <br>
                                      <center>
                                        <font color="#EB0000">Must match all records</font> 
                                      </center>
                                      </font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"> 
                                      <input type="text" name="CMCustNum" size="15" class="inputtext15">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Company 
                                      Type</font></b></font></td>
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
                                      <select name="CompanyType" class="inputtext">
									    <option value="BIGNULL">0000000000000000</option>
                                        <option value="Small" SELECTED>Small (1-100 Users)</option>
                                        <option value="Medium">Medium (100-1000 Users)</option>
                                        <option value="Corp">Corporation (1000+ Users)</option>
                                        <option value="Reseller">Reseller</option>
                                        <option value="Consult">Consultant</option>
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Primary 
                                      Business Phone Number</font></b></font></td>
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
                                      <input type="hidden" name="Phone">
                                      <nobr> 
                                      <input type="text" name="TelArea" size="3" class="inputtext3">
                                      <input type="text" name="TelNum" size="7" class="inputtext7">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Primary 
                                      Business Fax Number</font></b></font></td>
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
                                      <input type="hidden" name="Fax" value="">
                                      <nobr> 
                                      <input type="text" name="FaxArea" size="3" class="inputtext3">
                                      <input type="text" name="FaxNum" size="7" class="inputtext7">
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
                        </td>
                        <td align="center" valign="top"> <br>
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Business 
                                      Mailing Address</font></b></font></td>
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
                                      <input type="text" name="MailAdd" size="15" class="inputtext15">
                                      </nobr><br>
                                      <nobr><font face="verdana,arial,helvetica" size="1" color="#333366">Line 
                                      2:</font> 
                                      <input type="text" name="MailAdd2" size="15" class="inputtext15">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Mailing 
                                      Address City</font></b></font></td>
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
                                      <input type="text" name="MailCity" size="15" class="inputtext15">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Mailing 
                                      Address Zip</font></b></font></td>
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
                                      <input type="text" name="MailZip" size="7" class="inputtext7">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Mailing 
                                      Address State</font></b></font></td>
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
                                      <select name="MailState" class="inputtext">
                                        <option value="AK">AK</option>
                                        <option value="AL">AL</option>
                                        <option value="AR">AR</option>
                                        <option value="AZ">AZ</option>
                                        <option value="CA" SELECTED>CA</option>
                                        <option value="CO">CO</option>
                                        <option value="CT">CT</option>
                                        <option value="DC">DC</option>
                                        <option value="DE">DE</option>
                                        <option value="FL">FL</option>
                                        <option value="GA">GA</option>
                                        <option value="HI">HI</option>
                                        <option value="IA">IA</option>
                                        <option value="ID">ID</option>
                                        <option value="IL">IL</option>
                                        <option value="IN">IN</option>
                                        <option value="KS">KS</option>
                                        <option value="KY">KY</option>
                                        <option value="LA">LA</option>
                                        <option value="MA">MA</option>
                                        <option value="MD">MD</option>
                                        <option value="ME">ME</option>
                                        <option value="MI">MI</option>
                                        <option value="MN">MN</option>
                                        <option value="MO">MO</option>
                                        <option value="MS">MS</option>
                                        <option value="MT">MT</option>
                                        <option value="NC">NC</option>
                                        <option value="ND">ND</option>
                                        <option value="NE">NE</option>
                                        <option value="NH">NH</option>
                                        <option value="NJ">NJ</option>
                                        <option value="NM">NM</option>
                                        <option value="NV">NV</option>
                                        <option value="NY">NY</option>
                                        <option value="OH">OH</option>
                                        <option value="OK">OK</option>
                                        <option value="OR">OR</option>
                                        <option value="PA">PA</option>
                                        <option value="RI">RI</option>
                                        <option value="SC">SC</option>
                                        <option value="SD">SD</option>
                                        <option value="TN">TN</option>
                                        <option value="TX">TX</option>
                                        <option value="UT">UT</option>
                                        <option value="VA">VA</option>
                                        <option value="VT">VT</option>
                                        <option value="WA">WA</option>
                                        <option value="WI">WI</option>
                                        <option value="WV">WV</option>
                                        <option value="WY">WY</option>
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">CM 
                                      Primary Account Representative</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="45" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">Choose 
                                      a Primary Account Representative for this 
                                      new customer account.</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"> 
                                      <select name="RepID" class="inputtext">
									    <option value="BIGNULL">0000000000000000</option>
EOF
}
		## Get list of CM reps
		use DBI;
		my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
		$dbh->{RaiseError} = 1; 
		my $sth = $dbh->prepare("SELECT * FROM Users 
								 WHERE UserAccess = 'CMManage' 
								 OR UserAccess = 'CMAdmin' 
								 OR UserAccess = 'CMSales'
								 ORDER BY LastName ASC");
		$sth->execute or die "Unable to execute query\n"; 
		my @row;
		while(@row = $sth->fetchrow_array) { 
			my $UserID = $row[0];
			my $Username = $row[3];
			my $FirstName = $row[6];
			my $LastName = $row[7];
			print "
                                  <option value=\"$Username\">$LastName, $FirstName 
                                  ($Username)</option>";
		}
		$sth->finish;
		$dbh->disconnect;


## print closing html, dont forget tag
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
                          
                        </td>
                      </tr>
                      <tr> 
                        <td width="100%" align="center" height="27" bgcolor="#F2F2F7" class="tableBG" colspan="2"><font face="verdana,arial,helvetica" size="2" color="#333366"><b>Financial 
                          Information</b></font></td>
                      </tr>
                      <tr> 
                        <td width="50%" align="center" height="25" valign="top" class="tableBG"> 
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Product 
                                      Markup Values</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="125" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">The 
                                      markup values are what control a company's 
                                      specific product pricing. To understand 
                                      the logic behind this option you must ask 
                                      a Coastline Micro Supervisor or Manager. 
                                      All product categories must have a value 
                                      to add a new customer to the system.<br>
                                      <br>
                                      <center>
                                        <font color="#EB0000">* Range (1-99)<br>
                                        <br>
                                        * Peripherals is the Catch-All</font> 
                                      </center>
                                      </font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="45" align="center"> 
                                      <table width="280" border="0" cellspacing="0" cellpadding="0" bgcolor="#ffffff">
                                        <tr> 
                                          <td width="100" align="right" valign="middle" height="35"><nobr><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Desktop 
                                            PCs:&nbsp;&nbsp;&nbsp;</b></font></nobr></td>
                                          <td align="center" valign="middle" height="15" width="40"> 
                                            <input type="text" name="DesktopValue" size="3" class="inputtext3">
                                            <font face="verdana,arial,helvetica" size="1" color="#333366"><b>&nbsp;</b></font><font face="verdana,arial,helvetica" size="1" color="#333366"><b>&nbsp;</b></font> 
                                          </td>
                                          <td bgcolor="#8F8FAB" width="1" rowspan="10" valign="middle" height="35"><img src="images/verticalbar.gif" width="1" height="25"></td>
                                          <td width="100" align="right" height="35" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Servers: 
                                            &nbsp;&nbsp;</b></font></td>
                                          <td align="center" valign="middle" width="39"> 
                                            <input type="text" name="ServerValue" size="3" class="inputtext3">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="50%" valign="bottom" align="center" colspan="2" height="1" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="1" height="1"></td>
                                          <td width="50%" valign="bottom" align="center" colspan="2" height="1" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="1" height="1"></td>
                                        </tr>
                                        <tr> 
                                          <td width="100" align="right" valign="middle" height="35"><nobr><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Notebooks: 
                                            &nbsp;&nbsp;</b></font></nobr></td>
                                          <td align="center" valign="middle" height="15" width="40"> 
                                            <input type="text" name="NotebookValue" size="3" class="inputtext3">
                                            <font face="verdana,arial,helvetica" size="1" color="#333366"><b>&nbsp;</b></font> 
                                          </td>
                                          <td align="right" width="100" valign="middle" height="35"><nobr><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Monitors: 
                                            &nbsp;&nbsp;</b></font></nobr></td>
                                          <td align="center" valign="middle" width="39"> 
                                            <input type="text" name="MonitorValue" size="3" class="inputtext3">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="50%" align="center" colspan="2" height="1" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="1" height="1"></td>
                                          <td width="50%" align="center" colspan="2" height="1" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="1" height="1"></td>
                                        </tr>
                                        <tr> 
                                          <td width="100" align="right" valign="middle" height="35"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Memory: 
                                            &nbsp;&nbsp;</b></font></td>
                                          <td align="center" valign="middle" height="15" width="40"> 
                                            <input type="text" name="MemoryValue" size="3" class="inputtext3">
                                            <font face="verdana,arial,helvetica" size="1" color="#333366"><b>&nbsp;</b></font> 
                                          </td>
                                          <td width="100" align="right" valign="middle" height="35"><nobr><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Hard 
                                            Drives: &nbsp;&nbsp;</b></font></nobr></td>
                                          <td align="center" valign="middle" width="39"> 
                                            <input type="text" name="HDriveValue" size="3" class="inputtext3">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="50%" align="center" colspan="2" height="1" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="1" height="1"></td>
                                          <td width="50%" align="center" colspan="2" height="1" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="1" height="1"></td>
                                        </tr>
                                        <tr> 
                                          <td width="100" align="right" valign="middle" height="35"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Video 
                                            Cards: &nbsp;&nbsp;</b></font></td>
                                          <td align="center" valign="middle" height="15" width="40"> 
                                            <input type="text" name="VideoValue" size="3" class="inputtext3">
                                            <font face="verdana,arial,helvetica" size="1" color="#333366"><b>&nbsp;</b></font> 
                                          </td>
                                          <td width="100" align="right" valign="middle" height="35"><nobr><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Peripherals:&nbsp;&nbsp;&nbsp;</b></font></nobr></td>
                                          <td align="center" valign="middle" width="39"> 
                                            <input type="text" name="PeriphValue" size="3" class="inputtext3">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="50%" align="center" colspan="2" height="1" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="1" height="1"></td>
                                          <td width="50%" align="center" colspan="2" height="1" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="1" height="1"></td>
                                        </tr>
                                        <tr> 
                                          <td width="100" align="right" valign="middle" height="35"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Printers: 
                                            &nbsp;&nbsp;</b></font></td>
                                          <td align="center" valign="middle" height="15" width="40"> 
                                            <input type="text" name="PrinterValue" size="3" class="inputtext3">
                                            <font face="verdana,arial,helvetica" size="1" color="#333366"><b>&nbsp;</b></font> 
                                          </td>
                                          <td width="100" align="right" valign="middle" height="35"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Software: 
                                            &nbsp;&nbsp;</b></font></td>
                                          <td align="center" valign="middle" width="39"> 
                                            <input type="text" name="SoftwareValue" size="3" class="inputtext3">
                                          </td>
                                        </tr>
                                      </table>
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
                        </td>
                        <td width="50%" align="center" height="25" class="tableBG" valign="top">
EOF
}
## -------------------------->>> WITH PayOption FORM ELEMENTS - FOR THOSE WITH PayOption ADMIN RIGHTS
if (($Cookies{'UserType'} eq "CMManage") || ($Cookies{'UserType'} eq "CMAdmin")  || ($Cookies{'ExtraAccess'} =~ "PayOptions")) {

{
print <<EOF
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Approved 
                                      Payment Options</font></b><font color="#FFFFFF"> 
                                      (CM Admin Only)</font></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="95" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">To 
                                      grant permissions choose an item from the 
                                      'Available Options' list then click the 
                                      &gt;&gt;&gt;(Add) button.<br>
                                      <br>
                                      To remove a granted permission choose the 
                                      item you would like to remove from the 'Granted 
                                      Options' list then click the &lt;&lt;&lt;(Remove) 
                                      button.</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="45" align="center"> 
                                      <table width="280" border="0" cellspacing="0" cellpadding="0" bgcolor="#FFFFFF" align="center">
                                        <tr> 
                                          <td align="center" width="130"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Available 
                                            Options </b></font> </td>
                                          <td width="10" rowspan="3"><img src="images/spacer.gif" width="10" height="1"></td>
                                          <td bgcolor="#8F8FAB" width="1" rowspan="3"><img src="images/verticalbar.gif" width="1" height="25"></td>
                                          <td width="10" rowspan="3"><img src="images/spacer.gif" width="10" height="1"></td>
                                          <td align="center" width="129"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Granted 
                                            Options</b></font> </td>
                                        </tr>
                                        <tr> 
                                          <td width="130" valign="top" align="center"> 
                                            <select name="PayOptions" size="8" multiple width="20" class="multiselect">
                                              <option value="BIGNULL">0000000000000000</option>
                                              <option value="Cash">Cash</option>
                                              <option value="Check">Company Check</option>
                                              <option value="CCMaster">MasterCard</option>
                                              <option value="CCVisa">Visa</option>
                                              <option value="CCAmex">American Express</option>
                                              <option value="Net30">Net30</option>
                                              <option value="Net10">Net10</option>
                                              <option value="Net5">Net5</option>
                                            </select>
                                          </td>
                                          <td width="129" valign="bottom" align="center"> 
                                            <select name="PayOption" size="8" multiple class="multiselect">
                                              <option value="BIGNULL">0000000000000000</option>
                                              <option value="Cash">Cash</option>
                                              <option value="Check">Company Check</option>
                                              <option value="CCMaster">MasterCard</option>
                                              <option value="CCVisa">Visa</option>
                                              <option value="CCAmex">American Express</option>
                                            </select>
                                            <input type="hidden" name="PayTypes" value="">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="130" valign="bottom" align="center"> 
                                            <input type="Button" value=" >>> " onClick="javascript:jumpOption();" class="inputbut" name="Button">
                                          </td>
                                          <td width="129" valign="bottom" align="center"> 
                                            <input type="Button" value=" <<< " onClick="javascript:killOption();" class="inputbut" name="Button2">
                                          </td>
                                        </tr>
                                      </table>
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
EOF
}
}

## -------------------------->>> WITHOUT PayOption FORM ELEMENTS - FOR THOSE WITHOUT PayOption ADMIN RIGHTS
else { print "&nbsp;"; }

{
print <<EOF
                          <br>
                          <br>
                        </td>
                      </tr>
                    </table>
                </td>
              </tr>
              <tr bordercolor="#333366" bgcolor="#F2F2F7"> 
                  <td align="center" valign="middle" height="45" width="100%" bordercolor="#333366" bgcolor="#F2F2F7"> 
                    <input type="submit" value="Save Customer Profile" name="submit" class="inputbut">
                    <input type="reset" value="Reset Form" name="reset" class="inputbut">
                    &nbsp;</td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
        <br>
    </td>
  </tr>
</table>
  <table width="100%" background="images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0">
    <tr> 
      <td width="55%" align="left" height="56">&nbsp;</td>
    </tr>
  </table>
</form>
</body>
</html>

EOF
}
exit;
}

## if no useful calls present frameset
else {
{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - Shark Tank Admin System - Add Customer</title>
</head>
<frameset rows="64,*" rows="*" border="0" framespacing="0"> 
<frame name="topOne" scrolling="NO" noresize src="topper.cgi" marginwidth="0" marginheight="0" frameborder="NO">
<frame name="botOne" src="$script?enformthee=1" frameborder="NO" marginheight="0" marginwidth="0" scrolling="AUTO">
</frameset>
<noframes><body bgcolor="#FFFFFF">
</body></noframes>
</html>

EOF
}
exit;
}

sub topper {
{
print <<EOF
<html>
<head>
<title>Coastline Micro, Inc. - Shark Tank Admin System - Customer Accounts</title>
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
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>Create Customer Account</b></font></td>
          <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
EOF
}
}
exit;

sub bottom {
{
print <<EOF
                            </td>
                          </tr>
                          <tr> 
                            <td colspan="2" height="15"><img src="images/spacer.gif" width="1" height="15"></td>
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
    </td>
  </tr>
</table>
    </td>
  </tr>
</table>
<table width="100%" background="images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0"><tr><td width="55%" align="left" height="56">&nbsp;</td></tr></table>
</body>
</html>

EOF
}
}
exit;