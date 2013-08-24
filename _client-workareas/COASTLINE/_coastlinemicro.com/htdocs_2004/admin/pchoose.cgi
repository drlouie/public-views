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
if ($FORM{'Preview'} && $FORM{'CMPartNum'}) {

$CMPartNum = "$FORM{'CMPartNum'}";

# START HTML
&topper;

use DBI; 
my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
$dbh->{RaiseError} = 1; 
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
                              <td bgcolor="#F2F2F7" align="left" valign="top"><font face="verdana,arial,helvetica" size="1"><br>
                                <b>File Name</b><br>
								$FileName<br><br>
                                <b>Description</b><br>
								$Description<br><br>
                                <b>Keywords</b><br>
								$Keywords<br><br>
                                </font> </td>
                              <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                            </tr>
                          </table>

                        </td>
                    </tr>
              <tr bgcolor="#FFFFFF"> 
                  <td align="center" valign="middle" height="$TDHeight" width="100%" bgcolor="#FFFFFF"> 
                    <a href="/$InnerURL" target="InnerURL"><img src="/$InnerURL" border="0" alt="$Description"></a>
					<font face="verdana,arial,helvetica" size="1">
					<br><br>
					<a href="javascript:history.go(-1);" color="#333366">< < < Back</a></font>
                    </td>
              </tr>
              <tr bordercolor="#333366" bgcolor="#F2F2F7"> 
                  <td align="center" valign="middle" height="15" width="100%" bgcolor="#F2F2F7" bordercolor="#333366"> 
&nbsp;
                    </td>
              </tr>
                  </table>

EOF
}
&bottom;
}

## -------------------------->>> NO INPUT
elsif ($FORM{'FeedMe'} && $FORM{'ProdType'}) {

$FeedMe = "$FORM{'FeedMe'}";
$ProdType = "$FORM{'ProdType'}";

&topper;
{
print <<EOF

<script language="Javascript">
// CROSS-BROWSER FORM FEEDER
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function feedIt() {
var b = navigator.appName;
if (b=="Netscape") {
	mainFrame = parent.frames.botOne;
	ThisOne = mainFrame.document.forms[0].$FeedMe;
}

else {
	ThisOne = parent.document.forms[0].$FeedMe;
	parent.document.forms[0].$FeedMe.style.color = "EB0000";
}

var sizer = ThisOne.length;

// CLEARS ALL DATA ON MAIN SELECT
for(var i = (sizer-1); i >= 0; i--) {
while (ThisOne.options[i] != null) {
ThisOne.options[i] = null;
	}
}

// get length after kills
var sizer = ThisOne.length;

EOF
}

	## SAVE INFO TO NEW DB TABLE DATA ROW
	use DBI; 
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	$count=0;
	my $sth = $dbh->prepare("SELECT * FROM Products WHERE PricingClass='$ProdType'");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$count++;
		$CMPartNum = $row[1];
		$ItemName = $row[11];
		if ($ItemName =~ "&reg;") { $ItemName =~ s/&reg;//g; }
		if ($ItemName =~ "&#153;") { $ItemName =~ s/&#153;//g; }
		if ($ItemName =~ "&copy;") { $ItemName =~ s/&copy;//g; }
		if ($FeedMe eq "AllProducts") {
			print "ThisOne.options[sizer] = new Option('$ItemName');";
			print "ThisOne.options[sizer].value = '$CMPartNum';";
			print "sizer++;";
		}
		else {
	    	$ItemName = substr($ItemName, 0, 40); # ONLY 25 Characters			
			print "ThisOne.options[sizer] = new Option('$ItemName');";
			print "ThisOne.options[sizer].value = '$CMPartNum';";
			print "sizer++;";
		}
	}
	$sth->finish; 
	$dbh->disconnect; 

{
print <<EOF

// RE-GENERATE TYPES
}
</script>
</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:feedIt();">
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
                            <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Product List Generator</font></b></font></td>
                            <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                          </tr>
                          <tr> 
                            <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                          </tr>
                          <tr> 
                            <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                            <td height="75" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1"><b>Description</b><br>
                              The product listing for the Product Type you chose will now appear in the <b>Inventory Reader</b> field.</font></td>
                            <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
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

## SORRY YALL NO GOOD CALL
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
<title>Coastline Micro, Inc. - Shark Tank Admin System - File Uploader</title>
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
