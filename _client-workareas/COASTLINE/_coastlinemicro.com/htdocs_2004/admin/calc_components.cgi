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

if ($FORM{'FeedMe'} && $FORM{'LosNumbers'}) {

$FeedMe = "$FORM{'FeedMe'}";
$LosNumbers = "$FORM{'LosNumbers'}";
$Character = "$FORM{'Character'}";

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
}

EOF
}

    @LosNumbers = split(/,/, $LosNumbers);
	## SAVE INFO TO NEW DB TABLE DATA ROW
	use DBI; 
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	if ($Character eq "All") {
		foreach $ElNumber (@LosNumbers) {
			@ElDataface = split(/-----/, $ElNumber);
			my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$ElDataface[0]'");
			$sth->execute or die "Unable to execute query\n"; 
			my @row;
			while(@row = $sth->fetchrow_array) { 
				$MyCost = $row[21];
				$TheCost = $TheCost + $MyCost;
				$TheCost = sprintf("%.2f", $TheCost);
				print "ThisOne.value = 'Section Total = \$$TheCost';";
			}
			$sth->finish; 
		}
	}

	else {
		$LaCuenta=0;
		$PriNombre="";
		foreach $ElNumber (@LosNumbers) {
			@ElDataface = split(/-----/, $ElNumber);
				my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$ElDataface[0]'");
				$sth->execute or die "Unable to execute query\n"; 
				my @row;
				while(@row = $sth->fetchrow_array) { 
					$MyCost = $row[21];
					$TheCost = $TheCost + $MyCost;
					$TheCost = sprintf("%.2f", $TheCost);
					if ($LaCuenta eq "0") {
						print "ThisOne.value = 'Section Total = \$$TheCost';";
					}
					elsif ($PriNombre eq $ElDataface[1]) {
						print "ThisOne.value = 'Section Total = \$$TheCost';";
					}
					if ($LaCuenta eq "0") { $PriNombre = $ElDataface[1]; }
					$LaCuenta++;
				}
				$sth->finish; 
		}
	}

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
                            <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Product Pricer</font></b></font></td>
                            <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                          </tr>
                          <tr> 
                            <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                          </tr>
                          <tr> 
                            <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                            <td height="75" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1"><b>Description</b><br>
                              The section price totals for which you requested a re-calculation is now set with the price for it's selected components.</font></td>
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
