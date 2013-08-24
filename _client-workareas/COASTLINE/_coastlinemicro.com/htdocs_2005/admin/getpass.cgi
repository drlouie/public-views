#!/usr/bin/perl5 -w

require ("referer.nsp");
require ("parse_query.nsp");

## ----------------------->>> If attemping to login
if ($FORM{'Username'} && $FORM{'FirstName'} && $FORM{'Email'}) {
	require ("cookie.lib");
	## Define Variables
	my $Username = "$FORM{'Username'}";
	my $FirstName = "$FORM{'FirstName'}";
	my $TheirEmail = "$FORM{'Email'}";
	## Start DB connection
	use DBI; 
	use strict; 
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("SELECT * FROM Users WHERE Username = '$Username' AND FirstName = '$FirstName'");
	$sth->execute or die "Sorry, that Username/Password combination is incorrect, please try again.\n"; 
	my $row = $sth->fetchrow_arrayref; 
	my $TheNumber = $row->[1];
	my $Pass = $row->[4];
	my $Email = $row->[5];
	my $First = $row->[6];
	$sth->finish;
	$dbh->disconnect; 

## ----------------------->>> if form fields match with DB, send password as email to this user
	if ($First =~ /$FirstName/ && $Email eq $TheirEmail) {
		## Make all comparisons lowercase
		use locale;
		my $LEmail = uc($Email);
		my $LTheirEmail = uc($TheirEmail);
		my $LFirst = uc($First);
		my $LFirstName = uc($FirstName);
## ----------------------->>> make sure email is truly the right one
		if ($LEmail eq $LTheirEmail) {

## ----------------------->>> SEND EMAIL MESSAGE
	my $SenderIn = "stadmin\@rhomberg.com(Shark Tank)";
	use lib "/www/htdocs/MIME-Lite-2.117/lib/";
    use MIME::Lite;
        my $msg = MIME::Lite->new(
                     From    =>$SenderIn,
                     To      =>$Email,
                     Subject =>'Administration System - Retrieve Password',
                     Type    =>'multipart/related'
                     );
        $msg->attach(Type => 'text/html',
                     Data => qq{ 
<html>
<head>
<title>Shark Tank Admin System - Retrieve Password</title>
<LINK REL="STYLESHEET" HREF="http://www.rhomberg.com/systemConfigurator/Mailbox/commoncss.cgi" Type="text/css">
</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<br>
<table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
<tr height="40">
<td rowspan="2" width="15%" align="left" valign="top"><a href="http://www.rhomberg.com/"><img src="http://www.rhomberg.com/systemConfigurator/Mailbox/images/top_cm_logo.jpg" width="116" height="37" border="0"></a></td>
<td rowspan="2" align="center" valign="bottom" width="30%">&nbsp;</td>
<td width="55%" align="right" valign="bottom"><img src="http://www.rhomberg.com/systemConfigurator/Mailbox/images/god_bless_america.gif" width="118" height="35"></td>
</tr>
<tr><td colspan="3" width="100%" bgcolor="#FFFFFF" height="5"><img src="http://www.rhomberg.com/systemConfigurator/Mailbox/images/spacer.gif" width="2" height="5"></td></tr>
<tr><td colspan="3" width="100%" bgcolor="#8F8FAB" height="2"><img src="http://www.rhomberg.com/systemConfigurator/Mailbox/images/spacer.gif" width="2" height="2"></td></tr>
<tr><td colspan="3" width="100%" bgcolor="#FFFFFF" height="2"><img src="http://www.rhomberg.com/systemConfigurator/Mailbox/images/spacer.gif" width="2" height="2"></td></tr>
</table>
<table width="95%" align="center" cellspacing="0" cellpadding="0" border="1" bordercolor="#8F8FAB" class="comtableborder"><tr><td width="100%" valign="top">
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="http://www.rhomberg.com/systemConfigurator/Mailbox/images/top_tablebg_main.jpg" height="100"><tr><td width="30%" valign="top"><img src="http://www.rhomberg.com/systemConfigurator/Mailbox/images/illus_main.jpg" width="250" height="100"></td><td width="25%">&nbsp;</td><td align="left" valign="top"><img src="http://www.rhomberg.com/systemConfigurator/Mailbox/images/title_main.jpg" width="300" height="100"></td></tr></table>
<table width="100%" background="http://www.rhomberg.com/systemConfigurator/Mailbox/images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0"><tr><td width="55%" align="left" height="56">&nbsp;</td></tr></table>
</td></tr></table>
<br>
</body></html>
								}
                     );
        $msg->send();

####################################################################
####################################################################
## FIX ERROR WITH SAVING EMAIL TO DB SOMETHING TO DO WITH CustNum ##
####################################################################
####################################################################

## ----------------------->>> SAVE COPY OF EMAIL MESSAGE TO DB
#*
#-	my $RecipientsIn = "$Email\n";
#-	my $SubjectIn = "Administration System - Retrieve Password";
#-	my $BodyIn = "$FirstName,\n\nHere is Shark Tank login information for your account as requested. \n\nUsername - $Username\nPassword - $Pass\n\nYour account is valid within the Shark Tank administration system and ECom Store.\n\nShark Tank administration system: http://www.rhomberg.com/systemConfigurator/admin/\n\nECom Store: http://www.coastlinemicro.com/\n\nDid not request this info?: security\@coastlinemicro.com\n\n\n";
#-	my $Attach1In = "";
#-	my $Attach2In = "";
#-	my $Attach3In = "";
#-	my $Number = "$TheNumber";
#-	## Start DB connection
#-	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
#-	$dbh->{RaiseError} = 1; 
#-	my $sth = $dbh->prepare("INSERT INTO Messages (MessageID, Username, QuoteID, OrderID, ConfigID, 
#-							 ReplyAdd, Recipients, Subject, Body, Attachment1, Attachment2, 
#-							 Attachment3, AddedOn, DeletedBy, DeletedOn, InternalCustNum)
#- 
#-						 	VALUES (Null, 'SharkTankAdmin', '', '', '', '$SenderIn', 
#-							'$RecipientsIn', '$SubjectIn', '$BodyIn', '$Attach1In', '$Attach2In', 
#-							'$Attach3In', Null, '', '', '$Number')");
#-	$sth->execute or die "Unable to execute query\n";
#-	$sth->finish;
#-	$dbh->disconnect;
#-
## ----------------------->>> Pass Good Call HTML
	&goodone;
}
}
else { &retry; }
exit;
}

## ----------------------->>> NO INPUT RESIDENT FORM FIELDS POSTED, SHOW FORM
else {
	print "Content-type: text/html\n\n";
{
print <<EOF

<html>
<head>
<title>Shark Tank Admin System - Retrieve Password</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<SCRIPT LANGUAGE="JavaScript">
// QUICK CROSS-BROWSER MOUSE-OVER/OFF FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function imageOff(which,thisone) {
	var cual = 	"images/login/"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}
function imageOn(which,thisone) {
	var cual = 	"images/login/"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}

function imageOff2(daobject,which,thisone) {
	var cual = 	"images/login/"+which+"_"+thisone+".gif";
	daobject.src = cual;
}
function imageOn2(daobject,which,thisone) {
	var cual = 	"images/login/"+which+"_"+thisone+".gif";
	daobject.src = cual;
}
</SCRIPT>
<script language="Javascript">
<!--
function checkForm() {
var missingdrop = "";
var thefirst = "";

// Check Common form fields
if (document.getpass.Username.value == "" || document.getpass.Username.value == " ") {
    missingdrop += "\\n     - Username";
	thefirst = "Username";
}

if (document.getpass.FirstName.value == "" || document.getpass.FirstName.value == " ") {
    missingdrop += "\\n     - First Name";
	if (thefirst == "") { thefirst = "FirstName"; }
}


// CHECK EMAIL
  if (document.getpass.Email.value == "")	{
    missingdrop += "\\n     - Email";
	if (thefirst == "") { thefirst = "Email"; }
  } else if ((document.getpass.Email.value.indexOf('\@') == -1) || 
        (document.getpass.Email.value.indexOf('.') == -1)) {
    missingdrop += "\\n     - Email Format should be: username\@mycompany.com";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.getpass.Email.value.indexOf(',') != -1)) {
    missingdrop += "\\n     - Commas are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.getpass.Email.value.indexOf(';') != -1)) {
    missingdrop += "\\n     - Semicolons are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.getpass.Email.value.indexOf(':') != -1)) {
    missingdrop += "\\n     - Colons are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.getpass.Email.value.indexOf('&') != -1)) {
    missingdrop += "\\n     - Ampersands are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.getpass.Email.value.indexOf(' ') != -1)) {
    missingdrop += "\\n     - Spaces are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    missingdrop ="___________________________________________                   \\n\\n" + "  Sorry, I cannot process your request because the\\n  following fields are either blank or filled incorrectly:\\n" + "___________________________________________                   \\n\\n" +
    missingdrop + "\\n\\n___________________________________________                   " + "\\n\\n   To continue, check fields and submit form again!" + "\\n___________________________________________";
    alert(missingdrop);
	document.getpass(thefirst).focus();
    return false;
} 
else {
return true;
}
}

//-->
</script>
</head>

<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:document.getpass.Username.focus();">
<form method="post" name="getpass" onSubmit="return checkForm();">
<table width="100%" border="0" height="100%" cellpadding="0" cellspacing="0">
  <tr>
    <td width="25%" height="50">&nbsp;</td>
    <td width="50%" height="50">&nbsp;</td>
    <td width="25%" height="50">&nbsp;</td>
  </tr>
  <tr>
    <td width="25%">&nbsp;</td>
      <td align="center" width="50%" valign="middle"><img src="images/splash_logos.jpg" width="166" height="164"><br>
        <br>
        <font face="verdana,arial,helvetica" size="1" color="#333366"><b>Retrieve My Password</b><br>
        <br>
        </font> 
        <table width="350" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td width="135"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Username</b></font></td>
            <td rowspan="6" bgcolor="#8F8FAB" width="1"><img src="images/verticalbar.gif" width="1" height="25"></td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
            <td rowspan="6"s><font face="verdana,arial,helvetica" size="1" color="#333366">To retrieve your password please fill out these form fields. All information you input must match the information saved in your user profile. If you have any problems please ask a supervisor for further assistance.<br></font></td>
          </tr>
          <tr> 
            <td width="135"> 
              <input type="text" name="Username" size="15" tabindex="1">
            </td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>
          <tr> 
            <td width="135"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>First Name</b></font></td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>
          <tr> 
            <td width="135"> 
              <input type="text" name="FirstName" size="15" tabindex="2">
            </td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>

          <tr> 
            <td width="135"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Email Address</b></font></td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>
          <tr> 
            <td width="135"> 
              <input type="text" name="Email" size="15" tabindex="3">
            </td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>
          <tr> 
            <td colspan="4" height="20"><font face="verdana" size="-5">&nbsp;</font><font face="verdana" size="-5">&nbsp;</font><font face="verdana" size="-5">&nbsp;</font><font face="verdana" size="-5">&nbsp;</font></td>
          </tr>
          <tr align="center"> 
            <td colspan="4">
			<input type="image" name="submit" tabindex="4" src="images/login/getpass_off.gif" width="93" height="19" border="0" onMouseOver="javascript:imageOn2(this,'getpass','on');" onMouseOut="javascript:imageOff2(this,'getpass','off');">
			<font size="-4" face="verdana">&nbsp;</font>
			<a href="#" onClick="Javascript:document.location.reload();" tabindex="5" onMouseOver="javascript:imageOn('reset','on');" onMouseOut="javascript:imageOff('reset','off');"><img src="images/login/reset_off.gif" name="reset" width="88" height="19" border="0"></a>
			</td>
          </tr>
        </table>
    </td>
      <td width="25%">&nbsp;</td>
  </tr>
  <tr>
    <td width="25%" height="50">&nbsp;</td>
    <td width="50%" height="50">&nbsp;</td>
    <td width="25%" height="50">&nbsp;</td>
  </tr>
</table>
</form>
</body>
</html>

EOF
}
exit;
}

## IF GOOD ONE WAS SENT
sub goodone {

print "Content-type: text/html\n\n";
{
print <<EOF

<html>
<head>
<title>Shark Tank Admin System - Retrieve Password</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>

<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<form method="post">
<table width="100%" border="0" height="100%" cellpadding="0" cellspacing="0">
  <tr>
    <td width="25%" height="50">&nbsp;</td>
    <td width="50%" height="50">&nbsp;</td>
    <td width="25%" height="50">&nbsp;</td>
  </tr>
  <tr>
    <td width="25%">&nbsp;</td>
      <td align="center" width="50%" valign="middle"><img src="images/splash_logos.jpg" width="166" height="164"><br>
        <br>
        <font face="verdana,arial,helvetica" size="1" color="#333366"><b>Account Matched Successfully</b><br>
        <br>
        </font> 
        <table width="350" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td width="100%"><font face="verdana,arial,helvetica" size="1" color="#333366">Your login information has been sent to your email address. Please check your email and try logging back into the system again.<br><br>If you have any further problems please ask a supervisor for assistance.<br><br><center><font color="red"><a href="http://www.rhomberg.com/systemConfigurator/admin/">Back to Administration System</a></font></center></font></td>
          </tr>
        </table>
    </td>
      <td width="25%">&nbsp;</td>
  </tr>
  <tr>
    <td width="25%" height="50">&nbsp;</td>
    <td width="50%" height="50">&nbsp;</td>
    <td width="25%" height="50">&nbsp;</td>
  </tr>
</table>
</form>
</body>
</html>

EOF
}
exit;
}

## IF TRY WAS NO GOOD, TRY AGAIN SCREEN
sub retry {

print "Content-type: text/html\n\n";
{
print <<EOF

<html>
<head>
<title>Shark Tank Admin System - Retrieve Password</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<SCRIPT LANGUAGE="JavaScript">
// QUICK CROSS-BROWSER MOUSE-OVER/OFF FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function imageOff(which,thisone) {
	var cual = 	"images/login/"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}
function imageOn(which,thisone) {
	var cual = 	"images/login/"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}

function imageOff2(daobject,which,thisone) {
	var cual = 	"images/login/"+which+"_"+thisone+".gif";
	daobject.src = cual;
}
function imageOn2(daobject,which,thisone) {
	var cual = 	"images/login/"+which+"_"+thisone+".gif";
	daobject.src = cual;
}
</SCRIPT>
<script language="Javascript">
<!--
function checkForm() {
	if ((document.getpass.Username.value == "") || (document.getpass.Username.value == "0") || (document.getpass.Username.value == " ")) {
		alert('Before you can retrieve your login information you must type in your username.')
		document.getpass.Username.focus();
		return false;
	}	
	if ((document.getpass.FirstName.value == "") || (document.getpass.FirstName.value == "0") || (document.getpass.FirstName.value == " ")) {
		alert('Before you can retrieve your login information you must type in your first name as saved in the system.')
		document.getpass.FirstName.focus();
		return false;
	}	
	var x= document.getpass.Email.value;
	if( x.indexOf('\@')==-1 || x.indexOf('.')==-1 || x.indexOf(' ')!=-1 || x.length<7) {
    	alert('Your Email Address is invalid or missing. Please enter a valid email address.');
		document.getpass.Email.focus();
    	return false;
	}
	else {
		return true;
	}	
}

//-->
</script>
</head>

<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:document.getpass.Username.select();document.getpass.Username.focus();">
<form method="post" name="getpass" onSubmit="return checkForm();">
<table width="100%" border="0" height="100%" cellpadding="0" cellspacing="0">
  <tr>
    <td width="25%" height="50">&nbsp;</td>
    <td width="50%" height="50">&nbsp;</td>
    <td width="25%" height="50">&nbsp;</td>
  </tr>
  <tr>
    <td width="25%">&nbsp;</td>
      <td align="center" width="50%" valign="middle"><img src="images/splash_logos.jpg" width="166" height="164"><br>
        <br>
        <font face="verdana,arial,helvetica" size="1" color="#333366"><b>Sorry No Matching Accounts</b><br>
        <br>
        </font> 
        <table width="350" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td width="135"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Username</b></font></td>
            <td rowspan="6" bgcolor="#8F8FAB" width="1"><img src="images/verticalbar.gif" width="1" height="25"></td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
            <td rowspan="6"s><font face="verdana,arial,helvetica" size="1" color="#333366"><font color="red">*</font>Sorry, no accounts match the information you submitted, please try again.<br><br>All information you input must match the information saved in your user profile. If you have any problems please ask a supervisor for further assistance.<br></font></td>
          </tr>
          <tr> 
            <td width="135"> 
              <input type="text" name="Username" value="$FORM{'Username'}" size="15" tabindex="1">
            </td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>
          <tr> 
            <td width="135"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>First Name</b></font></td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>
          <tr> 
            <td width="135"> 
              <input type="text" name="FirstName"  value="$FORM{'FirstName'}" size="15" tabindex="2">
            </td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>

          <tr> 
            <td width="135"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Email Address</b></font></td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>
          <tr> 
            <td width="135"> 
              <input type="text" name="Email"  value="$FORM{'Email'}" size="15" tabindex="3">
            </td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>
          <tr> 
            <td colspan="4" height="20"><font face="verdana" size="-5">&nbsp;</font><font face="verdana" size="-5">&nbsp;</font><font face="verdana" size="-5">&nbsp;</font><font face="verdana" size="-5">&nbsp;</font></td>
          </tr>
          <tr align="center"> 
            <td colspan="4">
			<input type="image" name="submit" tabindex="4" src="images/login/getpass_off.gif" width="93" height="19" border="0" onMouseOver="javascript:imageOn2(this,'getpass','on');" onMouseOut="javascript:imageOff2(this,'getpass','off');">
			<font size="-4" face="verdana">&nbsp;</font>
			<a href="#" onClick="Javascript:document.location.reload();" tabindex="5" onMouseOver="javascript:imageOn('reset','on');" onMouseOut="javascript:imageOff('reset','off');"><img src="images/login/reset_off.gif" name="reset" width="88" height="19" border="0"></a>
			</td>
          </tr>
        </table>
    </td>
      <td width="25%">&nbsp;</td>
  </tr>
  <tr>
    <td width="25%" height="50">&nbsp;</td>
    <td width="50%" height="50">&nbsp;</td>
    <td width="25%" height="50">&nbsp;</td>
  </tr>
</table>
</form>
</body>
</html>

EOF
}
exit;
}