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
	my $Phone = "$FORM{'Phone'}";
	my $Fax = "$FORM{'Fax'}";
	my $MainEmail = "$FORM{'MainEmail'}";	
	my $CSEmail = "$FORM{'CSEmail'}";	
	my $CSPhone = "$FORM{'CSPhone'}";
	my $CSFax = "$FORM{'CSFax'}";
	my $TSEmail = "$FORM{'TSEmail'}";	
	my $TSPhone = "$FORM{'TSPhone'}";
	my $TSFax = "$FORM{'TSFax'}";
	my $ActionUser = "$Cookies{'Username'}";

##----------->>> Start MFG Account Check, make sure no dupes are made
	use DBI;
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $count=0;
	my $sth = $dbh->prepare("SELECT * FROM MFGs");
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
		if (($SavedName eq "$Name") || ($SavedUrl eq "$URL")) {
			if ($SavedName eq "$Name") { $SavedName = "<font color=\"red\">$SavedName</font>"}
			if ($SavedUrl eq "$URL") { $SavedUrl = "<font color=\"red\">$SavedUrl</font>"}

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
                            <td width="35%" height="20"><font class="stextbig"><b>Matching MFG Profile(s)</b></font></td>
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
<td align="center" width="15%"><font class="sresults1"><b>MFG Name</b><br></font></td>
<td align="center" width="25%"><font class="sresults1"><b>MFG URL</b></font></td>
<td align="center" width="15%"><font class="sresults1"><b>MFG Main Email</b></font></td>
<td align="center" width="15%"><font class="sresults1"><b>City</b></font></td>
<td align="center" width="15%"><font class="sresults1"><b>State</b></font></td>
<td align="center" width="15%"><font class="sresults1"><b>Phone</b></font></td>
</tr>
<tr width="100%">
<td><font class="stextbig" width="15%"><b>$SavedName&nbsp;</b></font></td>
<td><font class="stextbig" width="20%">$SavedUrl&nbsp;</font></td>
<td><font class="stextbig" width="25%">$SavedMainEmail&nbsp;</font></td>
<td><font class="stextbig" width="25%">$SavedCity&nbsp;</font></td>
<td><font class="stextbig" width="15%">$SavedState&nbsp;</font></td>
<td><font class="stextbig" width="15%">($AreaCode)<br>$PhoneNum3-$PhoneNum4&nbsp;</font></td>
</tr>
</table>
<br><center><form><input type="button" value="Try Again" onClick="javascript:history.go(-1)" class="inputbut"></form></center>

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
			
## END PAGE TEMPLATE
&bottom;
			$sth->finish;
			$dbh->disconnect;
			exit;
		}
	}
	$sth->finish;

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
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("INSERT INTO MFGs (ManufacturerID, Name, URL, 
							 MailAdd, MailAdd2, MailCity, MailState, MailZip,  
							 MainEmail, MainPhone, MainFax, CSEmail, CSPhone, 
							 CSFax, TSEmail, TSPhone, TSFax, Emblem, LogoSmall, 
							 LogoMedium, LogoLarge, AddedBy, AddedOn, ModifiedBy, 
							 ModifiedOn)

							 VALUES (Null, '$Name', '$URL', '$MailAdd', '$MailAdd2', 
							 '$MailCity', '$MailState', '$MailZip', '$MainEmail', 
							 '$Phone', '$Fax', '$CSEmail', '$CSPhone', 
							 '$CSFax', '$TSEmail', '$TSPhone', '$TSFax', '', '', 
							 '', '', '$ActionUser', Null, '', '')");

	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish; 
	print "<b>Create Manufactuer Profile</b><br>The manufactuer porfile for <b>$Name</b> has been created successfully. This profile will be used in conjuction with this company's product line.<center><br><br><form><input type=\"button\" value=\"Take Me Home\" onClick=\"javascript:parent.location.href='index.html'\" class=\"inputbut\"><br></center></font>";
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
<title>Coastline Micro, Inc. - Shark Tank Admin System - Manufacturer Profiles</title>
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
    missingdrop += "\\n     - Manufacturer's Name";
	thefirst = "Name";
}

if ((document.add.Url.value == "") || (document.add.Url.value == " ") || (document.add.Url.value.indexOf('.') == -1)) {
    missingdrop += "\\n     - MFG's Website URL";
	if (thefirst == "") { thefirst = "Url"; }
}

if (document.add.MailAdd.value == "" || document.add.MailAdd.value == " ") {
    missingdrop += "\\n     - Manufacturer's Mailing Address";
	if (thefirst == "") { thefirst = "MailAdd"; }
}

if (document.add.MailCity.value == "" || document.add.MailCity.value == " ") {
    missingdrop += "\\n     - Manufacturer's City";
	if (thefirst == "") { thefirst = "MailCity"; }
}

if (isNaN(document.add.MailZip.value) || (document.add.MailZip.value == "") || (document.add.MailZip.value == " ") || (document.add.MailZip.value.length != 5)) {
    missingdrop += "\\n     - Manufacturer's Zip Code must be a 5 digit number";
	if (thefirst == "") { thefirst = "MailZip"; }
}
// Check Phone number and format if it is there get the area code and num and feed the Phone field
if (isNaN(document.add.TelArea.value) || (document.add.TelArea.value == "") || (document.add.TelArea.value == " ") || (document.add.TelArea.value.length != 3)) {
    missingdrop += "\\n     - Manufacturer's Phone's Area Code must be a 3 digit number";
	if (thefirst == "") { thefirst = "TelArea"; }
}
else if (isNaN(document.add.TelNum.value) || (document.add.TelNum.value == "") || (document.add.TelNum.value == " ") || (document.add.TelNum.value.indexOf('-') != -1) || (document.add.TelNum.value.length != 7)) {
    missingdrop += "\\n     - Manufacturer's Phone Number must be a 7 digit number\\n        *No hyphen (-) necessary";
	if (thefirst == "") { thefirst = "TelNum"; }
}
else {
	PhoneValues = document.add.TelArea.value + document.add.TelNum.value;
	document.add.Phone.value = PhoneValues;
}

// Check Fax number and format if it is there get the area code and num and feed the Fax field
if (isNaN(document.add.FaxArea.value) || (document.add.FaxArea.value == "") || (document.add.FaxArea.value == " ") || (document.add.FaxArea.value.length != 3)) {
    missingdrop += "\\n     - Manufacturer's Fax's Area Code must be a 3 digit number";
	if (thefirst == "") { thefirst = "FaxArea"; }
}
else if (isNaN(document.add.FaxNum.value) || (document.add.FaxNum.value == "") || (document.add.FaxNum.value == " ") || (document.add.FaxNum.value.indexOf('-') != -1) || (document.add.FaxNum.value.length != 7)) {
    missingdrop += "\\n     - Manufacturer's Fax Number must be a 7 digit number\\n        *No hyphen (-) necessary";
	if (thefirst == "") { thefirst = "FaxNum"; }
}
else {
	FaxValues = document.add.FaxArea.value + document.add.FaxNum.value;
	document.add.Fax.value = FaxValues;
}

// CHECK MAIN EMAIL
  if (document.add.MainEmail.value == "")	{
    missingdrop += "\\n     - Manufacturer's Main Email";
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
  
// CHECK CS EMAIL
  if (document.add.CSEmail.value == "")	{
    missingdrop += "\\n     - Customer Service Email";
	if (thefirst == "") { thefirst = "CSEmail"; }
  } else if ((document.add.CSEmail.value.indexOf('\@') == -1) || 
        (document.add.CSEmail.value.indexOf('.') == -1)) {
    missingdrop += "\\n     - Customer Service Email Format should be: username\@mycompany.com";
	if (thefirst == "") { thefirst = "CSEmail"; }
  }
  if ((document.add.CSEmail.value.indexOf(',') != -1)) {
    missingdrop += "\\n     - Commas are not allowed in email addresses";
	if (thefirst == "") { thefirst = "CSEmail"; }
  }
  if ((document.add.CSEmail.value.indexOf(';') != -1)) {
    missingdrop += "\\n     - Semicolons are not allowed in email addresses";
	if (thefirst == "") { thefirst = "CSEmail"; }
  }
  if ((document.add.CSEmail.value.indexOf(':') != -1)) {
    missingdrop += "\\n     - Colons are not allowed in email addresses";
	if (thefirst == "") { thefirst = "CSEmail"; }
  }
  if ((document.add.CSEmail.value.indexOf('&') != -1)) {
    missingdrop += "\\n     - Ampersands are not allowed in email addresses";
	if (thefirst == "") { thefirst = "CSEmail"; }
  }
  if ((document.add.CSEmail.value.indexOf(' ') != -1)) {
    missingdrop += "\\n     - Spaces are not allowed in email addresses";
	if (thefirst == "") { thefirst = "CSEmail"; }
  }
  
// CHECK TS EMAIL
  if (document.add.TSEmail.value == "")	{
    missingdrop += "\\n     - Technical Support Email";
	if (thefirst == "") { thefirst = "TSEmail"; }
  } else if ((document.add.TSEmail.value.indexOf('\@') == -1) || 
        (document.add.TSEmail.value.indexOf('.') == -1)) {
    missingdrop += "\\n     - Technical Support Email Format should be: username\@mycompany.com";
	if (thefirst == "") { thefirst = "TSEmail"; }
  }
  if ((document.add.TSEmail.value.indexOf(',') != -1)) {
    missingdrop += "\\n     - Commas are not allowed in email addresses";
	if (thefirst == "") { thefirst = "TSEmail"; }
  }
  if ((document.add.TSEmail.value.indexOf(';') != -1)) {
    missingdrop += "\\n     - Semicolons are not allowed in email addresses";
	if (thefirst == "") { thefirst = "TSEmail"; }
  }
  if ((document.add.TSEmail.value.indexOf(':') != -1)) {
    missingdrop += "\\n     - Colons are not allowed in email addresses";
	if (thefirst == "") { thefirst = "TSEmail"; }
  }
  if ((document.add.TSEmail.value.indexOf('&') != -1)) {
    missingdrop += "\\n     - Ampersands are not allowed in email addresses";
	if (thefirst == "") { thefirst = "TSEmail"; }
  }
  if ((document.add.TSEmail.value.indexOf(' ') != -1)) {
    missingdrop += "\\n     - Spaces are not allowed in email addresses";
	if (thefirst == "") { thefirst = "TSEmail"; }
  }

// Check Customer Service Phone number and format if it is there get the area code and num and feed the Phone field
if (isNaN(document.add.CSTelArea.value) || (document.add.CSTelArea.value == "") || (document.add.CSTelArea.value == " ") || (document.add.CSTelArea.value.length != 3)) {
    missingdrop += "\\n     - Customer Service's Phone Area Code must be a 3 digit number";
	if (thefirst == "") { thefirst = "CSTelArea"; }
}
else if (isNaN(document.add.CSTelNum.value) || (document.add.CSTelNum.value == "") || (document.add.CSTelNum.value == " ") || (document.add.CSTelNum.value.indexOf('-') != -1) || (document.add.CSTelNum.value.length != 7)) {
    missingdrop += "\\n     - Customer Service Phone Number must be a 7 digit number\\n        *No hyphen (-) necessary";
	if (thefirst == "") { thefirst = "CSTelNum"; }
}
else {
	PhoneValues = document.add.CSTelArea.value + document.add.CSTelNum.value;
	document.add.CSPhone.value = PhoneValues;
}

// Check Customer Service Fax number and format if it is there get the area code and num and feed the Fax field
if (isNaN(document.add.CSFaxArea.value) || (document.add.CSFaxArea.value == "") || (document.add.CSFaxArea.value == " ") || (document.add.CSFaxArea.value.length != 3)) {
    missingdrop += "\\n     - Customer Service's Fax Area Code must be a 3 digit number";
	if (thefirst == "") { thefirst = "CSFaxArea"; }
}
else if (isNaN(document.add.CSFaxNum.value) || (document.add.CSFaxNum.value == "") || (document.add.CSFaxNum.value == " ") || (document.add.CSFaxNum.value.indexOf('-') != -1) || (document.add.CSFaxNum.value.length != 7)) {
    missingdrop += "\\n     - Customer Service Fax Number must be a 7 digit number\\n        *No hyphen (-) necessary";
	if (thefirst == "") { thefirst = "CSFaxNum"; }
}
else {
	FaxValues = document.add.CSFaxArea.value + document.add.CSFaxNum.value;
	document.add.CSFax.value = FaxValues;
} 

// Check Technical Support Phone number and format if it is there get the area code and num and feed the Phone field
if (isNaN(document.add.TSTelArea.value) || (document.add.TSTelArea.value == "") || (document.add.TSTelArea.value == " ") || (document.add.TSTelArea.value.length != 3)) {
    missingdrop += "\\n     - Technical Support's Phone Area Code must be a 3 digit number";
	if (thefirst == "") { thefirst = "TSTelArea"; }
}
else if (isNaN(document.add.TSTelNum.value) || (document.add.TSTelNum.value == "") || (document.add.TSTelNum.value == " ") || (document.add.TSTelNum.value.indexOf('-') != -1) || (document.add.TSTelNum.value.length != 7)) {
    missingdrop += "\\n     - Technical Support Phone Number must be a 7 digit number\\n        *No hyphen (-) necessary";
	if (thefirst == "") { thefirst = "TSTelNum"; }
}
else {
	PhoneValues = document.add.TSTelArea.value + document.add.TSTelNum.value;
	document.add.TSPhone.value = PhoneValues;
}

// Check Technical Support Fax number and format if it is there get the area code and num and feed the Fax field
if (isNaN(document.add.TSFaxArea.value) || (document.add.TSFaxArea.value == "") || (document.add.TSFaxArea.value == " ") || (document.add.TSFaxArea.value.length != 3)) {
    missingdrop += "\\n     - Technical Support's Fax Area Code must be a 3 digit number";
	if (thefirst == "") { thefirst = "TSFaxArea"; }
}
else if (isNaN(document.add.TSFaxNum.value) || (document.add.TSFaxNum.value == "") || (document.add.TSFaxNum.value == " ") || (document.add.TSFaxNum.value.indexOf('-') != -1) || (document.add.TSFaxNum.value.length != 7)) {
    missingdrop += "\\n     - Technical Support Fax Number must be a 7 digit number\\n        *No hyphen (-) necessary";
	if (thefirst == "") { thefirst = "TSFaxNum"; }
}
else {
	FaxValues = document.add.TSFaxArea.value + document.add.TSFaxNum.value;
	document.add.TSFax.value = FaxValues;
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

<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
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
              Manufacturer Profile</b></font></td>
          <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
              <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER" bordercolor="#333366">
                <tr bordercolor="#333366" valign="middle"> 
                  <td width="50%" align="center" height="50" class="tableBG"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Function 
                    Instructions</b></font></td>
              </tr>
              <tr bordercolor="#333366"> 
                  <td width="50%" align="center" valign="top" bordercolor="#333366"> 
                    <table width="100%" border="0" cellspacing="0" cellpadding="5">
                      <tr> 
                        <td width="100%" align="center" height="25" bgcolor="#F2F2F7" class="tableBG" colspan="2"><font face="verdana,arial,helvetica" size="2" color="#333366"><b>Manufacturer's 
                          Information</b></font></td>
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Manufacturer's 
                                      Company Name</font></b></font></td>
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
                                      <input type="text" name="Name" size="15" class="inputtext15">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Website 
                                      URL </font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="75" bgcolor="#F2F2F7" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366">Type 
                                      in this manufacturer's website URL, if applicaple.<br>
                                      <br>
                                      <center>
                                        <font color="#EB0000"><u>Example</u><br>
                                        www.coastlinemicro.com</font> 
                                      </center>
                                      </font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"> 
                                      <input type="text" name="Url" size="15" class="inputtext15">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Zip 
                                      Code </font></b></font></td>
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Fax 
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Main 
                                      Email Address </font></b></font></td>
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
                                      <input type="text" name="MainEmail" size="15" class="inputtext15">
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
                        <td width="100%" align="center" height="25" bgcolor="#F2F2F7" class="tableBG" colspan="2"><font face="verdana,arial,helvetica" size="2" color="#333366"><b>Customer Support Information</b></font></td>
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Customer Service Email Address</font></b></font></td>
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
                                      <input type="text" name="CSEmail" size="15" class="inputtext15">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Customer Service Phone Number</font></b></font></td>
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
                                      <input type="hidden" name="CSPhone">
                                      <nobr> 
                                      <input type="text" name="CSTelArea" size="3" class="inputtext3">
                                      <input type="text" name="CSTelNum" size="7" class="inputtext7">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Customer Service Fax Number</font></b></font></td>
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
                                      <input type="hidden" name="CSFax" value="">
                                      <nobr> 
                                      <input type="text" name="CSFaxArea" size="3" class="inputtext3">
                                      <input type="text" name="CSFaxNum" size="7" class="inputtext7">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Technical 
                                      Support Email Address</font></b></font></td>
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
                                      <input type="text" name="TSEmail" size="15" class="inputtext15">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Technical 
                                      Support Phone Number</font></b></font></td>
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
                                      <input type="hidden" name="TSPhone">
                                      <nobr> 
                                      <input type="text" name="TSTelArea" size="3" class="inputtext3">
                                      <input type="text" name="TSTelNum" size="7" class="inputtext7">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Technical 
                                      Support Fax Number</font></b></font></td>
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
                                      <input type="hidden" name="TSFax">
                                      <nobr> 
                                      <input type="text" name="TSFaxArea" size="3" class="inputtext3">
                                      <input type="text" name="TSFaxNum" size="7" class="inputtext7">
                                      </nobr> <font face="verdana,arial,helvetica" size="1" color="#333366"><br>
                                      Area &nbsp;&nbsp;Number</font></nobr></td>
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
                  <td align="center" valign="middle" height="45" width="100%" bgcolor="#F2F2F7" bordercolor="#333366"> 
                    <input type="submit" value="Save Manufacturer's Profile" name="submit" class="inputbut">
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
<title>Coastline Micro, Inc. - Shark Tank Admin System - Create Manufactuer Profile</title>
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
<title>Coastline Micro, Inc. - Shark Tank Admin System - Manufacturer Profiles</title>
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

<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
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
          <td width="50%"><font face="verdana,arial,helvetica" size="2" color="#333366"><b>Create Manufacturer Profile</b></font></td>
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