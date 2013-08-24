#!/usr/bin/perl5 -w

require ("referer.nsp");
require ("parse_query.nsp");

## If attemping to login
if ($FORM{'Username'} && $FORM{'Password'}) {
	require ("cookie.lib");
	## Define Variables
	my $Username = "$FORM{'Username'}";
	my $Password = "$FORM{'Password'}";
	my $lasturl = "$FORM{'lasturl'}";
	## Start DB connection
	use DBI; 
	use strict; 
	my $dbh = DBI->connect('DBI:mysql:coastline','drlouie','chinga2') or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("SELECT * FROM Users WHERE Username = '$Username'");
	$sth->execute or die "Sorry, that Username/Password combination is incorrect, please try again.\n"; 
	my $row = $sth->fetchrow_arrayref; 
	my $CMCustNum = $row->[1];
	my $Pass = $row->[4];
	my $First = $row->[6];
	my $Last = $row->[7];
	my $Type = $row->[11];
	my $ExtraAccess = $row->[18];
	$sth->finish;

	if ($Pass eq $Password) {
		# Print headers with only one \n 
		print "Content-type: text/html\n";
		&SetCookies('Logged','YES');
		&SetCookies('CMCustNum',$CMCustNum);
		&SetCookies('Username',$Username);
		&SetCookies('Password',$Password);
		&SetCookies('FirstName',$First);
		&SetCookies('LastName',$Last);
		&SetCookies('UserType',$Type);
		&SetCookies('ExtraAccess',$ExtraAccess);
	    # End the headers by laying last \n
    	print "\n";

		print "<html><head><title>Login Successful!</title>";
		if ($lasturl) { print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"1;URL=http://www.coastlinemicro.com$lasturl\" TARGET=\"_top\">"; }
		else { print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"1;URL=http://www.coastlinemicro.com/admin/\" TARGET=\"_top\">"; }
		print "</head><body></body></html>";
	}
	else {
		print "Content-type: text/html\n\n";
{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - Administration System Login</title>
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
	if ((document.login.Username.value == "") || (document.login.Username.value == "0") || (document.login.Username.value == " ")) {
	alert('Before you can login you must type in your account username.')
	document.login.Username.focus();
	return false;
	}	
	if ((document.login.Password.value == "") || (document.login.Password.value == "0") || (document.login.Password.value == " ")) {
	alert('Before you can login you must type in your account password.')
	document.login.Password.focus();
	return false;
	}	
	else {
	return true;
	}	
}
//-->
</script>
</head>

<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:document.login.Username.select();document.login.Username.focus();">
<form method="post" name="login" onSubmit="return checkForm();">
<input type="hidden" name="lasturl" value="$lasturl">
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
        <font face="verdana,arial,helvetica" size="1" color="#333366"><b>Bad Login Attempt</b><br>
        <br>
        </font> 
        <table width="350" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td width="135"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Username</b></font></td>
            <td rowspan="4" bgcolor="#8F8FAB" width="1"><img src="images/verticalbar.gif" width="1" height="25"></td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
            <td rowspan="4"><font face="verdana,arial,helvetica" size="1" color="#333366"><font color="red">*</font>Sorry, that Username/Password combination was incorrect, please try again.<br>
              <br>
              <center>
                <a href="getpass.cgi"><font color="red">Forgot your password?</font></a> 
              </center>
              </font></td>
          </tr>
          <tr> 
            <td width="135"> 
              <input type="text" name="Username" value="$Username" size="15" tabIndex="1">
            </td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>
          <tr> 
            <td width="135"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Password</b></font></td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>
          <tr> 
            <td width="135"> 
              <input type="password" name="Password" value="$Password" size="15" tabIndex="2">
            </td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>
          <tr> 
            <td colspan="4" height="20"><font face="verdana" size="-5">&nbsp;</font><font face="verdana" size="-5">&nbsp;</font><font face="verdana" size="-5">&nbsp;</font><font face="verdana" size="-5">&nbsp;</font></td>
          </tr>
          <tr align="center"> 
            <td colspan="4"><input type="image" name="submit" tabIndex="3" src="images/login/submit_off.gif" width="93" height="19" border="0" border="0" onMouseOver="javascript:imageOn2(this,'submit','on');" onMouseOut="javascript:imageOff2(this,'submit','off');">
			<font size="-4" face="verdana">&nbsp;</font>
			<a href="#" onClick="Javascript:document.location.reload();" tabIndex="4" onMouseOver="javascript:imageOn('reset','on');" onMouseOut="javascript:imageOff('reset','off');"><img src="images/login/reset_off.gif" name="reset" width="88" height="19" border="0"></a>
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

	}
	$dbh->disconnect; 
exit;
}

else {
	print "Content-type: text/html\n\n";
{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - Administration System Login</title>
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
	if ((document.login.Username.value == "") || (document.login.Username.value == "0") || (document.login.Username.value == " ")) {
	alert('Before you can login you must type in your account username.')
	document.login.Username.focus();
	return false;
	}	
	if ((document.login.Password.value == "") || (document.login.Password.value == "0") || (document.login.Password.value == " ")) {
	alert('Before you can login you must type in your account password.')
	document.login.Password.focus();
	return false;
	}	
	else {
	return true;
	}	
}
//-->
</script>
</head>

<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:document.login.Username.focus();">
<form method="post" name="login" onSubmit="return checkForm();">
<input type="hidden" name="lasturl" value="$FORM{'lasturl'}">
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
        <font face="verdana,arial,helvetica" size="1" color="#333366"><b>Administration 
        System Login</b><br>
        <br>
        </font> 
        <table width="350" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td width="135"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Username</b></font></td>
            <td rowspan="4" bgcolor="#8F8FAB" width="1"><img src="images/verticalbar.gif" width="1" height="25"></td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
            <td rowspan="4"><font face="verdana,arial,helvetica" size="1" color="#333366">To 
              access the Shark Tank's administrative system you must first login. 
              If you have any questions regarding this system or access to it 
              please contact a Coastline Micro manager.<br>
              <br>
              <center>
                <a href="getpass.cgi"><font color="red">Forgot your password?</font></a> 
              </center>
              </font></td>
          </tr>
          <tr> 
            <td width="135"> 
              <input type="text" name="Username" size="15" tabIndex="1">
            </td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>
          <tr> 
            <td width="135"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Password</b></font></td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>
          <tr> 
            <td width="135"> 
              <input type="password" name="Password" size="15" tabIndex="2">
            </td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>
          <tr> 
            <td colspan="4" height="20"><font face="verdana" size="-5">&nbsp;</font><font face="verdana" size="-5">&nbsp;</font><font face="verdana" size="-5">&nbsp;</font><font face="verdana" size="-5">&nbsp;</font></td>
          </tr>
          <tr align="center"> 
            <td colspan="4">
			<input type="image" name="submit" tabIndex="3" src="images/login/submit_off.gif" width="93" height="19" border="0" border="0" onMouseOver="javascript:imageOn2(this,'submit','on');" onMouseOut="javascript:imageOff2(this,'submit','off');">
			<font size="-4" face="verdana">&nbsp;</font>
			<a href="#" onClick="Javascript:document.location.reload();" tabIndex="4" onMouseOver="javascript:imageOn('reset','on');" onMouseOut="javascript:imageOff('reset','off');"><img src="images/login/reset_off.gif" name="reset" width="88" height="19" border="0"></a>
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

}

1;