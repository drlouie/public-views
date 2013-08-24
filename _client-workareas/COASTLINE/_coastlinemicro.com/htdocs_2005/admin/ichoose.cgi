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
if ($FORM{'Preview'} && $FORM{'ImageID'}) {

$ImageID = "$FORM{'ImageID'}";

# START HTML
&topper;

use DBI; 
my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
$dbh->{RaiseError} = 1; 

if ($ImageID =~ ",") { 
	$Mulitple = 1;  
	@Images = split(/,/, $ImageID);
	foreach $Image (@Images) {
		my $sth = $dbh->prepare("SELECT * FROM Images WHERE ImageID=$Image");
		$sth->execute or die "Unable to execute query\n"; 
		my @row;
		while(@row = $sth->fetchrow_array) { 
			push(@Imagenes,"$row[0],$row[1],$row[3],$row[5],$row[6],$row[8],$row[9]");
		}
		$sth->finish; 
	}
}

else {
	my $sth = $dbh->prepare("SELECT * FROM Images WHERE ImageID=$ImageID");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$ImageID = $row[0];
		$Type = $row[1];
		$FileName = $row[3];
		$Height = $row[5];
		$InnerURL = $row[6];
		$Description = $row[8];
		$Keywords = $row[9];
	}
	$sth->finish; 
}
$dbh->disconnect; 

$TDHeight = $Height + 50;

{
print <<EOF

</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<table border="0" cellpadding="0" cellspacing="0" align="center">
  <tr valign="top"> 
    <td align="center"> 
      <table border="0" cellspacing="0" cellpadding="0" width="300" align="center">
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
              <tr bordercolor="#333366"> 
                <td width="100%" align="center" valign="top"> 

                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr> 
                      <td width="100%" align="center"> 

                          <table width="100%" border="0" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                              <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Preview Image</font></b></font></td>
                              <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                            </tr>
                            <tr> 
                              <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                            </tr>
                            <tr> 
                              <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
<td bgcolor="#F2F2F7" align="left" valign="top">
EOF
}

if (@Imagenes) {
	foreach $ThyImagen (@Imagenes) {
		@ImageStack = split(/,/, $ThyImagen);
		print "<font face=\"verdana,arial,helvetica\" size=\"1\"><br>";
		print "<b>File Name</b><br>$ImageStack[2]<br><br><b>Description</b><br>$ImageStack[5]<br><br><b>Keywords</b><br>$ImageStack[6]<br><br>";
		print "<a href=\"/$ImageStack[4]\" target=\"InnerURL\"><center><img src=\"/$ImageStack[4]\" border=\"0\" alt=\"$ImageStack[5]\"></center></a>";
		print "<br><br></font>";
	}
}
else {
		print "<font face=\"verdana,arial,helvetica\" size=\"1\"><br>";
		print "<b>File Name</b><br>$FileName<br><br><b>Description</b><br>$Description<br><br><b>Keywords</b><br>$Keywords<br><br>";
		print "<a href=\"/$InnerURL\" target=\"InnerURL\"><center><img src=\"/$InnerURL\" border=\"0\" alt=\"$Description\"></center></a>";
		print "</font>";
}


{
print <<EOF

<br>
 </td>
<td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                            </tr>
                          </table>

                        </td>
                    </tr>
              <tr bgcolor="#FFFFFF"> 
                  <td align="center" valign="middle" height="25" width="100%" bgcolor="#FFFFFF"> 
<font face="verdana,arial,helvetica" size="1">
<a href="javascript:history.go(-1);" color="#333366">< < < Back</a></font>
</td>
              </tr>
                  </table>

EOF
}
&bottom;
}

## -------------------------->>> NO INPUT
elsif ($FORM{'FeedMe'} && $FORM{'Type'} && $FORM{'SubType'}) {

$FeedMe = "$FORM{'FeedMe'}";
$Type = "$FORM{'Type'}";
$SubType = "$FORM{'SubType'}";

if ($SubType eq "small") { $AppendButton = ""; }
elsif (($SubType eq "large" && $Type eq "mfg") || ($SubType eq "large" && $Type eq "dist")) { $AppendButton = "";  }
elsif (($SubType eq "medium" && $Type eq "mfg") || ($SubType eq "medium" && $Type eq "dist")) { $AppendButton = "";  }
elsif ($SubType eq "sneak") { $AppendButton = "";  }
else { $AppendButton = "<input type=\"button\" value=\"Append\" class=\"inputbut\" name=\"submit\" onClick=\"Javascript:appendIt();\">"; }

&topper;
{
print <<EOF

<script language="Javascript">
// CROSS-BROWSER FORM CHECKER
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function checkForm() {
var missingdrop = "";
var thefirst = "";

// Check Common form fields
if (document.Available.ImageID.value == "Null") {
    missingdrop += "\\n     - Sorry, there are no available images in the system. To add one click the 'Upload New Image' button below.";
	thefirst = "ImageID";
}

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    missingdrop ="___________________________________________                   \\n\\n" + "  Sorry, I cannot process your request because the\\n  following fields are either blank or filled incorrectly:\\n" + "___________________________________________                   \\n\\n" +
    missingdrop + "\\n\\n___________________________________________                   " + "\\n\\n   To continue, check fields and submit form again!" + "\\n___________________________________________";
    alert(missingdrop);
	document.Available[thefirst].focus();
    return false;
} 
else {
return true;
}
}

function makeMain() {
var formindex = document.forms.Available.ImageID.selectedIndex;
var thisone = document.forms.Available.ImageID.options[formindex].value;
if (thisone != "Null") {
		parent.document.change.$FeedMe.value = thisone;
		parent.document.change.$FeedMe.style.color = "EB0000";
}
else {
	alert('Sorry, there are no available images in the system. To add one click the \\'Upload New Image\\' button below.');
}
}

function appendIt () {
var formindex = document.forms.Available.ImageID.selectedIndex;
var thisone = document.forms.Available.ImageID.options[formindex].value;
		parent.document.change.$FeedMe.style.color = "EB0000"; 
		HungryOne = parent.document.change.$FeedMe.value;
		if ((HungryOne == "") || (HungryOne <= 0)) { NewHungry = thisone; }
		else {
			// do not do it if its there already
			if (HungryOne.indexOf(thisone) == -1) { NewHungry = HungryOne + "," + thisone; }
			else { NewHungry = HungryOne; }
		}
		parent.document.change.$FeedMe.value = NewHungry;
}

function iClear() {
		parent.document.change.$FeedMe.value = "";
}

function iPreview() {
var formindex = document.forms.Available.ImageID.selectedIndex;
var thisone = document.forms.Available.ImageID.options[formindex].value;
if (thisone != "Null") { location.href = "ichoose.cgi?Preview=1&ImageID="+thisone+""; }
}
</script>
</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<table border="0" cellpadding="0" cellspacing="0" align="left">
  <tr valign="top"> 
    <td align="left"> 
      <table border="0" cellspacing="0" cellpadding="0" width="300" align="left">
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
              <tr bordercolor="#333366"> 
                <td width="100%" align="center" valign="top"> 

                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr> 
                      <td width="100%" align="center"> 

                          
                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                          <tr> 
                            <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                            <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Choose Image(s)</font></b></font></td>
                            <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                          </tr>
                          <tr> 
                            <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                          </tr>
                          <tr> 
                            <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                            <td height="75" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1"><b>Description</b><br>
                              To get an image to use for the item you are configuring 
                              in the system you can either choose an image currently 
                              in the system or you can upload a new image to the 
                              system to use.</font></td>
                            <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                          </tr>
                          <tr> 
                            <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
<form action="$script" method="post" name="Available" onSubmit="return checkForm();">
                              <td height="165" align="left" valign="middle"> <font face="verdana,arial,helvetica" size="1"><b>To 
                                Use Existing Image</b><br>
                                Select an image to use from the 'Available Images' 
                                list. Then just click 'Use Selected' to continue. 
                                You can click 'Preview' to preview the image before 
                                you use it.<br><br></font>
                                <center>
                                  <font face="verdana,arial,helvetica" size="1" color="#333366"><b>Available 
                                  Images</b><br>
                                <br>
                                </font> 
                                <select name="ImageID" class="inputtext">
EOF
}

	## SAVE INFO TO NEW DB TABLE DATA ROW
	use DBI; 
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	$count=0;
	my $sth = $dbh->prepare("SELECT * FROM Images WHERE Type='$Type' AND SubType='$SubType' ORDER BY FileName");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$count++;
		$ImageID = $row[0];
		$FileName = $row[3];
		print "<option value=\"$ImageID\">$FileName</option>";
	}
	if ($count==0) {
		print "<option value=\"Null\">None Available</option>";
	}
	$sth->finish; 
	$dbh->disconnect; 

{
print <<EOF
                              </select>
                                <font face="verdana,arial,helvetica" size="1" color="#333366"><br>
                                <br></font><nobr>
	                            <input type="button" value="Main" class="inputbut" name="submit" onClick="Javascript:makeMain();">
                                $AppendButton
                                <input type="button" value="View" class="inputbut" name="button" onClick="Javascript:iPreview();">
                                <input type="button" value="Clear" class="inputbut" name="button" onClick="Javascript:iClear();"></nobr></center>
                            </td>
                              </form>
                            <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                          </tr>
                          <tr> 
                            <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                            <td height="15" bgcolor="#F2F2F7" align="left" valign="middle">&nbsp;</td>
                            <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                          </tr>
                          <tr> 
                            <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                              <form action="iupload.cgi" method="post" name="Upload">
                              <td height="100" align="left" valign="middle"> <font face="verdana,arial,helvetica" size="1"><b>To 
                                Upload New Image</b><br>
                                Adding a new image to the system requires a number 
                                of steps. To begin the process click 'Upload Image'<br>
                                <br>
                                </font> 
                                <center>
                                  <input type="hidden" name="Type" class="inputtext" value="$Type">
                                  <input type="hidden" name="SubType" class="inputtext" value="$SubType">
                                  <input type="hidden" name="FeedMe" class="inputtext" value="$FeedMe">
                                  <input type="hidden" name="Script" class="inputtext" value="$script">
                                  <input type="submit" value="Upload New Image" class="inputbut">
                                </center>
                              </td>
                              </form>
                            <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                          </tr>
                        </table>

                        </td>
                    </tr>
              <tr bordercolor="#333366" bgcolor="#F2F2F7"> 
                      <td align="center" valign="middle" height="15" width="100%" bgcolor="#F2F2F7" bordercolor="#333366">&nbsp; 
                      </td>
              </tr>
                  </table>

EOF
}
&bottom;
exit;
}

## if no useful calls present frameset
else {
$sorry = `cat sorry_nospec.nsf`;

{
print <<EOF

$sorry

EOF
}
exit;
}

sub topper {
{
print <<EOF
<html>
<head>
<title>Shark Tank Admin System - File Uploader</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
		  
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
