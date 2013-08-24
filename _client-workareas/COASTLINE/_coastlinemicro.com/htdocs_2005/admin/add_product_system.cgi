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
if (($Cookies{'UserType'} eq "COManage") || ($Cookies{'UserType'} eq "WEBAdmin") || ($Cookies{'UserType'} eq "COSales") || ($Cookies{'ExtraAccess'} =~ "AdminUser")) { $nextone = "1"; }
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
if (($FORM{'InternalPartNum'}) && ($FORM{'SystemSeries'})) { 

## top HTML
&topper;

	## Crumble Form Input to Variables
	$InternalPartNum = "$FORM{'InternalPartNum'}";
	$ItemName = "$FORM{'ItemName'}";
	$SystemSeries = "$FORM{'SystemSeries'}";
	
	## ------------->> Construct Product Name
	if ($SystemSeries eq "GreatWhite") { $LeSeries = "Great White Series&#153; Xeon&#153; Server"; }
	elsif ($SystemSeries eq "Mako") { $LeSeries = "Mako Series&#153; Performance Desktop PC"; }
	elsif ($SystemSeries eq "Reef") { $LeSeries = "Reef Series&#153; Notebook"; }
	elsif ($SystemSeries eq "Thresher") { $LeSeries = "Thresher Series&#153; Value Desktop PC"; }
	else { $LeSeries = "Tiger Series&#153; PIII Server"; }
	if ($ItemName eq "" || $ItemName eq " ") { $SYSName = "$LeSeries - Model $InternalPartNum"; }
	else { $SYSName = "$LeSeries - Model $InternalPartNum - $ItemName"; }

	$Reconfig = "$FORM{'Reconfig'}";
	$PricingClass = "$FORM{'PricingClass'}";
	$ActionUser = "$Cookies{'Username'}";

	## Start Account Check, make sure no dupes are made
	use DBI;
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("SELECT * FROM Products");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		my $SavedInternalPartNum = $row[1];
				
## ------------->>> IF EXISTS DIE
		if ($SavedInternalPartNum eq "$InternalPartNum") {
			if ($SavedInternalPartNum eq "$InternalPartNum") { $InternalPartNum = "<font color=\"red\">$InternalPartNum</font>"}
{
print <<EOF

                  <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr> 
                      <td width="100%"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Error Description</b><br>
                        While trying to complete your addition request we found 
                        an inventory item that mathces the information you are 
                        submitting. Following is the record that matches your 
                        request's parameters: </font><font face="verdana,arial,helvetica" size="1" color="#333366"><br>
                        <br>
                        <center><font color="#EB0000">*The red text denotes the item's 
                        matching field(s).</font></center>
                        </font><br>
                        <table width="100%" border="1" bordercolor="#333366" cellspacing="0" cellpadding="0" align="center" bgcolor="#F2F2F7">
						<tr><td width="100%">
                        <table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                          <tr> 
                            <td width="35%" height="20"><font class="stextbig"><b>Matching Inventory Item(s)</b></font></td>
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
							
<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
<tr width="100%"><td width="100%">
<table width="100%" height="35" border="1" bordercolor="#333366" cellspacing="1" cellpadding="3" align="center" bgcolor="#ffffff">
<tr height="20" width="100%" bgcolor="#F2F2F7">
<td align="center" width="15%"><font class="sresults1"><b>CM #</b><br></font></td>
</tr>
<tr width=\"100%\">
<td><font class=\"stextbig\" width=\"15%\"><b>$InternalPartNum&nbsp;</b></font></td>
</tr>
</table>
<br><center><form><input type=\"button\" value=\"Try Again\" onClick=\"javascript:history.go(-1)\" class=\"inputbut\"></form></center>

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
			
			## BOTTOM HTML TEMPLATE
			&bottom;

			$sth->finish;
			exit;
		}
	}
	$sth->finish;

## ------------->>> ELSE SAVE NEW USER DATA
## ----------------------->>> FIRST ADD NEW KIT TO KITS TABLE
my $sth = $dbh->prepare("INSERT INTO Systems (SystemID, Parent, SeriesType, Reconfig, 
						 MainCategory, MainType, MainCharacter, MainParts, 
						 Sub1Category, Sub1Type, Sub1Character, Sub1Parts, 
						 Sub2Category, Sub2Type, Sub2Character, Sub2Parts, 
   						 Sub3Category, Sub3Type, Sub3Character, Sub3Parts, 
						 Sub4Category, Sub4Type, Sub4Character, Sub4Parts, 
						 Sub5Category, Sub5Type, Sub5Character, Sub5Parts, 
						 Sub6Category, Sub6Type, Sub6Character, Sub6Parts, 
						 Sub7Category, Sub7Type, Sub7Character, Sub7Parts, 
						 Sub8Category, Sub8Type, Sub8Character, Sub8Parts, 
						 Sub9Category, Sub9Type, Sub9Character, Sub9Parts, 
						 Sub10Category, Sub10Type, Sub10Character, Sub10Parts, 
						 Sub11Category, Sub11Type, Sub11Character, Sub11Parts, 
						 Sub12Category, Sub12Type, Sub12Character, Sub12Parts, 
						 Sub13Category, Sub13Type, Sub13Character, Sub13Parts, 
						 Sub14Category, Sub14Type, Sub14Character, Sub14Parts, 
						 Sub15Category, Sub15Type, Sub15Character, Sub15Parts, 
						 Sub16Category, Sub16Type, Sub16Character, Sub16Parts, 
						 Sub17Category, Sub17Type, Sub17Character, Sub17Parts, 
						 Sub18Category, Sub18Type, Sub18Character, Sub18Parts, 
						 Sub19Category, Sub19Type, Sub19Character, Sub19Parts, 
						 Sub20Category, Sub20Type, Sub20Character, Sub20Parts, 
						 Sub21Category, Sub21Type, Sub21Character, Sub21Parts, 
						 Sub22Category, Sub22Type, Sub22Character, Sub22Parts, 
						 Sub23Category, Sub23Type, Sub23Character, Sub23Parts, 
						 Sub24Category, Sub24Type, Sub24Character, Sub24Parts, 
						 Sub25Category, Sub25Type, Sub25Character, Sub25Parts, 
						 AddedBy, AddedOn, ModifiedBy, ModifiedOn)
					 
						 VALUES (Null, '$InternalPartNum', '$SystemSeries', '$Reconfig', 
						 Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, 
						 Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, 
						 Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, 
						 Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, 
						 Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, 
						 Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, 
						 Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, 
						 Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, 
						 Null, Null, Null, Null, Null, Null, Null, Null, 
						 '$ActionUser', Null, '', '')");
$sth->execute or die "Unable to execute query\n"; 

## ----------------------->>> GET THE RECORD-ID FOR THIS NEW Kit
my $sth = $dbh->prepare("SELECT * FROM Systems WHERE Parent='$InternalPartNum'");
$sth->execute or die "Unable to execute query\n"; 
my @row;
while(@row = $sth->fetchrow_array) { $MIOSystemID = $row[0]; }
$sth->execute or die "Unable to execute query\n"; 
$sth->finish; 

	
## ----------------------->>> SAVE THE FORM INPUT FOR TO A NEW RECORD IN SHIPDESTS
my $sth = $dbh->prepare("INSERT INTO Products (ProductID, InternalPartNum, 
						 SYSCode, KITCode, MediaCode, DISTCode, MFGCode, MFGPartNum, 
						 MFGProdURL, MFGDriverURL, PricingClass, ItemName, Description, 
						 TechSpecs, Keywords, SneakPeak, Emblem, SmallPhoto, LargePhoto, 
						 Warranty, Weight, Cost, CompPrice, RelatedProd, Accessories, 
						 AddedBy, AddedOn, ModifiedBy, ModifiedOn, IngramPartNum, 
						 TechDataPartNum, SynnexPartNum, ComponentBriefing, Searchable)
					 
						 VALUES (Null, '$InternalPartNum', '$MIOSystemID', Null, Null, Null, Null, 
						 Null, Null, Null, '$PricingClass', '$SYSName', 
						 Null, Null, Null, Null, Null, Null, Null, Null, Null, 
						 Null, Null, Null, Null, '$ActionUser', Null, '', '', '', 
						 '', '', '', '')");
$sth->execute or die "Unable to execute query\n"; 
$sth->finish; 
## ----------------------->>> PRINT GOODONE HTML
print "<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"5\"><tr><td width=\"100%\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#333366\"><b>New $PricingClass Saved</b><br>The $PricingClass was added to the system successfully. Now you must continue with the system configuration process by clicking the button below<br><br><center><form><input type=\"button\" value=\"Continue Process\" onClick=\"javascript:location.href='change_product_system.cgi?InternalPartNum=$InternalPartNum&PricingClass=$PricingClass'\" class=\"inputbut\"></form></center><br></font>";
$dbh->disconnect;
	
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
EOF
}
	
## TOP HTML TEMPLATE
&bottom;
	
exit;
}

## ------------->>> If no resident form processing calls are given continue
elsif (($FORM{'enformthee'}) && ($FORM{'ProductType'})) {

my $ProductType = "$FORM{'ProductType'}";

{
print <<EOF

<html>
<head>
<title>Shark Tank Admin System - Inventory ( Computer Systems )</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<script language="Javascript" src="js/mousetable.js"></script>
<script language="Javascript">
// FORM CHECKER FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function checkForm() {
var missingdrop = "";
var thefirst = "";
var formindex = document.add.SystemSeries.selectedIndex;
var thisone = document.add.SystemSeries.options[formindex].value;

// Check Common form fields
if (thisone == "BIGNULL") {
    missingdrop += "\\n     - That is an invalid option for the System Series...";
	thefirst = "SystemSeries";
}

if ((document.add.InternalPartNum.value == "") || (document.add.InternalPartNum.value == " ")) {
    missingdrop += "\\n     - Part Number";
	if (thefirst == "") { thefirst = "InternalPartNum"; }
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
</SCRIPT>
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
  <table width="100%" border="0" cellpadding="0" cellspacing="0">
    <tr valign="top"> 
    <td width="20%">$legal</td>
    <td align="center" width="80%"> 
      <table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
            <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>Add 
              Product ($ProductType)</b></font></td>
          <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
              <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
                <tr bordercolor="#333366"> 
                  <td width="100%" align="center" valign="top" height="250"> 
                    <table width="100%" border="0" cellspacing="0" cellpadding="5">
                      <tr valign="top" align="center"> 
                        <td bordercolor="#333366" class="tableBORDER"> <br>
                          <table width="300" border="0" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="270" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="270" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">System Series</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="115" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366">Every configured system must have a system series associated with it. Below you will see the type of computer system you are attempting to add. If this is a Desktop PC or a Server you are attempting to add please make sure you select the correct series from the list. Notebooks will have this information automatically preset for you.</font></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                        <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                          <td width="270" height="25" align="center" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>CM Shark Series</b></font></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                        </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"><input type="hidden" name="PricingClass" value="$ProductType">
EOF
}

if ($ProductType eq "Desktop") {
	print "<select name=\"SystemSeries\" class=\"inputtext\">";
	print "<option value=\"BIGNULL\" SELECTED>Select One...</option>";
	print "<option value=\"Thresher\">Thresher Series&#153; Value Desktop PC</option>";
	print "<option value=\"Mako\">Mako Series&#153; Performance Desktop PC</option>";
	print "</select>";
}
elsif ($ProductType eq "Server") {
	print "<select name=\"SystemSeries\" class=\"inputtext\">";
	print "<option value=\"BIGNULL\" SELECTED>Select One...</option>";
	print "<option value=\"GreatWhite\">Great White Series&#153; Xeon&#153; Server</option>";
	print "<option value=\"Tiger\">Tiger Series&#153; PIII Server</option>";
	print "</select>";
}
else {
	print "<input type=\"hidden\" name=\"SystemSeries\" value=\"Reef\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#EB0000\">Reef Series&#153; Notebook</font>";
}

{
print <<EOF
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
                          <table width="300" border="0" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="270" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="270" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Product 
                                      Name</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="130" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366">You don't necessarily have to type a configured systems advertised name since the name is mostly derrived from the CM Part Number. But if you want to extend the name you can 
                                      do so by beefing up a name with a description using 
                                      size, speed and other technical factor's 
                                      of the systems performance and design.<br>
                                      <br>
                                      <center>
                                        <font color="#EB0000">Example: <i>3D Gaming Center</i></font> 
                                      </center>
                                      </font></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"> 
                                      <input type="text" name="ItemName" size="15" class="inputtext15">
                                      </font></td>
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
                        <td> <br>
                          <table width="300" border="0" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="270" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="270" valign="top"> 
                                <table width="270" border="0" cellspacing="0" cellpadding="0" align="center">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" width="318" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Product 
                                      Part Number</font></b><font color="#FFFFFF"> 
                                      (CLM)</font></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="115" bgcolor="#F2F2F7" width="318"><font face="verdana,arial,helvetica" size="1" color="#333366">In 
                                      order to add a product to the system you 
                                      MUST have the Coatline Micro part number.<br>
                                      <br>
                                      Please make sure you have the correct part 
                                      number for the product you are attempting 
                                      to add to the system. If you add an incorrect 
                                      part number and built upon that number you 
                                      could easily cause system errors in the 
                                      future.</font></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td align="center" valign="middle" width="318"> 
                                      <table width="270" border="0" cellspacing="0" cellpadding="0" align="center">
                                        <tr> 
                                          <td width="270" height="25" align="center" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>CM 
                                            Part Number</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="270" height="35" valign="middle" align="center"> 
                                            <input type="text" name="InternalPartNum" size="15" class="inputtext15">
                                          </td>
                                        </tr>
                                      </table>
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
                              <td bgcolor="#8F8FAB" width="1"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="270" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                          <br>
                          <table width="300" border="0" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="270" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="270" valign="top"> 
                                <table width="270" border="0" cellspacing="0" cellpadding="0" align="center">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" width="318" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Re-Configurable 
                                      System?</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="85" bgcolor="#F2F2F7" width="318"><font face="verdana,arial,helvetica" size="1" color="#333366">Every 
                                      system has the ability to be locked from 
                                      being re-configured by the user. This type 
                                      of action would be useful for Intel's Model 
                                      School Programs, QISV and any other programs 
                                      that offer lower/set prices for all products 
                                      no matter who the customer.</font></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td align="center" valign="middle" width="318"> 
                                      <table width="270" border="0" cellspacing="0" cellpadding="0" align="center">
                                        <tr> 
                                          <td width="270" height="25" align="center" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Is 
                                            System Re-Configurable?</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="270" height="35" valign="middle" align="center"> 
                                            <font face="verdana,arial,helvetica" size="1" color="#333366">Yes</font>
                                            <input type="radio" name="Reconfig" value="Y" checked>
                                            <font face="verdana,arial,helvetica" size="1" color="#333366">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No</font> 
                                            <input type="radio" name="Reconfig" value="N">
                                          </td>
                                        </tr>
                                      </table>
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
                              <td bgcolor="#8F8FAB" width="1"><img src="images/verticalbar.gif" width="1" height="25"></td>
                            </tr>
                            <tr> 
                              <td width="270" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
                <tr bordercolor="#333366" bgcolor="#F2F2F7"> 

                  <td align="center" valign="middle" height="45"> 
                    <input type="submit" value="Save Product" name="submit" class="inputbut">
                    <input type="reset" value="Reset Form" name="reset" class="inputbut">
                    &nbsp;&nbsp;</td>
                </tr>
              </table>
          </td>
        </tr>
      </table>
        <br>
    </td>
  </tr>
</table>
  <table width="100%" background="images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0">
    <tr>
      <td width="55%" align="left" height="56">&nbsp;</td>
    </tr>
  </table>
</form>
</body>
</html>

EOF
}
exit;
}

## ------------->>> if no useful calls present frameset
else {
$ProductType = "$FORM{'ProductType'}";
if (($ProductType eq "") || ($ProductType eq " ")) {
	print "Sorry, you must have a Product Type to add when you call to this script...";
	exit;
}
else {

{
print <<EOF

<html>
<head>
<title>Shark Tank Admin System - Inventory ( Computer Systems )</title>
</head>
<frameset rows="64,*" rows="*" border="0" framespacing="0"> 
<frame name="topOne" scrolling="NO" noresize src="topper.cgi" marginwidth="0" marginheight="0" frameborder="NO">
<frame name="botOne" src="$script?enformthee=1&ProductType=$ProductType" frameborder="NO" marginheight="0" marginwidth="0" scrolling="AUTO">
</frameset>
<noframes><body bgcolor="#FFFFFF">
</body></noframes>
</html>

EOF
}

}
exit;
}


sub topper {
{
print <<EOF

<html>
<head>
<title>Shark Tank Admin System - Inventory ( Computer Systems )</title>
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
    <td width="20%"><br>$legal</td>
    <td align="center" width="80%"> 
      <table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
              <tr bordercolor="#333366" valign="middle"> 
                <td width="100%" align="center" height="20" bgcolor="#F2F2F7" class="tableBG"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Request Response</b></font></td>
              </tr>
              <tr bordercolor="#333366"> 
                <td width="50%" align="center" valign="top" height="250"><font face="verdana,arial,helvetica" size="1" color="#333366"> 
EOF
}
}
exit;

sub bottom {
{
print <<EOF

</font>
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