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
if (($Cookies{'UserType'} eq "CMManage") || ($Cookies{'UserType'} eq "CMAdmin") || ($Cookies{'UserType'} eq "CMSales") || ($Cookies{'ExtraAccess'} =~ "AdminUser")) { $nextone = "1"; }
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
if ($FORM{'leData'}) { 

use DBI;

## TOP OF DOCUMENT
{
print <<EOF

<html>
<head>
<title>Add User Account</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<script language="Javascript">
function checkPort() {
var missingdrop = "";
var thefirst = "";

if (document.IPorter.leData.value == "" || document.IPorter.leData.value == " ") {
    missingdrop += "\\n     - You must type drop in some valid data...";
	thefirst = "leData";
}

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    missingdrop ="___________________________________________                   \\n\\n" + "  Sorry, I cannot process your request because the\\n  following fields are either blank or filled incorrectly:\\n" + "___________________________________________                   \\n\\n" +
    missingdrop + "\\n\\n___________________________________________                   " + "\\n\\n   To continue, check fields and submit form again!" + "\\n___________________________________________";
    alert(missingdrop);
	document.IPorter[thefirst].focus();
    return false;
} 
else {
return true;
}
}


</script>
</head>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
$MenuConfig



$MenuConstructor
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%" valign="top"><img src="images/illus_main.jpg" width="250" height="100"></td>
    <td width="25%">&nbsp;</td>
    <td align="left" valign="top"><img src="images/title_main.jpg" width="300" height="100"></td>
  </tr>
</table>
<form method="post" action="$script" name="IPorter" onSubmit="return checkPort();">
  <table width="100%" border="0" cellpadding="0" cellspacing="0">
    <tr valign="top"> 
    <td width="20%">$legal</td>
      <td align="center" width="80%"> 
        <table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
            <td width="90%"><font face="verdana,arial,helvetica" size="2" color="#333366"><b>Import Product Data ( !!Caution - Read Instructions Carefully!! )</b></font></td>
            <td align="right" width="10%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
              <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER" bordercolor="#333366">
                <tr bordercolor="#333366" valign="middle"> 
                  <td width="100%" align="center" height="50" class="tableBG"><font face="verdana,arial,helvetica" size="1" color="#EB0000">*If you have any questions please ask your Supervisor or Manager for help using the system or updating it's information.</font></td>
              </tr>
              <tr bordercolor="#333366"> 
                  <td width="50%" align="center" valign="top" bordercolor="#333366"> 
                    <table width="100%" border="0" cellspacing="0" cellpadding="5">
                      <tr> 
                        <td width="100%" align="center" height="25" bgcolor="#F2F2F7" class="tableBG" colspan="2"><font face="verdana,arial,helvetica" size="2" color="#333366"><b>!! READ FEEDBACK CAREFULLY !!</b></font></td>
                      </tr>
                      <tr> 
                        <td align="center" valign="top" colspan="2"><br>

EOF
}

	## Crumble Form Input to Variables
	my $leData = "$FORM{'leData'}";
	my $ActionUser = "$Cookies{'Username'}";
	## Split data by line
	@leLines = split(/\n/, $leData);

	## kill all Double-Quotes (")
	s/"//g foreach @leLines;
	s/'//g foreach @leLines;
	s/,//g foreach @leLines;
	
	$CLines=0;
	## ----------------->>> SPLIT DATA
	foreach $leLinea (@leLines) {
		$CLines++;
		## Split line by tabs
		@leFields = split(/\t/, $leLinea);
		$leCM = $leFields[0];
		$leMFG = $leFields[1];
		$leMFGCode = $leFields[2];
		$lePClass = $leFields[3];
		$leIName = $leFields[4];
		$leWeight = $leFields[5];
		$leCost = $leFields[6];
		$leIngram = $leFields[7];
		$leAction = $leFields[8];
		$lePType = $leFields[9];
		$leSear = $leFields[10];
		
		if ($leCM eq "" || $leCM eq " ") { push(@NoCM, "$leFields[0]-----$leFields[1]-----$leFields[2]-----$leFields[3]-----$leFields[4]-----$leFields[5]-----$leFields[6]-----$leFields[7]-----$leFields[8]-----$leFields[9]-----$leFields[10]"); }
		elsif ($leMFG eq "" || $leMFG eq " ") { push(@NoMFG, "$leFields[0]-----$leFields[1]-----$leFields[2]-----$leFields[3]-----$leFields[4]-----$leFields[5]-----$leFields[6]-----$leFields[7]-----$leFields[8]-----$leFields[9]-----$leFields[10]"); }
		elsif ($leMFGCode eq "" || $leMFGCode eq " " || $leMFGCode eq "NULL" || $leMFGCode eq "NONE") { push(@NoMFGCode, "$leFields[0]-----$leFields[1]-----$leFields[2]-----$leFields[3]-----$leFields[4]-----$leFields[5]-----$leFields[6]-----$leFields[7]-----$leFields[8]-----$leFields[9]-----$leFields[10]"); }
		elsif ($lePClass eq "" || $lePClass eq " ") { push(@NoPClass, "$leFields[0]-----$leFields[1]-----$leFields[2]-----$leFields[3]-----$leFields[4]-----$leFields[5]-----$leFields[6]-----$leFields[7]-----$leFields[8]-----$leFields[9]-----$leFields[10]"); }
		elsif ($leIName eq "" || $leIName eq " ") { push(@NoIName, "$leFields[0]-----$leFields[1]-----$leFields[2]-----$leFields[3]-----$leFields[4]-----$leFields[5]-----$leFields[6]-----$leFields[7]-----$leFields[8]-----$leFields[9]-----$leFields[10]"); }
		elsif ($leWeight eq "" || $leWeight eq " ") { push(@NoWeight, "$leFields[0]-----$leFields[1]-----$leFields[2]-----$leFields[3]-----$leFields[4]-----$leFields[5]-----$leFields[6]-----$leFields[7]-----$leFields[8]-----$leFields[9]-----$leFields[10]"); }
		elsif ($leCost eq "" || $leCost eq " ") { push(@NoCost, "$leFields[0]-----$leFields[1]-----$leFields[2]-----$leFields[3]-----$leFields[4]-----$leFields[5]-----$leFields[6]-----$leFields[7]-----$leFields[8]-----$leFields[9]-----$leFields[10]"); }
		elsif ($lePType eq "" || $lePType eq " ") { push(@NoPType, "$leFields[0]-----$leFields[1]-----$leFields[2]-----$leFields[3]-----$leFields[4]-----$leFields[5]-----$leFields[6]-----$leFields[7]-----$leFields[8]-----$leFields[9]-----$leFields[10]"); }
		elsif ($leSear eq "" || $leSear eq " ") { push(@NoSear, "$leFields[0]-----$leFields[1]-----$leFields[2]-----$leFields[3]-----$leFields[4]-----$leFields[5]-----$leFields[6]-----$leFields[7]-----$leFields[8]-----$leFields[9]-----$leFields[10]"); }
		
		if ($leAction =~ "Add" || $leAction =~ "add") { push(@Additions, "$leFields[0]-----$leFields[1]-----$leFields[2]-----$leFields[3]-----$leFields[4]-----$leFields[5]-----$leFields[6]-----$leFields[7]-----$leFields[8]-----$leFields[9]-----$leFields[10]"); }
		elsif ($leAction =~ "Delete" || $leAction =~ "delete") { push(@Deletions, "$leFields[0]-----$leFields[1]-----$leFields[2]-----$leFields[3]-----$leFields[4]-----$leFields[5]-----$leFields[6]-----$leFields[7]-----$leFields[8]-----$leFields[9]-----$leFields[10]"); }
		elsif ($leAction =~ "Update" || $leAction =~ "update") { push(@Updates, "$leFields[0]-----$leFields[1]-----$leFields[2]-----$leFields[3]-----$leFields[4]-----$leFields[5]-----$leFields[6]-----$leFields[7]-----$leFields[8]-----$leFields[9]-----$leFields[10]"); }
		else { push(@NoAction, "$leFields[0]-----$leFields[1]-----$leFields[2]-----$leFields[3]-----$leFields[4]-----$leFields[5]-----$leFields[6]-----$leFields[7]-----$leFields[8]-----$leFields[9]-----$leFields[10]"); }
	}

	## ----------------->>> BEGIN VERIFICATION PROCESS
	## ----------------->>> IF MISSING ACTION FIELD
	if (@NoAction) {

		print "<table width=\"95%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" align=\"center\"><tr><td width=\"348\" colspan=\"3\" bgcolor=\"#8F8FAB\"><img src=\"images/spacer.gif\" width=\"25\" height=\"1\"></td></tr><tr><td bgcolor=\"#8F8FAB\" width=\"1\" height=\"80\"><img src=\"images/verticalbar.gif\" width=\"1\" height=\"25\"></td><td width=\"100%\" valign=\"top\"><table border=\"0\" cellspacing=\"0\" cellpadding=\"0\" width=\"100%\"><tr><td width=\"2%\" height=\"15\" bgcolor=\"#8F8FAB\">&nbsp;</td><td height=\"20\" bgcolor=\"#8F8FAB\" width=\"96%\" colspan=\"2\" align=\"center\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#FFFFFF\"><b>Error: Product(s) missing 'Action' specification</b></font></td><td width=\"2%\" height=\"15\" bgcolor=\"#8F8FAB\">&nbsp;</td></tr>";
		print "<tr><td colspan=\"4\" height=\"1\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"1\"></td></tr><tr><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td><td height=\"20\" align=\"left\" colspan=\"2\" bgcolor=\"#F2F2F7\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#333366\"><b><center><br>All products must specify an ACTION: Add, Update or Delete</center></b><br>This program cannot continue if ALL REQUIRED FIELDS are not completed. Please make sure you review the instructions for Importing Products to the system and correct your data before continuing. ONLY the products shown here are missing the action, all other products submitted are properly tagged but will not be processed until you fix the problem(s) with the item(s) shown below.<br><br></font></td><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td></tr>";
		print "<tr><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td><td align=\"center\" width=\"96%\" colspan=\"2\">";
		print "<table width=\"100%\" cellpadding=\"3\" cellspacing=\"1\" border=\"1\" bordercolor=\"#8F8FAB\"><tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>CmPartNum</b></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><b>MfgPartNum</b></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Product Type</nobr></b></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Pricing Class</nobr></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Weight</b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Cost</b></font></td><td width=\"5%\" align=\"left\"><font class=\"btext3\"><b>IngramPart</b></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btextred\"><b><u>Action</u></b></font></td></tr>";

		foreach $noAct (@NoAction) {
			@splitAct = split(/-----/, $noAct);
        	print "<tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[0]</nobr></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[1]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[9]</nobr></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\">$splitAct[3]</font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[5]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[6]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[7]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btextred\"><nobr>None</nobr></font></td></tr>";
		}
		print "</table></td><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td></tr><tr><td width=\"2%\" bgcolor=\"#F2F2F7\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td><td height=\"15\" align=\"center\" width=\"96%\" valign=\"top\" bgcolor=\"#F2F2F7\" colspan=\"2\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td><td width=\"2%\" bgcolor=\"#F2F2F7\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td></tr></table></td><td bgcolor=\"#8F8FAB\" width=\"1\" height=\"70\"><img src=\"images/verticalbar.gif\" width=\"1\" height=\"25\"></td></tr><tr><td width=\"100%\" colspan=\"3\" bgcolor=\"#8F8FAB\"><img src=\"images/spacer.gif\" width=\"25\" height=\"1\"></td></tr></table><br>";

	## STOP PROCESS
	exit;
	}

	## ----------------->>> IF MISSING ANY OTHER REQUIRED FIELD
	if (@NoCM || @NoMFG || @NoPType || @NoIName || @NoWeight || @NoCost || @NoPClass || @NoSear || @NoMFGCode) {

		print "<table width=\"95%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" align=\"center\"><tr><td width=\"348\" colspan=\"3\" bgcolor=\"#8F8FAB\"><img src=\"images/spacer.gif\" width=\"25\" height=\"1\"></td></tr><tr><td bgcolor=\"#8F8FAB\" width=\"1\" height=\"80\"><img src=\"images/verticalbar.gif\" width=\"1\" height=\"25\"></td><td width=\"100%\" valign=\"top\"><table border=\"0\" cellspacing=\"0\" cellpadding=\"0\" width=\"100%\"><tr><td width=\"2%\" height=\"15\" bgcolor=\"#8F8FAB\">&nbsp;</td><td height=\"20\" bgcolor=\"#8F8FAB\" width=\"96%\" colspan=\"2\" align=\"center\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#FFFFFF\"><b>Error: Product(s) missing 'REQUIRED' field</b></font></td><td width=\"2%\" height=\"15\" bgcolor=\"#8F8FAB\">&nbsp;</td></tr>";
		print "<tr><td colspan=\"4\" height=\"1\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"1\"></td></tr><tr><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td><td height=\"20\" align=\"left\" colspan=\"2\" bgcolor=\"#F2F2F7\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#333366\"><b><center><br>All products must have REQUIRED fields filled in</center></b><br>This program cannot continue if ALL REQUIRED FIELDS are not completed. Please make sure you review the instructions for Importing Products to the system and correct your data before continuing. ONLY the products shown here have missing data, all other products submitted are properly tagged but will not be processed until you fix the problem(s) with the item(s) shown below.<br><br></font></td><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td></tr>";
		print "<tr><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td><td align=\"center\" width=\"96%\" colspan=\"2\">";

		if (@NoCM) {
		print "<table width=\"100%\" cellpadding=\"3\" cellspacing=\"1\" border=\"1\" bordercolor=\"#8F8FAB\"><tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btextred\"><b>CmPartNum</b></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><b>MfgPartNum</b></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Product Type</nobr></b></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Pricing Class</nobr></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Weight</b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Cost</b></font></td><td width=\"5%\" align=\"left\"><font class=\"btext3\"><b>IngramPart</b></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><u>Action</u></b></font></td></tr>";
			foreach $noAct (@NoCM) {
				@splitAct = split(/-----/, $noAct);
        		print "<tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btextred\"><nobr>none</nobr></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[1]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[9]</nobr></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\">$splitAct[3]</font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[5]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[6]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[7]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[8]</nobr></font></td></tr>";
			}
		print "</table>";
		}
		if (@NoMFG) {
			print "<table width=\"100%\" cellpadding=\"3\" cellspacing=\"1\" border=\"1\" bordercolor=\"#8F8FAB\"><tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>CmPartNum</b></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btextred\"><b><b>MfgPartNum</b></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Product Type</nobr></b></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Pricing Class</nobr></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Weight</b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Cost</b></font></td><td width=\"5%\" align=\"left\"><font class=\"btext3\"><b>IngramPart</b></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><u>Action</u></b></font></td></tr>";
			foreach $noAct (@NoMFG) {
				@splitAct = split(/-----/, $noAct);
        		print "<tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[0]</nobr></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>none</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[9]</nobr></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\">$splitAct[3]</font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[5]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[6]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[7]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[8]</nobr></font></td></tr>";
			}
			print "</table>";
		}
		if (@NoPClass) {
			print "<table width=\"100%\" cellpadding=\"3\" cellspacing=\"1\" border=\"1\" bordercolor=\"#8F8FAB\"><tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>CmPartNum</b></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><b>MfgPartNum</b></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Product Type</nobr></b></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btextred\"><b><nobr>Pricing Class</nobr></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Weight</b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Cost</b></font></td><td width=\"5%\" align=\"left\"><font class=\"btext3\"><b>IngramPart</b></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><u>Action</u></b></font></td></tr>";
			foreach $noAct (@NoPClass) {
				@splitAct = split(/-----/, $noAct);
        		print "<tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[0]</nobr></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[1]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[9]</nobr></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btextred\">none</font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[5]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[6]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[7]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[8]</nobr></font></td></tr>";
			}
			print "</table>";
		}
		if (@NoPType) {
			print "<table width=\"100%\" cellpadding=\"3\" cellspacing=\"1\" border=\"1\" bordercolor=\"#8F8FAB\"><tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>CmPartNum</b></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><b>MfgPartNum</b></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btextred\"><b><nobr>Product Type</nobr></b></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Pricing Class</nobr></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Weight</b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Cost</b></font></td><td width=\"5%\" align=\"left\"><font class=\"btext3\"><b>IngramPart</b></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><u>Action</u></b></font></td></tr>";
			foreach $noAct (@NoPType) {
				@splitAct = split(/-----/, $noAct);
        		print "<tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[0]</nobr></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[1]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btextred\"><nobr>none</nobr></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\">$splitAct[3]</font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[5]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[6]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[7]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[8]</nobr></font></td></tr>";
			}		
			print "</table>";
		}
		if (@NoWeight) {
			print "<table width=\"100%\" cellpadding=\"3\" cellspacing=\"1\" border=\"1\" bordercolor=\"#8F8FAB\"><tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>CmPartNum</b></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><b>MfgPartNum</b></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Product Type</nobr></b></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Pricing Class</nobr></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btextred\"><b>Weight</b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Cost</b></font></td><td width=\"5%\" align=\"left\"><font class=\"btext3\"><b>IngramPart</b></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><u>Action</u></b></font></td></tr>";
			foreach $noAct (@NoWeight) {
				@splitAct = split(/-----/, $noAct);
        		print "<tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[0]</nobr></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[1]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[9]</nobr></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\">$splitAct[3]</font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btextred\"><nobr>none</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[6]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[7]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[8]</nobr></font></td></tr>";
			}
			print "</table>";
		}	
		if (@NoCost) {
			print "<table width=\"100%\" cellpadding=\"3\" cellspacing=\"1\" border=\"1\" bordercolor=\"#8F8FAB\"><tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>CmPartNum</b></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><b>MfgPartNum</b></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Product Type</nobr></b></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Pricing Class</nobr></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Weight</b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btextred\"><b>Cost</b></font></td><td width=\"5%\" align=\"left\"><font class=\"btext3\"><b>IngramPart</b></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><u>Action</u></b></font></td></tr>";
			foreach $noAct (@NoCost) {
				@splitAct = split(/-----/, $noAct);
        		print "<tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[0]</nobr></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[1]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[9]</nobr></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\">$splitAct[3]</font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[5]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btextred\"><nobr>none</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[7]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[8]</nobr></font></td></tr>";
			}		
			print "</table>";
		}
		if (@NoSear) {
			print "<table width=\"100%\" cellpadding=\"3\" cellspacing=\"1\" border=\"1\" bordercolor=\"#8F8FAB\"><tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>CmPartNum</b></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><b>MfgPartNum</b></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Product Type</nobr></b></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Pricing Class</nobr></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Weight</b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Cost</b></font></td><td width=\"5%\" align=\"left\"><font class=\"btext3\"><b>IngramPart</b></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btextred\"><b><u>Searchable</u></b></font></td></tr>";
			foreach $noAct (@NoSear) {
				@splitAct = split(/-----/, $noAct);
        		print "<tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[0]</nobr></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[1]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[9]</nobr></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\">$splitAct[3]</font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[5]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[6]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[7]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btextred\"><nobr>none</nobr></font></td></tr>";
			}
			print "</table>";
		}
		if (@NoMFGCode) {
			print "<table width=\"100%\" cellpadding=\"3\" cellspacing=\"1\" border=\"1\" bordercolor=\"#8F8FAB\"><tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>CmPartNum</b></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><b>MfgPartNum</b></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Product Type</nobr></b></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Pricing Class</nobr></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Weight</b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Cost</b></font></td><td width=\"5%\" align=\"left\"><font class=\"btext3\"><b>IngramPart</b></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btextred\"><b><u>MFGCode</u></b></font></td></tr>";
			foreach $noAct (@NoMFGCode) {
				@splitAct = split(/-----/, $noAct);
        		print "<tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[0]</nobr></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[1]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[9]</nobr></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\">$splitAct[3]</font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[5]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[6]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[7]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btextred\"><nobr>none</nobr></font></td></tr>";
			}
			print "</table>";
		}
		if (@NoIName) {
			print "<table width=\"100%\" cellpadding=\"3\" cellspacing=\"1\" border=\"1\" bordercolor=\"#8F8FAB\"><tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>CmPartNum</b></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><b>MfgPartNum</b></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Product Type</nobr></b></font></td><td width=\"65%\" align=\"left\" valign=\"top\"><font class=\"btextred\"><b>Item Name</b></font></td></tr>";
			foreach $noAct (@NoIName) {
				@splitAct = split(/-----/, $noAct);
        		print "<tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[0]</nobr></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[1]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAct[9]</nobr></font></td><td width=\"65%\" align=\"left\" valign=\"top\"><font class=\"btextred\">none</font></td></tr>";
			}
			print "</table>";
		}
		print "</td><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td></tr><tr><td width=\"2%\" bgcolor=\"#F2F2F7\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td><td height=\"15\" align=\"center\" width=\"96%\" valign=\"top\" bgcolor=\"#F2F2F7\" colspan=\"2\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td><td width=\"2%\" bgcolor=\"#F2F2F7\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td></tr></table></td><td bgcolor=\"#8F8FAB\" width=\"1\" height=\"70\"><img src=\"images/verticalbar.gif\" width=\"1\" height=\"25\"></td></tr><tr><td width=\"100%\" colspan=\"3\" bgcolor=\"#8F8FAB\"><img src=\"images/spacer.gif\" width=\"25\" height=\"1\"></td></tr></table><br>";

	## STOP PROCESS
	exit;
	}
	
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 

	## ----------------->>> MAKE SURE PRODUCTS BEING ADDED ARE NOT ALREADY IN SYSTEM
	$AddMatching=0;	
	if (@Additions) {
		foreach $Addition1 (@Additions) {
			@split1Add = split(/-----/, $Addition1);
			$miCM = $split1Add[0];
			$miMFG = $split1Add[1];
			$miIngram = $split1Add[7];

			my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$miCM'");
			$sth->execute or die "Unable to execute query\n"; 
			my @row;
			while(@row = $sth->fetchrow_array) {
				$CMParte = $row[1]; 
				$MFGParte = $row[7]; 
				$IngramParte = $row[29]; 
				$AddMatching++;
				push(@AddMatches, "$split1Add[0]-----$split1Add[1]-----$split1Add[2]-----$split1Add[3]-----$split1Add[4]-----$split1Add[5]-----$split1Add[6]-----$split1Add[7]-----$split1Add[8]-----$split1Add[9]-----$split1Add[10]");
			}
			$sth->execute or die "Unable to execute query\n"; 
			$sth->finish;
		}
	}
	
	## ----------------->>> MAKE SURE PRODUCTS BEING DELETED ARE NOT BEING USED IN THE SYSTEM
	$DelMatching=0;	
	if (@Deletions) {

		##----------->>> FIRST GRAB ALL SYSTEMS COMPONENTS, IE: LIST OF ALL PRODUCTS BEING USED
		##----------->>> FIRST CMPART
		my $sth = $dbh->prepare("SELECT * FROM Products WHERE SYSCode != 'NULL'");
		$sth->execute or die "Unable to execute query\n";
		my @row;
		while(@row = $sth->fetchrow_array) { 
			push(@LosSystemas, $row[1]);
			push(@LosComponents, "$row[1]-----$row[24]");
		}
		$sth->execute or die "Unable to execute query\n"; 
		$sth->finish;
		##----------->>> THEN SYSTEM CONFIG FOR EACH CMPART
		foreach $ElSystema (@LosSystemas) {
			my $sth = $dbh->prepare("SELECT * FROM Systems WHERE Parent='$ElSystema'");
			$sth->execute or die "Unable to execute query\n"; 
			my @row;
			while(@row = $sth->fetchrow_array) { 
				push(@LosComponents, "$ElSystema-----$row[7]");
				push(@LosComponents, "$ElSystema-----$row[11]");
				push(@LosComponents, "$ElSystema-----$row[15]");
				push(@LosComponents, "$ElSystema-----$row[19]");
				push(@LosComponents, "$ElSystema-----$row[23]");		
				push(@LosComponents, "$ElSystema-----$row[27]");		
				push(@LosComponents, "$ElSystema-----$row[31]");
				push(@LosComponents, "$ElSystema-----$row[35]");
				push(@LosComponents, "$ElSystema-----$row[39]");
				push(@LosComponents, "$ElSystema-----$row[43]");
				push(@LosComponents, "$ElSystema-----$row[47]");
				push(@LosComponents, "$ElSystema-----$row[51]");
				push(@LosComponents, "$ElSystema-----$row[55]");		
				push(@LosComponents, "$ElSystema-----$row[59]");		
				push(@LosComponents, "$ElSystema-----$row[63]");		
				push(@LosComponents, "$ElSystema-----$row[67]");				
				push(@LosComponents, "$ElSystema-----$row[71]");				
				push(@LosComponents, "$ElSystema-----$row[75]");				
				push(@LosComponents, "$ElSystema-----$row[79]");				
				push(@LosComponents, "$ElSystema-----$row[83]");				
				push(@LosComponents, "$ElSystema-----$row[87]");				
				push(@LosComponents, "$ElSystema-----$row[91]");				
				push(@LosComponents, "$ElSystema-----$row[95]");				
				push(@LosComponents, "$ElSystema-----$row[99]");						
				push(@LosComponents, "$ElSystema-----$row[103]");						
				push(@LosComponents, "$ElSystema-----$row[107]");				
			}
			$sth->execute or die "Unable to execute query\n"; 
			$sth->finish;
		}
		##----------->>> NOW, CHECK TO SEE IF ANY OF THE PRODUCTS BEING DELETED ARE BEING USED BY A SYSTEM
		foreach $Update1 (@Deletions) {
			@split1Up = split(/-----/, $Update1);
			$mioCM = $split1Up[0];
			foreach $ElComponent (@LosComponents) {
				@splitComp = split(/-----/, $ElComponent);
				$elCM = $splitComp[1];
				$elSys = $splitComp[0];
				if ($elCM =~ $mioCM) {

					##----------->>> PICKUP MATCHING PRODUCT NAME FOR DISPLAY AND EASE OF USE
					my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$elCM'");
					$sth->execute or die "Unable to execute query\n";
					my @row;
					while(@row = $sth->fetchrow_array) {
						$leNombre = "$row[11]";
					}
					$sth->execute or die "Unable to execute query\n"; 
					$sth->finish;
					##----------->>> PICKUP MATCHING SYSTEM'S PRICING CLASS FOR LINKING
					my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$elSys'");
					$sth->execute or die "Unable to execute query\n";
					my @row;
					while(@row = $sth->fetchrow_array) {
						$lePClass = "$row[10]";
					}
					$sth->execute or die "Unable to execute query\n"; 
					$sth->finish;
					
					push(@DelMatches, "$mioCM-----$elSys-----$leNombre-----$lePClass");
					$DelMatching++;
				}
			}
		}
	}

	## ----------------->>> IF PRODUCTS BEING ADDED AND NO MATCHES FOUND IN SYSTEM
	if ((@Additions) && ($AddMatching eq "0") && ($DelMatching eq "0")) {
		print "<table width=\"95%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" align=\"center\"><tr><td width=\"348\" colspan=\"3\" bgcolor=\"#8F8FAB\"><img src=\"images/spacer.gif\" width=\"25\" height=\"1\"></td></tr><tr><td bgcolor=\"#8F8FAB\" width=\"1\" height=\"80\"><img src=\"images/verticalbar.gif\" width=\"1\" height=\"25\"></td><td width=\"100%\" valign=\"top\"><table border=\"0\" cellspacing=\"0\" cellpadding=\"0\" width=\"100%\"><tr><td width=\"2%\" height=\"15\" bgcolor=\"#8F8FAB\">&nbsp;</td><td height=\"20\" bgcolor=\"#8F8FAB\" width=\"96%\" colspan=\"2\" align=\"center\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#FFFFFF\"><b>Products Added Successfully</b></font></td><td width=\"2%\" height=\"15\" bgcolor=\"#8F8FAB\">&nbsp;</td></tr>";
		print "<tr><td colspan=\"4\" height=\"1\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"1\"></td></tr><tr><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td><td height=\"20\" align=\"left\" colspan=\"2\" bgcolor=\"#F2F2F7\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#333366\"><b><center><br>The following products have been successfully added to the system:</center></b><br></font></td><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td></tr>";
		print "<tr><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td><td align=\"center\" width=\"96%\" colspan=\"2\">";
		print "<table width=\"100%\" cellpadding=\"3\" cellspacing=\"1\" border=\"1\" bordercolor=\"#8F8FAB\"><tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>CmPartNum</b></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><b>MfgPartNum</b></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Product Type</nobr></b></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Pricing Class</nobr></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Weight</b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Cost</b></font></td><td width=\"5%\" align=\"left\"><font class=\"btext3\"><b>IngramPart</b></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><u>Action</u></b></font></td></tr>";
		foreach $Addition2 (@Additions) {
			@splitAdd = split(/-----/, $Addition2);

			$AdCM = $splitAdd[0];
			$AdMFG = $splitAdd[1];
			$AdMFGCode = $splitAdd[2];
			$AdPClass = $splitAdd[3];
			$AdIName = $splitAdd[4];
			$AdWeight = $splitAdd[5];
			$AdCost = $splitAdd[6];
			$AdIngram = $splitAdd[7];
			$AdAction = $splitAdd[8];
			$AdPType = $splitAdd[9];
			$AdSear = $splitAdd[10];
			
			my $sth = $dbh->prepare("INSERT INTO Products (ProductID, CMPartNum, 
									 SYSCode, KITCode, MediaCode, DISTCode, MFGCode, MFGPartNum, 
									 MFGProdURL, MFGDriverURL, PricingClass, ItemName, Description, 
									 TechSpecs, Keywords, SneakPeak, Emblem, SmallPhoto, LargePhoto, 
									 Warranty, Weight, Cost, CompPrice, RelatedProd, Accessories, 
									 AddedBy, AddedOn, ModifiedBy, ModifiedOn, IngramPartNum, 
						 			 TechDataPartNum, SynnexPartNum, ProductType, Searchable)
					 
									 VALUES (Null, '$AdCM', Null, Null, Null, Null, '$AdMFGCode', 
									 '$AdMFG', Null, Null, '$AdPClass', '$AdIName', 
									 Null, Null, Null, Null, Null, Null, Null, Null, '$AdWeight', 
						 			'$AdCost', Null, Null, Null, '$ActionUser', Null, '', '', '$AdIngram', 
						 			'', '', '$AdPType', '$AdSear')");
			$sth->execute or die "Unable to execute query\n"; 
			$sth->finish; 

       		print "<tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAdd[0]</nobr></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAdd[1]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAdd[9]</nobr></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\">$splitAdd[3]</font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAdd[5]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAdd[6]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAdd[7]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitAdd[8]</nobr></font></td></tr>";
		}
		print "</table></td><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td></tr><tr><td width=\"2%\" bgcolor=\"#F2F2F7\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td><td height=\"15\" align=\"center\" width=\"96%\" valign=\"top\" bgcolor=\"#F2F2F7\" colspan=\"2\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td><td width=\"2%\" bgcolor=\"#F2F2F7\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td></tr></table></td><td bgcolor=\"#8F8FAB\" width=\"1\" height=\"70\"><img src=\"images/verticalbar.gif\" width=\"1\" height=\"25\"></td></tr><tr><td width=\"100%\" colspan=\"3\" bgcolor=\"#8F8FAB\"><img src=\"images/spacer.gif\" width=\"25\" height=\"1\"></td></tr></table><br>";
	}
	## ----------------->>> IF MATCHES FOUND FOR ADDITIONS IN SYSTEM
	elsif (@Additions) {
		print "<table width=\"95%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" align=\"center\"><tr><td width=\"348\" colspan=\"3\" bgcolor=\"#8F8FAB\"><img src=\"images/spacer.gif\" width=\"25\" height=\"1\"></td></tr><tr><td bgcolor=\"#8F8FAB\" width=\"1\" height=\"80\"><img src=\"images/verticalbar.gif\" width=\"1\" height=\"25\"></td><td width=\"100%\" valign=\"top\"><table border=\"0\" cellspacing=\"0\" cellpadding=\"0\" width=\"100%\"><tr><td width=\"2%\" height=\"15\" bgcolor=\"#8F8FAB\">&nbsp;</td><td height=\"20\" bgcolor=\"#8F8FAB\" width=\"96%\" colspan=\"2\" align=\"center\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#FFFFFF\"><b>Duplicate Product(s) Found</b></font></td><td width=\"2%\" height=\"15\" bgcolor=\"#8F8FAB\">&nbsp;</td></tr>";
		print "<tr><td colspan=\"4\" height=\"1\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"1\"></td></tr><tr><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td><td height=\"20\" align=\"left\" colspan=\"2\" bgcolor=\"#F2F2F7\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#333366\"><br>Product(s) you are attempting to ADD to the system already exist. Make sure you specify the correct data for all product(s) you are attempting to import, then try again.<br><br><b><center>Duplicate product(s):</center></b><br></font></td><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td></tr>";
		print "<tr><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td><td align=\"center\" width=\"96%\" colspan=\"2\">";
		print "<table width=\"100%\" cellpadding=\"3\" cellspacing=\"1\" border=\"1\" bordercolor=\"#8F8FAB\"><tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>CmPartNum</b></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><b>MfgPartNum</b></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Product Type</nobr></b></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Pricing Class</nobr></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Weight</b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Cost</b></font></td><td width=\"5%\" align=\"left\"><font class=\"btext3\"><b>IngramPart</b></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><u>Action</u></b></font></td></tr>";
		foreach $AddMatch (@AddMatches) {
			@matchAdd = split(/-----/, $AddMatch);
       		print "<tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$matchAdd[0]</nobr></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$matchAdd[1]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$matchAdd[9]</nobr></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\">$matchAdd[3]</font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$matchAdd[5]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$matchAdd[6]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$matchAdd[7]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$matchAdd[8]</nobr></font></td></tr>";
		}
		print "</table></td><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td></tr><tr><td width=\"2%\" bgcolor=\"#F2F2F7\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td><td height=\"15\" align=\"center\" width=\"96%\" valign=\"top\" bgcolor=\"#F2F2F7\" colspan=\"2\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td><td width=\"2%\" bgcolor=\"#F2F2F7\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td></tr></table></td><td bgcolor=\"#8F8FAB\" width=\"1\" height=\"70\"><img src=\"images/verticalbar.gif\" width=\"1\" height=\"25\"></td></tr><tr><td width=\"100%\" colspan=\"3\" bgcolor=\"#8F8FAB\"><img src=\"images/spacer.gif\" width=\"25\" height=\"1\"></td></tr></table><br>";
	## stop process
	exit;
	}	
		
## ----------------->>
## ----------------->> IF PASSED ALL PARAMETERS AND CHECKS CONTINUE
## ----------------->> 

	## ----------------->>> IF PRODUCTS BEING UPDATED
	if ((@Deletions) && ($DelMatching eq "0")) {
		print "<table width=\"95%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" align=\"center\"><tr><td width=\"348\" colspan=\"3\" bgcolor=\"#8F8FAB\"><img src=\"images/spacer.gif\" width=\"25\" height=\"1\"></td></tr><tr><td bgcolor=\"#8F8FAB\" width=\"1\" height=\"80\"><img src=\"images/verticalbar.gif\" width=\"1\" height=\"25\"></td><td width=\"100%\" valign=\"top\"><table border=\"0\" cellspacing=\"0\" cellpadding=\"0\" width=\"100%\"><tr><td width=\"2%\" height=\"15\" bgcolor=\"#8F8FAB\">&nbsp;</td><td height=\"20\" bgcolor=\"#8F8FAB\" width=\"96%\" colspan=\"2\" align=\"center\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#FFFFFF\"><b>Products Deleted Successfully</b></font></td><td width=\"2%\" height=\"15\" bgcolor=\"#8F8FAB\">&nbsp;</td></tr>";
		print "<tr><td colspan=\"4\" height=\"1\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"1\"></td></tr><tr><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td><td height=\"20\" align=\"left\" colspan=\"2\" bgcolor=\"#F2F2F7\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#333366\"><b><center><br>The following products have been successfully deleted from the system:</center></b><br></font></td><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td></tr>";
		print "<tr><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td><td align=\"center\" width=\"96%\" colspan=\"2\">";
		print "<table width=\"100%\" cellpadding=\"3\" cellspacing=\"1\" border=\"1\" bordercolor=\"#8F8FAB\"><tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>CmPartNum</b></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><b>MfgPartNum</b></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Product Type</nobr></b></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Pricing Class</nobr></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Weight</b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Cost</b></font></td><td width=\"5%\" align=\"left\"><font class=\"btext3\"><b>IngramPart</b></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><u>Action</u></b></font></td></tr>";
		foreach $Deletion (@Deletions) {
			@splitDel = split(/-----/, $Deletion);

			my $sth = $dbh->prepare("DELETE FROM Products WHERE CMPartNum='$splitDel[0]'");
			$sth->execute or die "Unable to execute query\n"; 
			$sth->finish;
			
        	print "<tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitDel[0]</nobr></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitDel[1]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitDel[9]</nobr></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\">$splitDel[3]</font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitDel[5]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitDel[6]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitDel[7]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitDel[8]</nobr></font></td></tr>";
		}
		print "</table></td><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td></tr><tr><td width=\"2%\" bgcolor=\"#F2F2F7\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td><td height=\"15\" align=\"center\" width=\"96%\" valign=\"top\" bgcolor=\"#F2F2F7\" colspan=\"2\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td><td width=\"2%\" bgcolor=\"#F2F2F7\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td></tr></table></td><td bgcolor=\"#8F8FAB\" width=\"1\" height=\"70\"><img src=\"images/verticalbar.gif\" width=\"1\" height=\"25\"></td></tr><tr><td width=\"100%\" colspan=\"3\" bgcolor=\"#8F8FAB\"><img src=\"images/spacer.gif\" width=\"25\" height=\"1\"></td></tr></table><br>";

	## STOP PROCESS
	exit;
	}
	elsif (@Deletions) {
		print "<table width=\"95%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" align=\"center\"><tr><td width=\"348\" colspan=\"3\" bgcolor=\"#8F8FAB\"><img src=\"images/spacer.gif\" width=\"25\" height=\"1\"></td></tr><tr><td bgcolor=\"#8F8FAB\" width=\"1\" height=\"80\"><img src=\"images/verticalbar.gif\" width=\"1\" height=\"25\"></td><td width=\"100%\" valign=\"top\"><table border=\"0\" cellspacing=\"0\" cellpadding=\"0\" width=\"100%\"><tr><td width=\"2%\" height=\"15\" bgcolor=\"#8F8FAB\">&nbsp;</td><td height=\"20\" bgcolor=\"#8F8FAB\" width=\"96%\" colspan=\"2\" align=\"center\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#FFFFFF\"><b>Product(s) Being Referenced By System Config</b></font></td><td width=\"2%\" height=\"15\" bgcolor=\"#8F8FAB\">&nbsp;</td></tr>";
		print "<tr><td colspan=\"4\" height=\"1\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"1\"></td></tr><tr><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td><td height=\"20\" align=\"left\" colspan=\"2\" bgcolor=\"#F2F2F7\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#333366\"><br>Product(s) you are attempting to DELETE from the system are currently being referenced(Matching CmPartNum) by one or more Systems(System CMPartNum) in the database. Please make sure you change these dependencies by removing the product(s) listed below from the configuration of the system(s) listed below, then try again. Also, ALWAYS make sure you specify the correct data for all product(s) you are attempting to import. Keep in mind: Not all matches will show the product's name. This is NOT an issue, just make sure you remove the dependencies listed below and you are clear to try again.<br><br><b><center>Dependencies found:</center></b><br></font></td><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td></tr>";
		print "<tr><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td><td align=\"center\" width=\"96%\" colspan=\"2\">";
		print "<table width=\"100%\" cellpadding=\"3\" cellspacing=\"1\" border=\"1\" bordercolor=\"#8F8FAB\"><tr><td width=\"50%\" align=\"left\" valign=\"top\"><font class=\"btextred\"><b><nobr>System CMPartNum</nobr></b></font></td><td width=\"50%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><nobr>Matching CmPartNum</nobr></b></font></td></tr>";
		foreach $DelMatch (@DelMatches) {
			@matchDel = split(/-----/, $DelMatch);
       		print "<tr><td width=\"50%\" align=\"left\" valign=\"top\"><a href=\"#\" onClick=\"javascript:window.open('change_product_system.cgi?CMPartNum=$matchDel[1]&PricingClass=$matchDel[3]','KILLDEP');\"><font class=\"btextred\"><nobr>$matchDel[1]</nobr></font></a></td><td width=\"50%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$matchDel[0]</nobr></font></td></tr>";
		}

		print "</table></td><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td></tr><tr><td width=\"2%\" bgcolor=\"#F2F2F7\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td><td height=\"15\" align=\"center\" width=\"96%\" valign=\"top\" bgcolor=\"#F2F2F7\" colspan=\"2\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td><td width=\"2%\" bgcolor=\"#F2F2F7\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td></tr></table></td><td bgcolor=\"#8F8FAB\" width=\"1\" height=\"70\"><img src=\"images/verticalbar.gif\" width=\"1\" height=\"25\"></td></tr><tr><td width=\"100%\" colspan=\"3\" bgcolor=\"#8F8FAB\"><img src=\"images/spacer.gif\" width=\"25\" height=\"1\"></td></tr></table><br>";
		print "<table width=\"100%\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\"><tr><td align=\"center\" valign=\"middle\" height=\"45\" width=\"100%\"><input type=\"button\" value=\"Re-try This Import\" class=\"inputbut\" onClick=\"javascript:questionEm();\"></td></tr></table><br>";
		print "<script language=\"Javascript\">
<!--
function questionEm() {
var agree=confirm(\"This action will re-post the same you just imported. Before re-posting it is suggested you clear all the dependencies listed. \\n\\nAre you sure you want to continue?\\n\\n\");
if (agree)
location.reload();
else
nogo=1;
}
//-->
</script>";

	## stop process
	exit;
	}

	## ----------------->>> IF PRODUCTS BEING UPDATED
	if (@Updates) {
		print "<table width=\"95%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" align=\"center\"><tr><td width=\"348\" colspan=\"3\" bgcolor=\"#8F8FAB\"><img src=\"images/spacer.gif\" width=\"25\" height=\"1\"></td></tr><tr><td bgcolor=\"#8F8FAB\" width=\"1\" height=\"80\"><img src=\"images/verticalbar.gif\" width=\"1\" height=\"25\"></td><td width=\"100%\" valign=\"top\"><table border=\"0\" cellspacing=\"0\" cellpadding=\"0\" width=\"100%\"><tr><td width=\"2%\" height=\"15\" bgcolor=\"#8F8FAB\">&nbsp;</td><td height=\"20\" bgcolor=\"#8F8FAB\" width=\"96%\" colspan=\"2\" align=\"center\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#FFFFFF\"><b>Products Updated Successfully</b></font></td><td width=\"2%\" height=\"15\" bgcolor=\"#8F8FAB\">&nbsp;</td></tr>";
		print "<tr><td colspan=\"4\" height=\"1\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"1\"></td></tr><tr><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td><td height=\"20\" align=\"left\" colspan=\"2\" bgcolor=\"#F2F2F7\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#333366\"><b><center><br>The following products have been successfully updated with your new data:</center></b><br></font></td><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td></tr>";
		print "<tr><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td><td align=\"center\" width=\"96%\" colspan=\"2\">";
		print "<table width=\"100%\" cellpadding=\"3\" cellspacing=\"1\" border=\"1\" bordercolor=\"#8F8FAB\"><tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>CmPartNum</b></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><b>MfgPartNum</b></b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Type</b></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Pricing Class</b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Weight</b></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b>Cost</b></font></td><td width=\"5%\" align=\"left\"><font class=\"btext3\"><b>IngramPart</b></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><b><u>Action</u></b></font></td></tr>";
		foreach $Update (@Updates) {
			@splitUpd = split(/-----/, $Update);

			$UpCM = $splitUpd[0];
			$UpMFG = $splitUpd[1];
			$UpMFGCode = $splitUpd[2];
			$UpPClass = $splitUpd[3];
			$UpIName = $splitUpd[4];
			$UpWeight = $splitUpd[5];
			$UpCost = $splitUpd[6];
			$UpIngram = $splitUpd[7];
			$UpAction = $splitUpd[8];
			$UpPType = $splitUpd[9];
			$UpSear = $splitUpd[10];
			
			my $sth = $dbh->prepare("UPDATE LOW_PRIORITY Products 
							 SET MFGCode='$UpMFGCode', 
							 MFGPartNum='$UpMFG', 
							 PricingClass='$UpPClass', 
							 ItemName='$UpIName', 
							 Cost='$UpCost', 
							 Weight='$UpWeight', 
							 ModifiedBy='$ActionUser', 
							 ModifiedOn=Null, 
							 IngramPartNum='$UpIngram', 
							 ProductType='$UpPType', 
							 Searchable='$UpSear' 
							 WHERE CMPartNum='$UpCM'");
			$sth->execute or die "Unable to execute query\n"; 
			$sth->finish; 

        	print "<tr><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitUpd[0]</nobr></font></td><td width=\"15%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitUpd[1]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitUpd[3]</nobr></font></td><td width=\"35%\" align=\"left\" valign=\"top\"><font class=\"btext3\">$splitUpd[9]</font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitUpd[5]</nobr></font></td><td width=\"10%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitUpd[6]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitUpd[7]</nobr></font></td><td width=\"5%\" align=\"left\" valign=\"top\"><font class=\"btext3\"><nobr>$splitUpd[8]</nobr></font></td></tr>";
		}
		print "</table></td><td width=\"2%\" bgcolor=\"#F2F2F7\">&nbsp;</td></tr><tr><td width=\"2%\" bgcolor=\"#F2F2F7\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td><td height=\"15\" align=\"center\" width=\"96%\" valign=\"top\" bgcolor=\"#F2F2F7\" colspan=\"2\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td><td width=\"2%\" bgcolor=\"#F2F2F7\"><img src=\"images/verticalbar.gif\" width=\"15\" height=\"15\"></td></tr></table></td><td bgcolor=\"#8F8FAB\" width=\"1\" height=\"70\"><img src=\"images/verticalbar.gif\" width=\"1\" height=\"25\"></td></tr><tr><td width=\"100%\" colspan=\"3\" bgcolor=\"#8F8FAB\"><img src=\"images/spacer.gif\" width=\"25\" height=\"1\"></td></tr></table><br>";
	}
	
	$dbh->disconnect;

## BOTTOM OF DOCUMENT
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
        
      </td>
  </tr>
</table>
</body>
</html>

EOF
}
	
## STOP PROCESS
exit;
}

## ------------->>> If no resident form processing calls are given continue
elsif ($FORM{'enformthee'}) {

{
print <<EOF

<html>
<head>
<title>Add User Account</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<script language="Javascript">
function checkPort() {
var missingdrop = "";
var thefirst = "";

if (document.IPorter.leData.value == "" || document.IPorter.leData.value == " ") {
    missingdrop += "\\n     - You must type drop in some valid data...";
	thefirst = "leData";
}

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    missingdrop ="___________________________________________                   \\n\\n" + "  Sorry, I cannot process your request because the\\n  following fields are either blank or filled incorrectly:\\n" + "___________________________________________                   \\n\\n" +
    missingdrop + "\\n\\n___________________________________________                   " + "\\n\\n   To continue, check fields and submit form again!" + "\\n___________________________________________";
    alert(missingdrop);
	document.IPorter[thefirst].focus();
    return false;
} 
else {
return true;
}
}


</script>
</head>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
$MenuConfig



$MenuConstructor
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%" valign="top"><img src="images/illus_main.jpg" width="250" height="100"></td>
    <td width="25%">&nbsp;</td>
    <td align="left" valign="top"><img src="images/title_main.jpg" width="300" height="100"></td>
  </tr>
</table>
<form method="post" action="$script" name="IPorter" onSubmit="return checkPort();">
  <table width="100%" border="0" cellpadding="0" cellspacing="0">
    <tr valign="top"> 
    <td width="20%">$legal</td>
      <td align="center" width="80%"> 
        <table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
            <td width="90%"><font face="verdana,arial,helvetica" size="2" color="#333366"><b>Import Product Data ( !!Caution - Read Instructions Carefully!! )</b></font></td>
            <td align="right" width="10%">&nbsp;</td>
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
                        <td width="100%" align="center" height="25" bgcolor="#F2F2F7" class="tableBG" colspan="2"><font face="verdana,arial,helvetica" size="2" color="#333366"><b>!! CAUTION LIVE DATA !! - Shark Tank Inventory - !! CAUTION LIVE DATA !!</b></font></td>
                      </tr>
                      <tr> 
                        <td align="center" valign="top" colspan="2"><br>
                          <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="100%" valign="top"> 
                                <table border="0" cellspacing="0" cellpadding="0" width="100%">
                                  <tr> 
                                    <td width="2%" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB" width="96%" colspan="2" align="center"><font face="verdana,arial,helvetica" size="1" color="#EB0000">&nbsp;</font></td>
                                    <td width="2%" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="4" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="20" align="left" colspan="2" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366">
									
<br>
<b>DATA STRUCTURE FIELD NAMES:</b><br>
CmPartNum - MfgPartNum - MfgCode - PricingClass - ItemName - Weight - Cost - IngramPart - Action - ProductType - Searchable<br><br>
<center><font color="#EB0000"><b>Import Data ( !!! MUST MATCH SAMPLE DATA STRUCTURE !!! )</b></font></center></font></td>
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="65" align="center" colspan="2"> 
                                      <textarea name="leData" cols="100" class="textarea_large" rows="25">$SavedBodyText</textarea>
                                    </td>
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="2%" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="96%" valign="top" bgcolor="#F2F2F7" colspan="2"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="2%" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
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
                  <td align="center" valign="middle" height="45" width="100%" bordercolor="#333366" bgcolor="#F2F2F7"> 
                    <input type="submit" value="Save Changes" name="submit" class="inputbut">
                    <input type="reset" value="Reset Form" name="reset" class="inputbut">
                    &nbsp;</td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
        
      </td>
  </tr>
</table>

<input type="hidden" name="DROPIN" value="1">
</form>
</body>
</html>

EOF
}
exit;
}

## ------------->>> if no useful calls present frameset
else {
{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - Shark Tank Admin System - Add Product ($ProductType)</title>
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
