#!/usr/bin/perl5 -s

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
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("SELECT * FROM Users WHERE Username = '$Username'");
	$sth->execute or die "Sorry, that Username/Password combination is incorrect, please try again.\n"; 
	my $row = $sth->fetchrow_arrayref; 
	my $ThyCustNum = $row->[1];
	my $EType = $row->[2];
	my $Pass = $row->[4];
	my $Email = $row->[5];
	my $First = $row->[6];
	my $Last = $row->[7];
	my $Type = $row->[11];
	my $ExtraAccess = $row->[18];
	$sth->finish;

	if ($Pass eq $Password) {

		my $sth = $dbh->prepare("SELECT * FROM Customers WHERE InternalCustomerNumber = '$ThyCustNum'");
		$sth->execute or die "Sorry, that Username/Password combination is incorrect, please try again.\n"; 
		my $row = $sth->fetchrow_arrayref; 
		my $ShippingID = $row->[2];
		my $RepID = $row->[3];
		my $CompanyName = $row->[6];
		my $PayOption = $row->[15];
		my $DesktopValue = $row->[25];
		my $ServerValue = $row->[26];
		my $NotebookValue = $row->[27];
		my $MonitorValue = $row->[28];
		my $MemoryValue = $row->[29];
		my $HDriveValue = $row->[30];
		my $VideoValue = $row->[31];
		my $PeriphValue = $row->[32];
		my $PrinterValue = $row->[33];
		my $SoftwareValue = $row->[34];
		$sth->finish;
	
		# Print headers with only one \n 
		print "Content-type: text/html\n";
		&SetCookies('Echado','YES');
		&SetCookies('CeeEmmNo',$ThyCustNum);
		&SetCookies('EDomi',$Email);
		&SetCookies('GID',$Username);
		&SetCookies('FiNo',$First);
		&SetCookies('LaNo',$Last);
		&SetCookies('UTipe', "$Type");
		&SetCookies('CoNo', "$CompanyName");
		&SetCookies('DTV', "$DesktopValue");
		&SetCookies('SRV', "$ServerValue");
		&SetCookies('NBV', "$NotebookValue");
		&SetCookies('MOV', "$MonitorValue");
		&SetCookies('MYV', "$MemoryValue");
		&SetCookies('HDV', "$HDriveValue");
		&SetCookies('VDV', "$VideoValue");
		&SetCookies('PHV', "$PeriphValue");
		&SetCookies('PRV', "$PrinterValue");
		&SetCookies('SWV', "$SoftwareValue");
		&SetCookies('CNFIGS', '');
		&SetCookies('PTIES', '');
		
	    # End the headers by laying last \n
    	print "\n";

if ($FORM{'lasturl'}) {
	if ($FORM{'CID'}) { $muaURL = "http://www.rhomberg.com/systemConfigurator/$FORM{'lasturl'}?CID=$FORM{'CID'}"; }
	else { $muaURL = "http://www.rhomberg.com/systemConfigurator/$FORM{'lasturl'}"; }
}
else {
	$muaURL = "http://www.rhomberg.com/systemConfigurator/index.cgi";
}
		print "<html><head><title>Login Successful!</title>";
		print "<STYLE TYPE=\"text/css\">";
		print "body { background-color:#ffffff; scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }";
		print "</STYLE>";
		print "<script language=\"Javascript\">\n";
		print "		var b = navigator.appName;\n";
		print "		if (b==\"Netscape\" && navigator.userAgent.indexOf(\"6.\")) { this.location.href = \"$muaURL\"; }\n";
		print "		else if (b==\"Netscape\") { parent.frames.botOne.location.href = \"$muaURL\"; }\n";
		print "		else { this.location.href = \"$muaURL\"; }\n";
		print "</script>\n";
		print "</head><body bgcolor=\"#FFFFFF\" leftmargin=\"0\" topmargin=\"0\" marginwidth=\"0\" marginheight=\"0\"></body></html>";
	}
	else {
		print "Content-type: text/html\n\n";
{
print <<EOF

<html>
<head>
<title>Login</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<STYLE TYPE="text/css">
body { background-color:#ffffff; scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</STYLE>
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
<form method="post" name="login" action="login.cgi" onSubmit="return checkForm();">
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
                <a href="getpass.html"><font color="red">Forgot your password?</font></a> 
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
            <td colspan="4"><input type="image" name="submit" src="images/login/submit_off.gif" width="93" height="19" border="0" border="0" onMouseOver="javascript:imageOn2(this,'submit','on');" onMouseOut="javascript:imageOff2(this,'submit','off');"tabIndex="3">
			<font size="-4" face="verdana">&nbsp;</font>
			<a href="#" tabIndex="4" onClick="Javascript:document.location.reload();" onMouseOver="javascript:imageOn('reset','on');" onMouseOut="javascript:imageOff('reset','off');"><img src="images/login/reset_off.gif" name="reset" width="88" height="19" border="0"></a>
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

if ($FORM{'CID'}) { $CIDSTUFF = "<input type=\"hidden\" name=\"CID\" value=\"$FORM{'CID'}\">"; }

	print "Content-type: text/html\n\n";
{
print <<EOF

<html>
<head>
<title>Login</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<STYLE TYPE="text/css">
body { background-color:#ffffff; scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</STYLE>
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
$CIDSTUFF
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
        <font face="verdana,arial,helvetica" size="1" color="#333366"><b>E-Com Store Login</b><br>
        <br>
        </font> 
        <table width="350" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td width="135"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Username</b></font></td>
            <td rowspan="4" bgcolor="#8F8FAB" width="1"><img src="images/verticalbar.gif" width="1" height="25"></td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
            <td rowspan="4"><font face="verdana,arial,helvetica" size="1" color="#333366">To 
              access the Store Front, our E-Commerce Store, you must first login. 
              If you have any questions regarding this system or access to it 
              please contact a Coastline Micro manager.<br>
              <br>
              <center>
                <a href="getpass.html"><font color="red">Forgot your password?</font></a> 
              </center>
              </font></td>
          </tr>
          <tr> 
            <td width="135"> 
              <input type="text" name="Username" size="15">
            </td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>
          <tr> 
            <td width="135"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Password</b></font></td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>
          <tr> 
            <td width="135"> 
              <input type="password" name="Password" size="15">
            </td>
            <td width="15" bgcolor="#FFFFFF">&nbsp;</td>
          </tr>
          <tr> 
            <td colspan="4" height="20"><font face="verdana" size="-5">&nbsp;</font><font face="verdana" size="-5">&nbsp;</font><font face="verdana" size="-5">&nbsp;</font><font face="verdana" size="-5">&nbsp;</font></td>
          </tr>
          <tr align="center"> 
            <td colspan="4">
			<input type="image" name="submit" src="images/login/submit_off.gif" width="93" height="19" border="0" border="0" onMouseOver="javascript:imageOn2(this,'submit','on');" onMouseOut="javascript:imageOff2(this,'submit','off');">
			<font size="-4" face="verdana">&nbsp;</font>
			<a href="#" onClick="Javascript:document.location.reload();" onMouseOver="javascript:imageOn('reset','on');" onMouseOut="javascript:imageOff('reset','off');"><img src="images/login/reset_off.gif" name="reset" width="88" height="19" border="0"></a>
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