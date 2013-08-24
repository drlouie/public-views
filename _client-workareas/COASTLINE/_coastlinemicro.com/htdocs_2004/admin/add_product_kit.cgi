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
if (($FORM{'CMPartNum'}) && ($FORM{'ItemName'})) { 

## top HTML
&topper;

	## Crumble Form Input to Variables
	my $CMPartNum = "$FORM{'CMPartNum'}";
	my $ItemName = "$FORM{'ItemName'}";
	my $PricingClass = "$FORM{'PricingClass'}";
	my $ActionUser = "$Cookies{'Username'}";

	## Start User Account Check, make sure no dupes are made
	use DBI;
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("SELECT * FROM Products");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		my $SavedCMPartNum = $row[1];
				
## ------------->>> IF EXISTS DIE
		if ($SavedCMPartNum eq "$CMPartNum") {
			if ($SavedCMPartNum eq "$CMPartNum") { $CMPartNum = "<font color=\"red\">$CMPartNum</font>"}
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
<td><font class=\"stextbig\" width=\"15%\"><b>$CMPartNum&nbsp;</b></font></td>
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
## ----------------------->>> FIRST ADD NEW KIT TO KITS TABLE
my $sth = $dbh->prepare("INSERT INTO Kits (KitID, Parent, 
						 Part1Name, Part1Number, Part1Count, Part1Type,	
						 Part2Name, Part2Number, Part2Count, Part2Type,	
						 Part3Name, Part3Number, Part3Count, Part3Type,	
						 Part4Name, Part4Number, Part4Count, Part4Type, 
						 Part5Name, Part5Number, Part5Count, Part5Type, 
						 Part6Name, Part6Number, Part6Count, Part6Type, 
						 Part7Name, Part7Number, Part7Count, Part7Type, 
						 Part8Name, Part8Number, Part8Count, Part8Type, 
   						 Part9Name, Part9Number, Part9Count, Part9Type, 
   						 Part10Name, Part10Number, Part10Count, Part10Type, 
						 Part11Name, Part11Number, Part11Count, Part11Type, 
						 Part12Name, Part12Number, Part12Count, Part12Type, 
						 Part13Name, Part13Number, Part13Count, Part13Type, 
						 Part14Name, Part14Number, Part14Count, Part14Type, 
						 Part15Name, Part15Number, Part15Count, Part15Type, 
						 AddedBy, AddedOn, ModifiedBy, ModifiedOn)
					 
						 VALUES (Null, '$CMPartNum', Null, Null, Null, Null, 
						 Null, Null, Null, Null, Null, Null, Null, Null, 
						 Null, Null, Null, Null, Null, Null, Null, Null, 
						 Null, Null, Null, Null, Null, Null, Null, Null, 
						 Null, Null, Null, Null, Null, Null, Null, Null, 
						 Null, Null, Null, Null, Null, Null, Null, Null, 
						 Null, Null, Null, Null, Null, Null, Null, Null, 
						 Null, Null, Null, Null, Null, Null, Null, Null, 
						 '$ActionUser', Null, '', '')");
$sth->execute or die "Unable to execute query\n"; 

## ----------------------->>> GET THE RECORD-ID FOR THIS NEW Kit
my $sth = $dbh->prepare("SELECT * FROM Kits WHERE Parent='$CMPartNum'");
$sth->execute or die "Unable to execute query\n"; 
my @row;
while(@row = $sth->fetchrow_array) { $MIOKitID = $row[0]; }
$sth->execute or die "Unable to execute query\n"; 
$sth->finish; 

	
## ----------------------->>> SAVE THE FORM INPUT FOR TO A NEW RECORD IN SHIPDESTS
my $sth = $dbh->prepare("INSERT INTO Products (ProductID, CMPartNum, 
						 SYSCode, KITCode, MediaCode, DISTCode, MFGCode, MFGPartNum, 
						 MFGProdURL, MFGDriverURL, PricingClass, ItemName, Description, 
						 TechSpecs, Keywords, SneakPeak, Emblem, SmallPhoto, LargePhoto, 
						 Warranty, Weight, Cost, CompPrice, RelatedProd, Accessories, 
						 AddedBy, AddedOn, ModifiedBy, ModifiedOn, IngramPartNum, 
						 TechDataPartNum, SynnexPartNum)
					 
						 VALUES (Null, '$CMPartNum', Null, '$MIOKitID', Null, Null, Null, 
						 Null, Null, Null, '$PricingClass', '$ItemName', 
						 Null, Null, Null, Null, Null, Null, Null, Null, Null, 
						 Null, Null, Null, Null, '$ActionUser', Null, '', '', '', 
						 '', '')");
$sth->execute or die "Unable to execute query\n"; 
$sth->finish; 
## ----------------------->>> PRINT GOODONE HTML
print "<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"5\"><tr><td width=\"100%\"><font face=\"verdana,arial,helvetica\" size=\"1\" color=\"#333366\"><b>New Shipping Location Saved</b><br>The kit was added to the system successfully. Now you must continue with the kit configuration process by clicking the button below<br><br><center><form><input type=\"button\" value=\"Continue Process\" onClick=\"javascript:location.href='change_product_kit.cgi?CMPartNum=$CMPartNum&PricingClass=$PricingClass'\" class=\"inputbut\"></form></center><br></font>";
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
<title>Coastline Micro, Inc. - Shark Tank Admin System - Inventory ( Kits )</title>
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
var formindex = document.add.PricingClass.selectedIndex;
var thisone = document.add.PricingClass.options[formindex].value;

// Check Common form fields
if (thisone == "BIGNULL") {
    missingdrop += "\\n     - That is an invalid option for Pricing Class...";
	thefirst = "PricingClass";
}

if (document.add.ItemName.value == "" || document.add.ItemName.value == " ") {
    missingdrop += "\\n     - Product Name";
	if (thefirst == "") { thefirst = "ItemName"; }
}

if ((document.add.CMPartNum.value == "") || (document.add.CMPartNum.value == " ")) {
    missingdrop += "\\n     - Coastline Micro Part Number";
	if (thefirst == "") { thefirst = "CMPartNum"; }
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Pricing 
                                      Class</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="65" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366">This 
                                      kit must have a pricing class assciated 
                                      wit it in order to calculate pricing for 
                                      the customer. Please make sure you consult 
                                      with your manager to see which class your 
                                      product should be set as.</font></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"> 
                                      <select name="PricingClass" class="inputtext">
<option value="BIGNULL" SELECTED>:::::  Configurables  :::::</option>
<option value="Desktop">Desktop PC</option>
<option value="Server">Server</option>
<option value="Notebook">Notebook</option>
<option value="BIGNULL"> </option>
<option value="BIGNULL">:::::    Components   :::::</option>
<option value="Monitor">Monitor</option>
<option value="Memory">Memory</option>
<option value="HardDrive">Hard Drive</option>
<option value="VideoCard">Video Card</option>
<option value="Peripheral">Peripheral</option>
<option value="Printer">Printer</option>
<option value="Software">Software</option>
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
                                      in this product's advertised name. You can 
                                      beef up a name with a description using 
                                      size, speed and other technical factor's 
                                      of a product's performance and design.<br>
                                      <br>
                                      <center>
                                        <font color="#EB0000">Example: <i>CM Mega 
                                        3D Action Pack A / V</i></font> 
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
                                            <input type="text" name="CMPartNum" size="15" class="inputtext15">
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
<title>Coastline Micro, Inc. - Shark Tank Admin System - Inventory ( Kits )</title>
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
<title>Coastline Micro, Inc. - Shark Tank Admin System - Inventory ( Kits )</title>
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