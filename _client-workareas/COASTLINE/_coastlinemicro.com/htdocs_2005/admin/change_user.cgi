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

###############
## If SAVING ##
###############
if (($FORM{'DROPIN'}) && ($FORM{'Username'}) && ($FORM{'LastName'})) {

## TOP HTML TEMPLATE
&topper;

	## Crumble Form Input to Variables
	my $CustomerID = "$FORM{'InternalCustNum'}";
	my $EmailType = "$FORM{'EmailType'}";
	my $Username = "$FORM{'Username'}";
	my $Password = "$FORM{'Password2'}";
	my $Email = "$FORM{'Email'}";
	my $FirstName = "$FORM{'FirstName'}";
	my $LastName = "$FORM{'LastName'}";
	my $Position = "$FORM{'Position'}";
	my $Phone = "$FORM{'Phone'}";
	my $Extension = "$FORM{'Extension'}";
	my $UserAccess = "$FORM{'UserAccess'}";
	my $ExtraAccess = "$FORM{'ExtraAccess'}";
	my $ActionUser = "$Cookies{'Username'}";
	
{
print <<EOF

<table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update User Account</b></font></td>
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
	print "<center><br><b>Update User Account</b><br><br>The account for <b>$Username</b> has been updated successfully.<br><br><form><input type=\"button\" value=\"Back to Profile\" onClick=\"javascript:location.href='change_user.cgi?Username=$Username&LastName=1'\" class=\"inputbut\"><br></center>";
	print "<br><br></font>";
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("UPDATE LOW_PRIORITY Users 
							 SET EmailType='$EmailType', 
							 Username='$Username', 
							 Password='$Password', 
							 Email='$Email', 
							 FirstName='$FirstName', 
							 LastName='$LastName', 
							 Position='$Position', 
							 Phone='$Phone', 
							 Extension='$Extension', 
							 UserAccess='$UserAccess', 
							 ExtraAccess='$ExtraAccess', 
							 ModifiedBy='$ActionUser', 
							 ModifiedOn=Null 
							 WHERE Username='$Username'");
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
#################
## If DELETING ##
#################
elsif (($FORM{'DELETEIT'}) && ($FORM{'Username'}) && ($FORM{'LastName'})) {

## TOP HTML TEMPLATE
&topper;

	## Crumble Form Input to Variables
	my $Username = "$FORM{'Username'}";
	my $LastName = "$FORM{'LastName'}";
	my $ActionUser = "$Cookies{'Username'}";

{
print <<EOF

<table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update User Account</b></font></td>
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
	print "<center><br><b>Delete User Account</b><br><br>The account for <b>$Username</b> has been deleted from the system effective immediately.<br><br><form><input type=\"button\" value=\"Back to Home\" onClick=\"javascript:parent.location.href='http://www.rhomberg.com/systemConfigurator/admin/index.cgi'\" class=\"inputbut\"><br></center>";
	print "<br><br></font>";
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("DELETE FROM Users WHERE Username='$Username' AND LastName='$LastName'");
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
################
## If VIEWING ##
################
elsif ($FORM{'Username'} && $FORM{'LastName'}) {

	## Crumble Form Input to Variables
	my $Username = "$FORM{'Username'}";
	my $LastName = "$FORM{'LastName'}";
	my $ActionUser = "$Cookies{'Username'}";
	##----------->>> If checking information for new user account... IE: Implementing Admin user to new user account
	if ($FORM{'AdminUser'}) { print "Please overlook the following fields to make sure all information is correct for this new user account."; }
	my $AdminUser = "$FORM{'AdminUser'}";

	##----------->>> Grab user Account Information
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $count=0;
	my $sth = $dbh->prepare("SELECT * FROM Users WHERE Username='$Username'");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		my $SavedCustomerID = $row[1];
		my $SavedEmailType = $row[2];
		my $SavedUsername = $row[3];
		my $SavedPassword = $row[4];
		my $SavedEmail = $row[5];
		my $SavedFirstName = $row[6];
		my $SavedLastName = $row[7];
		my $SavedPosition = $row[8];
		my $SavedPhone = $row[9];
		my $SavedExtension = $row[10];
		my $SavedUserAccess = $row[11];
		my $SavedAddedBy = $row[12];
		my $SavedAddedOn = $row[13];
		my $SavedModifiedBy = $row[14];
		my $SavedModifiedOn = $row[15];
		my $SavedDeletedBy = $row[16];
		my $SavedDeletedOn = $row[17];
		my $SavedExtraAccess = $row[18];
		## Re-Structure data as necessary
		my $TelArea = substr($SavedPhone, 0, 3);
		my $TelNum = substr($SavedPhone, 3, 7);
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
##----------->>> IF user Account DELETED, Show user who deleted profile
if ($SavedDeletedBy != "" || $SavedDeletedBy != " " || $SavedDeletedOn > 0) {
	print "<b>User Profile Deleted By:</b>$SavedDeletedBy<br>";
	print "<b>Deleted On:</b> <input type=\"text\" name=\"DeletedOn\" size=\"7\" class=\"inputtext7\" value=\"$DelMonth/$DelDay/$DelYear\"><br>";
}
##----------->>> ELSE read User Account Profile
else {

{
print <<EOF

<html>
<head>
<title>Add User Account</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="http://www.rhomberg.com/systemConfigurator/admin/admincss.cgi" Type="text/css">
<script language="Javascript">
function checkForm() {
var missingdrop = "";
var thefirst = "";

if (document.change.Password.value == "" || document.change.Password.value == " ") {
    missingdrop += "\\n     - Password";
	thefirst = "Password";
}
else if (document.change.Password.value.length < 8) {
    missingdrop += "\\n     - Password must be at least 8 characters";
	if (thefirst == "") { thefirst = "Password"; }
}

if (document.change.Password2.value != document.change.Password.value) {
    missingdrop += "\\n     - Confirm Password does not match Password";
	if (thefirst == "") { thefirst = "Password2"; }
}

// CHECK EMAIL
  if (document.change.Email.value == "")	{
    missingdrop += "\\n     - Email";
	if (thefirst == "") { thefirst = "Email"; }
  } else if ((document.change.Email.value.indexOf('\@') == -1) || 
        (document.change.Email.value.indexOf('.') == -1)) {
    missingdrop += "\\n     - Email Format should be: username\@mycompany.com";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.change.Email.value.indexOf(',') != -1)) {
    missingdrop += "\\n     - Commas are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.change.Email.value.indexOf(';') != -1)) {
    missingdrop += "\\n     - Semicolons are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.change.Email.value.indexOf(':') != -1)) {
    missingdrop += "\\n     - Colons are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.change.Email.value.indexOf('&') != -1)) {
    missingdrop += "\\n     - Ampersands are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.change.Email.value.indexOf(' ') != -1)) {
    missingdrop += "\\n     - Spaces are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }


if (document.change.FirstName.value == "" || document.change.FirstName.value == " ") {
    missingdrop += "\\n     - First Name";
	if (thefirst == "") { thefirst = "FirstName"; }
}

if (document.change.LastName.value == "" || document.change.LastName.value == " ") {
    missingdrop += "\\n     - Last Name";
	if (thefirst == "") { thefirst = "LastName"; }
}

if (document.change.Position.value == "" || document.change.Position.value == " ") {
    missingdrop += "\\n     - Position";
	if (thefirst == "") { thefirst = "Position"; }
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

// Check extension character
if (isNaN(document.change.Extension.value)) {
    missingdrop += "\\n     - Extension must be a number";
	if (thefirst == "") { thefirst = "Extension"; }
}

// Check GRANTED Access Rights
var strValues = "";
	var boxLength = document.change.GrantedRights.length;
	var count = 0;
if (boxLength != 0) {
	for (i = 0; i < boxLength; i++) {
		if (count == 0) {
			strValues = document.change.GrantedRights.options[i].value;
		}
		else {
			strValues = strValues + "," + document.change.GrantedRights.options[i].value;
		}
	count++;
   }
}
else { }
if (strValues.length == 0) { }
else {
	// Grab selected fields from PayOption and make PayTypes form field for processing
	document.change.ExtraAccess.value = strValues;
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

function checkSelects() {
MessageID = document.forms[0].MessageID; 

// CLEARS DEFAULT DATA FOR ALL NECESSARY SELECTS THAT WILL BE FED INFO FROM DB AT LOAD
MessageID.options[0] = null;
}

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

<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:checkSelects();feedMessages();">
$MenuConstructor
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%" valign="top"><img src="images/illus_main.jpg" width="250" height="100"></td>
    <td width="25%">&nbsp;</td>
    <td align="left" valign="top"><img src="images/title_main.jpg" width="300" height="100"></td>
  </tr>
</table>
<form method="post" action="$script" name="change" onSubmit="return checkForm();">
<table width="100%" border="0" height="100%" cellpadding="0" cellspacing="0">
  <tr valign="top"> 
    <td width="20%">$legal</td>
      <td align="center" width="80%"> 
        <table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
            <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update 
              User Account</b></font></td>
            <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
              <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER" bordercolor="#333366">
                <tr bordercolor="#333366" valign="middle"> 
                  <td width="100%" align="center" height="50" class="tableBG"><font face="verdana,arial,helvetica" size="1" color="#EB0000">*If 
                    you have any questions please ask your Supervisor or Manager 
                    for help using the system or updating it's information.</font> 
                    <font face="verdana,arial,helvetica" size="1" color="#333366"></font><font face="verdana,arial,helvetica" size="1" color="#333366"></font></td>
              </tr>
              <tr bordercolor="#333366"> 
                  <td width="50%" align="center" valign="top" bordercolor="#333366"> 
                    <table width="100%" border="0" cellspacing="0" cellpadding="5">
                      <tr> 
                        <td width="100%" align="center" height="25" bgcolor="#F2F2F7" class="tableBG" colspan="2"><font face="verdana,arial,helvetica" size="2" color="#333366"><b>User's 
                          Personal Information</b></font></td>
                      </tr>
                      <tr> 
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Username</font></b></font></td>
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
                                    <td height="35" align="center"> <font face="verdana,arial,helvetica" size="1" color="#333366">$SavedUsername</font> 
                                      <input type="hidden" name="Username" value="$Username">
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
                                      Password</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="105" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">Both 
                                      these fiels contain the password as saved 
                                      in the system. To retrieve a password for 
                                      a user please ask the user to utilize the 
                                      'Get Pass' function within the site. To 
                                      change the password type the new password 
                                      in both the password and confirm password 
                                      fields.<br>
                                      <br>
                                      <center>
                                        <font color="#EB0000">Minimum 8 characters</font> 
                                      </center>
                                      </font></td>
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
                                            <input type="password" name="Password" size="15" class="inputtext15" value="$SavedPassword">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Confirm 
                                            Password </b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="125" height="35" valign="top" align="center"> 
                                            <input type="password" name="Password2" size="15" class="inputtext15" value="$SavedPassword">
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
                                      <input type="text" name="Email" size="15" class="inputtext15" value="$SavedEmail">
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
                                      To/From User</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="85" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">This 
                                      system saves it's outgoing email messages 
                                      sent by the system or by the user to the 
                                      database. To view messages sent/recieved 
                                      by this user choose a message and click 
                                      'View Message'</font></td>
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
                                      <input type="button" value="View Message" class="inputbut" name="button">
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
                          <!--ONE-->
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
                          <!--TWO-->
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
                                      <input type="text" name="Position" size="15" class="inputtext15" value="$SavedPosition">
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
                                      <input type="text" name="TelArea" size="3" value="$TelArea" class="inputtext3">
                                      <input type="text" name="TelNum" size="7" value="$TelNum" class="inputtext7">
                                      </nobr> <font face="verdana,arial,helvetica" size="1" color="#333366"></font><nobr> 
                                      <input type="text" name="Extension" size="3" class="inputtext3" value="$SavedExtension">
                                      <input type="hidden" name="Phone">
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
                                    <td height="105" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366"><center>
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
</center>
                                      </font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"><nobr> 
                                      <select name="UserAccess" class="inputtext">
EOF
}

## ------------->>> IF Employee User RUN Employee User RIGHTS
if ($SavedUserAccess =~ "CO" || $SavedUserAccess =~ "WEB") { 

## WHICH UserAccess IS CHOSEN?
@Types = ("WEBAdmin","COManage","COSales","COUser");
foreach $Type (@Types) {
	if ($Type eq "$SavedUserAccess") { print "<option value=\"$Type\" SELECTED>$Type</option>"; }
	else { print "<option value=\"$Type\">$Type</option>"; }
}

}
## ------------->>> ELSE MUST BE CUSTOMER ACCOUNT RUN CUSTOMER USER RIGHTS
else { 

## WHICH UserAccess IS CHOSEN?
@Types = ("CustAdmin","CustUser");
foreach $Type (@Types) {
	if ($Type eq "$SavedUserAccess") { print "<option value=\"$Type\" SELECTED>$Type</option>"; }
	else { print "<option value=\"$Type\">$Type</option>"; }
}

}

{
print <<EOF
                                      </select>
<!--THREE-->
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
                        </td>
                      </tr>
                      <tr> 
                        <td width="100%" align="center" height="27" bgcolor="#F2F2F7" class="tableBG" colspan="2"><font face="verdana,arial,helvetica" size="2" color="#333366"><b>User's 
                          Profile Information </b></font></td>
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
EOF
}

## WHICH ExtraAccess rights are granted?
$count=0;
@AccessTypes = ("PayOptions,Payment Options","MarkupValues,Markup Values","Passwords,Passwords","OrderReview,Orders","AdminCust,Customer Accounts","AdminUser,User Accounts","ConfigDef,Main Configs","AdminProd,Product Inventory","AdminMess,Message Depot","AdminWeb,Website (Content)","AdminPress,Press Releases","AdminQISV,QISV");
foreach $Access (@AccessTypes) {
	$count++;
   	# Split the pair up into individual variables.
   	local($value, $name) = split(/,/, $Access);
	if ($SavedExtraAccess =~ "$value") { 
		print "<option value=\"$value\">$name</option>"; 
	}
}

{
print <<EOF
                                            </select>
<!--FOUR-->
                                            <input type="hidden" name="ExtraAccess" value="">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="130" valign="bottom" align="center"> 
                                            <input type="Button" value=" >>> "  onClick="javascript:jumpOption();" name="Button22">
                                          </td>
                                          <td width="129" valign="bottom" align="center"> 
                                            <input type="Button" value=" <<< "  onClick="javascript:killOption();" name="Button2">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Email 
                                      Format</font></b></font></td>
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
                                      <select name="EmailType" class="inputtext">
EOF
}

## WHICH EmailType IS CHOSEN?
@Types = ("HTML","TEXT");
foreach $Type (@Types) {
	if ($Type eq "$SavedEmailType") { print "<option value=\"$Type\" SELECTED>$Type</option>"; }
	else { print "<option value=\"$Type\">$Type</option>"; }
}

{
print <<EOF
                                      </select>
<!--FIVE-->
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
                    </table>
                </td>
              </tr>
              <tr bordercolor="#333366" bgcolor="#F2F2F7"> 
                  <td align="center" valign="middle" height="45" width="100%" bordercolor="#333366" bgcolor="#F2F2F7"> 
                    <input type="submit" value="Save User Profile" name="submit" class="inputbut">
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

##----------->>> GET MESSAGE FOR AND FROM USER
{
print <<EOF 

<script language="Javascript">
function feedMessages() {
MessageID = document.forms[0].MessageID;
var sizer = MessageID.length;
// GETTING READY TO FEED INFO

EOF
}

## Get list of Messages to and/or from this user
my $count=0;
my $sth = $dbh->prepare("SELECT * FROM Messages ORDER BY AddedOn ASC");
$sth->execute or die "Unable to execute query\n"; 
my @row;
while(@row = $sth->fetchrow_array) { 
	my $MessageID = $row[0];
	my $Username = $row[1];
	my $ReplyAdd = $row[5];
	my $Recipients = $row[6];
	my $AddedOn = $row[12];
	## reformat data
	my $AddYear = substr($AddedOn, 0, 2);
	my $AddMonth = substr($AddedOn, 2, 2);
	my $AddDay = substr($AddedOn, 4, 2);
	if (($ReplyAdd =~ $SavedEmail) || ($Recipients =~ $SavedEmail)) {
		print "MessageID.options[sizer] = new Option('$Username - $AddMonth/$AddDay/$AddYear');";
		print "MessageID.options[sizer].value = '$MessageID';";
		print "sizer++;";
		$count++;
	}
}
$sth->finish;
## if no messages from or to this user
if ($count eq "0") {
		print "MessageID.options[sizer] = new Option('No Messages Available');";
		print "MessageID.options[sizer].value = 'NONE';";
		print "sizer++;";
}
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

{
print <<EOF

<html>
<head>
<title>Shark Tank Admin System - Customer Accounts</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="http://www.rhomberg.com/systemConfigurator/admin/admincss.cgi" Type="text/css">
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
<table width="100%" border="0" cellpadding="0" cellspacing="0">
  <tr valign="top"> 
    <td width="20%"><br>$legal</td>
    <td align="center" width="80%"> 


<table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
            
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Add/Update 
            User Accounts</b></font></td>
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
<form method="post" action="$script" name="change">
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
                                        User Account</font></b></font></td>
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="55" bgcolor="#F2F2F7" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366">To 
                                        change or update a user's account profile 
                                        please choose the user you would like 
                                        to update from the list below then click 
                                        'View/Update'</font></td>
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="35" align="center"> 

                                        <select name="Username" class="inputtext">
EOF
}

	## Get list of CM reps
	use DBI;
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("SELECT * FROM Users ORDER BY Username ASC");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
		while(@row = $sth->fetchrow_array) { 
		my $Username = $row[3];
		my $LastName = $row[6];
		my $FirstName = $row[7];
		print "<option value=\"$Username\">$LastName, $FirstName ($Username)</option>";
	}
	$sth->finish;
	$dbh->disconnect;
	## print closing select tag

{
print <<EOF
</select>
                                        &nbsp;
                                        
                                        &nbsp;
<input type="submit" value="View/Update" class="inputbut" name="submit">
                                        <input type="hidden" name="LastName" value="1">
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
<form>
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
                                      New User Account</font></b></font></td>
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      
                                    <td height="35" bgcolor="#F2F2F7" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366">Click 
                                      the button below to create a new user account. 
                                      </font></td>
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="35" align="center"> 
                                        
                                      <input type="button" value="Create User Account" class="inputbut" onClick="javascript:parent.location.href='http://www.rhomberg.com/systemConfigurator/admin/add_user.cgi'">
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
</form>
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
                                      User Accounts</font></b></font></td>
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td colspan="4" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      
                                    <td height="85" bgcolor="#F2F2F7" align="left" colspan="2"><font face="verdana,arial,helvetica" size="1" color="#333366">To 
                                      Search user accounts, type in the Terms/Keywords 
                                      to help you locate the user account you 
                                      are interested in reviewing and/or updating. 
                                      Then, select a Search Filter Option, this 
                                      is the field searched in the database. Finally, 
                                      click 'Search Users'<br>
                                        <br>
                                      *To Browse user accounts, simply select 
                                      a Browse Filter Option then click 'Browse 
                                      Users' </font></td>
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="280" align="center" width="234" valign="top"> 
                                        <br>
<form method="post" action="http://www.rhomberg.com/systemConfigurator/admin/view_users.cgi">
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
                                              <input type="radio" name="SearchType" value="Username" SELECTED checked>
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">Username</font><br>
                                              <input type="radio" name="SearchType" value="FirstName">
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">First 
                                              Name</font><br>
                                              <input type="radio" name="SearchType" value="LastName">
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">Last 
                                              Name</font><br>
                                              <input type="radio" name="SearchType" value="Email">
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">Email 
                                              Address</font><br>
                                            </td>
                                          </tr>
                                          <tr> 
                                            <td align="center" height="35" valign="middle" width="200"> 
                                              <input type="submit" value="Search Users" class="inputbut" name="Submit">
                                            </td>
                                          </tr>
                                        </table>
</form>
                                      </td>
                                      <td height="280" align="center" width="234" valign="top"> 
                                        <br>
<form method="post" action="http://www.rhomberg.com/systemConfigurator/admin/view_users.cgi">
                                        <table border="1" cellspacing="0" cellpadding="0" width="200" bordercolor="#8F8FAB">
                                          <tr> 
                                            <td height="20" align="center" bgcolor="#F2F2F7" width="200"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Browse 
                                              Filter Options </b></font></td>
                                          </tr>
                                          <tr> 
                                            <td width="200" height="125"> 
                                              <input type="radio" name="Browse" value="Username" SELECTED checked>
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">Username</font><br>
                                              <input type="radio" name="Browse" value="FirstName">
                                              <font face="verdana,arial,helvetica" size="1" color="#333366"> 
                                              First Name</font><br>
                                              <input type="radio" name="Browse" value="LastName">
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">Last 
                                              Name</font><br>
                                              <input type="radio" name="Browse" value="Email">
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">Email 
                                              Address </font><br>
                                            </td>
                                          </tr>
                                          <tr> 
                                            <td width="200" align="center" height="35" valign="middle"> 
                                              <input type="submit" value="Browse Users" class="inputbut">
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
      </table>    </td>
  </tr>
</table>
<table width="100%" background="images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0"><tr><td width="55%" align="left" height="56">&nbsp;</td></tr></table>
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
<title>Administration System - $date</title>
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
<title>User Accounts</title>
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