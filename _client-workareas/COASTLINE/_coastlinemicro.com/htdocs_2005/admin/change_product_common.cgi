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

## If SAVING
if (($FORM{'DROPIN'}) && ($FORM{'InternalPartNum'})) {

## TOP HTML TEMPLATE
&topper;

	## Crumble Form Input to Variables
	$InternalPartNum = "$FORM{'InternalPartNum'}";
	$MediaCode = "$FORM{'Multimedia'}";
	$DISTCode = "$FORM{'DISTCode'}";
	$MFGCode = "$FORM{'MFGCode'}";
	$MFGPartNum = "$FORM{'MFGPartNum'}";
	$MFGProdURL = "$FORM{'ProdURL'}";
	$MFGDriverURL = "$FORM{'DriverURL'}";
	$PricingClass = "$FORM{'PricingClass'}";
	$ItemName = "$FORM{'ItemName'}";
	$Description = "$FORM{'Description'}";	
	$TechSpecs = "$FORM{'TechSpecs'}";
	$Keywords = "$FORM{'Keywords'}";
	$SneakPeak = "$FORM{'SneakPeak'}";
	$Emblem = "$FORM{'Emblem'}";
	$SmallLogo = "$FORM{'SmallLogo'}";
	$LargeLogo = "$FORM{'LargeLogo'}";
	$Warranty = "$FORM{'Warranty'}";
	$Cost = "$FORM{'Cost'}";
	$Weight = "$FORM{'Weight'}";
	$Cost = "$FORM{'Cost'}";
	$RelatedProd = "";
	$Accessories = "$FORM{'Accessories'}";
	$IngramPartNum = "$FORM{'IngramPartNum'}";
	$TechDataPartNum = "$FORM{'TechDataPartNum'}";
	$SynnexPartNum = "$FORM{'SynnexPartNum'}";
	$ProductType = "$FORM{'ProductType'}";
	$ComponentBriefing = "$FORM{'ComponentBriefing'}";
	$Searchable = "$FORM{'Searchable'}";
	$ActionUser = "$Cookies{'Username'}";
	
{
print <<EOF

<table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update Distributor Profile</b></font></td>
          <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
              <tr bordercolor="#333366"> 
                <td width="50%" align="center" valign="top" height="250"> 
                  <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr> 
                      <td width="100%"><font face="verdana,arial,helvetica" size="1" color="#333366">
					  
EOF
}
	print "<center><br><b>Inventory Updated</b><br><br>The the changes you have made to <b>$ItemName ($InternalPartNum)</b> have been successfully saved to the system.<br><br><form><input type=\"button\" value=\"Back to Product: $InternalPartNum\" onClick=\"javascript:location.href='change_product_common.cgi?InternalPartNum=$InternalPartNum'\" class=\"inputbut\"><br><br><input type=\"button\" value=\"View/Add/Update Inventory\" onClick=\"javascript:parent.location.href='change_product.cgi'\" class=\"inputbut\"></form><br></center>";
	print "<br><br></font>";
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("UPDATE LOW_PRIORITY Products 
							 SET MediaCode='$MediaCode', 
							 DISTCode='$DISTCode', 
							 MFGCode='$MFGCode', 
							 MFGPartNum='$MFGPartNum', 
							 MFGProdURL='$MFGProdURL', 
							 MFGDriverURL='$MFGDriverURL', 
							 PricingClass='$PricingClass', 
							 ItemName='$ItemName', 
							 Description='$Description', 
							 TechSpecs='$TechSpecs', 
							 Keywords='$Keywords', 
							 SneakPeak='$SneakPeak', 
							 Emblem='$Emblem', 
							 SmallPhoto='$SmallLogo', 
							 LargePhoto='$LargeLogo', 
							 Warranty='$Warranty', 
							 Cost='$Cost', 
							 Weight='$Weight', 
							 RelatedProd='$RelatedProd', 
							 Accessories='$Accessories', 
							 ModifiedBy='$ActionUser', 
							 ModifiedOn=Null, 
							 IngramPartNum='$IngramPartNum', 
							 TechDataPartNum='$TechDataPartNum', 
							 SynnexPartNum='$SynnexPartNum', 
							 ComponentBriefing='$ComponentBriefing', 
							 Searchable='$Searchable' 
							 WHERE InternalPartNum='$InternalPartNum'");
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish; 
	$dbh->disconnect; 	
	
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
	  
EOF
}
	
## END PAGE TEMPLATE
&bottom;

exit;
}

## If DELETING
elsif (($FORM{'DELETEIT'}) && ($FORM{'InternalPartNum'})) {

## TOP HTML TEMPLATE
&topper;

	## Crumble Form Input to Variables
	my $InternalPartNum = "$FORM{'InternalPartNum'}";
	my $ActionUser = "$Cookies{'Username'}";

{
print <<EOF

<table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update Distributor Profile</b></font></td>
          <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
              <tr bordercolor="#333366"> 
                <td width="50%" align="center" valign="top" height="250"> 
                  <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr> 
                      <td width="100%"><font face="verdana,arial,helvetica" size="1" color="#333366">
					  
EOF
}
	print "<center><br><b>Delete Product from Inventory</b><br><br>The product you chose to remove from the system was deleted. All products previously associated with this product, if any, will be updated with a similar inventory item effective immediately.<br><br><form><input type=\"button\" value=\"View/Add/Update Inventory\" onClick=\"javascript:parent.location.href='change_product.cgi'\" class=\"inputbut\"><br></center>";
	print "<br><br></font>";
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("DELETE FROM Products WHERE InternalPartNum='$InternalPartNum'");
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
	$dbh->disconnect;
	
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
	  
EOF
}
	
## END PAGE TEMPLATE
&bottom;

exit;
}

## If VIEWING
elsif ($FORM{'InternalPartNum'}) {

	## Crumble Form Input to Variables
	my $InternalPartNum = "$FORM{'InternalPartNum'}";
	my $PricingClass = "$FORM{'PricingClass'}";
	my $ActionUser = "$Cookies{'Username'}";

	##----------->>> Grab DIST Account Information
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	$count=0;
	my $sth = $dbh->prepare("SELECT * FROM Products WHERE InternalPartNum='$InternalPartNum'");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$SavedProductID = $row[0];
		$SavedInternalPartNum = $row[1];
		$SavedSYSCode = $row[2];
		$SavedKITCode = $row[3];
		$SavedMediaCode = $row[4];
		$SavedDISTCode = $row[5];
		$SavedMFGCode = $row[6];
		$SavedMFGPartNum = $row[7];
		$SavedMFGProdURL = $row[8];
		$SavedMFGDriverURL = $row[9];
		$SavedPricingClass = $row[10];
		$SavedItemName = $row[11];
		$SavedDescription = $row[12];
		$SavedTechSpecs = $row[13];
		$SavedKeywords = $row[14];
		$SavedSneakPeak = $row[15];
		$SavedEmblem = $row[16];
		$SavedSmallLogo = $row[17];
		$SavedLargeLogo = $row[18];
		$SavedWarranty = $row[19];
		$SavedWeight = $row[20];
		$SavedCost = $row[21];
		$SavedCompPrice = $row[22];
		$SavedRelatedProd = $row[23];
		$SavedAccessories = $row[24];
		$SavedAddedBy = $row[25];
		$SavedAddedOn = $row[26];
		$SavedModifiedBy = $row[27];
		$SavedModifiedOn = $row[28];
		$SavedIngramPartNum = $row[29];
		$SavedTechDataPartNum = $row[30];
		$SavedSynnexPartNum = $row[31];
		$SavedComponentBriefing = $row[32];
		$SavedSearchable = $row[33];
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

##----------->>> IF NO RECORD FOUND
if ($count eq "0") {
	&topper;

	{
print <<EOF

<table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update Distributor Profile</b></font></td>
          <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
              <tr bordercolor="#333366">
                <td width="50%" align="center" valign="top" height="250">
                  <table width="65%" border="0" cellspacing="0" cellpadding="5">
                    <tr>
                      <td width="100%"><font face="verdana,arial,helvetica" size="1" color="#333366">
<br><b>No Matching Records Found</b><ul><li>The Part Number you specified does not match the Product Type you selected: <b>$PricingClass</b>.</li><li>Are you sure <b>$InternalPartNum</b> isn't actually a Kit and not just a stand-alone item?</li></ul><form><center><input type="button" value="Try Again" onClick="javascript:history.go('-1')" class="inputbut"></center><br>
<br><br></font>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
	  
EOF
}
	&bottom;
	exit;
}

##----------->>> ELSE CONTINUE
else {
##----------->>> START DYNAMO WINDOW STUFF
	$browser = "$ENV{'HTTP_USER_AGENT'}";
	## DYNAMIC BROWSER PLACEMENTS
	if ($browser =~ "MSIE" || $browser =~ "Netscape6" || $browser =~ "netscape6" || $browser =~ "netscape5" || $browser =~ "Netscape5") { $zindex = ""; }
	else { $zindex = "z-index:5"; }

	$divcont = "#divCont{position:absolute; overflow:hidden; left:25%; top:2160; clip:rect(0,300,450,0); height:450; width:300;}";
	$divload = "#divLoad{position:absolute; left:25%; top:2160; clip:rect(0,300,450,0); height:450; width:300; visibility:hidden;}";	
	$divArrows = "#divArrows{position:absolute; left:0; top:1155; z-index:25; visibility:hidden}";
	$divBground = "#bground{position:absolute; left:0; top:0; clip:rect(0,1,1,0); height:1; width:1;$zindex}";
##----------->>> END DYNAMO WINDOW STUFF

## ------------>> WHICH DISTRIBUTOR IS CHOSEN AS MAIN?
if ($SavedDISTCode =~ "Ingram") { $LeIngram="checked"; }
elsif ($SavedDISTCode =~ "TechData") { $LeTechData="checked"; }
else { $LeSynnex="checked"; }

## ------------>> IS PRODUCT SEARCHABLE?
if ($SavedSearchable eq "No") { $Syes = ""; $Sno = "selected"; }
else { $Syes = "selected"; $Sno = ""; }

{
print <<EOF

<html>
<head>
<title>Shark Tank Admin System - Inventory ( Stand-Alone Products )</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<script language="Javascript">
// HTML TAGGING SCRIPT FOR HTML 4.0 COMPLIANT CHARACTERS ON ALL BROWSERS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions
function htmlUsIn() {
	ItemName = document.change.ItemName.value;
	ItemName = ItemName.replace(/&reg;/g, "®");
	ItemName = ItemName.replace(/&#153;/g, "™");
	ItemName = ItemName.replace(/&copy;/g, "©");
	ItemName = ItemName.replace(/&#8216;/g, "‘");
	ItemName = ItemName.replace(/&#8216;/g, "'");
	ItemName = ItemName.replace(/&#34;/g, "\\"");
	ItemName = ItemName.replace(/\\n<br>/g, "\\n");
	document.change.ItemName.value = ItemName;

	Description = document.change.Description.value;
	Description = Description.replace(/&reg;/g, "®");
	Description = Description.replace(/&#153;/g, "™");
	Description = Description.replace(/&copy;/g, "©");
	Description = Description.replace(/&#8216;/g, "‘");
	Description = Description.replace(/&#8216;/g, "'");
	Description = Description.replace(/&#34;/g, "\\"");
	document.change.Description.value = Description;
	
	TechSpecs = document.change.TechSpecs.value;
	TechSpecs = TechSpecs.replace(/&reg;/g, "®");
	TechSpecs = TechSpecs.replace(/&#153;/g, "™");
	TechSpecs = TechSpecs.replace(/&copy;/g, "©");
	TechSpecs = TechSpecs.replace(/&#8216;/g, "‘");
	TechSpecs = TechSpecs.replace(/&#8216;/g, "'");
	TechSpecs = TechSpecs.replace(/&#34;/g, "\\"");
	document.change.TechSpecs.value = TechSpecs;
}

function htmlUsOut() {
	ItemName = document.change.ItemName.value;
	ItemName = ItemName.replace(/®/g, "&reg;");
	ItemName = ItemName.replace(/™/g, "&#153;");
	ItemName = ItemName.replace(/©/g, "&copy;");
	ItemName = ItemName.replace(/‘/g, "&#8216;");
	ItemName = ItemName.replace(/'/g, "&#8216;");
	ItemName = ItemName.replace(/\\"/g, "&#34;");
	ItemName = ItemName.replace(/\\n\\n/g, "<br><br>");
	ItemName = ItemName.replace(/\\n/g, "<br>");
	document.change.ItemName.value = ItemName;

	Description = document.change.Description.value;
	Description = Description.replace(/®/g, "&reg;");
	Description = Description.replace(/™/g, "&#153;");
	Description = Description.replace(/©/g, "&copy;");
	Description = Description.replace(/‘/g, "&#8216;");
	Description = Description.replace(/'/g, "&#8216;");
	Description = Description.replace(/\\"/g, "&#34;");
	document.change.Description.value = Description;
	
	TechSpecs = document.change.TechSpecs.value;
	TechSpecs = TechSpecs.replace(/®/g, "&reg;");
	TechSpecs = TechSpecs.replace(/™/g, "&#153;");
	TechSpecs = TechSpecs.replace(/©/g, "&copy;");
	TechSpecs = TechSpecs.replace(/‘/g, "&#8216;");
	TechSpecs = TechSpecs.replace(/'/g, "&#8216;");
	TechSpecs = TechSpecs.replace(/\\"/g, "&#34;");
	document.change.TechSpecs.value = TechSpecs;
}
</script>
<script language="javascript">
function trigger(myurl) {
var b = navigator.appName;
if (b=="Netscape") {
	mainFrame = parent.frames.botOne;
	mainFrame.frame.loadpage(''+myurl+'');
}

else {
	parent.botOne.frame.loadpage(''+myurl+'');
	}
}

function makeAccessory() {
TheAccess = document.change.TheAccess;
AllProducts = document.change.AllProducts; 
var sizer = TheAccess.length;
for(var i = 0; i < AllProducts.length; i++) {
if ((AllProducts.options[i] != null) && (AllProducts.options[i].selected)) {
var there = false;
for(var count = 0; count < sizer; count++) {
if (TheAccess.options[count] != null) {
if (AllProducts.options[i].value == TheAccess.options[count].value) {
there = true;
break;
      }
   }
}
if (there != true) {
var thisone = AllProducts.options[i].value;
if (thisone == "$SavedInternalPartNum") { }
else {
TheAccess.options[sizer] = new Option(AllProducts.options[i].text); 
TheAccess.options[sizer].value = AllProducts.options[i].value;
sizer++;
}
         }
      }
   }
}

function killAccessory() {
var TheAccess  = document.change.TheAccess;
var sizer = TheAccess.options.length;
for(var i = (sizer-1); i >= 0; i--) {
if ((TheAccess.options[i] != null) && (TheAccess.options[i].selected == true)) {
TheAccess.options[i] = null;
      }
   }
}


function getProducts(me,me2) {
var missingdrop = "";
var formindex = document.change.ProdTypes.selectedIndex;
var thisone = document.change.ProdTypes.options[formindex].value;
var me = "ProdTypes";

if (thisone == "BIGNULL") {
	thefirst = "ProdTypes";
    missingdrop += "\\nThat is not a valid option, please select another...";
}

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    alert(missingdrop);
 	document.change[thefirst].focus();
    return false;
} 
else {
	if ((thisone == "Desktop") || (thisone == "Server") || (thisone == "Notebook") || (thisone == "Kit") || (thisone == "Monitor") || (thisone == "Memory") || (thisone == "HardDrive") || (thisone == "VideoCard") || (thisone == "Peripheral") || (thisone == "Printer") || (thisone == "Software")) {
		var b = navigator.appName;
		if (b=="Netscape") {
			mainFrame = parent.frames.botOne;
			mainFrame.frame.loadpage('pchoose.cgi?FeedMe='+me2+'&ProdType='+thisone+'');
		}

		else {
			parent.botOne.frame.loadpage('pchoose.cgi?FeedMe='+me2+'&ProdType='+thisone+'');
		}
	return false;
	}
}
}

function getTypes() {
var b = navigator.appName;
ProdTypes = document.change.ProdTypes;
var sizer = ProdTypes.length;
AllProducts = document.change.AllProducts;
var sizer2 = AllProducts.length;

// CLEARS ALL DATA ON ALLPRODUCTS
for(var i = (sizer2-1); i >= 0; i--) {
while (AllProducts.options[i] != null) {
AllProducts.options[i] = null;
	}
}

// CLEARS ALL DATA ON ProdTypes
for(var i = (sizer-1); i >= 0; i--) {
while (ProdTypes.options[i] != null) {
ProdTypes.options[i] = null;
	}
}

// get length after kills
var sizer = ProdTypes.length;

// GENERATE PRODTYPES
ProdTypes.options[sizer] = new Option('Select an Item'); ProdTypes.options[sizer].value = 'BIGNULL'; sizer++;
ProdTypes.options[sizer] = new Option('Desktop PC'); ProdTypes.options[sizer].value = 'Desktop'; sizer++;
ProdTypes.options[sizer] = new Option('Notebook'); ProdTypes.options[sizer].value = 'Notebook'; sizer++;
ProdTypes.options[sizer] = new Option('Server'); ProdTypes.options[sizer].value = 'Server'; sizer++;
ProdTypes.options[sizer] = new Option('Monitor'); ProdTypes.options[sizer].value = 'Monitor'; sizer++;
ProdTypes.options[sizer] = new Option('Memory'); ProdTypes.options[sizer].value = 'Memory'; sizer++;
ProdTypes.options[sizer] = new Option('Hard Drive'); ProdTypes.options[sizer].value = 'HardDrive'; sizer++;
ProdTypes.options[sizer] = new Option('Video Card'); ProdTypes.options[sizer].value = 'VideoCard'; sizer++;
ProdTypes.options[sizer] = new Option('Peripheral'); ProdTypes.options[sizer].value = 'Peripheral'; sizer++;
ProdTypes.options[sizer] = new Option('Printer'); ProdTypes.options[sizer].value = 'Printer'; sizer++;
ProdTypes.options[sizer] = new Option('Software'); ProdTypes.options[sizer].value = 'Software'; sizer++;
}

function theHungry(me, me2) {
var b = navigator.appName;
if (b=="Netscape") {
	mainFrame = parent.frames.botOne;
	mainFrame.frame.loadpage('ichoose.cgi?FeedMe='+me+'&Type=prod_common&SubType='+me2+'');
}

else {
	parent.botOne.frame.loadpage('ichoose.cgi?FeedMe='+me+'&Type=prod_common&SubType='+me2+'');
	}
}

function iPreview(me) {
	image = document.change[me].value;
	if (document.change[me].value == null || document.change[me].value == "" || document.change[me].value == " ") {
		alert('You must have an ImageID number for image you want to preview.');
	}
	else {
	var b = navigator.appName;
		if (b=="Netscape") {
			mainFrame = parent.frames.botOne;
			mainFrame.frame.loadpage('ichoose.cgi?Preview=1&ImageID='+image+'');
		}

		else {
			parent.botOne.frame.loadpage('ichoose.cgi?Preview=1&ImageID='+image+'');
		}
	}
}

function noChange(este,mua) {
	if (este == "MultimediaBut") {
		alert('Sorry, you cannot directly edit the contents of this field. If you would like to change the multimedia object being used by this field click \\'Get Mine\\'. To Preview the multimedia obejct curretnly being used click the \\'Preview\\' button.');
		alert(document.change[mua].value);
		document.change[este].focus();
	}
	else {
		alert('Sorry, you cannot directly edit the contents of this field. If you would like to change the image being used by this field click \\'Get Mine\\'. To Preview the image currently being used click the \\'Preview\\' button.');
		alert(document.change[mua].value);
		document.change[este].focus();
	}
}


function clearUs() {
// CLEARS ALL DATA ON WARRANTY ONLOAD
Warranty = document.change.Warranty;
var sizer = Warranty.length;
	for(var i = (sizer-1); i >= 0; i--) {
		while (Warranty.options[i] != null) {
			if (Warranty.options[i].value == "BIGNULL") {
				Warranty.options[i] = null;
			}
		}
	}

// CLEARS ALL DATA ON TheAccess
TheAccess = document.change.TheAccess;
var sizer = TheAccess.length;
	for(var i = (sizer-1); i >= 0; i--) {
		while (TheAccess.options[i] != null) {
			if (TheAccess.options[i].value == "BIGNULL") {
				TheAccess.options[i] = null;
			}
		}
	}

// CLEARS ALL DATA ON MFGCode
MFGCode = document.change.MFGCode;
var sizer = MFGCode.length;
	for(var i = (sizer-1); i >= 0; i--) {
		while (MFGCode.options[i] != null) {
			if (MFGCode.options[i].value == "BIGNULL") {
				MFGCode.options[i] = null;
			}
		}
	}
	
}
</script>
<script language="Javascript">
function checkForm() {
var missingdrop = "";
var thefirst = "";

if (document.change.ItemName.value == "" || document.change.ItemName.value == " ") {
    missingdrop += "\\n     - Product Name";
	thefirst = "ItemName";
}

if (document.change.Description.value == "" || document.change.Description.value == " ") {
    missingdrop += "\\n     - Descriptions";
	if (thefirst == "") { thefirst = "Description"; }
}

if (document.change.TechSpecs.value == "" || document.change.TechSpecs.value == " ") {
    missingdrop += "\\n     - Technical Specifications";
	if (thefirst == "") { thefirst = "TechSpecs"; }
}

if (document.change.Keywords.value == "" || document.change.Keywords.value == " ") {
    missingdrop += "\\n     - Indexing Keywords";
	if (thefirst == "") { thefirst = "Keywords"; }
}

if (isNaN(document.change.Weight.value) || (document.change.Weight.value == "") || (document.change.Weight.value == " ")) {
    missingdrop += "\\n     - Weight";
	if (thefirst == "") { thefirst = "Weight"; }
}

if (isNaN(document.change.Cost.value) || (document.change.Cost.value == "") || (document.change.Cost.value == " ")) {
    missingdrop += "\\n     - Cost";
	if (thefirst == "") { thefirst = "Cost"; }
}

// Check Product Accessories
var strValues = "";
	var boxLength = document.change.TheAccess.length;
	var count = 0;
if (boxLength != 0) {
	for (i = 0; i < boxLength; i++) {
		if (count == 0) {
			strValues = document.change.TheAccess.options[i].value;
		}
		else {
			strValues = strValues + "," + document.change.TheAccess.options[i].value;
		}
	count++;
   }
}
else { }
if (strValues.length == 0) { }
else {
	// Grab selected fields from TheAccess and make Accessories form field for processing
	document.change.Accessories.value = strValues;
}

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    missingdrop ="___________________________________________                   \\n\\n" + "  Sorry, I cannot process your request because the\\n  following fields are either blank or filled incorrectly:\\n" + "___________________________________________                   \\n\\n" +
    missingdrop + "\\n\\n___________________________________________                   " + "\\n\\n   To continue, check fields and submit form again!" + "\\n___________________________________________";
    alert(missingdrop);
	document.change[thefirst].focus();
    return false;
} 
else {
htmlUsOut();
return true;
}
}
</script>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:ifrinit();htmlUsIn();getTypes();clearUs();feedAccessories();feedMFGs();">
$MenuConfig
<script language="JavaScript" src="../js/reload.js"></script>
<style type="text/css">
$divcont
$divload
$divBground
#divIEText{position:absolute; left:0; top:0}
$divArrows
#divLinks{position:absolute; left:420; top:220}
</style>



$MenuConstructor
<div id="divLinks"></div>

<!-- THIS DIV IS USED BY ALL BROWSERS EXCEPT IE5.5 AND NS6 FOR DYNAMIC CONTENT WINDOW SCROLLING -->
<div id="divArrows">
<a href="#" onmouseover="frame.scroll=true; frame.up(3);" onmouseout="frame.scroll=false"><img src="images/scrollers/arrowup_1off.gif" border="0" width="17" height="7" name="arrowup1"></a><br>
<a href="#" onmouseover="frame.scroll=true; frame.up(8)" onmouseout="frame.scroll=false"><img src="images/scrollers/arrowup_2off.gif" border="0" width="17" height="11" name="arrowup2"></a><br>
<a href="#" onmouseover="frame.scroll=true; frame.up(15)" onmouseout="frame.scroll=false"><img src="images/scrollers/arrowup_3off.gif" border="0" width="17" height="5" name="arrowup3"></a><br>
<br><br><br>
<a href="#" onmouseover="frame.scroll=true; frame.down(3)" onmouseout="frame.scroll=false"><img src="images/scrollers/arrowdn_1off.gif" border="0" width="17" height="5" name="arrowdn1"></a><br>
<a href="#" onmouseover="frame.scroll=true; frame.down(8)" onmouseout="frame.scroll=false"><img src="images/scrollers/arrowdn_2off.gif" border="0" width="17" height="11" name="arrowdn2"></a><br>
<a href="#" onmouseover="frame.scroll=true; frame.down(15)" onmouseout="frame.scroll=false"><img src="images/scrollers/arrowdn_3off.gif" border="0" width="17" height="7" name="arrowdn3"></a><br>
</div>

<script language="JavaScript" src="../js/pageload1.js"></script>
<!-- Copyright NetMedia Solutions and Coasltine Micro, Inc.-->
<script language="Javascript" src="../js/pageload2.js"></script>

<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/top_tablebg_main.jpg" height="100">
  <tr> 
    <td width="30%" valign="top"><img src="images/illus_main.jpg" width="250" height="100"></td>
    <td width="25%">&nbsp;</td>
    <td align="left" valign="top"><img src="images/title_main.jpg" width="300" height="100"></td>
  </tr>
</table>
<form method="post" action="$script" name="change" onSubmit="return checkForm();">
  <table width="100%" border="0" height="100%" cellpadding="0" cellspacing="0">
    <tr valign="top"> 
      <td width="20%">$legal</td>
      <td align="center" width="80%"> 
        <table width="95%" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td width="90%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update Product ($SavedProductType - $SavedItemName)</b></font></td>
            <td align="right" width="10%">&nbsp;</td>
          </tr>
          <tr> 
            <td colspan="2"> 
              <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
                <tr bordercolor="#333366"> 
                  <td width="100%" align="center" valign="top" height="250"> 
                    <table width="100%" border="0" cellspacing="0" cellpadding="5">
                      <tr valign="top" align="center"> 
                        <td bordercolor="#333366" class="tableBORDER" width="50%"> 
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
                                        <font color="#EB0000">Example: <i>NEC 
                                        18.1 Inch MultiSync Monitor - White</i></font> 
                                      </center>
                                      </font></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"> 
                                      <input type="text" name="ItemName" size="15" class="inputtext15" value="$SavedItemName">
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
                  is the pricing class for the product you are currently viewing. 
                  The pricing class is the function that controls a product's 
                  price markup for the customer.</font></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="35" align="center"><font face="verdana,arial,helvetica" size="1" color="#EB0000">$SavedPricingClass</font> 
                                      <input type="hidden" name="PricingClass" value="$SavedPricingClass">
                                      <input type="hidden" name="InternalPartNum" value="$InternalPartNum">
									  <input type="hidden" name="MFGPartNum" value="$SavedMFGPartNum">
									  <input type="hidden" name="ProductID" value="$ProductID">
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
                  Type </font></b></font></td>
                <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
              </tr>
              <tr> 
                <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
              </tr>
              <tr> 
                <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                <td height="65" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366">This 
                  field specifies the actual Product Type for this product, which 
                  makes searches and other site functions easier to use and read 
                  by the website user.</font></td>
                <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
              </tr>
              <tr> 
                <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                <td height="35" align="center">
                  <select name="ProductType" class="inputtext">
EOF
}

## WHICH ProductType IS CHOSEN?
$count=0;
@ProductTypes = ("Audio,Audio Cards","CDROM,CD-ROM","CDRW,CD Re-Writer (cdrw/cd combo)","DigitalCam,Digital Camera","DVDROM,DVD-ROM (cdrw/dvd combo)","Floppy,Floppy Drive","HardDrive,Hard Drive","InternetCam,Internet Cam","Joystick,Joystick/Gamepad","Keyboard,Keyboard","Memory,Memory","Modem,Modem","Monitor,Monitor","Networking,Networking","NIC,Network Card","NoteExtra,Notebook Extra","Pointer,Pointer Device","UPS,Utility Power Supply","Printer,Printer","Processor,Processor","Scanner,Scanner","Software,Software (OS/Software)","Speaker,Speaker","Storage,Mass Storage (Non-Zip)","SystemBoard,System Board","SystemChassis,System Chassis (server/desktop)","VideoCard,Video Card","WirelessNet,Wireless Networking","ZipDrive,Zip Drive","Warranty,Extended Warranty","License,Software License","Assembly,Product Assembly","Peripheral,Peripheral (catch-all)");
foreach $ProductType (@ProductTypes) {
	$count++;
   	# Split the pair up into individual variables.
   	local($value, $name) = split(/,/, $ProductType);
	if ($SavedProductType =~ "$value") { 
		print "<option value=\"$value\" SELECTED>$name</option>"; 
	}
	else {
		print "<option value=\"$value\">$name</option>"; 
	}
}

{
print <<EOF

                    
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
                <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Searchable</font></b></font></td>
                <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
              </tr>
              <tr> 
                <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
              </tr>
              <tr> 
                <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                <td height="65" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366">This 
                  field allows you to let this product be presented via the various 
                  website search points. Choose yes if you want this product to 
                  be available for searching, no if you do not.</font></td>
                <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
              </tr>
              <tr> 
                <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                <td height="35" align="center"> 
                  <select name="Searchable" class="inputtext">
                    <option value="Yes" $Syes>Yes</option>
                    <option value="No" $Sno>No</option>
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
                              <td bgcolor="#8F8FAB" width="1"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="300" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0" align="center">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" width="268" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Product 
                                      Part Numbers</font></b><font color="#FFFFFF"> 
                                      (CLM / MFG / DIST)</font></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="225" bgcolor="#F2F2F7" width="268"><font face="verdana,arial,helvetica" size="1" color="#333366">In 
                                      order to add a product to the system you 
                                      MUST have the CM and MFG part numbers at 
                                      the very least. With that much data at hand 
                                      you can successfully add a product to the 
                                      system. Yet, if you want your product listing 
                                      to be searchable using the distributor's 
                                      part number, then you must type in those 
                                      numbers. Finally, you must choose which 
                                      distributor is the primary for this product. 
                                      You can do this by clicking the radio button 
                                      next to either the Ingram Micro, Tech Data 
                                      or Synnex Part Number.<br>
                                      <br>
                                      Please make sure you have the correct part 
                                      number for the product you are attempting 
                                      to add to the system. If you add an incorrect 
                                      part number and build upon that number, 
                                      especially the CM Part Number, you could 
                                      easily cause system errors in the future.</font></td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td align="center" valign="middle" width="100%"> 
                                      <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
                                        <tr> 
                                          <td width="100%" height="25" align="center" bgcolor="#F2F2F7" colspan="2"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Part Number</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="100%" height="35" valign="middle" align="center" colspan="2"> 
                                            <font face="verdana,arial,helvetica" size="1" color="#333366">$InternalPartNum</font> 
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="100%" height="25" align="center" bgcolor="#F2F2F7" colspan="2"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>MFG 
                                            Part Number</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="100%" height="35" valign="middle" align="center" colspan="2"> 
                                            <font face="verdana,arial,helvetica" size="1" color="#333366">$SavedMFGPartNum</font> 
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td colspan="2" height="25" width="100%" align="center" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Ingram 
                                            Micro Part Number</b></font><font face="verdana,arial,helvetica" size="1" color="#333366"> 
                                            </font></td>
                                        </tr>
                                        <tr> 
                                          <td width="85%" height="35" valign="middle" align="center"> 
                                            <input type="text" name="IngramPartNum" size="15" class="inputtext15" value="$SavedIngramPartNum">
                                          </td>
                                          <td width="15%" height="35" valign="middle" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"> 
                                            <input type="radio" name="DISTCode" class="radiobut" value="Ingram" $LeIngram>
                                            </font></td>
                                        </tr>
                                        <tr> 
                                          <td colspan="2" height="25" width="100%" align="center" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Tech 
                                            Data Part Number</b></font> </td>
                                        </tr>
                                        <tr> 
                                          <td height="35" width="85%" valign="middle" align="center"> 
                                            <input type="text" name="TechDataPartNum" size="15" class="inputtext15" value="$SavedTechDataPartNum">
                                          </td>
                                          <td height="35" width="15%" valign="middle" align="center"> 
                                            <input type="radio" name="DISTCode" class="radiobut" value="TechData" $LeTechData>
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td colspan="2" height="25" width="100%" align="center" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Synnex Part Number</b></font> </td>
                                        </tr>
                                        <tr> 
                                          <td height="35" width="85%" valign="middle" align="center"> 
                                            <input type="text" name="SynnexPartNum" size="15" class="inputtext15" value="$SavedSynnexPartNum">
                                          </td>
                                          <td height="35" width="15%" valign="middle" align="center"> 
                                            <input type="radio" name="DISTCode" class="radiobut" value="Synnex" $LeSynnex>
                                          </td>
                                        </tr>
                                      </table>
                                    </td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="100%" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
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
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="270" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Manufacturer's 
                                      Information</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" rowspan="3">&nbsp;</td>
                                    <td height="115" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Manufacturer's 
                                      Profile</b><br>
                                      Every product should have it's manufacturer's 
                                      profile listed in the system. If it is not, 
                                      it is strongly suggested that you take the 
                                      time to configure one for the manufacturer. 
                                      Select the manufacturer of this product 
                                      from the list below.<br>
                                      <br>
                                      <center>
                                        <select name="MFGCode" class="inputtext">
                                          <option value="BIGNULL">0000000000000000</option>
                                        </select>
                                      </center>
                                      </font> </td>
                                    <td width="15" bgcolor="#F2F2F7" rowspan="3">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td height="35" align="center" valign="middle"> 
                                      <input type="button" value="Review Selected Profile" class="inputbut" onClick="javascript:alert('Script Coming Soon...');" name="button222">
                                    </td>
                                  </tr>
                                  <tr> 
                                    <td height="35" align="center" valign="middle"> 
                                      <input type="button" value="Create New Profile" class="inputbut" onClick="javascript:parent.location.href='add_mfg.cgi'" name="button232">
                                    </td>
                                  </tr>
  
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="125" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Product 
                                      URL</b><br>
                                      </font><font face="verdana,arial,helvetica" size="1" color="#333366">If 
                                      the product you are adding to the system 
                                      has it's <b>own page/section</b> within 
                                      the <b>Manufacturer's</b> website or our website please add that URL here.<br>
                                      <br>
                                      <center>
                                        <font color="#EB0000">Example: <i>http://www.intel.com/pentium4/</i><br>
                                        </font> 
                                        <input type="text" name="ProdURL" size="15" class="inputtext15" value="$SavedMFGProdURL">
                                      </center>
                                      </font> </td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="125" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Driver 
                                      Update URL</b><br>
                                      If the product you are adding to the system 
                                      has a <b>Driver Update Page/Section or File</b> 
                                      within the <b>Manufacturer's</b> website 
                                      or our website please add 
                                      that URL here.<br>
                                      <br>
                                      <center>
                                        <font color="#EB0000">Example: <i>http://www.intel.com/pentium4/drivers/</i></font> 
                                        <br>
                                        <input type="text" name="DriverURL" size="15" class="inputtext15" value="$SavedMFGDriverURL">
                                      </center>
                                      </font> </td>
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
          <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Warranty</font></b></font></td>
          <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
        </tr>
        <tr> 
          <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
          <td height="85" bgcolor="#F2F2F7" align="left" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">Most 
            products have a warranty on it set forth by it's Manufacturer. If 
            this is the case, you can easily describe the warranty for this product 
            offered by it's Manufacturer.</font></td>
          <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
        </tr>
        <tr> 
          <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
          <td height="30" align="center" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366"> 
            <input type="text" name="Warranty" size="15" class="inputtext15" value="$SavedWarranty">
            </font> </td>
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
                        <td width="50%"> <br>
                          <table width="300" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="300" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="270" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Description</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="95" bgcolor="#F2F2F7" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366">Type 
                                      in a descriptive summary of this product's 
                                      performance, design and other distinct information 
                                      about this product that will help it stand 
                                      out from other products in the system. By 
                                      default, Ingram Micro descriptions are impoted 
                                      for your product once the automated data 
                                      import process has been completed at the 
                                      end of week.</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="125" align="center"> 
                                      <textarea name="Description" cols="25" class="textarea1" rows="5">$SavedDescription</textarea>
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
                              <td width="270" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="270" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Technical 
                                      Specifications </font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="195" bgcolor="#F2F2F7" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366">Technical 
                                      specifications are best when acquired from 
                                      a product's manual or from the Manfuacturer's 
                                      website, whichever is most descriptive. 
                                      Every chunk of data separated with a double 
                                      space will be presented as a bullet to the 
                                      viewing user.<br>
                                      <br>
                                      <b>Example</b><br>
                                      75 Ohms Positive Input Video Signal<br>
                                      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#EB0000">< < - - Double Space</font><br>
                                      Over 16,000,000 Display Colors <br>
                                      <br>
                                      <b>Will Display</b> 
                                      <li>&nbsp;75 Ohms Positive Input Video Signal<br>
                                        <br>
                                      </li>
                                      <li></li>
                                      &nbsp;Over 16,000,000 Display Colors<br>
                                      </font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="125" align="center"> 
                                      <textarea name="TechSpecs" cols="25" class="textarea1" rows="5">$SavedTechSpecs</textarea>
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
                              <td width="270" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="270" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Indexing 
                                      Keywords</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="95" bgcolor="#F2F2F7" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366">Type 
                                      at least 10 different keywords for this 
                                      product to make it easier to find when a 
                                      user is searching for product in the system.<br>
                                      <br>
                                      <font color="#EB0000"><b>Example</b><br>
                                      Flat, Digital, Monitor, White, 1280 x 1024, 
                                      LCD, TFT, 18.1</font></font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="125" align="center"> 
                                      <textarea name="Keywords" cols="25" class="textarea1" rows="5">$SavedKeywords</textarea>
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
                                      <input type="text" name="Weight" size="15" class="inputtext15" value="$SavedWeight">
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
                                      <input type="text" name="Cost" size="15" class="inputtext15" value="$SavedCost">
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
                        </td>
                      </tr>
                      <tr> 
                        <td width="100%" align="center" height="27" bgcolor="#F2F2F7" class="tableBG" colspan="2"><font face="verdana,arial,helvetica" size="2" color="#333366"><b>Product 
                          Imagery and Multimedia</b></font></td>
                      </tr>
                      <tr> 
                        <td width="50%" align="center" class="tableBG">&nbsp; </td>
                        <td width="50%" align="center" class="tableBG" height="500" valign="top"> 
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#FFFFFF"><b>Emblem</b> (Multiple)</font></td>
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
                                      <nobr><input type="text" name="Emblem" size="7" class="inputtext7" value="$SavedEmblem" onFocus="Javascript:noChange('EmblemBut');">
                                      <input type="button" value="Get Mine!" onClick="Javascript:theHungry('Emblem','emblem')" class="inputbut" name="EmblemBut"><input type="button" value="Preview" onClick="Javascript:iPreview('Emblem')" class="inputbut"></nobr>
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><font color="#FFFFFF"><b>Small Image</b> (One only)</font></font></td>
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
                                    <td height="35" align="center"> <nobr> 
                                      <input type="text" name="SmallLogo" size="7" class="inputtext7" value="$SavedSmallLogo" onFocus="Javascript:noChange('SmallLogoBut','SmallLogo');">
                                      <input type="button" value="Get Mine!" onClick="Javascript:theHungry('SmallLogo','small')" class="inputbut" name="SmallLogoBut">
                                      <input type="button" value="Preview" onClick="Javascript:iPreview('SmallLogo')" class="inputbut" name="button">
                                      </nobr> </td>
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><font color="#FFFFFF"><b>Large Image</b> (Multiple)</font></font></td>
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
                                      <input type="text" name="LargeLogo" size="7" class="inputtext7" value="$SavedLargeLogo" onFocus="Javascript:noChange('LargeLogoBut','LargeLogo');">
                                      <input type="button" value="Get Mine!" onClick="Javascript:theHungry('LargeLogo','large')" class="inputbut" name="LargeLogoBut">
                                      <input type="button" value="Preview" onClick="Javascript:iPreview('LargeLogo')" class="inputbut" name="button">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Multimedia</font></b></font></td>
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
                                    <td height="35" align="center"> <nobr> 
                                      <input type="text" name="Multimedia" size="7" class="inputtext7" value="$SavedMultimedia" onFocus="Javascript:noChange('MulitmediaBut','Multimedia');">
                                      <input type="button" value="Get Mine!" onClick="javascript:alert('Script Coming Soon...');" class="inputbut" name="MulitmediaBut">
                                      <input type="button" value="Preview" onClick="javascript:alert('Script Coming Soon...');" class="inputbut" name="button2">
                                      </nobr> </td>
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
                        <td width="100%" align="center" height="27" bgcolor="#F2F2F7" class="tableBG" colspan="2"><font face="verdana,arial,helvetica" size="2" color="#333366"><b>Accessories</b></font></td>
                      </tr>
                      <tr valign="middle" align="center"> 
                        <td bordercolor="#333366" class="tableBORDER" width="50%"> 
                          <table width="300" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="300" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="300" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB" width="268"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Inventory 
                                      Reader </font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="155" bgcolor="#F2F2F7" align="left" valign="middle" width="268"><font face="verdana,arial,helvetica" size="1" color="#333366">To 
                                      list products in the Inventory Reader by 
                                      type, simply select a Product Type from 
                                      the menu and the Inventory Generator will 
                                      automatically be updated with those products. 
                                      <br>
                                      <br>
                                      To make a product an Accessory to this product 
                                      choose a product from the Inventory Generator 
                                      then click <font color="#EB0000">Accessory</font> 
                                      to make the selected product an accessory. 
                                      To clear the Inventory Generator list simply 
                                      click the <font color="#EB0000">Clear List</font> 
                                      button.</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="45" align="center"> 
                                      <table width="270" border="0" cellspacing="0" cellpadding="0" bgcolor="#FFFFFF" align="center">
                                        <tr> 
                                          <td align="center" width="100%" height="25"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Product Types</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td align="center" width="100%" height="45"> 
                                            <select name="ProdTypes" class="inputtext" onChange="javascript:getProducts('ProdTypes','AllProducts');">
                                              <option value="BIGNULL">Select an Item</option>
                                            </select>
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td align="center" width="100%" height="25"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Inventory 
                                            Generator</b></font> </td>
                                        </tr>
                                        <tr> 
                                          <td rowspan="5" valign="middle" align="center" width="100%"> 
                                            <select name="AllProducts" size="20" multiple width="20" class="prodselect">
                                              <option value="BIGNULL">00000000000000000000000000000000</option>
                                            </select>
                                            <nobr><input type="Button" value="Clear List" onClick="javascript:getTypes();" class="inputbut" name="Button342"><input type="Button" value="Accessory" onClick="javascript:makeAccessory();" class="inputbut" name="Button332"></nobr>
                                          </td>
                                        </tr>
                                        <tr> </tr>
                                        <tr> </tr>
                                        <tr> </tr>
                                        <tr> </tr>
                                      </table>
                                    </td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="268" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
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
                        <td width="50%"> <br>
                          <table width="300" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="300" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="300" valign="top"> 
                                <table width="300" border="0" cellspacing="0" cellpadding="0">
                                  <tr> 
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    <td height="20" bgcolor="#8F8FAB" width="268"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Accessories</font></b></font></td>
                                    <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                    <td height="135" bgcolor="#F2F2F7" align="left" valign="middle" width="268"><font face="verdana,arial,helvetica" size="1" color="#333366"> 
                                      Follow the directions in the screen to your 
                                      left labeled <font color="#EB0000">Inventory 
                                      Reader</font> to make changes to this section.<br>
                                      <br>
                                      To remove a product being used as an accessory 
                                      just select the product from the 'Accessories' list you would like to remove 
                                      and click the <font color="#EB0000">Remove</font> 
                                      button <font color="#EB0000">BELOW</font> 
                                      the list.</font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="45" align="center"> 
                                      <table width="270" border="0" cellspacing="0" cellpadding="0" bgcolor="#FFFFFF" align="center">
                                        <tr> 
                                          <td align="center" width="100%" height="25"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Product 
                                            Accessories</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="100%" valign="bottom" align="center"> 
                                            <select name="TheAccess" size="8" multiple class="prodguinea">
											 <option value="BIGNULL">0000000000000000</option>
                                            </select>
                                            <input type="hidden" name="Accessories">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="100%" valign="middle" align="center" height="45"> 
                                            <input type="Button" value=" Remove" onClick="javascript:killAccessory();" class="inputbut" name="Button3">
                                            <input type="button" value="Preview" onClick="javascript:alert(document.change.TheAccess.value);" class="inputbut" name="button252">
                                          </td>
                                        </tr>

                                      </table>
                                    </td>
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="268" valign="top" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
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
        <br>
      </td>
    </tr>
  </table>

EOF
}

##----------->>> FEED ACCESSORIES
{
print <<EOF 

<script language="Javascript">
function feedAccessories() {
TheAccess = document.change.TheAccess;
var sizer = TheAccess.length;
// GETTING READY TO FEED INFO

EOF
}

@Accessories = split(/,/, $SavedAccessories);
foreach $Accessory (@Accessories) {
	my $count=0;
	my $sth = $dbh->prepare("SELECT * FROM Products WHERE InternalPartNum='$Accessory' ORDER BY ItemName ASC");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		my $ThyInternalPartNum = $row[1];
		my $ThyItemName = $row[11];
		print "TheAccess.options[sizer] = new Option('$ThyItemName');";
		print "TheAccess.options[sizer].value = '$ThyInternalPartNum';";
		print "sizer++;";
		$count++;
	}
	$sth->finish;
}
print "}";
print "</script>";

##----------->>> FEED MFGs
{
print <<EOF

<script language="Javascript">
function feedMFGs() {
MFGCode = document.change.MFGCode;
var sizer = MFGCode.length;
// GETTING READY TO FEED INFO

// GIVE NULL FIELD OPTION 
MFGCode.options[sizer] = new Option('Leave Blank (Not suggested...)');
MFGCode.options[sizer].value = 'NONE';
sizer++;


EOF
}

my $count=0;
my $sth = $dbh->prepare("SELECT * FROM MFGs ORDER BY Name ASC");
$sth->execute or die "Unable to execute query\n"; 
my @row;
while(@row = $sth->fetchrow_array) { 
	my $ThyMFGID = $row[0];
	my $ThyMFGName = $row[1];
	if ($SavedMFGCode == $ThyMFGID) {
		print "MFGCode.options[sizer] = new Option('$ThyMFGName');";
		print "MFGCode.options[sizer].value = '$ThyMFGID';";
		print "MFGCode.selectedIndex = sizer;";
		print "sizer++;";
		$count++;
	}
	else {
		print "MFGCode.options[sizer] = new Option('$ThyMFGName');";
		print "MFGCode.options[sizer].value = '$ThyMFGID';";
		print "sizer++;";
		$count++;	
	}
}
$sth->finish;

print "}";
print "</script>";

{
print <<EOF

<input type="hidden" name="DROPIN" value="1">
</form>
</body>
</html>

EOF
}
}
exit;
}

## If no resident form processing calls are given continue
elsif ($FORM{'enformthee'}) {

{
print <<EOF

<html>
<head>
<title>Shark Tank Admin System - Inventory ( Stand-Alone Products )</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
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
<table width="100%" border="0" cellpadding="0" cellspacing="0">
  <tr valign="top"> 
    <td width="20%"><br>$legal</td>
    <td align="center" width="80%"> 


<table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
            
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Add/Update 
            Distributor Profiles</b></font></td>
            <td align="right" width="50%">&nbsp;</td>
        </tr>
        <tr> 
          <td colspan="2"> 
            <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER" bordercolor="#333366">
              <tr valign="middle"> 
                        <td height="50" width="100%"> 
                          <center>
                            <font face="verdana,arial,helvetica" size="1" color="#EB0000">*If 
                            you have any questions please ask your Supervisor 
                            or Manager for help using the system or updating it's 
                            information.</font> 
                          </center>
                        </td>
                      </tr>
              <tr> 
                  <td width="50%" align="center" valign="top"> 
                    <table width="100%" border="0" cellspacing="0" cellpadding="5">
                    <tr> 
                      <td width="100%"><center>
                            <font face="verdana,arial,helvetica" size="1" color="#333366"> 
                            </font> <br>
<form method="post" action="$script" name="change" onSubmit="return checkForm();">
                            <table width="500" border="0" cellspacing="0" cellpadding="0" align="center">
                              <tr> 
                                <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                              </tr>
                              <tr> 
                                <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                                <td width="348" valign="top"> 
                                  <table width="500" border="0" cellspacing="0" cellpadding="0">
                                    <tr> 
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                      <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">View/Update 
                                        Distributor Profile</font></b></font></td>
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="55" bgcolor="#F2F2F7" align="left"><font face="verdana,arial,helvetica" size="1" color="#333366">To 
                                        view or update a distributor's profile 
                                        please choose the distributor you would 
                                        like to update from the list below then 
                                        click 'View/Update'</font></td>
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="35" align="center"> 
                                        <script language="Javascript">
function checkForm() {
var missingdrop = "";

// Implement selected User's name into UserName form field
// Grab selected fields from PayOption and make PayTypes form field for processing
var formindex = document.change.DISTID.selectedIndex;
var thisone = document.change.DISTID.options[formindex].text;
document.change.Name.value = thisone;

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    missingdrop ="___________________________________________                   \\n\\n" + "  Sorry, I cannot process your request because the\\n  following fields are either blank or filled incorrectly:\\n" + "___________________________________________                   \\n\\n" +
    missingdrop + "\\n\\n___________________________________________                   " + "\\n\\n   To continue, check fields and submit form again!" + "\\n___________________________________________";
    alert(missingdrop);
    return false;
} 
else {
return true;
}
}
</SCRIPT>
<select name="DISTID" class="inputtext">
EOF
}

	## Get list of CM reps
	use DBI;
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("SELECT * FROM DISTs ORDER BY Name ASC");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
		while(@row = $sth->fetchrow_array) { 
		my $DISTID = $row[0];
		my $Name = $row[1];
		print "<option value=\"$DISTID\">$Name</option>";
	}
	$sth->finish;
	$dbh->disconnect;
	## print closing select tag

{
print <<EOF

                                        </select>
                                        &nbsp;
<input type="hidden" name="Name" value="">                                        
                                        &nbsp;
<input type="submit" value="View/Update" class="inputbut" name="submit">
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
                            </table></form>
                            <table width="500" border="0" cellspacing="0" cellpadding="0" align="center">
                              <tr> 
                                <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                              </tr>
                              <tr> 
                                <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                                <td width="348" valign="top"> 
                                  <table width="500" border="0" cellspacing="0" cellpadding="0">
                                    <tr> 
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                      
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Create 
                                      New Distributor Profile</font></b></font></td>
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td colspan="3" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      
                                    <td height="35" bgcolor="#F2F2F7" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366">Click 
                                      the button below to create a new distributor 
                                      profile. </font></td>
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="35" align="center"> 
                                        
                                      <input type="button" value="Create DIST Profile" class="inputbut" onClick="javascript:parent.location.href='add_dist.cgi'">
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
                            <table width="500" border="0" cellspacing="0" cellpadding="0" align="center">
                              <tr> 
                                <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                              </tr>
                              <tr> 
                                <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                                <td width="348" valign="top"> 
                                  <table width="500" border="0" cellspacing="0" cellpadding="0">
                                    <tr> 
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                      
                                    <td height="20" bgcolor="#8F8FAB" colspan="2"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Search/Browse 
                                      Distributor Profiles</font></b></font></td>
                                      <td width="15" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td colspan="4" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      
                                    <td height="85" bgcolor="#F2F2F7" align="left" colspan="2"><font face="verdana,arial,helvetica" size="1" color="#333366">To 
                                      Search user accounts, type in the Terms/Keywords 
                                      to help you locate the distributor's profile 
                                      you are interested in reviewing and/or updating. 
                                      Then, select a Search Filter Option, this 
                                      is the field searched in the database. Finally, 
                                      click 'Search DISTs'<br>
                                        <br>
                                      *To Browse user accounts, simply select 
                                      a Browse Filter Option then click 'Browse 
                                      Users' </font></td>
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                      <td height="280" align="center" width="234" valign="top"> 
                                        <br>
<form method="post" action="view_dists.cgi">
                                        <table border="1" cellspacing="0" cellpadding="0" width="200" bordercolor="#8F8FAB">
                                          <tr> 
                                            <td height="20" align="center" bgcolor="#F2F2F7" class="tableBG" width="200"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Search 
                                              Terms/Keywords</b></font></td>
                                          </tr>
                                          <tr> 
                                            <td align="center" height="40" width="200"> 
                                              <input type="text" name="SearchTerms" size="15">
                                            </td>
                                          </tr>
                                          <tr> 
                                            <td height="20" align="center" bgcolor="#F2F2F7" width="200"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Search 
                                              Filter Options </b></font></td>
                                          </tr>
                                          <tr> 
                                            <td height="125" width="200"> 
                                              <input type="radio" name="SearchType" value="Name" SELECTED checked>
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">Company 
                                              Name </font><br>
                                              <input type="radio" name="SearchType" value="URL">
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">Website 
                                              URL </font><br>
                                              <input type="radio" name="SearchType" value="MailCity">
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">City</font><br>
                                              <input type="radio" name="SearchType" value="MailState">
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">State</font><br>
                                            </td>
                                          </tr>
                                          <tr> 
                                            <td align="center" height="35" valign="middle" width="200"> 
                                              <input type="submit" value="Search DISTs" class="inputbut" name="Submit">
                                            </td>
                                          </tr>
                                        </table>
</form>
                                      </td>
                                      <td height="280" align="center" width="234" valign="top"> 
                                        <br>
<form method="post" action="view_dists.cgi">
                                        <table border="1" cellspacing="0" cellpadding="0" width="200" bordercolor="#8F8FAB">
                                          <tr> 
                                            <td height="20" align="center" bgcolor="#F2F2F7" width="200"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Browse 
                                              Filter Options </b></font></td>
                                          </tr>
                                          <tr> 
                                            <td width="200" height="125"> 
                                              <input type="radio" name="Browse" value="Name" SELECTED checked>
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">Company 
                                              Name </font><br>
                                              <input type="radio" name="Browse" value="Email">
                                              <font face="verdana,arial,helvetica" size="1" color="#333366"> 
                                              Website URL</font><br>
                                              <input type="radio" name="Browse" value="MailCity">
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">City</font><br>
                                              <input type="radio" name="Browse" value="MailState">
                                              <font face="verdana,arial,helvetica" size="1" color="#333366">State</font><br>
                                            </td>
                                          </tr>
                                          <tr> 
                                            <td width="200" align="center" height="35" valign="middle"> 
                                              <input type="submit" value="Browse DISTs" class="inputbut">
                                            </td>
                                          </tr>
                                        </table>
</form>
                                      </td>
                                      <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    </tr>
                                    <tr> 
                                      <td width="15" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                      <td height="15" align="center" width="318" valign="top" bgcolor="#F2F2F7" colspan="2"><img src="images/verticalbar.gif" width="15" height="15"></td>
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
</center>
                      </td>
                    </tr>
                  </table>
                  </td>
              </tr>
            </table>
<br>
          </td>
        </tr>
      </table>    </td>
  </tr>
</table>
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
<title>Shark Tank Admin System - Inventory ( Stand-Alone Products )</title>
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
<title>Shark Tank Admin System - Inventory ( Stand-Alone Products )</title>
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
</body>
</html>

EOF
}
}
exit;