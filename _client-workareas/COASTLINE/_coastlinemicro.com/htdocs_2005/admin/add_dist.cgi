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
if (($Cookies{'UserType'} eq "COManage") || ($Cookies{'UserType'} eq "WEBAdmin") || ($Cookies{'UserType'} eq "COSales") || ($Cookies{'ExtraAccess'} =~ "AdminCust")) { $nextone = "1"; }
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
if (($FORM{'Name'}) && ($FORM{'Url'}) && ($FORM{'MailAdd'}) && ($FORM{'MailZip'})) {

## TOP HTML TEMPLATE
&topper;

	## Crumble Form Input to Variables
	my $Name = "$FORM{'Name'}";
	my $URL = "$FORM{'Url'}";
	my $MailAdd = "$FORM{'MailAdd'}";
	my $MailAdd2 = "$FORM{'MailAdd2'}";
	my $MailCity = "$FORM{'MailCity'}";
	my $MailState = "$FORM{'MailState'}";
	my $MailZip = "$FORM{'MailZip'}";
	my $MainPhone = "$FORM{'Phone'}";
	my $MainFax = "$FORM{'Fax'}";
	my $MainEmail = "$FORM{'MainEmail'}";	
	my $ActionUser = "$Cookies{'Username'}";

##----------->>> Start Customer Account Check, make sure no dupes are made
	use DBI;
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $count=0;
	my $sth = $dbh->prepare("SELECT * FROM DISTs");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		my $SavedName = $row[1];
		my $SavedUrl = $row[2];
		my $SavedCity = $row[5];
		my $SavedState = $row[6];
		my $SavedMainEmail = $row[8];
		my $SavedPhone = $row[9];
		## Re-Structure data as necessary
		my $AreaCode = substr($SavedPhone, 0, 3);
		my $PhoneNum3 = substr($SavedPhone, 3, 3);
		my $PhoneNum4 = substr($SavedPhone, 6, 4);
		
## ---------->>> IF EXISTS DIE PRINT OUT RECORD(s) THAT MATCH REQUEST
		if (($SavedName eq $Name) || ($SavedUrl eq $URL) || ($SavedMainEmail eq $MainEmail)) {
{
print <<EOF

            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
              <tr bordercolor="#333366" valign="middle">
                <td width="100%" align="center" height="20" bgcolor="#F2F2F7" class="tableBG"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Request 
                  Cannot Be Completed</b></font></td>
              </tr>
              <tr bordercolor="#333366"> 
                <td width="50%" align="center" valign="top" height="250"> 
                  <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr> 
                      <td width="100%"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Error Description</b><br>
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
<tr height="20" width="100%">
<td align="center" width="15%"><font class="sresultsred"><b>DIST's Name</b><br></font></td>
<td align="center" width="25%"><font class="sresults1"><b>DIST URL</b></font></td>
<td align="center" width="15%"><font class="sresults1"><b>DIST Email</b></font></td>
<td align="center" width="15%"><font class="sresults1"><b>City</b></font></td>
<td align="center" width="15%"><font class="sresults1"><b>State</b></font></td>
<td align="center" width="15%"><font class="sresults1"><b>Phone</b></font></td>
</tr>

EOF
}

			if ($SavedName eq $Name) { $SavedName = "<font color=\"red\">$SavedName</font>"}
			if ($SavedUrl eq $URL) { $SavedUrl = "<font color=\"red\">$SavedUrl</font>"}
			if ($SavedMainEmail eq $MainEmail) { $SavedMainEmail = "<font color=\"red\">$SavedMainEmail</font>"}
			$count++;
			print "<tr width=\"100%\">";
			print "<td><font class=\"stextbig\" width=\"15%\"><b>$SavedName&nbsp;</b></font></td>";
			print "<td><font class=\"stextbig\" width=\"25%\">$SavedUrl&nbsp;</font></td>";
			print "<td><font class=\"stextbig\" width=\"15%\">$SavedMainEmail&nbsp;</font></td>";
			print "<td><font class=\"stextbig\" width=\"15%\">$SavedCity&nbsp;</font></td>";
			print "<td><font class=\"stextbig\" width=\"15%\">$SavedState&nbsp;</font></td>";
			print "<td><font class=\"stextbig\" width=\"15%\">($AreaCode) $PhoneNum3-$PhoneNum4&nbsp;</font></td>";
			print "</tr>";
			$dbh->disconnect;
			$sth->finish;
			print "</table>";
			print "<center><form><input type=\"button\" value=\"Try Again\" onClick=\"javascript:history.go(-1)\" class=\"inputbut\"><br><br><input type=\"button\" value=\"Cancel Account Addition\" onClick=\"javascript:parent.location.href='index.html'\" class=\"inputbut\"></form></center>";
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
              <tr bordercolor="#333366" valign="middle"> 
                <td width="100%" align="center" height="20" bgcolor="#F2F2F7" class="tableBG"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Request Completed Successfully</b></font></td>
              </tr>
              <tr bordercolor="#333366"> 
                <td width="50%" align="center" valign="top" height="250"> 
                  <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr> 
                      <td width="100%"><font face="verdana,arial,helvetica" size="1" color="#333366">
					  
EOF
}
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("INSERT INTO DISTs (DistributorID, Name, URL, 
							 MailAdd, MailAdd2, MailCity, MailState, MailZip,  
							 MainEmail, MainPhone, MainFax, Emblem, LogoSmall, 
							 LogoMedium, LogoLarge, AddedBy, AddedOn, ModifiedBy, 
							 ModifiedOn)

							 VALUES (Null, '$Name', '$URL', '$MailAdd', '$MailAdd2', 
							 '$MailCity', '$MailState', '$MailZip', '$MainEmail', 
							 '$MainPhone', '$MainFax', '', '', '', '', 
							 '$ActionUser', Null, '', '')");

	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish; 
	print "<b>Create Distributor Profile</b><br>The distributor porfile for <b>$Name</b> has been created successfully. This profile will be used in conjuction with this distributor's product line.<center><br><br><form><input type=\"button\" value=\"Take Me Home\" onClick=\"javascript:parent.location.href='index.html'\" class=\"inputbut\"><br></center></font>";
	print "<br><br>";
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
<title>Shark Tank Admin System - Customer Accounts</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<script language="Javascript">
// CROSS-BROWSER FORM CHECKER
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function checkForm() {
var missingdrop = "";
var thefirst = "";

// Check Common form fields
if (document.add.Name.value == "" || document.add.Name.value == " ") {
    missingdrop += "\\n     - Distributor's Name";
	thefirst = "Name";
}

if ((document.add.Url.value == "") || (document.add.Url.value == " ") || (document.add.Url.value.indexOf('.') == -1)) {
    missingdrop += "\\n     - DIST's Website URL";
	if (thefirst == "") { thefirst = "Url"; }
}

if (document.add.MailAdd.value == "" || document.add.MailAdd.value == " ") {
    missingdrop += "\\n     - Distributor's Mailing Address";
	if (thefirst == "") { thefirst = "MailAdd"; }
}

if (document.add.MailCity.value == "" || document.add.MailCity.value == " ") {
    missingdrop += "\\n     - Distributor's City";
	if (thefirst == "") { thefirst = "MailCity"; }
}

if (isNaN(document.add.MailZip.value) || (document.add.MailZip.value == "") || (document.add.MailZip.value == " ") || (document.add.MailZip.value.length != 5)) {
    missingdrop += "\\n     - Distributor's Zip Code must be a 5 digit number";
	if (thefirst == "") { thefirst = "MailZip"; }
}
// Check Phone number and format if it is there get the area code and num and feed the Phone field
if (isNaN(document.add.TelArea.value) || (document.add.TelArea.value == "") || (document.add.TelArea.value == " ") || (document.add.TelArea.value.length != 3)) {
    missingdrop += "\\n     - Distributor's Phone's Area Code must be a 3 digit number";
	if (thefirst == "") { thefirst = "TelArea"; }
}
else if (isNaN(document.add.TelNum.value) || (document.add.TelNum.value == "") || (document.add.TelNum.value == " ") || (document.add.TelNum.value.indexOf('-') != -1) || (document.add.TelNum.value.length != 7)) {
    missingdrop += "\\n     - Distributor's Phone Number must be a 7 digit number\\n        *No hyphen (-) necessary";
	if (thefirst == "") { thefirst = "TelNum"; }
}
else {
	PhoneValues = document.add.TelArea.value + document.add.TelNum.value;
	document.add.Phone.value = PhoneValues;
}

// Check Fax number and format if it is there get the area code and num and feed the Fax field
if (isNaN(document.add.FaxArea.value) || (document.add.FaxArea.value == "") || (document.add.FaxArea.value == " ") || (document.add.FaxArea.value.length != 3)) {
    missingdrop += "\\n     - Distributor's Fax's Area Code must be a 3 digit number";
	if (thefirst == "") { thefirst = "FaxArea"; }
}
else if (isNaN(document.add.FaxNum.value) || (document.add.FaxNum.value == "") || (document.add.FaxNum.value == " ") || (document.add.FaxNum.value.indexOf('-') != -1) || (document.add.FaxNum.value.length != 7)) {
    missingdrop += "\\n     - Distributor's Fax Number must be a 7 digit number\\n        *No hyphen (-) necessary";
	if (thefirst == "") { thefirst = "FaxNum"; }
}
else {
	FaxValues = document.add.FaxArea.value + document.add.FaxNum.value;
	document.add.Fax.value = FaxValues;
}

// CHECK MAIN EMAIL
  if (document.add.MainEmail.value == "")	{
    missingdrop += "\\n     - Distributor's Main Email";
	if (thefirst == "") { thefirst = "MainEmail"; }
  } else if ((document.add.MainEmail.value.indexOf('\@') == -1) || 
        (document.add.MainEmail.value.indexOf('.') == -1)) {
    missingdrop += "\\n     - Mainufactuer's Email Format should be: username\@mycompany.com";
	if (thefirst == "") { thefirst = "MainEmail"; }
  }
  if ((document.add.MainEmail.value.indexOf(',') != -1)) {
    missingdrop += "\\n     - Commas are not allowed in email addresses";
	if (thefirst == "") { thefirst = "MainEmail"; }
  }
  if ((document.add.MainEmail.value.indexOf(';') != -1)) {
    missingdrop += "\\n     - Semicolons are not allowed in email addresses";
	if (thefirst == "") { thefirst = "MainEmail"; }
  }
  if ((document.add.MainEmail.value.indexOf(':') != -1)) {
    missingdrop += "\\n     - Colons are not allowed in email addresses";
	if (thefirst == "") { thefirst = "MainEmail"; }
  }
  if ((document.add.MainEmail.value.indexOf('&') != -1)) {
    missingdrop += "\\n     - Ampersands are not allowed in email addresses";
	if (thefirst == "") { thefirst = "MainEmail"; }
  }
  if ((document.add.MainEmail.value.indexOf(' ') != -1)) {
    missingdrop += "\\n     - Spaces are not allowed in email addresses";
	if (thefirst == "") { thefirst = "MainEmail"; }
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
<form method="post" action="$script" name="add" onSubmit="return checkForm();">
<table width="100%" border="0" height="100%" cellpadding="0" cellspacing="0">
  <tr valign="top"> 
    <td width="20%">$legal</td>
    <td align="center" width="80%"> 
      <table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
            <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>Create 
              Distributor Profile</b></font></td>
          <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
              <tr bordercolor="#333366" valign="middle"> 
                <td width="50%" align="center" height="20" bgcolor="#F2F2F7" class="tableBG"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Function 
                  Instructions</b></font></td>
              </tr>
              <tr bordercolor="#333366"> 
                <td width="50%" align="center" valign="top"> 
                    <table width="100%" border="0" cellspacing="0" cellpadding="5">
                      <tr> 
                        <td height="165" valign="top" colspan="2"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Function 
                          Overview</b><br>
                          K</font><font face="verdana,arial,helvetica" size="1" color="#333366">eep 
                          in mind that you are given specific access to this system 
                          to add, change and delete users. Please use that access 
                          wisely for many actions associated with this administration 
                          system cannot be redone and are destrcutive especially 
                          when deleting stored data. <br>
                          <br>
                          Please make sure you are fully aware of this system's 
                          layout and function before making changes to it. For 
                          security's sake we have implemented a log system that 
                          traces every add, change and deletion of the database's 
                          data and structure.<br>
                          <br>
                          <b>To Create Distributor Profile<br>
                          </b>Follow the instructions next to the each form field. 
                          <b>ALL</b> fields must be completed to create the new 
                          Distributor profile in the system. <br>
                          <br>
                          <font color="#EB0000">*If you have any questions please 
                          ask your Supervisor or Manager for help using the system 
                          or updating it's information.</font></font></td>
                      </tr>
                      <tr> 
                        <td width="100%" align="center" height="25" bgcolor="#F2F2F7" class="tableBG" colspan="2"><font face="verdana,arial,helvetica" size="2" color="#333366"><b>Distributor 
                          Information</b></font></td>
                      </tr>
                      <tr> 
                        <td align="center" valign="top"> <br>
                          <table width="350" border="0" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="100%" colspan="9" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="60"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="15" rowspan="2" height="60"><img src="images/spacer.gif" width="15" height="8"></td>
                              <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Distributor's 
                                Name</b></font></td>
                              <td width="10" rowspan="2" height="60"><img src="images/spacer.gif" width="10" height="1"></td>
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="60"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="10" rowspan="2" bgcolor="#F2F2F7" height="60"><img src="images/spacer.gif" width="10" height="8"></td>
                              <td width="175" rowspan="2" bgcolor="#F2F2F7" height="60" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366">Type 
                                the Distributor's true full company name as specified 
                                in all it's correspondence.</font></td>
                              <td width="15" rowspan="2" bgcolor="#F2F2F7" height="60"><img src="images/spacer.gif" width="15" height="8"></td>
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="60"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="125" height="40" valign="top" align="center"> 
                                <input type="text" name="Name" size="15" class="inputtext15">
                              </td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="9" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="350" border="0" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="100%" colspan="9" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="15" rowspan="2" height="80"><img src="images/spacer.gif" width="15" height="8"></td>
                              <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>DIST's 
                                Website URL</b></font></td>
                              <td width="10" rowspan="2" height="80"><img src="images/spacer.gif" width="10" height="8"></td>
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="10" rowspan="2" bgcolor="#F2F2F7" height="80"><img src="images/spacer.gif" width="10" height="8"></td>
                              <td width="175" rowspan="2" bgcolor="#F2F2F7" height="80" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366">Type 
                                in this Distributor's website URL, if applicaple.<br>
                                <br>
                                <center>
                                  <font color="#EB0000"><u>Example</u></font> 
                                </center>
                                </font></td>
                              <td width="15" rowspan="2" bgcolor="#F2F2F7" height="80"><img src="images/spacer.gif" width="15" height="8"></td>
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="125" height="70" valign="top" align="center"> 
                                <input type="text" name="Url" size="15" class="inputtext15">
                              </td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="9" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="350" border="0" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="100%" colspan="9" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" rowspan="4" height="100"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="15" rowspan="4" height="100"><img src="images/spacer.gif" width="15" height="8"></td>
                              <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Mailing 
                                Address Line 1</b></font></td>
                              <td width="10" rowspan="4" height="100"><img src="images/spacer.gif" width="10" height="1"></td>
                              <td bgcolor="#8F8FAB" width="1" rowspan="4" height="100"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="10" rowspan="4" bgcolor="#F2F2F7" height="100"><img src="images/spacer.gif" width="10" height="8"></td>
                              <td width="175" rowspan="4" bgcolor="#F2F2F7" height="100" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366">Type 
                                in the primary Distributor mailing address. If 
                                the Distributor's address consists of a secondary 
                                line please make sure you add it to Address Line 
                                2.</font></td>
                              <td width="15" rowspan="4" bgcolor="#F2F2F7" height="100"><img src="images/spacer.gif" width="15" height="8"></td>
                              <td bgcolor="#8F8FAB" width="1" rowspan="4" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="125" height="30" valign="top" align="center"> 
                                <input type="text" name="MailAdd" size="15" class="inputtext15">
                              </td>
                            </tr>
                            <tr> 
                              <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Mailing 
                                Address Line 2</b></font></td>
                            </tr>
                            <tr> 
                              <td width="125" height="30" valign="top" align="center"> 
                                <input type="text" name="MailAdd2" size="15" class="inputtext15">
                              </td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="9" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="350" border="0" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="100%" colspan="9" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="60"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="15" rowspan="2" height="60"><img src="images/spacer.gif" width="15" height="8"></td>
                              <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Mailing 
                                Address City</b></font></td>
                              <td width="10" rowspan="2" height="60"><img src="images/spacer.gif" width="10" height="1"></td>
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="60"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="10" rowspan="2" bgcolor="#F2F2F7" height="60"><img src="images/spacer.gif" width="10" height="8"></td>
                              <td width="175" rowspan="2" bgcolor="#F2F2F7" height="60" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366">Type 
                                a city for this Distributor's mailing address.</font></td>
                              <td width="15" rowspan="2" bgcolor="#F2F2F7" height="60"><img src="images/spacer.gif" width="15" height="8"></td>
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="125" height="40" valign="top" align="center"> 
                                <input type="text" name="MailCity" size="15" class="inputtext15">
                              </td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="9" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="350" border="0" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="100%" colspan="9" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="60"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="15" rowspan="2" height="60"><img src="images/spacer.gif" width="15" height="8"></td>
                              <td width="150" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Mailing 
                                Address State</b></font></td>
                              <td width="10" rowspan="2" height="60"><img src="images/spacer.gif" width="10" height="1"></td>
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="60"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="10" rowspan="2" bgcolor="#F2F2F7" height="60"><img src="images/spacer.gif" width="10" height="8"></td>
                              <td width="150" rowspan="2" bgcolor="#F2F2F7" height="60" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366">Type 
                                a state for this Distributor's mailing address.</font></td>
                              <td width="15" rowspan="2" bgcolor="#F2F2F7" height="60"><img src="images/spacer.gif" width="15" height="8"></td>
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="150" height="40" valign="top" align="center"> 
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
                            </tr>
                            <tr> 
                              <td width="100%" colspan="9" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <br>
                        </td>
                        <td align="center" valign="top"> <br>
                          <table width="350" border="0" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="100%" colspan="9" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="60"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="15" rowspan="2" height="60"><img src="images/spacer.gif" width="15" height="8"></td>
                              <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Mailing 
                                Address Zip</b></font></td>
                              <td width="10" rowspan="2" height="60"><img src="images/spacer.gif" width="10" height="1"></td>
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="60"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="10" rowspan="2" bgcolor="#F2F2F7" height="60"><img src="images/spacer.gif" width="10" height="8"></td>
                              <td width="175" rowspan="2" bgcolor="#F2F2F7" height="60" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366">Type 
                                a zip code for this Distributor's mailing address.</font></td>
                              <td width="15" rowspan="2" bgcolor="#F2F2F7" height="60"><img src="images/spacer.gif" width="15" height="8"></td>
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="125" height="40" valign="top" align="center"> 
                                <input type="text" name="MailZip" size="7" class="inputtext7">
                              </td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="9" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="350" border="0" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="100%" colspan="9" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="15" rowspan="2" height="80"><img src="images/spacer.gif" width="15" height="8"></td>
                              <td width="150" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Phone 
                                Number</b></font></td>
                              <td width="10" rowspan="2" height="80"><img src="images/spacer.gif" width="10" height="1"></td>
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="10" rowspan="2" bgcolor="#F2F2F7" height="80"><img src="images/spacer.gif" width="10" height="8"></td>
                              <td width="150" rowspan="2" bgcolor="#F2F2F7" height="80" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366">Type 
                                in the this Distributor's phone number along 
                                with its area code.<br>
                                <br>
                                <center>
                                  <font color="#EB0000">Area Code - 3 digits<br>
                                  Phone Number - 7 digits</font> 
                                </center>
                                </font></td>
                              <td width="15" rowspan="2" bgcolor="#F2F2F7" height="80"><img src="images/spacer.gif" width="15" height="8"></td>
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="60"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="150" height="60" valign="middle" align="center"> 
                                <input type="hidden" name="Phone">
                                <nobr> 
                                <input type="text" name="TelArea" size="3" class="inputtext3">
                                <input type="text" name="TelNum" size="7" class="inputtext7">
                                </nobr> <font face="verdana,arial,helvetica" size="1" color="#333366"><br>
                                Area &nbsp;&nbsp;Number</font> </td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="9" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="350" border="0" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="100%" colspan="9" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="15" rowspan="2" height="80"><img src="images/spacer.gif" width="15" height="8"></td>
                              <td width="150" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Fax 
                                Number</b></font></td>
                              <td width="10" rowspan="2" height="80"><img src="images/spacer.gif" width="10" height="1"></td>
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="10" rowspan="2" bgcolor="#F2F2F7" height="80"><img src="images/spacer.gif" width="10" height="8"></td>
                              <td width="150" rowspan="2" bgcolor="#F2F2F7" height="80" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366">Type 
                                in this Distributor's fax number along with its 
                                area code.<br>
                                <br>
                                <center>
                                  <font color="#EB0000">Area Code - 3 digits<br>
                                  Fax Number - 7 digits</font> 
                                </center>
                                </font></td>
                              <td width="15" rowspan="2" bgcolor="#F2F2F7" height="80"><img src="images/spacer.gif" width="15" height="8"></td>
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="60"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="150" height="60" valign="middle" align="center"> 
                                <input type="hidden" name="Fax">
                                <nobr> 
                                <input type="text" name="FaxArea" size="3" class="inputtext3">
                                <input type="text" name="FaxNum" size="7" class="inputtext7">
                                </nobr> <font face="verdana,arial,helvetica" size="1" color="#333366"><br>
                                Area &nbsp;&nbsp;Number</font> </td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="9" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="350" border="0" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="100%" colspan="9" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="60"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="15" rowspan="2" height="60"><img src="images/spacer.gif" width="15" height="8"></td>
                              <td width="125" height="20" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Main 
                                Email Address</b></font></td>
                              <td width="10" rowspan="2" height="60"><img src="images/spacer.gif" width="10" height="1"></td>
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="60"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="10" rowspan="2" bgcolor="#F2F2F7" height="60"><img src="images/spacer.gif" width="10" height="8"></td>
                              <td width="175" rowspan="2" bgcolor="#F2F2F7" height="60" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366">Type 
                                in the Distributor's main email address.</font></td>
                              <td width="15" rowspan="2" bgcolor="#F2F2F7" height="60"><img src="images/spacer.gif" width="15" height="8"></td>
                              <td bgcolor="#8F8FAB" width="1" rowspan="2" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="125" height="40" valign="top" align="center"> 
                                <input type="text" name="MainEmail" size="15" class="inputtext15">
                              </td>
                            </tr>
                            <tr> 
                              <td width="100%" colspan="9" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                </td>
              </tr>
              <tr bordercolor="#333366" bgcolor="#F2F2F7"> 
                  <td align="center" valign="middle" height="45" width="100%"> 
                    <input type="submit" value="Save Distributor's Profile" name="submit" class="inputbut">
                    <input type="reset" value="Reset Form" name="reset" class="inputbut">
                    &nbsp;</td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
      <br>
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
exit;
}

## if no useful calls present frameset
else {
{
print <<EOF

<html>
<head>
<title>Shark Tank Admin System - Add Customer</title>
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
<title>Shark Tank Admin System - Customer Accounts</title>
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
    <td width="20%">$legal</td>
    <td align="center" width="80%"> 
      <table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>Add 
            New Customer</b></font></td>
          <td align="right" width="50%"><a href="view_customers.cgi" target="_top" onMouseOver="javascript:imageOn('search','on');" onMouseOut="javascript:imageOff('search','off');"><img src="images/button_search_off.gif" width="65" height="19" name="search" border="0"></a><a href="add_customer.cgi" target="_top" onMouseOver="javascript:imageOn('addnew','on');" onMouseOut="javascript:imageOff('addnew','off');"><img src="images/button_addnew_off.gif" width="65" height="19" name="addnew" border="0"></a></td>
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