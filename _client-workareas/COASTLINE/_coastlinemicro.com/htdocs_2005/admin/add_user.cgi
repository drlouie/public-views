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
if (($Cookies{'UserType'} eq "COManage") || ($Cookies{'UserType'} eq "WEBAdmin") || ($Cookies{'UserType'} eq "COSales") || ($Cookies{'ExtraAccess'} =~ "AdminUser")) { $nextone = "1"; }
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

## If data present scan it...
if (($FORM{'Username'}) && ($FORM{'Password'}) && ($FORM{'Email'}) && ($FORM{'FirstName'}) && ($FORM{'LastName'}) && ($FORM{'InternalCustNum'}) && ($FORM{'UserAccess'})) { 

## TOP HTML TEMPLATE
&topper;


	## Crumble Form Input to Variables
	my $CustomerID = "$FORM{'InternalCustNum'}";
	my $CompanyName = "$FORM{'CompanyName'}";
	my $Username = "$FORM{'Username'}";
	my $Password = "$FORM{'Password'}";
	my $Email = "$FORM{'Email'}";
	my $FirstName = "$FORM{'FirstName'}";
	my $LastName = "$FORM{'LastName'}";
	my $Position = "$FORM{'Position'}";
	my $Phone = "$FORM{'Phone'}";
	my $Extension = "$FORM{'Extension'}";
	my $UserAccess = "$FORM{'UserAccess'}";
	my $ExtraAccess = "$FORM{'ExtraAccess'}";
	my $ActionUser = "$Cookies{'Username'}";

	## Start User Account Check, make sure no dupes are made
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("SELECT * FROM Users");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		my $SavedCustomerID = $row[1];
		my $SavedUsername = $row[3];
		my $SavedEmail = $row[5];
		my $SavedFirstName = $row[6];
		my $SavedLastName = $row[7];
		my $SavedAddedBy = $row[12];
		
## ------------->>> IF EXISTS DIE
		if (($SavedEmail eq "$Email") || ($SavedUsername eq "$Username")) {
			if ($SavedEmail eq "$Email") { $SavedEmail = "<font color=\"red\">$SavedEmail</font>"}
			if ($SavedUsername eq "$Username") { $SavedUsername = "<font color=\"red\">$SavedUsername</font>"}
{
print <<EOF

                  <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr> 
                      <td width="100%"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><br>Error Description</b><br>
                        While trying to complete your addition request we found 
                        a User record that mathces the information you are 
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
                            <td width="35%" height="20"><font class="stextbig"><b>Matching User Record(s)</b></font></td>
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
							
<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
<tr width="100%"><td width="100%">
<table width="100%" height="35" border="1" bordercolor="#333366" cellspacing="1" cellpadding="3" align="center" bgcolor="#ffffff">
<tr height="20" width="100%" bgcolor="#F2F2F7">
<td align="center" width="15%"><font class="sresults1"><b>Username</b><br></font></td>
<td align="center" width="20%"><font class="sresults1"><b>First</b></font></td>
<td align="center" width="25%"><font class="sresults1"><b>Last</b></font></td>
<td align="center" width="25%"><font class="sresults1"><b>Email</b></font></td>
<td align="center" width="15%"><font class="sresults1"><b>Added By</b></font></td>
</tr>
<tr width=\"100%\">
<td><font class=\"stextbig\" width=\"15%\"><b>$SavedUsername&nbsp;</b></font></td>
<td><font class=\"stextbig\" width=\"20%\">$SavedFirstName&nbsp;</font></td>
<td><font class=\"stextbig\" width=\"25%\">$SavedLastName&nbsp;</font></td>
<td><font class=\"stextbig\" width=\"25%\">$SavedEmail&nbsp;</font></td>
<td><font class=\"stextbig\" width=\"15%\">$SavedAddedBy&nbsp;</font></td>
</tr>
</table>
<br><center><form><input type=\"button\" value=\"Try Again\" onClick=\"javascript:history.go(-1)\" class=\"inputbut\"></form></center>

                            </td>
                          </tr>
                          <tr> 
                            <td colspan="2" height="15"><img src="images/spacer.gif" width="1" height="15"></td>
                          </tr>
                        </table>

                      </td>
                    </tr>
                  </table>
EOF
}
			
			## BOTTOM HTML TEMPLATE
			&bottom;

			$sth->finish;
			exit;
		}
	}
	$sth->finish;

## ------------->>> ELSE SAVE NEW USER DATA

{
print <<EOF

                  <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr><td width="100%"><font face="verdana,arial,helvetica" size="1" color="#333366">
EOF
}




	## SAVE INFO TO NEW DB TABLE DATA ROW
	my $sth = $dbh->prepare("INSERT INTO Users (UserID, CustomerID, EmailType, 
						 	Username, Password, Email, FirstName, LastName, 
						 	Position, Phone, Extension, UserAccess, AddedBy, 
							AddedOn, ModifiedBy, ModifiedOn, DeletedBy, DeletedOn, 
							ExtraAccess)
						 
						 	VALUES (Null, '$CustomerID', 'HTML', '$Username', 
							'$Password', '$Email', '$FirstName', '$LastName', 
							'$Position', '$Phone', '$Extension', '$UserAccess', 
							'$ActionUser', Null, Null, Null, Null, Null, '$ExtraAccess')");
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish; 


## ------------->>> IF ADDING NEW CUSTOMER ACCOUNT'S ADMIN USER
if ($FORM{'AddAdmin'}) {
	print "<b><br>Administrative User Account Saved</b><br><br>The administrative user account for <b>$Username</b> has been created successfully. An email regarding this action has been sent to the added user's email address: <b>$Email</b>. Finally, you must check over all the information you have submitted in this session by clicking on the button below.<br><br><center><form><input type=\"button\" value=\"Continue Customer Addition Process\" onClick=\"javascript:location.href='change_customer.cgi?InternalCustNum=$CustomerID&CompanyName=$CompanyName&AdminUser=$Username'\" class=\"inputbut\"></form></center><br></font>";
}
## ------------->>> IF ADDING NEW CUSTOMER ACCOUNT'S ADMIN USER
elsif ($FORM{'NewCompanyUser'}) {
	print "<b><br>New User Account Saved</b><br><br>The new account for <b>$Username</b> ($CompanyName) has been created successfully. An email regarding this action has been sent to the added user's email address: <b>$Email.</b><br><br><center><form><input type=\"button\" value=\"Back to $CompanyName's Profile\" onClick=\"javascript:location.href='change_customer.cgi?InternalCustNum=$CustomerID&CompanyName=$CompanyName'\" class=\"inputbut\"></form></center><br></font>";
}
## ------------->>> ELSE
else {
	print "<b><br>User Account Saved</b><br><br>The user account for <b>$Username</b> has been created successfully. An email regarding this action has been sent to the added user's email address: <b>$Email</b><br><br><center><form><input type=\"button\" value=\"Back to Home\" onClick=\"javascript:parent.location.href='http://www.rhomberg.com/systemConfigurator/admin/index.cgi'\" class=\"inputbut\"></form></center><br></font>";
}



	
## ----------------------->>> SEND EMAIL START
## ----------------------->>> PREPARE VARIABLES FOR OUTER SEND EMAIL PROGRZM
 $TO = "$Email";
 $FROM = "admin\@rhomberg.com";
 $SUBJECT = "Administration System - New User Account Information";
 $GREETING = "$FirstName,\n\n";
 $BODY = "A user account has just been created for you in our E-Com store. Following is the login information for that account:\n\nUsername - $Username\n\nPassword - $Password\nClick here to access the login screen.\n\n\n";
 $ATTACHMENTS = "";
 $FOOTER = "";
 $MYHTMLTITLE = "<title>New User Account Information</title>";
 $MYHTMLSTAMP = "<table width=\"400\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" align=\"center\"><tr><td width=\"100%\" valign=\"top\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#333366\">$FirstName,<br><br>A user account has just been created for you in the E-Com store. Following is the login information for that account:<br><br><b>Username</b> - $Username<br><b>Password</b> - $Password<br><br><ul><li>Did not request this info?<br><a href=\"mailto:admin\@rhomberg.com?Subject=Bad User Addition (eCom System)\">Report It</a></li></ul></font></td></tr></table>";
 $MYHTMLATTACH = "";
## ----------------------->>> EXECUTE OUTER EMAIL PROGRAM
 require("mailer_2nd.nsp");
## ----------------------->>> END EMAILINGS

	## SAVE COPY OF EMAIL MESSAGE TO DB
		my $htmlToSendSave = $htmlToSendSave;
 		my $RecipientsIn = "$Email\n";
 		my $SenderIn = "admin\@rhomberg.com";
 		my $SubjectIn = "Administration System - New User Account Information";
 		my $BodyIn = "$FirstName,\n\nA user account has just been created for you in the eCom administrative system. Following is the login information for that account:Username - $Username\n\nPassword - $Password\nClick here to access the administration system: http://www.rhomberg.com/\n\n\n";
 		my $Attach1In = "";
 		my $Attach2In = "";
		my $Attach3In = "";
	## Start DB connection
 		use strict;
		my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
		$dbh->{RaiseError} = 1; 
 		my $sth = $dbh->prepare("INSERT INTO Messages (MessageID, Username, QuoteID, OrderID, ConfigID, 
 								 ReplyAdd, Recipients, Subject, Body, Attachment1, Attachment2, 
 								 Attachment3, AddedOn, DeletedBy, DeletedOn, CustomerID)
 	 
 							 	VALUES (Null, '$Username', '', '', '', '$SenderIn', 
 								'$RecipientsIn', '$SubjectIn', '$htmlToSendSave', '$Attach1In', '$Attach2In', 
 								'$Attach3In', Null, '', '', '$CustomerID')");
 		$sth->execute or die "Unable to execute query\n";
 		$sth->finish;
 		$dbh->disconnect;
		
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
EOF
}
	
## TOP HTML TEMPLATE
&bottom;
	
exit;
}

## ------------->>> If no resident form processing calls are given continue
elsif ($FORM{'enformthee'}) {
{
print <<EOF

<html>
<head>
<title>Add User</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="http://www.rhomberg.com/systemConfigurator/admin/admincss.cgi" Type="text/css">
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

// FORM CHECKER FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function checkForm() {
var missingdrop = "";
var thefirst = "";

// Check Common form fields
if (document.add.Username.value == "" || document.add.Username.value == " ") {
    missingdrop += "\\n     - Username";
	thefirst = "Username";
}
else if (document.add.Username.value.length < 7) {
    missingdrop += "\\n     - Username must be at least 7 characters";
	if (thefirst == "") { thefirst = "Username"; }
}

if (document.add.Password.value == "" || document.add.Password.value == " ") {
    missingdrop += "\\n     - Password";
	if (thefirst == "") { thefirst = "Password"; }
}
else if (document.add.Password.value.length < 8) {
    missingdrop += "\\n     - Password must be at least 8 characters";
	if (thefirst == "") { thefirst = "Password"; }
}

if (document.add.Password2.value != document.add.Password.value) {
    missingdrop += "\\n     - Confirm Password does not match Password";
	if (thefirst == "") { thefirst = "Password2"; }
}

if (document.add.FirstName.value == "" || document.add.FirstName.value == " ") {
    missingdrop += "\\n     - First Name";
	if (thefirst == "") { thefirst = "FirstName"; }
}

if (document.add.LastName.value == "" || document.add.LastName.value == " ") {
    missingdrop += "\\n     - Last Name";
	if (thefirst == "") { thefirst = "LastName"; }
}

// CHECK EMAIL
  if (document.add.Email.value == "")	{
    missingdrop += "\\n     - Email";
	if (thefirst == "") { thefirst = "Email"; }
  } else if ((document.add.Email.value.indexOf('\@') == -1) || 
        (document.add.Email.value.indexOf('.') == -1)) {
    missingdrop += "\\n     - Email Format should be: username\@mycompany.com";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.add.Email.value.indexOf(',') != -1)) {
    missingdrop += "\\n     - Commas are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.add.Email.value.indexOf(';') != -1)) {
    missingdrop += "\\n     - Semicolons are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.add.Email.value.indexOf(':') != -1)) {
    missingdrop += "\\n     - Colons are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.add.Email.value.indexOf('&') != -1)) {
    missingdrop += "\\n     - Ampersands are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.add.Email.value.indexOf(' ') != -1)) {
    missingdrop += "\\n     - Spaces are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }

if (document.add.Position.value == "" || document.add.Position.value == " ") {
    missingdrop += "\\n     - Position";
	if (thefirst == "") { thefirst = "Position"; }
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

// Check extension character
if (isNaN(document.add.Extension.value)) {
    missingdrop += "\\n     - Extension must be a number";
	if (thefirst == "") { thefirst = "Extension"; }
}

// -------------------------->>> PERL STARTS 
EOF
}
## -------------------------->>> WITH JAVASCRIPT FORM CHECK FOR ExtraAccess CONFIGURATION - FOR THOSE WITH ExtraAccess ADMIN RIGHTS
if (($Cookies{'UserType'} eq "COManage") || ($Cookies{'ExtraAccess'} =~ "ExtraAccess")) {

{
print <<EOF
// -------------------------->>> PERL ENDS

// Check GRANTED Access Rights
var strValues = "";
	var boxLength = document.add.GrantedRights.length;
	var count = 0;
if (boxLength != 0) {
	for (i = 0; i < boxLength; i++) {
		if (count == 0) {
			strValues = document.add.GrantedRights.options[i].value;
		}
		else {
			strValues = strValues + "," + document.add.GrantedRights.options[i].value;
		}
	count++;
   }
}
else { }
if (strValues.length == 0) { }
else {
	// Grab selected fields from PayOption and make PayTypes form field for processing
	document.add.ExtraAccess.value = strValues;
}

// -------------------------->>> PERL STARTS
EOF
}
}

{
print <<EOF
// -------------------------->>> PERL ENDS

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
GrantedRights = document.forms[0].GrantedRights;
AccessRights = document.forms[0].AccessRights; 
var sizer = GrantedRights.length;
for(var i = 0; i < AccessRights.length; i++) {
if ((AccessRights.options[i] != null) && (AccessRights.options[i].selected)) {
var there = false;
for(var count = 0; count < sizer; count++) {
if (GrantedRights.options[count] != null) {
if (AccessRights.options[i].text == GrantedRights.options[count].text) {
there = true;
break;
      }
   }
}
if (there != true) {
GrantedRights.options[sizer] = new Option(AccessRights.options[i].text); 
GrantedRights.options[sizer].value = AccessRights.options[i].value;
sizer++;
         }
      }
   }
}

function killOption() {
var GrantedRights  = document.forms[0].GrantedRights;
var sizer = GrantedRights.options.length;
for(var i = (sizer-1); i >= 0; i--) {
if ((GrantedRights.options[i] != null) && (GrantedRights.options[i].selected == true)) {
GrantedRights.options[i] = null;
      }
   }
}

function checkOptions() {
AccessRights = document.forms[0].AccessRights;
GrantedRights = document.forms[0].GrantedRights; 
var sizer = AccessRights.length;
for(var i = 0; i < GrantedRights.length; i++) {
for(var count = 0; count < sizer; count++) {
if (GrantedRights.options[i] != null) {
if (AccessRights.options[count] != null) {
if (AccessRights.options[count].text == GrantedRights.options[i].value) {
AccessRights.options[count] = new Option(GrantedRights.options[i].text); 
AccessRights.options[count].value = GrantedRights.options[i].value;
sizer++;
      		}
   		  }
		}
      }
   }
// CLEARS DEFAULT DATA FOR SECONDARY SELECT
GrantedRights.options[0] = null;
}

// -------------------------->>> PERL STARTS 
EOF
}

## -------------------------->>> WITHOUT ONLOAD JAVASCRIPT PROMPT - FOR THOSE WITH ExtraAccess ADMIN RIGHTS
if (($Cookies{'UserType'} eq "COManage") || ($Cookies{'UserType'} eq "WEBAdmin") || ($Cookies{'ExtraAccess'} =~ "ExtraAccess")) { $next=1; }
## -------------------------->>> WITH ONLOAD JAVASCRIPT PROMPT - FOR THOSE WITHOUT ExtraAccess ADMIN RIGHTS
else {
{
print <<EOF
// -------------------------->>> PERL ENDS

var selectoption = "";
selectoption = "______________________________________________________________________________________                   " + "\\nYou have access to add customers to the system, yet you do not have access to grant Payment Options to customers in the system. Please make sure a Company Managerr or Accounting Rep can configure the Payment Options for this account for you as soon as you are finished with the customer addition process. All CM Accounting Staff will recieve a reminder to do so everytime they log on to the system until the request is fulfilled." + "\\n______________________________________________________________________________________";
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
if (($Cookies{'UserType'} eq "COManage") || ($Cookies{'UserType'} eq "WEBAdmin") || ($Cookies{'ExtraAccess'} =~ "PayOptions")) { print "<body TEXT=\"#333366\" LINK=\"#8F8FAB\" VLINK=\"#8F8FAB\" ALINK=\"#8F8FAB\" BGCOLOR=\"#ffffff\" leftmargin=\"0\" topmargin=\"0\" marginwidth=\"0\" marginheight=\"0\">"; }
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
              User Account</b></font></td>
            <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
              <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER" bordercolor="#333366">
                <tr valign="middle"> 
                  <td width="100%" align="center" height="50" class="tableBG"><font face="verdana,arial,helvetica" size="1" color="#333366"> 
                    </font><font face="verdana,arial,helvetica" size="1" color="#EB0000">*If 
                    you have any questions please ask your Supervisor or Manager 
                    for help using the system or updating it's information.</font> 
                    <font face="verdana,arial,helvetica" size="1" color="#333366"></font></td>
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">New 
                                      User's Parent Company</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="65" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">
EOF
}

## ------------->>> Just a adding user to system or is this an admin user addition for a SPECIFIED new company?
## ------------->>> IF AddAdmin SPECIFIED then use that CompanyName and InternalCustNum - FOR USERS ADDING NEW CUSTOMER ACCOUNT WITH ADMIN USER
if ($FORM{'AddAdmin'} && $FORM{'InternalCustNum'} && $FORM{'CompanyName'}) {
	print "The name of the company you just added to the system. If it is incorrect, finish this user addition form, then you will be able to change this or any other saved company information.";
}
## ------------->>> IF NewCompanyUser SPECIFIED then use that CompanyName and InternalCustNum - FOR ADDING NEW USERS TO EXISTING COMPANY PROFILE
elsif ($FORM{'NewCompanyUser'} && $FORM{'InternalCustNum'} && $FORM{'CompanyName'}) {
	print "The name of the company you are about to add a new user to.";
}
## ------------->>> ELSE IF CUSTOMER NOT SPECIFIED then grab all Customers from system filtering CM test Customer accounts out
else {
	print "To add a user to the system, their parent company, the company he/she works for, must have a Customer account in the system.";
}

{
print <<EOF
                                      </font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"> 
EOF
}

## ------------->>> IF AddAdmin SPECIFIED then use that CompanyName and InternalCustNum - FOR USERS ADDING NEW CUSTOMER ACCOUNT WITH ADMIN USER
if ($FORM{'AddAdmin'} && $FORM{'InternalCustNum'} && $FORM{'CompanyName'}) {
	my $InternalCustNum = "$FORM{'InternalCustNum'}";
	my $CompanyName = "$FORM{'CompanyName'}";
	print "<input type=\"hidden\" value=\"$InternalCustNum\" name=\"InternalCustNum\"><input type=\"hidden\" value=\"$CompanyName\" name=\"CompanyName\"><input type=\"hidden\" value=\"1\" name=\"AddAdmin\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#EB0000\">$CompanyName</font><!--PARENT COMPANY-->";
}
## ------------->>> IF NewCompanyUser SPECIFIED then use that CompanyName and InternalCustNum - FOR ADDING NEW USERS TO EXISTING COMPANY PROFILE
elsif ($FORM{'NewCompanyUser'} && $FORM{'InternalCustNum'} && $FORM{'CompanyName'}) {
	my $InternalCustNum = "$FORM{'InternalCustNum'}";
	my $CompanyName = "$FORM{'CompanyName'}";
	print "<input type=\"hidden\" value=\"$InternalCustNum\" name=\"InternalCustNum\"><input type=\"hidden\" value=\"$CompanyName\" name=\"CompanyName\"><input type=\"hidden\" value=\"1\" name=\"NewCompanyUser\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#EB0000\">$CompanyName</font><!--PARENT COMPANY-->";
}
## ------------->>> ELSE IF CUSTOMER NOT SPECIFIED then grab all Customers from system filtering CM test Customer accounts out
else {
	my $InternalCustNum = "$FORM{'InternalCustNum'}";
	my $CompanyName = "$FORM{'CompanyName'}";
	print "<select name=\"InternalCustNum\" width=\"20\" class=\"inputtext\">";
	## Get list of CM reps
	use DBI;
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("SELECT * FROM Customers ORDER BY CompanyName ASC");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
		while(@row = $sth->fetchrow_array) { 
		my $InternalCustNum = $row[1];
		my $CompanyName = $row[6];
    	$Company = substr($CompanyName, 0, 30);     # ONLY 30 Characters
		print "<option value=\"$InternalCustNum\">$CompanyName</option>";
	}
	$sth->finish;
	$dbh->disconnect;
	## print closing select tag
	print "</select>";
}

{
print <<EOF
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Username</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="65" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">Type 
                                      in a Username for this new user. Please 
                                      make sure to use only Alpha-Numeric characters.<br>
                                      <br>
                                      <center>
                                        <font color="#EB0000">Must be at least 
                                        8 characters</font> 
                                      </center>
                                      </font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="55" align="center"> <nobr> 
                                      <input type="text" name="Username" size="15" class="inputtext15">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF"> 
                                      Secret Password</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="105" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">
                                        <font face="verdana,arial,helvetica" size="1" color="#333366">Type 
                                        in a secure password for this new user 
                                        account. Please use a combination of numbers 
                                        and letters for the password. Then re-type 
                                        the password in the 'Confirm Password' 
                                        field.<br>
                                        <br>
                                        <center>
                                          <font color="#EB0000">Must be at least 
                                          8 characters</font> 
                                        </center>
                                        
                                      </font> </font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="65" align="center"><nobr> 
                                      <table width="150" border="0" cellspacing="0" cellpadding="0">
                                        <tr> 
                                          <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Password</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="35" valign="top" align="center"> 
                                            <input type="password" name="Password" size="15" class="inputtext15">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Confirm 
                                            Password </b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="35" valign="top" align="center"> 
                                            <input type="password" name="Password2" size="15" class="inputtext15">
                                          </td>
                                        </tr>
                                      </table>
                                      </nobr><nobr></nobr></td>
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
                                      Name </font></b></font></td>
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
                                      <input type="text" name="FirstName" size="15" class="inputtext15">
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
                                      Name </font></b></font></td>
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
                                      <input type="text" name="LastName" size="15" class="inputtext15">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Email 
                                      Address</font></b></font></td>
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
                                      <input type="text" name="Email" size="15" class="inputtext15">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">User's 
                                      Position within Parent Company</font></b></font></td>
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
                                      <input type="text" name="Position" size="15" class="inputtext15">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Phone 
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
                                      Phone Number - 7 digits</font> </font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="55" align="center"> <nobr> 
                                      <input type="text" name="TelArea" size="3" class="inputtext3">
                                      <input type="text" name="TelNum" size="7" class="inputtext7">
                                      <input type="text" name="Extension" size="3" class="inputtext3">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">User 
                                      Type</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="105" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">
                                      
                                        <font face="verdana,arial,helvetica" size="1" color="#333366">Selected 
                                        is the type of user this person is. Each 
                                        user type consists of a set of system 
                                        access rights. To view the default access 
                                        right layout for all user types click 
                                        the link below.<br>
                                        <br>
                                        <center>
                                          <a href="#"><font color="#EB0000">Access 
                                          Rights Layout</font></a> 
                                        </center>
                                        </font> 
                                      
                                      </font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"><nobr> 
                                      <select name="UserAccess" class="inputtext">
EOF
}

## ------------->>> CUSTOMER IF SPECIFIED
if ($FORM{'InternalCustNum'} && $FORM{'CompanyName'} ) { print "<option value=\"CustUser\" SELECTED>Customer User</option><option value=\"CustAdmin\">Customer Admin</option>"; }
## ------------->>> ELSE IF CUSTOMER NOT SPECIFIED
else { print "<option value=\"CustUser\" SELECTED>Customer User</option><option value=\"CustAdmin\">Customer Admin</option><option value=\"COUser\">Employee User</option><option value=\"COSales\">Sales Representative</option><option value=\"WEBAdmin\">Web Store Administator</option><option value=\"COManage\">Company Manager</option>"; }

{
print <<EOF
                                      </select>
                                      </nobr><nobr></nobr></td>
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

EOF
}
## -------------------------->>> WITH ExtraAccess FORM ELEMENTS - FOR THOSE WITH ExtraAccess ADMIN RIGHTS
if (($Cookies{'UserType'} eq "COManage") || ($Cookies{'ExtraAccess'} =~ "ExtraAccess")) {

{
print <<EOF
						  
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Extended 
                                      Access Rights </font></b><font color="#FFFFFF">(CM 
                                      Users Only)</font></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="275" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">Before 
                                      attempting to complete this section make 
                                      sure you have already selected the 'User 
                                      Type' for this new user from the previous 
                                      list.<br>
                                      <br>
                                      Now that you have selected a 'User Type' 
                                      for this user you will notice that the Granted 
                                      Rights list shows the rights associated 
                                      with the selected User Type. If you would 
                                      like to add to this default rights layout 
                                      follow the directions below. Keep in mind 
                                      that you cannot delete from the default 
                                      rights layout, so if you want a user not 
                                      a certain right it is suggested that you 
                                      change the User Type to a lower level user.<br>
                                      <br>
                                      To grant extra access rights to this user 
                                      choose an item from the 'Access Rights' 
                                      list then click the &gt;&gt;&gt;(Add) button.<br>
                                      <br>
                                      To remove a granted right, choose the item 
                                      you would like to remove from the 'Granted 
                                      Rights' list then click the &lt;&lt;&lt;(Remove) 
                                      button. You can ONLY remove a right that 
                                      has been added as an 'Extra Access Right'.</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="45" align="center"> 
                                      <table width="270" border="0" cellspacing="0" cellpadding="0" bgcolor="#FFFFFF" align="center">
                                        <tr> 
                                          <td align="center" width="130"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Access 
                                            Rights </b></font></td>
                                          <td width="10" rowspan="3"><img src="images/spacer.gif" width="10" height="1"></td>
                                          <td bgcolor="#8F8FAB" width="1" rowspan="3"><img src="images/verticalbar.gif" width="1" height="25"></td>
                                          <td width="10" rowspan="3"><img src="images/spacer.gif" width="10" height="1"></td>
                                          <td align="center" width="129"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Granted 
                                            Rights </b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="130" valign="top" align="center"> 
                                            <select name="AccessRights" size="8" multiple width="20" class="multiselect">
                                              <option value="PayOptions" SELECTED>Payment 
                                              Options</option>
                                              <option value="MarkupValues">Markup 
                                              Values</option>
                                              <option value="Passwords">Passwords</option>
                                              <option value="OrderReview">Orders</option>
                                              <option value="AdminCust">Customer 
                                              Accounts</option>
                                              <option value="AdminUser">User Accounts</option>
                                              <option value="ConfigDef">Main Configs</option>
                                              <option value="AdminProd">Product 
                                              Inventory</option>
                                              <option value="AdminMess">Message 
                                              Depot</option>
                                              <option value="AdminWeb">Website 
                                              (Content)</option>
                                              <option value="AdminPress">Press 
                                              Releases</option>
                                              <option value="AdminQISV">QISV</option>
                                            </select>
                                          </td>
                                          <td width="129" valign="bottom" align="center"> 
                                            <select name="GrantedRights" size="8" multiple width="20" class="multiselect">
                                              <option value="BIGNULL">0000000000000000</option>
                                            </select>
                                            <input type="hidden" name="ExtraAccess" value="">
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

## -------------------------->>> WITHOUT ExtraAccess FORM ELEMENTS - FOR THOSE WITHOUT ExtraAccess ADMIN RIGHTS
else { print "&nbsp;"; }

{
print <<EOF
                          <br>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
                <tr bordercolor="#333366" bgcolor="#F2F2F7"> 
                  <td align="center" valign="middle" height="45" bordercolor="#333366" bgcolor="#F2F2F7"> 
                    <input type="submit" value="Save Changes" name="submit" class="inputbut">
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

## ------------->>> if no useful calls present frameset
else {
{
print <<EOF

<html>
<head>
<title>User Accounts</title>
</head>
<frameset rows="64,*" rows="*" border="0" framespacing="0"> 
<frame name="topOne" scrolling="NO" noresize src="http://www.rhomberg.com/systemConfigurator/admin/topper.cgi" marginwidth="0" marginheight="0" frameborder="NO">
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
<title>User Accounts</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="http://www.rhomberg.com/systemConfigurator/admin/admincss.cgi" Type="text/css">
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
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>Create User Account</b></font></td>
          <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
              <tr bordercolor="#333366"> 
                <td width="50%" align="center" valign="top" height="250"> 
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
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>    </td>
  </tr>
</table>    </td>
  </tr>
</table>
  <table width="100%" background="images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0">
    <tr> 
      <td width="55%" align="left" height="56">&nbsp;</td>
    </tr>
  </table>
</body>
</html>

EOF
}
}
exit;