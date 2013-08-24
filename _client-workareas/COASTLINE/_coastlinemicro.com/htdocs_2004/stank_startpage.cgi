#!/usr/bin/perl5 -s

###########################################################################################################
# Company: ©2001 NetMedia Solutions                                                                             #
# Date: Saturday, September 21, 2001                                                                      #
# Location: Los Angeles County, California, United States of America                                      #
# Made By: Luis Rodriguez (drlouie)                                                                       #
# Email: Drlouie@NetMediaSol.com                                                                          #
#                                                                                                         #
# This program cannot be duplicated, distributed or re-used for any other purpose other than its original #
# intended purpose and function. You may request NetMedia Solutions for a copy of the script,             #
# personalized to fit your exact needs for a small re-programming fee.                                    #
###########################################################################################################

require ("parse_query.nsp");
require ("date.nsp");

## ----------------->>> GIVE THE DOCUMENT SOME STYLE DEPENDING ON BROWSER AND DOCUMENT LOCATION
$browser = "$ENV{'HTTP_USER_AGENT'}";
if (($browser =~ "Mozilla/" && $browser =~ "6.") || ($browser =~ "Mozilla/" && $browser =~ "4.") || $browser =~ "Netscape6") { $tablewidth = "100%"; $t1 = "1%"; $t2 = "64%"; $t3 = "18%"; $t4 = "18%"; }	
else { $tablewidth = "470"; $t1 = "5"; $t2 = "339"; $t3 = "79"; $t4 = "42"; }

if ($browser =~ "MSIE 5.0" || $browser =~ "MSIE 5.5" || $browser =~ "Mozilla/4.7" || $browser =~ "MSIE 4.0") { $StartURLer="javascript:void(0);\" onClick=\"javascript:window.open"; $EndURLer=",'EMAILIT','width=485,height=590');";}
else { $StartURLer="javascript:trigger"; $EndURLer=");";}

## ----------------->>> Must Have SERIES!
if ($FORM{'Series'}) {
$Series = "$FORM{'Series'}";

## WHICH MAIN TITLE?
if ($Series eq "mako") { $CopyID = "0000000001"; }
if ($Series eq "gw") { $CopyID = "0000000002"; }
if ($Series eq "thresher") { $CopyID = "0000000003"; }
if ($Series eq "tiger") { $CopyID = "0000000004"; }
if ($Series eq "reef") { $CopyID = "0000000005"; }
if ($Series eq "thresher2") { $CopyID = "0000000006"; }
if ($Series eq "nmusd") { $CopyID = "0000000007"; }
if ($Series eq "nmusdCustCom") { $CopyID = "0000000008"; }

## ----------------->>> GET Copy and Title and EmailSubject for this page from DB
use DBI; 
my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
$dbh->{RaiseError} = 1; 
$count=0;
my $sth = $dbh->prepare("SELECT * FROM Copy WHERE CopyID='$CopyID'");
$sth->execute or die "Unable to execute query\n";
my @row;
while(@row = $sth->fetchrow_array) { 
	$MainTitle = $row[1];
	$BodyCopy = $row[2];
	$EmailSubject = $row[5];
	$SavedAddedBy = $row[6];
	$SavedAddedOn = $row[7];
	$SavedModifiedBy = $row[8];
	$SavedModifiedBy = $row[9];
	## Re-Structure data as necessary
	$AddYear = substr($SavedAddedOn, 0, 2);
	$AddMonth = substr($SavedAddedOn, 2, 2);
	$AddDay = substr($SavedAddedOn, 4, 2);
	$ModYear = substr($SavedModifiedOn, 0, 2);
	$ModMonth = substr($SavedModifiedOn, 2, 2);
	$ModDay = substr($SavedModifiedOn, 4, 2);
	$count++;
}
$sth->execute or die "Unable to execute query\n"; 
$sth->finish;
$dbh->disconnect; 	

## IF PRINTING SCREEN
if ($FORM{'NSPRINT'}) { 
	$PrintPage = "<script>javascript:window.print()</script>"; 
	$TBack = "";
	$TLeft = "&nbsp;";
	$TRight = "&nbsp;";
	$PrintIt = "&nbsp;";
	$EmailIt = "&nbsp;";
	$PageURL = "<font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#EB0000\">Page URL - http://www.coastlinemicro.com/$Series/</font>";
}
if ($FORM{'MSP'} eq "1" || $FORM{'NMUSD'} eq "1") { 
	$PrintPage = "";
	$TBack = "background=\"images/tables/topbar.jpg\" height=\"24\"";
	$TLeft = "<img src=\"images/tables/topbar_left.jpg\" width=\"5\" height=\"24\">";
	$TRight = "<img src=\"images/tables/topbar_right.jpg\" width=\"5\" height=\"24\">";
	$PrintIt = "<a href=\"javascript:void(0);\" onClick=\"javascript:printPage('stank_startpage.html','Series','$Series');\" onMouseOver=\"javascript:imageOnDHTML('printit','ov');\" onMouseOut=\"javascript:imageOffDHTML('printit','off');\"><img src=\"images/tables/but_printit_off.gif\" width=\"67\" height=\"21\" name=\"printit\" border=\"0\"></a>";
	$EmailIt = "&nbsp;";
	$PageURL = "&nbsp;";
}
else {
	$PrintPage = "";
	$TBack = "background=\"images/tables/topbar.jpg\" height=\"24\"";
	$TLeft = "<img src=\"images/tables/topbar_left.jpg\" width=\"5\" height=\"24\">";
	$TRight = "<img src=\"images/tables/topbar_right.jpg\" width=\"5\" height=\"24\">";
	$PrintIt = "<a href=\"javascript:void(0);\" onClick=\"javascript:printPage('stank_startpage.html','Series','$Series');\" onMouseOver=\"javascript:imageOnDHTML('printit','ov');\" onMouseOut=\"javascript:imageOffDHTML('printit','off');\"><img src=\"images/tables/but_printit_off.gif\" width=\"67\" height=\"21\" name=\"printit\" border=\"0\"></a>";
	$EmailIt = "<a href=\"$StartURLer('https://www.coastlinemicro.com/stank_emailit.html?MySubject=$Series&MyTitle=$Series&MyLoad=loadthis&MyData=$Series&EmailSubject=$MainTitle'$EndURLer\" onMouseOver=\"javascript:imageOnDHTML('emailit','ov');\" onMouseOut=\"javascript:imageOffDHTML('emailit','off');\"><img src=\"images/tables/but_emailit_off.gif\" width=\"62\" height=\"21\" name=\"emailit\" border=\"0\"></a>";
	$PageURL = "";
}

print "Content-type: text/html\n\n";
{
print <<EOF

<html>
<head>
<title>Coastline Micro Inc.</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<STYLE TYPE="text/css">
body { background-color:#ffffff; scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</STYLE>
<LINK REL="STYLESHEET" HREF="common_css.html" Type="text/css">
<SCRIPT LANGUAGE="JavaScript">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

// QUICK CROSS-BROWSER MOUSE-OVER/OFF FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

// Specific Mouseover for DHTML window, must be placed on main document in order to work for
// MSIE 4 & 5

function imageOffDHTML(which,thisone) {
	var cual = 	"images/tables/but_"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}
function imageOnDHTML(which,thisone) {
	var cual = 	"images/tables/but_"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}

function imageOffDHTML2(which,thei,thisone) {
	var cual = 	"images/db/but_"+thei+"_"+thisone+".gif";
	document.images[which].src = cual;
}
function imageOnDHTML2(which,thei,thisone) {
	var cual = 	"images/db/but_"+thei+"_"+thisone+".gif";
	document.images[which].src = cual;
}
</SCRIPT>

<script language="javascript">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

<!--
function trigger(myurl) {
var b = navigator.appName;
if (b=="Netscape" && navigator.userAgent.indexOf("6.")) {
	this.location.href=myurl;
	}
else if (b=="Netscape") {
	mainFrame = parent.frames.botOne;
	mainFrame.frame.loadpage(''+myurl+'');
}
else {
	this.location.href=myurl;
	}
}
//-->
</script>
<!--START PRINT-->

<SCRIPT LANGUAGE="JavaScript">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

<!--

var da = (document.all) ? 1 : 0;
var pr = (window.print) ? 1 : 0;
var mac = (navigator.userAgent.indexOf("Mac") != -1); 
var ns4 = ((navigator.userAgent.indexOf("Mozilla") != -1) && (navigator.userAgent.indexOf("4.") != -1)  && (navigator.userAgent.indexOf("MSIE") == -1));
var ns6 = ((navigator.userAgent.indexOf("Netscape") != -1) && (navigator.userAgent.indexOf("6.") != -1));

function printPageNS() {
    window.print()
}

function printPage(uno,dos) {
  if (ns4) // NS4
    window.open('stank_startpage.html?Series=$Series&NSPRINT=1','PRINT','width=470,height=590');
  else if (pr) // IE5+
    window.print()
  else if (ns6) // NS6
    window.document.print()
  else if (da && !mac) // IE4 (Windows)
    lePrint()
  else // other browsers
    alert("Sorry, your browser doesn't support this feature.");
  return false;
}

if (da && !pr && !mac) with (document) {
  writeln('<OBJECT ID="wbp" CLASSID="CLSID:778C58A9-81B6-11D3-BB8F-00C04FA3471C">');
  writeln('<' + 'SCRIPT LANGUAGE="VBScript">');
  writeln('    Sub lePrint()');
  writeln('        If Len(wbp.DefaultPrinterName) = 0 Then');
  writeln('            MsgBox "No default printer!"');
  writeln('            Exit Sub');
  writeln('        End If');
  writeln('        wbp.Print');
  writeln('    End Sub');
  writeln('<' + '/SCRIPT>');
}
// -->
</SCRIPT>
<!--END PRINT-->

<base href="http://www.coastlinemicro.com/">
</head>
<body bgcolor="#ffffff" text="#8F8FAB" leftmargin="0" topmargin="0" marginwidth="0" scroll="yes" marginheight="0">

<table width="$tablewidth" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td align="center" valign="middle" width="$tablewidth" height="25"> 
      <table width="$tablewidth" border="0" cellspacing="0" cellpadding="0" $TBack>
        <tr> 
          <td width="$t1">$TLeft</td>
          <td width="$t2"><nobr><font class="btext">&nbsp;&nbsp;<b>$MainTitle</b></font></nobr></td>
          <td width="$t3" align="center" valign="top">$EmailIt</td>
          <td width="$t4" align="center" valign="top">$PrintIt</td>
          <td width="$t1" align="left" valign="top">$TRight</td>
        </tr>
      </table>
    </td>
  </tr>
  <tr>
    <td height="4"><img src="spacer.gif" width="1" height="4" border="0"></td>
  </tr>
  <tr> 
    <td width="100%"> 
      <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
        <tr> 
          <td width="100%"><font class="btext"> 
            <p>$BodyCopy</p>
            </font> </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
<p>&nbsp;</p>
<center>$PageURL</center>

$PrintPage

</body>
</html>

EOF
}
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