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

## get legal piece
$legal = `cat legal.nsf`;

## If data present scan it...
if (($FORM{'InternalPartNum'}) && ($FORM{'MFGPartNum'}) && ($FORM{'ItemName'}) && ($FORM{'Cost'})) { 

## top HTML
&topper;

	## Crumble Form Input to Variables
	my $InternalPartNum = "$FORM{'InternalPartNum'}";
	my $MFGPartNum = "$FORM{'MFGPartNum'}";
	my $IngramPartNum = "$FORM{'IngramPartNum'}";
	my $TechDataPartNum = "$FORM{'TechDataPartNum'}";
	my $SynnexPartNum = "$FORM{'SynnexPartNum'}";
	my $ItemName = "$FORM{'ItemName'}";
	my $PricingClass = "$FORM{'ProdClass'}";
	my $Weight = "$FORM{'Weight'}";
	my $Cost = "$FORM{'Cost'}";
	my $ActionUser = "$Cookies{'Username'}";
	my $ProductType = $PricingClass;
	
	## Start User Account Check, make sure no dupes are made
	use DBI;
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("SELECT * FROM Products");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		my $SavedInternalPartNum = $row[1];
		my $SavedMFGPartNum = $row[7];
		my $SavedIngramPartNum = $row[29];
		my $SavedTechDataPartNum = $row[30];
		my $SavedSynnexPartNum = $row[31];
				
## ------------->>> IF EXISTS DIE
		if (($SavedInternalPartNum eq "$InternalPartNum") || ($SavedMFGPartNum eq "$MFGPartNum")) {
			if ($SavedInternalPartNum eq "$InternalPartNum") { $InternalPartNum = "<font color=\"red\">$InternalPartNum</font>"}
			if ($SavedMFGPartNum eq "$MFGPartNum") { $MFGPartNum = "<font color=\"red\">$MFGPartNum</font>"}
			if ($SavedIngramPartNum eq "$IngramPartNum") { $IngramPartNum = "<font color=\"red\">$IngramPartNum</font>"}
			if ($SavedTechDataPartNum eq "$TechDataPartNum") { $TechDataPartNum = "<font color=\"red\">$TechDataPartNum</font>"}
			if ($SavedSynnexPartNum eq "$SynnexPartNum") { $SynnexPartNum = "<font color=\"red\">$SynnexPartNum</font>"}
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
<td align="center" width="15%"><font class="sresults1"><b>Part #</b><br></font></td>
<td align="center" width="20%"><font class="sresults1"><b>MFG #</b></font></td>
<td align="center" width="25%"><font class="sresults1"><b>Ingram #</b></font></td>
<td align="center" width="25%"><font class="sresults1"><b>TechData #</b></font></td>
<td align="center" width="15%"><font class="sresults1"><b>Synnex #</b></font></td>
</tr>
<tr width=\"100%\">
<td><font class=\"stextbig\" width=\"15%\"><b>$InternalPartNum&nbsp;</b></font></td>
<td><font class=\"stextbig\" width=\"20%\">$MFGPartNum&nbsp;</font></td>
<td><font class=\"stextbig\" width=\"25%\">$IngramPartNum&nbsp;</font></td>
<td><font class=\"stextbig\" width=\"25%\">$TechDataPartNum&nbsp;</font></td>
<td><font class=\"stextbig\" width=\"15%\">$SynnexPartNum&nbsp;</font></td>
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
			$dbh->disconnect;
			exit;
		}
	}
	$sth->finish;

## ------------->>> ELSE SAVE NEW USER DATA
print "<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"5\"><tr><td width=\"100%\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#333366\"><b>New Shipping Location Saved</b><br>The product was added to the system successfully. Now you must continue with the product configuration process by clicking the button below<br><br><center><form><input type=\"button\" value=\"Continue Process\" onClick=\"javascript:location.href='change_product_common.cgi?InternalPartNum=$InternalPartNum&MFGPartNum=$MFGPartNum'\" class=\"inputbut\"></form></center><br></font>";

	my $sth = $dbh->prepare("SELECT * FROM SystemComponents WHERE ComponentName='$ProductType' ORDER BY ComponentName ASC");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$CID = $row[0];
	}
	$sth->finish;
## ----------------------->>> SAVE THE FORM INPUT FOR TO A NEW RECORD IN SHIPDESTS
my $sth = $dbh->prepare("INSERT INTO Products (ProductID, InternalPartNum, 
						 SYSCode, KITCode, MediaCode, DISTCode, MFGCode, MFGPartNum, 
						 MFGProdURL, MFGDriverURL, PricingClass, ItemName, Description, 
						 TechSpecs, Keywords, SneakPeak, Emblem, SmallPhoto, LargePhoto, 
						 Warranty, Weight, Cost, CompPrice, RelatedProd, Accessories, 
						 AddedBy, AddedOn, ModifiedBy, ModifiedOn, IngramPartNum, 
						 TechDataPartNum, SynnexPartNum, ComponentBriefing, Searchable)
					 
						 VALUES (Null, '$InternalPartNum', Null, Null, Null, Null, Null, 
						 '$MFGPartNum', Null, Null, '$CID', '$ItemName', 
						 Null, Null, Null, Null, Null, Null, Null, Null, '$Weight', 
						 '$Cost', Null, Null, Null, '$ActionUser', Null, '', '', '', 
						 '', '', '', '')");
$sth->execute or die "Unable to execute query\n"; 
$sth->finish; 
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

	$ProductType = "$FORM{'ProductType'}";



{
print <<EOF

<html>
<head>
<title>Shark Tank Admin System - Shipping Locations</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<script language="Javascript">
// FORM CHECKER FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function checkForm() {
var missingdrop = "";
var thefirst = "";

// Check Common form fields
if (document.add.ItemName.value == "" || document.add.ItemName.value == " ") {
    missingdrop += "\\n     - Product Name";
	thefirst = "ItemName";
}

if (isNaN(document.add.Weight.value) || (document.add.Weight.value == "") || (document.add.Weight.value == " ") || (document.add.Weight.value.length < 0)) {
    missingdrop += "\\n     - Weight";
	if (thefirst == "") { thefirst = "Weight"; }
}

if (isNaN(document.add.Cost.value) || (document.add.Cost.value == "") || (document.add.Weight.value == " ") || (document.add.Cost.value.length < 0)) {
    missingdrop += "\\n     - Cost";
	if (thefirst == "") { thefirst = "Weight"; }
}

if ((document.add.InternalPartNum.value == "") || (document.add.InternalPartNum.value == " ")) {
    missingdrop += "\\n     - Part Number";
	if (thefirst == "") { thefirst = "InternalPartNum"; }
}

if ((document.add.MFGPartNum.value == "") || (document.add.MFGPartNum.value == " ")) {
    missingdrop += "\\n     - Manufactuer's Part Number";
	if (thefirst == "") { thefirst = "MFGPartNum"; }
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
<table width="100%" border="0" height="100%" cellpadding="0" cellspacing="0">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Pricing Class</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="65" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366">This 
                                      is the pricing class for the product you have chosen to 
                                      add to the system's inventory. If this incorrect 
                                      please stop now and choose the right product 
                                      type by using the DHTML menu: Product Inventory 
                                      -&gt; View/Add/Update Inventory</font></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"><font face="verdana,arial,helvetica" size="1" color="#EB0000">$ProductType</font> 
                                      <input type="hidden" name="ProdClass" value="$ProductType">
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
                                    <td height="75" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366">Type 
                                      in this product's actual box/advertised 
                                      name. You can beef up a description using 
                                      size, speed and other technical factor's 
                                      of a product's performance and design.<br>
                                      <br>
                                      <center>
                                        <font color="#EB0000">Example: <i>NEC 18.1 Inch MultiSync Monitor - White</i></font> 
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Weight</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="25" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"> 
                                      <center>
                                        <font color="#EB0000">Example: <i>23.6</i></font> 
                                      </center>
                                      </font></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"> 
                                      <input type="text" name="Weight" size="7" class="inputtext7">
                                      Lbs.</font></td>
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Cost</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="25" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"> 
                                      <center>
                                        <font color="#EB0000">Example: <i>596.65</i></font> 
                                      </center>
                                      </font></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"> 
                                      \$
                                      <input type="text" name="Cost" size="7" class="inputtext7">
                                      US Dlls.</font></td>
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
                                      Part Numbers</font></b><font color="#FFFFFF"> 
                                      (CLM / MFG / DIST)</font></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="155" bgcolor="#F2F2F7" width="318"><font face="verdana,arial,helvetica" size="1" color="#333366">In 
                                      order to add a product to the system you 
                                      MUST have the Internal and MFG part numbers at 
                                      the very least. With that much data at hand 
                                      you can successfully add a product to the 
                                      system. Yet, if you want your product listing 
                                      to be searchable using the distributor's 
                                      part number, then you must type in those 
                                      numbers.<br>
                                      <br>
                                      Please make sure you have the correct part 
                                      number for the product you are attempting 
                                      to add to the system. If you add an incorrect 
                                      part number and built upon that number, 
                                      especially the Internal Part Number, you could 
                                      easily cause system errors in the future.</font></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td align="center" valign="middle" width="318"> 
                                      <table width="270" border="0" cellspacing="0" cellpadding="0" align="center">
                                        <tr> 
                                          <td width="270" height="25" align="center" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Internal Part #</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="270" height="35" valign="middle" align="center"> 
                                            <input type="text" name="InternalPartNum" size="15" class="inputtext15">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="270" height="25" align="center" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>MFG 
                                            Part #</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="270" height="35" valign="middle" align="center"> 
                                            <input type="text" name="MFGPartNum" size="15" class="inputtext15">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="270" height="25" align="center" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Ingram 
                                            Micro Part #</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="270" height="35" valign="middle" align="center"> 
                                            <input type="text" name="IngramPartNum" size="15" class="inputtext15">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="270" height="25" align="center" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Tech 
                                            Data Part #</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="318" height="35" valign="middle" align="center"> 
                                            <input type="text" name="TechDataPartNum" size="15" class="inputtext15">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="270" height="25" align="center" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Synnex 
                                            Part #</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="270" height="35" valign="middle" align="center"> 
                                            <input type="text" name="SynnexPartNum" size="15" class="inputtext15">
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
<title>Shark Tank Admin System - Add Product ($ProductType)</title>
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
<title>Shark Tank Admin System - Shipping Locations</title>
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