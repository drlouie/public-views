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
if (($Cookies{'UserType'} eq "CMManage") || ($Cookies{'UserType'} eq "CMAdmin")) { $nextone = "1"; }
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
if (($FORM{'DROPIN'}) && ($FORM{'CMCustNum'}) && ($FORM{'CompanyName'})) {

## TOP HTML TEMPLATE
&topper;

	## Crumble Form Input to Variables
	my $CMCustNum = "$FORM{'CMCustNum'}";
	my $RepID = "$FORM{'TheReps'}";
	my $AdminID = "$FORM{'TheAdmin'}";
	my $CompanyName = "$FORM{'CompanyName'}";
	my $CompanyType = "$FORM{'CompanyType'}";
	my $Phone = "$FORM{'Phone'}";
	my $Fax = "$FORM{'Fax'}";
	my $MailAdd = "$FORM{'MailAdd'}";
	my $MailAdd2 = "$FORM{'MailAdd2'}";
	my $MailCity = "$FORM{'MailCity'}";
	my $MailState = "$FORM{'MailState'}";
	my $MailZip = "$FORM{'MailZip'}";
	my $PayOption = "$FORM{'PayTypes'}";	
	my $CCVisaName = "$FORM{'CCVisaName'}";	
	my $CCVisa = "$FORM{'CCVisa'}";	
	my $CCVisaExp = "$FORM{'CCVisaExp'}";	
	my $CCMasterName = "$FORM{'CCMasterName'}";	
	my $CCMaster = "$FORM{'CCMaster'}";	
	my $CCMasterExp = "$FORM{'CCMasterExp'}";	
	my $CCAmexName = "$FORM{'CCAmexName'}";	
	my $CCAmex = "$FORM{'CCAmex'}";	
	my $CCAmexExp = "$FORM{'CCAmexExp'}";	
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

{
print <<EOF

<table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update Customer Account</b></font></td>
          <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
              <tr bordercolor="#333366"> 
                <td width="50%" align="center" valign="top" height="250"> 
                  <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr> 
                      <td width="100%"><font face="verdana,arial,helvetica" size="1" color="#333366">
					  
EOF
}
	print "<center><br><b>View/Update Customer Account</b><br><br>The account for <b>$CompanyName</b> has been updated successfully.<br><br><form><input type=\"button\" value=\"Back to $CompanyName's Profile\" onClick=\"javascript:location.href='change_customer.cgi?CMCustNum=$CMCustNum&CompanyName=$CompanyName'\" class=\"inputbut\"><br></center>";
	print "<br><br></font>";
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("UPDATE LOW_PRIORITY Customers 
							 SET AdminID='$AdminID', 
							 RepID='$RepID', 
							 CompanyName='$CompanyName', 
							 CompanyType='$CompanyType', 
							 Phone='$Phone', 
							 Fax='$Fax', 
							 MailAdd='$MailAdd', 
							 MailAdd2='$MailAdd2', 
							 MailCity='$MailCity', 
							 MailState='$MailState', 
							 MailZip='$MailZip', 
							 PayOption='$PayOption', 
							 CCVisaName='$CCVisaName', 
							 CCVisa='$CCVisa', 
							 CCVisaExp='$CCVisaExp', 
							 CCMasterName='$CCMasterName', 
							 CCMaster='$CCMaster', 
							 CCMasterExp='$CCMasterExp', 
							 CCAmexName='$CCAmexName', 
							 CCAmex='$CCAmex', 
							 CCAmexExp='$CCAmexExp', 
							 DesktopValue='$DesktopValue', 
							 ServerValue='$ServerValue', 
							 NotebookValue='$NotebookValue', 
							 MonitorValue='$MonitorValue', 
							 MemoryValue='$MemoryValue', 
							 HDriveValue='$HDriveValue', 
							 VideoValue='$VideoValue', 
							 PeriphValue='$PeriphValue', 
							 PrinterValue='$PrinterValue', 
							 SoftwareValue='$SoftwareValue', 
							 ModifiedBy='$ActionUser', 
							 ModifiedOn=Null 
							 WHERE CMCustNum='$CMCustNum'");
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish; 
	$dbh->disconnect; 	
	
{
print <<EOF

                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
	  
EOF
}
	
## END PAGE TEMPLATE
&bottom;

exit;
}

## If DELETING
elsif (($FORM{'DELETEIT'}) && ($FORM{'CMCustNum'}) && ($FORM{'CompanyName'})) {

## TOP HTML TEMPLATE
&topper;

	## Crumble Form Input to Variables
	my $CMCustNum = "$FORM{'CMCustNum'}";
	my $CompanyName = "$FORM{'CompanyName'}";
	my $ActionUser = "$Cookies{'Username'}";

{
print <<EOF

<table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update Customer Account</b></font></td>
          <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
              <tr bordercolor="#333366"> 
                <td width="50%" align="center" valign="top" height="250"> 
                  <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr> 
                      <td width="100%"><font face="verdana,arial,helvetica" size="1" color="#333366">
					  
EOF
}
	print "<br><center><b>Delete Customer Account</b><br><br>The account for <b>$CompanyName</b> has been deleted from the system effective immediately.<br><br><form><input type=\"button\" value=\"Back to Home\" onClick=\"javascript:parent.location.href='index.cgi'\" class=\"inputbut\"><br></center>";
	print "<br><br></font>";
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("DELETE FROM Customers WHERE CMCustNum='$CMCustNum'");
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
	my $sth = $dbh->prepare("DELETE FROM Users WHERE CustomerID='$CMCustNum'");
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
	$dbh->disconnect;
	
{
print <<EOF

                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
	  
EOF
}
	
## END PAGE TEMPLATE
&bottom;

exit;
}

## If VIEWING
elsif ($FORM{'CMCustNum'} && $FORM{'CompanyName'}) {

	## Crumble Form Input to Variables
	my $CMCustNum = "$FORM{'CMCustNum'}";
	my $CompanyName = "$FORM{'CompanyName'}";
	my $ActionUser = "$Cookies{'Username'}";
	##----------->>> If checking information for new customer account... IE: Implementing Admin user to new customer account
	my $AdminUser = "$FORM{'AdminUser'}";

	##----------->>> Grab Customer Account Information
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $count=0;
	my $sth = $dbh->prepare("SELECT * FROM Customers WHERE CMCustNum='$CMCustNum'");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		my $SavedCMCustNum = $row[1];
		my $SavedShippingID = $row[2];
		my $SavedRepID = $row[3];
		my $SavedAdminID = $row[4];
		my $SavedMessageID = $row[5];
		my $SavedCompanyName = $row[6];
		my $SavedCompanyType = $row[7];
		my $SavedPhone = $row[8];
		my $SavedFax = $row[9];
		my $SavedMailAdd = $row[10];
		my $SavedMailAdd2 = $row[11];
		my $SavedMailCity = $row[12];
		my $SavedMailState = $row[13];
		my $SavedMailZip = $row[14];
		my $SavedPayOption = $row[15];
		## GET SAVED CC INFO
		my $SavedCCVisaName = $row[16];
		my $SavedCCVisa = $row[17];
		my $SavedCCVisaExp = $row[18];
		my $SavedCCMasterName = $row[19];
		my $SavedCCMaster = $row[20];
		my $SavedCCMasterExp = $row[21];
		my $SavedCCAmexName = $row[22];
		my $SavedCCAmex = $row[23];
		my $SavedCCAmexExp = $row[24];
		my $SavedDesktopValue = $row[25];
		my $SavedServerValue = $row[26];
		my $SavedNotebookValue = $row[27];		
		my $SavedMonitorValue = $row[28];		
		my $SavedMemoryValue = $row[29];		
		my $SavedHDriveValue = $row[30];		
		my $SavedVideoValue = $row[31];		
		my $SavedPeriphValue = $row[32];		
		my $SavedPrinterValue = $row[33];		
		my $SavedSoftwareValue = $row[34];		
		my $SavedAddedBy = $row[35];
		my $SavedAddedOn = $row[36];
		my $SavedModifiedBy = $row[37];
		my $SavedModifiedOn = $row[38];
		my $SavedDeletedBy = $row[39];
		my $SavedDeletedOn = $row[40];
		## Re-Structure data as necessary
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
		$count++;
##----------->>> IF Customer Account DELETED, Show user who deleted profile
if ($SavedDeletedBy != "" || $SavedDeletedBy != " " || $SavedDeletedOn > 0) {
	print "<b>Customer Profile Deleted By:</b> <input type=\"text\" name=\"DeletedBy\" size=\"7\" class=\"inputtext7\" value=\"$SavedDeletedBy\"><br>";
	print "<b>Deleted On:</b> <input type=\"text\" name=\"DeletedOn\" size=\"7\" class=\"inputtext7\" value=\"$DelMonth/$DelDay/$DelYear\"><br>";
}
##----------->>> ELSE read Customer Account Profile
else {

{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - Shark Tank Admin System - Add Customer</title>
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
if (document.change.CompanyName.value == "" || document.change.CompanyName.value == " ") {
    missingdrop += "\\n     - Company Name";
	thefirst = "CompanyName";
}

if (document.change.CMCustNum.value == "" || document.change.CMCustNum.value == " ") {
    missingdrop += "\\n     - CM Customer Number";
	if (thefirst == "") { thefirst = "CMCustNum"; }
}

if (document.change.MailAdd.value == "" || document.change.MailAdd.value == " ") {
    missingdrop += "\\n     - Mailing Address";
	if (thefirst == "") { thefirst = "MailAdd"; }
}

if (document.change.MailCity.value == "" || document.change.MailCity.value == " ") {
    missingdrop += "\\n     - City";
	if (thefirst == "") { thefirst = "MailCity"; }
}

if (isNaN(document.change.MailZip.value) || (document.change.MailZip.value == "") || (document.change.MailZip.value == " ") || (document.change.MailZip.value.length != 5)) {
    missingdrop += "\\n     - Zip Code must be a 5 digit number";
	if (thefirst == "") { thefirst = "MailZip"; }
}

// Check Phone number and format if it is there get the area code and num and feed the Phone field
if (isNaN(document.change.TelArea.value) || (document.change.TelArea.value == "") || (document.change.TelArea.value == " ") || (document.change.TelArea.value.length != 3)) {
    missingdrop += "\\n     - Phone's Area Code must be a 3 digit number";
	if (thefirst == "") { thefirst = "TelArea"; }
}
else if (isNaN(document.change.TelNum.value) || (document.change.TelNum.value == "") || (document.change.TelNum.value == " ") || (document.change.TelNum.value.indexOf('-') != -1) || (document.change.TelNum.value.length != 7)) {
    missingdrop += "\\n     - Phone Number must be a 7 digit number\\n        *No hyphen (-) necessary";
	if (thefirst == "") { thefirst = "TelNum"; }
}
else {
	PhoneValues = document.change.TelArea.value + document.change.TelNum.value;
	document.change.Phone.value = PhoneValues;
}

// Check Fax number and format if it is there get the area code and num and feed the Fax field
if (isNaN(document.change.FaxArea.value) || (document.change.FaxArea.value == "") || (document.change.FaxArea.value == " ") || (document.change.FaxArea.value.length != 3)) {
    missingdrop += "\\n     - Fax's Area Code must be a 3 digit number or 000\\n       to clear this error";
	if (thefirst == "") { thefirst = "FaxArea"; }
}
else if (isNaN(document.change.FaxNum.value) || (document.change.FaxNum.value == "") || (document.change.FaxNum.value == " ") || (document.change.FaxNum.value.indexOf('-') != -1) || (document.change.FaxNum.value.length != 7)) {
    missingdrop += "\\n     - Fax Number must be a 7 digit number or 0000000 to \\n       clear this error *No hyphen (-) necessary";
	if (thefirst == "") { thefirst = "FaxNum"; }
}
else {
	FaxValues = document.change.FaxArea.value + document.change.FaxNum.value;
	document.change.Fax.value = FaxValues;
}


// Check GRANTED PayOptions
var strValues = "";
	var boxLength = document.change.PayOption.length;
	var count = 0;
if (boxLength != 0) {
	for (i = 0; i < boxLength; i++) {
		if (count == 0) {
			strValues = document.change.PayOption.options[i].value;
		}
		else {
			strValues = strValues + "," + document.change.PayOption.options[i].value;
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
	document.change.PayTypes.value = strValues;
}


// Check THEADMIN
if (document.change.AdminID) {
var strValues = "";
	var boxLength = document.change.AdminID.length;
	var count = 0;
if (boxLength != 0) {
	for (i = 0; i < boxLength; i++) {
		if (count == 0) {
			strValues = document.change.AdminID.options[i].value;
		}
		else {
			strValues = strValues + "," + document.change.AdminID.options[i].value;
		}
	count++;
   }
}
else {
    missingdrop += "\\n     - Administrator is missing";
	if (thefirst == "") { thefirst = "AdminID"; }
}
if (strValues.length == 0) {
}
else {
	// Grab selected fields from AdminID and make TheAdmin form field for processing
	document.change.TheAdmin.value = strValues;
}
}

// Check THEREPS
var strValues = "";
	var boxLength = document.change.RepID.length;
	var count = 0;
if (boxLength != 0) {
	for (i = 0; i < boxLength; i++) {
		if (count == 0) {
			strValues = document.change.RepID.options[i].value;
		}
		else {
			strValues = strValues + "," + document.change.RepID.options[i].value;
		}
	count++;
   }
}
else {
    missingdrop += "\\n     - Please select at least one Account Rep";
	if (thefirst == "") { thefirst = "RepID"; }
}
if (strValues.length == 0) {
}
else {
	// Grab selected fields from RepID and make TheReps form field for processing
	document.change.TheReps.value = strValues;
}


// Check markup values if one is missing add error message tp MissingValues variable
var missingvalue = "";
if (isNaN(document.change.DesktopValue.value) || document.change.DesktopValue.value <= 0 || document.change.DesktopValue.value >= 100) {
    missingvalue += "\\n           - Desktop PCs";
	if (thefirst == "") { thefirst = "DesktopValue"; }
}
if (isNaN(document.change.ServerValue.value) || document.change.ServerValue.value <= 0 || document.change.DesktopValue.value >= 100) {
    missingvalue += "\\n           - Servers";
	if (thefirst == "") { thefirst = "ServerValue"; }
}
if (isNaN(document.change.NotebookValue.value) || document.change.NotebookValue.value <= 0 || document.change.NotebookValue.value >= 100) {
    missingvalue += "\\n           - Notebooks";
	if (thefirst == "") { thefirst = "NotebookValue"; }
}
if (isNaN(document.change.MonitorValue.value) || document.change.MonitorValue.value <= 0 || document.change.MonitorValue.value >= 100) {
    missingvalue += "\\n           - Monitors";
	if (thefirst == "") { thefirst = "MonitorValue"; }
}
if (isNaN(document.change.MemoryValue.value) || document.change.MemoryValue.value <= 0 || document.change.MemoryValue.value >= 100) {
    missingvalue += "\\n           - Memory";
	if (thefirst == "") { thefirst = "MemoryValue"; }
}
if (isNaN(document.change.HDriveValue.value) || document.change.HDriveValue.value <= 0 || document.change.HDriveValue.value >= 100) {
    missingvalue += "\\n           - Hard Drives";
	if (thefirst == "") { thefirst = "HDriveValue"; }
}
if (isNaN(document.change.VideoValue.value) || document.change.VideoValue.value <= 0 || document.change.VideoValue.value >= 100) {
    missingvalue += "\\n           - Video Cards";
	if (thefirst == "") { thefirst = "VideoValue"; }
}
if (isNaN(document.change.PeriphValue.value) || document.change.PeriphValue.value <= 0 || document.change.PeriphValue.value >= 100) {
    missingvalue += "\\n           - Peripherals";
	if (thefirst == "") { thefirst = "PeriphValue"; }
}
if (isNaN(document.change.PrinterValue.value) || document.change.PrinterValue.value <= 0 || document.change.PrinterValue.value >= 100) {
    missingvalue += "\\n           - Printers";
	if (thefirst == "") { thefirst = "PrinterValue"; }
}
if (isNaN(document.change.SoftwareValue.value) || document.change.SoftwareValue.value <= 0 || document.change.SoftwareValue.value >= 100) {
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
	document.change(thefirst).focus();
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

function jumpRep() {
RepID = document.forms[0].RepID;
RepIDs = document.forms[0].RepIDs; 
var sizer = RepID.length;
for(var i = 0; i < RepIDs.length; i++) {
if ((RepIDs.options[i] != null) && (RepIDs.options[i].selected)) {
var there = false;
for(var count = 0; count < sizer; count++) {
if (RepID.options[count] != null) {
if (RepIDs.options[i].text == RepID.options[count].text) {
there = true;
break;
      }
   }
}
if (there != true) {
RepID.options[sizer] = new Option(RepIDs.options[i].text); 
RepID.options[sizer].value = RepIDs.options[i].value;
sizer++;
         }
      }
   }
}

function jumpUser() {
if (document.change.AdminID) {
AdminID = document.forms[0].AdminID;
UserIDs = document.forms[0].UserIDs; 
var sizer = AdminID.length;
for(var i = 0; i < UserIDs.length; i++) {
if ((UserIDs.options[i] != null) && (UserIDs.options[i].selected)) {
var there = false;
for(var count = 0; count < sizer; count++) {
if (AdminID.options[count] != null) {
AdminID.options[count] = null;
   }
}
if (there != true) {
var sizer = AdminID.length;
AdminID.options[sizer] = new Option(UserIDs.options[i].text); 
AdminID.options[sizer].value = UserIDs.options[i].value;
sizer++;
         }
      }
   }
  }
}

function killRep() {
var RepID  = document.forms[0].RepID;
var sizer = RepID.options.length;
for(var i = (sizer-1); i >= 0; i--) {
if ((RepID.options[i] != null) && (RepID.options[i].selected == true)) {
RepID.options[i] = null;
      }
   }
}

function viewUser() {
var UserIDs  = document.forms[0].UserIDs;
for(var i = 0; i < UserIDs.length; i++) {
	if ((UserIDs.options[i] != null) && (UserIDs.options[i].selected)) {
		location.href = "change_user.cgi?Username="+UserIDs.options[i].value+"&LastName=1";
	}
}
}

//DELETE SHIPPING LOCATION
function delLocation() {
var ShippingID  = document.forms[0].ShippingID;
for(var i = 0; i < ShippingID.length; i++) {
	if ((ShippingID.options[i] != null) && (ShippingID.options[i].selected)) {
		location.href = "change_shipdest.cgi?DELETEIT=1&ShippingID="+ShippingID.options[i].value+"&CMCustNum=$SavedCMCustNum&CompanyName=$SavedCompanyName";
	}
  }
}

//CHANGE SHIPPING LOCATION
function changeLocation() {
var ShippingID  = document.forms[0].ShippingID;
for(var i = 0; i < ShippingID.length; i++) {
	if ((ShippingID.options[i] != null) && (ShippingID.options[i].selected)) {
		parent.location.href = "change_shipdest.cgi?ShippingID="+ShippingID.options[i].value+"&CMCustNum=$SavedCMCustNum&CompanyName=$SavedCompanyName";
	}
  }
}

function checkSelects() {
RepID = document.forms[0].RepID;
RepIDs = document.forms[0].RepIDs; 
ShippingID = document.forms[0].ShippingID; 
MessageID = document.forms[0].MessageID; 

// CLEARS DEFAULT DATA FOR ALL NECESSARY SELECTS THAT WILL BE FED INFO FROM DB AT LOAD
RepID.options[0] = null;
RepIDs.options[0] = null;
ShippingID.options[0] = null;
MessageID.options[0] = null;

// IF ADDING NEW CUSTOMERS NO NEED TO SEARCH/LOAD ALL THIS CUSTOMER'S USERS
if (document.forms[0].AdminID && document.forms[0].UserIDs) {
UserIDs = document.forms[0].UserIDs; 
UserIDs.options[0] = null;
}
}
</script>
$MenuConfig
</head>

<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:checkSelects();feedReps();feedUsers();feedMessages();feedShipping();makeReps();">

$MenuConstructor
<form method="post" action="$script" name="change" onSubmit="return checkForm();">
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
            <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update 
              Customer Account</b></font></td>
            <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
              <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER" bordercolor="#333366">
                <tr bordercolor="#333366" valign="middle"> 
                  <td width="100%" align="center" height="50" bordercolor="#333366" class="tableBG"><font face="verdana,arial,helvetica" size="1" color="#EB0000">*If 
                    you have any questions please ask your Supervisor or Manager 
                    for help using the system or updating it's information.</font> 
                    <font face="verdana,arial,helvetica" size="1" color="#333366"></font></td>
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
                                      <input type="text" size="15" class="inputtext15" name="CompanyName" value="$SavedCompanyName">
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
                                    <td height="65" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">The 
                                      Coastline Micro Customer Number is used 
                                      to save information to various databases 
                                      in the system, please make sure this number 
                                      matches all in-house company records.</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"> 
                                      <input type="text" size="15" class="inputtext15" name="CMCustNum" value="$SavedCMCustNum">
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

EOF
}

## WHICH CompanyType IS CHOSEN?

@Types = ("Small,Small (1-100 Users)","Medium,Medium (100-1000 Users)","Corp,Corporation (1000+ Users)","Reseller,Reseller","Consult,Consultant");
foreach $Type (@Types) {
	$count++;
   	# Split each pair into individual variables.
   	local($value, $name) = split(/,/, $Type);
	if ($Type =~ "$SavedCompanyType") { print "<option value=\"$value\" SELECTED>$name</option>"; }
	else { print "<option value=\"$value\">$name</option>"; }
	print "sizer++;";
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
                                      <input type="text" name="TelArea" size="3" value="$TelArea" class="inputtext3">
                                      <input type="text" name="TelNum" size="7" value="$TelNum" class="inputtext7">
                                      <input type="hidden" name="Phone" value="">
                                      </nobr> <font face="verdana,arial,helvetica" size="1" color="#333366"><br>
                                      Area &nbsp;&nbsp;Number</font> </td>
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
                                      <input type="text" name="FaxArea" size="3" value="$FaxArea" class="inputtext3">
                                      <input type="text" name="FaxNum" size="7" value="$FaxNum" class="inputtext7">
                                      <input type="hidden" name="Fax" value="">
                                      <nobr></nobr> <font face="verdana,arial,helvetica" size="1" color="#333366"><br>
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Business Mailing Address</font></b></font></td>
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
                                      <input type="text" size="15" class="inputtext15" name="MailAdd" value="$SavedMailAdd">
                                      </nobr><br>
                                      <nobr><font face="verdana,arial,helvetica" size="1" color="#333366">Line 2:</font> 
                                      <input type="text" size="15" class="inputtext15" name="MailAdd2" value="$SavedMailAdd2">
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
                                      <input type="text" size="15" class="inputtext15" name="MailCity" value="$SavedMailCity">
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
                                      <input type="text" name="MailZip" size="7" class="inputtext7" value="$SavedMailZip">
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

EOF
}

## WHICH STATE IS CHOSEN?
@States = ("AK","AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","HI","IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VA","VT","WA","WI","WV","WY");
foreach $State (@States) {
	if ($State eq "$SavedMailState") { print "
                                        <option value=\"$State\" SELECTED>$State</option>"; }
	else { print "
                                        <option value=\"$State\">$State</option>"; }
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
                          <br>
                          <br>
                        </td>
                        <td align="center" valign="top"><br>
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
                                      Shipping Locations</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="85" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">Every 
                                      company profile can have unlimited shipping 
                                      locations configured for it. To add a new 
                                      location for this customer click 'Add Location'. 
                                      To delete a location, select a location 
                                      from the list and click 'Delete Location'.</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" rowspan="2">&nbsp;</td>
                                    <td height="30" align="center" valign="middle"> 
                                      <select name="ShippingID" class="inputtext">
                                        <option value="BIGNULL">0000000000000000</option>
                                      </select>
                                      <br>
                                    </td>
                                    <td width="15" bgcolor="#F2F2F7" rowspan="2">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td height="30" align="center" valign="middle"> 
                                      <input type="button" value="Delete Selected Location" class="inputbut" onClick="javascript:delLocation();" name="button">
                                    </td>
                                  </tr>
                                  <tr>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="30" align="center" valign="middle">
                                      <input type="button" value="Update Selected Location" class="inputbut" onClick="javascript:changeLocation();" name="button22">
                                    </td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="30" align="center" valign="middle">
                                      <input type="button" value="Create New Location" class="inputbut" onClick="javascript:parent.location.href='add_shipdest.cgi?enformthee=1&CMCustNum=$CMCustNum';" name="button23">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Messages 
                                      To/From Company </font></b><font color="#FFFFFF">(Tracks 
                                      all Users)</font></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="85" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">This 
                                      system saves it's outgoing email messages 
                                      sent by the and from the system to a table 
                                      within our system's database. To view messages 
                                      sent/recieved by this company and/or it's 
                                      users choose a message and click 'View Message'</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" rowspan="2">&nbsp;</td>
                                    <td height="30" align="center" valign="middle"> 
                                      <select name="MessageID" class="inputtext">
                                        <option value="BIGNULL">0000000000000000</option>
                                      </select>
                                      <br>
                                    </td>
                                    <td width="15" bgcolor="#F2F2F7" rowspan="2">&nbsp;</td>
                                  </tr>
                                  <tr>
                                    <td height="30" align="center" valign="middle"> 
                                      <input type="button" value="View Message" class="inputbut" name="button2">
                                    </td>
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Account 
                                      Created By</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="55" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">This 
                                      field allows for the tracking of administrative 
                                      actions on the database, in this case the 
                                      addition of this customer profile to the 
                                      system.</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="45" align="center"> <font face="verdana,arial,helvetica" size="1" color="#333366">$SavedAddedBy<br>
                                      $AddMonth/$AddDay/$AddYear</font></td>
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
                          <!--ONE LAST MOD BEGIN-->
EOF
}

if ($SavedModifiedBy != "" || $SavedModifiedBy != " " || $SavedModifiedOn > 0) {
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Account 
                                      Last Modified By</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="55" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">This 
                                      field allows for the tracking of administrative 
                                      actions on the database, in this case the 
                                      last modification to this customer profile.</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="45" align="center"> <font face="verdana,arial,helvetica" size="1" color="#333366">$SavedModifiedBy<br>
                                      $ModMonth/$ModDay/$ModYear</font></td>
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
                          <!--TWO LAST MOD END-->
EOF
}
}

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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Account 
                                      Representatives </font></b><font color="#FFFFFF">(Sales 
                                      Reps)</font></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="135" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">This 
                                      system allows for a company profile to have 
                                      as many Coastline Micro representatives 
                                      servicing it as necessary.<br>
                                      <br>
                                      The <b>Active</b> field denotes the representatives 
                                      currently chosen to service this account.<br>
                                      <br>
                                      The <b>Inactive</b> field shows all the 
                                      Coastline Micro representatives in the system. 
                                      This feature only reads in users with CMManage 
                                      or CMSales rights.</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="45" align="center"> 
                                      <table width="270" border="0" cellspacing="0" cellpadding="0" bgcolor="#FFFFFF" align="center">
                                        <tr> 
                                          <td align="center" width="130"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Active</b></font></td>
                                          <td width="10" rowspan="3"><img src="images/spacer.gif" width="10" height="1"></td>
                                          <td bgcolor="#8F8FAB" width="1" rowspan="3"><img src="images/verticalbar.gif" width="1" height="25"></td>
                                          <td width="10" rowspan="3"><img src="images/spacer.gif" width="10" height="1"></td>
                                          <td align="center" width="129"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Inactive</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="130" valign="top" align="center"> 
                                            <input type="hidden" name="TheReps" value="">
                                            <select name="RepID" size="8" multiple class="multiselect">
                                              <option value="BIGNULL">0000000000000000</option>
                                            </select>
                                          </td>
                                          <td width="129" valign="bottom" align="center"> 
                                            <select name="RepIDs" size="8" multiple class="multiselect">
                                              <option value="BIGNULL">0000000000000000</option>
                                            </select>
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="130" valign="bottom" align="center"> 
                                            <input type="Button" value=" >>> " onClick="javascript:killRep();" class="inputbut" name="Button">
                                          </td>
                                          <td width="129" valign="bottom" align="center"> 
                                            <input type="Button" value=" <<< " onClick="javascript:jumpRep();" class="inputbut" name="Button">
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
                          <br>
                          <!--THREE ADMIN USER BEGIN-->
EOF
}

if ($FORM{'AdminUser'}) { 

{
print <<EOF

                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Account Administrator</font></b></font></td>
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
                                      <font face="verdana,arial,helvetica" size="1" color="#333366">$AdminUser</font><input type="hidden" size="15" class="inputtext15" name="TheAdmin" value="$AdminUser">
                                    </td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                </table>

EOF
}
}

else { 
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Account 
                                      Administrator</font></b><font color="#FFFFFF"> 
                                      (Company User)</font></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="315" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">Only 
                                      one user can be a company's main administrator 
                                      at a time. This user will have access to 
                                      the company's full profile and configuration. 
                                      This means this user can add, delete change 
                                      any of the company's users, data or profiles 
                                      as necessary. This user will also get a 
                                      copy of all messages sent to any and all 
                                      other users in the system. That option can 
                                      be changed if necessary.<br>
                                      <br>
                                      There will always be an administrator showing 
                                      in the <b>Administrator</b> field. To change 
                                      the administrator choose a user from the 
                                      List of Company Users and click 'Make Admin'<br>
                                      <br>
                                      To edit a user's profile select the user 
                                      you would like to update from the <b>List 
                                      of Company Users</b> list then click 'Edit 
                                      Selected'<br>
                                      <br>
                                      To edit the current administrator's user 
                                      profile select a different user to be the 
                                      administrator, then when the user that was 
                                      the administrator shows up in the <b>List 
                                      of Company Users</b> list, choose that user 
                                      and click 'Edit Selected'</font><font face="verdana,arial,helvetica" size="1" color="#333366"><br>
                                      <br>
                                      To add a new user to this company's profile 
                                      just click 'Add User'</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="45" align="center">
                                      <table width="280" border="0" cellspacing="0" cellpadding="0" bgcolor="#FFFFFF" align="center">
                                        <tr> 
                                          <td align="center" width="130" height="20"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Administrator</b></font></td>
                                          <td width="10" rowspan="6"><img src="images/spacer.gif" width="10" height="1"></td>
                                          <td bgcolor="#8F8FAB" width="1" rowspan="6"><img src="images/verticalbar.gif" width="1" height="25"></td>
                                          <td width="10" rowspan="6"><img src="images/spacer.gif" width="10" height="1"></td>
                                          <td align="center" width="129"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>List 
                                            of Company Users</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="130" valign="top" align="center" height="30"> 
                                            <select name="AdminID" size="2" multiple class="singleselect">
                                            </select>
                                            <input type="hidden" name="TheAdmin" value="">
                                          </td>
                                          <td width="129" valign="bottom" align="center" rowspan="3"> 
                                            <select name="UserIDs" size="8" multiple class="multiselect">
                                              <option value="BIGNULL">0000000000000000</option>
                                            </select>
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td valign="top" align="center" width="130"> 
                                            <input type="Button" value="Edit Selected" onClick="javascript:viewUser();" class="inputbut" name="Button2">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td valign="top" align="center" width="130"> 
                                            <input type="Button" value="Make Admin" onClick="javascript:jumpUser();" class="inputbut" name="Button2">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td valign="top" align="center" width="130"> 
                                            <input type="Button" value="Add New User" onClick="javascript:location.href='add_user.cgi?enformthee=1&NewCompanyUser=1&CMCustNum=$CMCustNum&CompanyName=$CompanyName';" class="inputbut" name="Button2">
                                          </td>
                                          <td width="129" valign="bottom" align="center" rowspan="2">&nbsp;</td>
                                        </tr>
                                        <tr> 
                                          <td valign="top" align="center" width="130">&nbsp;</td>
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
                          <!--FOUR ADMIN USER END-->
EOF
}
}

{
print <<EOF
                          <br>
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
                                            <input type="text" name="DesktopValue" size="3" class="inputtext3" value="$SavedDesktopValue">
                                            <font face="verdana,arial,helvetica" size="1" color="#333366"><b>&nbsp;</b></font><font face="verdana,arial,helvetica" size="1" color="#333366"><b>&nbsp;</b></font> 
                                          </td>
                                          <td bgcolor="#8F8FAB" width="1" rowspan="10" valign="middle" height="35"><img src="images/verticalbar.gif" width="1" height="25"></td>
                                          <td width="100" align="right" height="35" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Servers: 
                                            &nbsp;&nbsp;</b></font></td>
                                          <td align="center" valign="middle" width="39"> 
                                            <input type="text" name="ServerValue" size="3" class="inputtext3" value="$SavedServerValue">
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
                                            <input type="text" name="NotebookValue" size="3" class="inputtext3" value="$SavedNotebookValue">
                                            <font face="verdana,arial,helvetica" size="1" color="#333366"><b>&nbsp;</b></font> 
                                          </td>
                                          <td align="right" width="100" valign="middle" height="35"><nobr><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Monitors: 
                                            &nbsp;&nbsp;</b></font></nobr></td>
                                          <td align="center" valign="middle" width="39"> 
                                            <input type="text" name="MonitorValue" size="3" class="inputtext3" value="$SavedMonitorValue">
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
                                            <input type="text" name="MemoryValue" size="3" class="inputtext3" value="$SavedMemoryValue">
                                            <font face="verdana,arial,helvetica" size="1" color="#333366"><b>&nbsp;</b></font> 
                                          </td>
                                          <td width="100" align="right" valign="middle" height="35"><nobr><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Hard 
                                            Drives: &nbsp;&nbsp;</b></font></nobr></td>
                                          <td align="center" valign="middle" width="39"> 
                                            <input type="text" name="HDriveValue" size="3" class="inputtext3" value="$SavedHDriveValue">
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
                                            <input type="text" name="VideoValue" size="3" class="inputtext3" value="$SavedVideoValue">
                                            <font face="verdana,arial,helvetica" size="1" color="#333366"><b>&nbsp;</b></font> 
                                          </td>
                                          <td width="100" align="right" valign="middle" height="35"><nobr><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Peripherals:&nbsp;&nbsp;&nbsp;</b></font></nobr></td>
                                          <td align="center" valign="middle" width="39"> 
                                            <input type="text" name="PeriphValue" size="3" class="inputtext3" value="$SavedPeriphValue">
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
                                            <input type="text" name="PrinterValue" size="3" class="inputtext3" value="$SavedPrinterValue">
                                            <font face="verdana,arial,helvetica" size="1" color="#333366"><b>&nbsp;</b></font> 
                                          </td>
                                          <td width="100" align="right" valign="middle" height="35"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Software: 
                                            &nbsp;&nbsp;</b></font></td>
                                          <td align="center" valign="middle" width="39"> 
                                            <input type="text" name="SoftwareValue" size="3" class="inputtext3" value="$SavedSoftwareValue">
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
                        <td width="50%" align="center" height="25" class="tableBG" valign="top"><br>
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

EOF
}

## WHICH PayOption IS CHOSEN?
@Options = ("Cash","Check","CCMaster","CCVisa","CCAmex","Net30","Net10","Net5");
foreach $Option (@Options) {
	if ($SavedPayOption =~ "$Option") { print "
                                              <option value=\"$Option\" SELECTED>$Option</option>"; }
}

{
print <<EOF

                                            </select>
                                            <input type="hidden" name="PayTypes" value="">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="130" valign="bottom" align="center"> 
                                            <input type="Button" value=" >>> " onClick="javascript:jumpOption();" class="inputbut" name="Button3">
                                          </td>
                                          <td width="129" valign="bottom" align="center"> 
                                            <input type="Button" value=" <<< " onClick="javascript:killOption();" class="inputbut" name="Button3">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Visa 
                                      Card Account Information</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" bgcolor="#F2F2F7" align="left" valign="middle"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="60" align="center" valign="middle"> 
                                      <table width="150" border="0" cellspacing="0" cellpadding="0">
                                        <tr> 
                                          <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Card 
                                            Number</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="30" valign="top" align="center"> 
                                            <input type="text" name="CCVisa" size="15" class="inputtext15" value="$SavedCCVisa">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Name 
                                            on Card</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="15" valign="top" align="center"> 
                                            <input type="text" name="CCVisaName" size="15" class="inputtext15" value="$SavedCCVisaName">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Expiration 
                                            Date </b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="30" valign="top" align="center"> 
                                            <input type="text" name="CCVisaExp" size="7" class="inputtext7" value="$SavedCCVisaExp">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">MasterCard 
                                      Account Information</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" bgcolor="#F2F2F7" align="left" valign="middle"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="60" align="center" valign="middle"> 
                                      <table width="150" border="0" cellspacing="0" cellpadding="0">
                                        <tr> 
                                          <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Card 
                                            Number</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="30" valign="top" align="center"> 
                                            <input type="text" name="CCMaster" size="15" class="inputtext15" value="$SavedCCMaster">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Name 
                                            on Card</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="15" valign="top" align="center"> 
                                            <input type="text" name="CCMasterName" size="15" class="inputtext15" value="$SavedCCMasterName">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Expiration 
                                            Date </b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="30" valign="top" align="center"> 
                                            <input type="text" name="CCMasterExp" size="7" class="inputtext7" value="$SavedCCMasterExp">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">American 
                                      Express Card Account Information</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" bgcolor="#F2F2F7" align="left" valign="middle"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="60" align="center" valign="middle"> 
                                      <table width="150" border="0" cellspacing="0" cellpadding="0">
                                        <tr> 
                                          <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Amex 
                                            Card Number</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="30" valign="top" align="center"> 
                                            <input type="text" name="CCAmex" size="15" class="inputtext15" value="$SavedCCAmex">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Name 
                                            on Card</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="15" valign="top" align="center"> 
                                            <input type="text" name="CCAmexName" size="15" class="inputtext15" value="$SavedCCAmexName">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Expiration 
                                            Date </b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="30" valign="top" align="center"> 
                                            <input type="text" name="CCAmexExp" size="7" class="inputtext7" value="$SavedCCAmexExp">
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
                          <br>
                        </td>
                      </tr>
                    </table>
                </td>
              </tr>
              <tr bordercolor="#333366" bgcolor="#F2F2F7"> 
                  <td align="center" valign="middle" height="45" width="100%" bgcolor="#F2F2F7"> 
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

EOF
}

##----------->>> GET ALL CM REPS
{
print <<EOF 

<script language="Javascript">
function makeReps() {
if (document.change.AdminID) {
AdminID = document.forms[0].AdminID;
RepID = document.forms[0].RepID; 
var sizer = RepID.length;
// GETTING READY TO FEED INFO

EOF
}

## Get list CM REPS WHO ARE THIS CUSTOMERS REPS
my $sth = $dbh->prepare("SELECT * FROM Users ORDER BY LastName ASC");
$sth->execute or die "Unable to execute query\n"; 
my @row;
while(@row = $sth->fetchrow_array) { 
	my $UserID = $row[0];
	my $Username = $row[3];
	my $FirstName = $row[6];
	my $LastName = $row[7];
	my $UserAccess = $row[11];
	if ($SavedAdminID =~ "$Username") {
		print "AdminID.options[0] = new Option('$LastName, $FirstName');";
		print "AdminID.options[0].value = '$Username';";
	}
	if (($UserAccess eq "CMManage") || ($UserAccess eq "CMAdmin") || ($UserAccess eq "CMSales")) {
		if ($SavedRepID =~ "$Username") {
			print "RepID.options[sizer] = new Option('$LastName, $FirstName');";
			print "RepID.options[sizer].value = '$Username';";
			print "sizer++;";
		}
	}
}
$sth->finish;
print "}";
print "}";
print "</script>";



##----------->>> GET CM REP CONFIG AND IN SYS
{
print <<EOF 


<script language="Javascript">
function feedReps() {
RepID = document.forms[0].RepID;
RepIDs = document.forms[0].RepIDs; 
var sizer = RepIDs.length;
// GETTING READY TO FEED INFO

EOF
}

## Get list of ALL CM reps
my $sth = $dbh->prepare("SELECT * FROM Users WHERE UserAccess = 'CMManage' OR UserAccess = 'CMAdmin' OR UserAccess = 'CMSales' ORDER BY LastName ASC");
$sth->execute or die "Unable to execute query\n"; 
my @row;
while(@row = $sth->fetchrow_array) { 
	my $UserID = $row[0];
	my $Username = $row[3];
	my $FirstName = $row[6];
	my $LastName = $row[7];
	print "RepIDs.options[sizer] = new Option('$LastName, $FirstName');";
	print "RepIDs.options[sizer].value = '$Username';";
	print "sizer++;";
}
$sth->finish;
print "}";
print "</script>";


##----------->>> GET ALL USERS FOR THIS CUSTOMER
if ($FORM{'AdminUser'}) { 
{
print <<EOF 

<script language="Javascript">
function feedUsers() { end=1; }
</script>

EOF
}
}

else {

{
print <<EOF 

<script language="Javascript">
function feedUsers() {
UserIDs = document.forms[0].UserIDs; 
var sizer = UserIDs.length;
// GETTING READY TO FEED INFO

EOF
}

## Get list of ALL CM reps
my $sth = $dbh->prepare("SELECT * FROM Users WHERE CustomerID='$CMCustNum' ORDER BY LastName ASC");
$sth->execute or die "Unable to execute query\n"; 
my @row;
while(@row = $sth->fetchrow_array) { 
	my $UserID = $row[0];
	my $Username = $row[3];
	my $FirstName = $row[6];
	my $LastName = $row[7];
print "UserIDs.options[sizer] = new Option('$LastName, $FirstName');";
print "UserIDs.options[sizer].value = '$Username';";
print "sizer++;";
}
$sth->finish;
print "}";
print "</script>";
}


##----------->>> GET MESSAGE FOR AND FROM COMPANY
{
print <<EOF 

<script language="Javascript">
function feedMessages() {
MessageID = document.forms[0].MessageID;
var sizer = MessageID.length;
// GETTING READY TO FEED INFO

EOF
}

## Get list of Messages for/from this company
my $sth = $dbh->prepare("SELECT * FROM Messages WHERE CMCustNum='$CMCustNum' ORDER BY AddedOn ASC");
$sth->execute or die "Unable to execute query\n"; 
my @row;
while(@row = $sth->fetchrow_array) { 
	my $MessageID = $row[0];
	my $Username = $row[1];
	my $AddedOn = $row[12];
	## reformat data
    my $Subject = substr($Subject, 0, 10);     # ONLY 10 Characters
	my $AddYear = substr($AddedOn, 0, 2);
	my $AddMonth = substr($AddedOn, 2, 2);
	my $AddDay = substr($AddedOn, 4, 2);
print "MessageID.options[sizer] = new Option('$Username - $AddMonth/$AddDay/$AddYear');";
print "MessageID.options[sizer].value = '$MessageID';";
print "sizer++;";
}
$sth->finish;
print "}";
print "</script>";


##----------->>> GET MESSAGE FOR AND FROM COMPANY
{
print <<EOF 

<script language="Javascript">
function feedShipping() {
ShippingID = document.forms[0].ShippingID;
var sizer = ShippingID.length;
// GETTING READY TO FEED INFO

EOF
}

## Get list of Shipping Addresses for this company
my $sth = $dbh->prepare("SELECT * FROM ShipDests WHERE CMCustNum='$CMCustNum' ORDER BY AddedOn ASC");
$sth->execute or die "Unable to execute query\n"; 
my @row;
while(@row = $sth->fetchrow_array) { 
	my $ShipID = $row[0];
	my $Courier = $row[2];
	my $Price = $row[4];
	my $Address = $row[10];
	my $City = $row[12];
	my $AddedOn = $row[15];
	## reformat data
    my $Address = substr($Address, 0, 10);     # ONLY 10 Characters
	my $AddYear = substr($AddedOn, 0, 2);
	my $AddMonth = substr($AddedOn, 2, 2);
	my $AddDay = substr($AddedOn, 4, 2);
print "ShippingID.options[sizer] = new Option('$City / $Courier');";
print "ShippingID.options[sizer].value = '$ShipID';";
print "sizer++;";
}
$sth->finish;
$dbh->disconnect;
print "}";
print "</script>";

{
print <<EOF


<input type="hidden" name="DROPIN" value="1">
</form>
</body>
</html>

EOF
}
}
exit;
}
}

## If no resident form processing calls are given continue
elsif ($FORM{'enformthee'}) {

## TOP HTML TEMPLATE
&topper;

{
print <<EOF



<table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
            <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Add/Update 
              Customer Accounts</b></font></td>
            <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER" bordercolor="#333366">
              <tr valign="middle"> 
                        <td height="50" width="100%"> 
                          <center>
                            <font face="verdana,arial,helvetica" size="1" color="#EB0000">*If 
                            you have any questions please ask your Supervisor 
                            or Manager for help using the system or updating it's 
                            information.</font> 
                          </center>
                        </td>
                      </tr>
              <tr> 
                  <td width="50%" align="center" valign="top"> 
                    <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr> 
                      <td width="100%"><center>
                            <font face="verdana,arial,helvetica" size="1" color="#333366"> 
                            </font> <br>
<form method="post" action="$script" name="change" onSubmit="return checkForm();">
                            <table width="500" border="0" cellspacing="0" cellpadding="0" align="center">
                              <tr> 
                                <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                              </tr>
                              <tr> 
                                <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                                <td width="348" valign="top"> 
                                  <table width="500" border="0" cellspacing="0" cellpadding="0">
                                    <tr> 
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                      <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">View/Update 
                                        Customer Account</font></b></font></td>
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="55" bgcolor="#F2F2F7" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366">To 
                                        change or update a company's account profile 
                                        as saved in the system please choose the 
                                        company you would like to change from 
                                        the list below then click 'View/Update'</font></td>
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="35" align="center"> 
                                        <script language="Javascript">
function checkForm() {
var missingdrop = "";

// Implement selected customer's name into CustomerName form field
// Grab selected fields from PayOption and make PayTypes form field for processing
var formindex = document.change.CMCustNum.selectedIndex;
var thisone = document.change.CMCustNum.options[formindex].text;
document.change.CompanyName.value = thisone;

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    missingdrop ="___________________________________________                   \\n\\n" + "  Sorry, I cannot process your request because the\\n  following fields are either blank or filled incorrectly:\\n" + "___________________________________________                   \\n\\n" +
    missingdrop + "\\n\\n___________________________________________                   " + "\\n\\n   To continue, check fields and submit form again!" + "\\n___________________________________________";
    alert(missingdrop);
    return false;
} 
else {
return true;
}
}
</script>
                                        <select name="CMCustNum" class="inputtext">
EOF
}

	## Get list of CM reps
	use DBI;
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("SELECT * FROM Customers ORDER BY CompanyName ASC");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
		while(@row = $sth->fetchrow_array) { 
		my $CMCustNum = $row[1];
		my $CompanyName = $row[6];
    	$Company = substr($CompanyName, 0, 30);     # ONLY 30 Characters
		print "<option value=\"$CMCustNum\">$CompanyName</option>";
	}
	$sth->finish;
	$dbh->disconnect;
	## print closing select tag

{
print <<EOF
                                        </select>
                                        &nbsp;
                                        
                                        &nbsp;
<input type="submit" value="View/Update" class="inputbut" name="submit"><input type="hidden" name="CompanyName" value="">
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
                            </table></form>
                            <table width="500" border="0" cellspacing="0" cellpadding="0" align="center">
                              <tr> 
                                <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                              </tr>
                              <tr> 
                                <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                                <td width="348" valign="top"> 
                                  <table width="500" border="0" cellspacing="0" cellpadding="0">
                                    <tr> 
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                      <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Create 
                                        New Customer Account</font></b></font></td>
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="35" bgcolor="#F2F2F7" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366">Click 
                                        the button below to create a new customer 
                                        account. </font></td>
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="35" align="center"> 
                                        <input type="button" value="Create Customer Account" class="inputbut" onClick="javascript:parent.location.href='add_customer.cgi'">
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
                            <table width="500" border="0" cellspacing="0" cellpadding="0" align="center">
                              <tr> 
                                <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                              </tr>
                              <tr> 
                                <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                                <td width="348" valign="top"> 
                                  <table width="500" border="0" cellspacing="0" cellpadding="0">
                                    <tr> 
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                      <td height="20" bgcolor="#8F8FAB" colspan="2"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Search/Browse 
                                        Customer Accounts</font></b></font></td>
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td colspan="4" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="85" bgcolor="#F2F2F7" align="left" colspan="2"><font face="verdana,arial,helvetica" size="1" color="#333366">To 
                                        Search customer accounts, type in the 
                                        Terms/Keywords to help you locate the 
                                        customer account you are interested in 
                                        reviewing and/or updating. Then, select 
                                        a Search Filter Option, this is the field 
                                        searched in the database. Finally, click 
                                        'Search Customers'<br>
                                        <br>
                                        *To Browse customer accounts, simply select 
                                        a Browse Filter Option then click 'Browse 
                                        Customers' </font></td>
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="280" align="center" width="234" valign="top"> 
                                        <br>
<form method="post" action="view_customers.cgi">
                                        <table border="1" cellspacing="0" cellpadding="0" width="200" bordercolor="#8F8FAB">
                                          <tr> 
                                            <td height="20" align="center" bgcolor="#F2F2F7" class="tableBG" width="200"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Search 
                                              Terms/Keywords</b></font></td>
                                          </tr>
                                          <tr> 
                                            <td align="center" height="40" width="200"> 
                                              <input type="text" name="SearchTerms" size="15">
                                            </td>
                                          </tr>
                                          <tr> 
                                            <td height="20" align="center" bgcolor="#F2F2F7" width="200"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Search 
                                              Filter Options </b></font></td>
                                          </tr>
                                          <tr> 
                                            <td height="125" width="200"> 
                                              <input type="radio" name="SearchType" value="CMCustNum" SELECTED checked>
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">CM 
                                              Customer Number</font><br>
                                              <input type="radio" name="SearchType" value="CompanyName">
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">Company 
                                              Name</font><br>
                                              <input type="radio" name="SearchType" value="MailCity">
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">Business 
                                              City</font><br>
                                              <input type="radio" name="SearchType" value="MailState">
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">Business 
                                              State</font><br>
                                            </td>
                                          </tr>
                                          <tr> 
                                            <td align="center" height="35" valign="middle" width="200"> 
                                              <input type="submit" value="Search Customers" class="inputbut" name="Submit">
                                            </td>
                                          </tr>
                                        </table>
</form>
                                      </td>
                                      <td height="280" align="center" width="234" valign="top"> 
                                        <br>
<form method="post" action="view_customers.cgi">
                                        <table border="1" cellspacing="0" cellpadding="0" width="200" bordercolor="#8F8FAB">
                                          <tr> 
                                            <td height="20" align="center" bgcolor="#F2F2F7" width="200"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Browse 
                                              Filter Options </b></font></td>
                                          </tr>
                                          <tr> 
                                            <td width="200" height="125"> 
                                              <input type="radio" name="Browse" value="CMCustNum" SELECTED checked>
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">CM 
                                              Customer Number</font><br>
                                              <input type="radio" name="Browse" value="CompanyName">
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">Company 
                                              Name</font><br>
                                              <input type="radio" name="Browse" value="MailCity">
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">Business 
                                              City</font><br>
                                              <input type="radio" name="Browse" value="MailState">
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">Business 
                                              State</font><br>
                                            </td>
                                          </tr>
                                          <tr> 
                                            <td width="200" align="center" height="35" valign="middle"> 
                                              <input type="submit" value="Browse Customers" class="inputbut">
                                            </td>
                                          </tr>
                                        </table>
</form>
                                      </td>
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                      <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7" colspan="2"><img src="images/verticalbar.gif" width="15" height="15"></td>
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
</center>
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
    
EOF
}


## BOTTOM HTML TEMPLATE
&bottom;

exit;
}

## if no useful calls present frameset
else {
{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - Shark Tank Admin System - Customer Accounts</title>
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

EOF
}
}
exit;

sub bottom {
{
print <<EOF

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