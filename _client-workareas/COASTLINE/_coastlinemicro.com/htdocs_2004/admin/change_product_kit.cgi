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

## If SAVING
if (($FORM{'DROPIN'}) && ($FORM{'CMPartNum'})) {

## TOP HTML TEMPLATE
&topper;

	## Crumble Form Input to Variables
	$Numero = "$FORM{'Numero'}";
	$CMPartNum = "$FORM{'CMPartNum'}";
	$MediaCode = "$FORM{'Multimedia'}";
	$PricingClass = "$FORM{'PricingClass'}";
	$ItemName = "$FORM{'ItemName'}";
	$Description = "$FORM{'Description'}";	
	$TechSpecs = "$FORM{'TechSpecs'}";
	$Keywords = "$FORM{'Keywords'}";
	$SmallLogo = "$FORM{'SmallLogo'}";
	$LargeLogo = "$FORM{'LargeLogo'}";
	$Warranty = "$FORM{'Warranty'}";
	$RelatedProd = "$FORM{'RelatedProd'}";
	$Accessories = "$FORM{'Accessories'}";
	$Part1Name = "$FORM{'Part1Name'}"; $Part1Number = "$FORM{'Part1Number'}"; $Part1Type = "$FORM{'Part1Type'}"; $Part1Count = "$FORM{'Part1Count'}";
	if ($Part1Number ne "null" || $Part1Number ne "Null" || $Part1Number ne "NULL" || $Part1Number ne "") { $Part2Name = "$FORM{'Part2Name'}"; $Part2Number = "$FORM{'Part2Number'}"; $Part2Type = "$FORM{'Part2Type'}"; $Part2Count = "$FORM{'Part2Count'}"; }
	if ($Part2Number ne "null" || $Part2Number ne "Null" || $Part2Number ne "NULL" || $Part2Number ne "") { $Part3Name = "$FORM{'Part3Name'}"; $Part3Number = "$FORM{'Part3Number'}"; $Part3Type = "$FORM{'Part3Type'}"; $Part3Count = "$FORM{'Part3Count'}"; }
	if ($Part3Number ne "null" || $Part3Number ne "Null" || $Part3Number ne "NULL" || $Part3Number ne "") { $Part4Name = "$FORM{'Part4Name'}"; $Part4Number = "$FORM{'Part4Number'}"; $Part4Type = "$FORM{'Part4Type'}"; $Part4Count = "$FORM{'Part4Count'}"; }
	if ($Part4Number ne "null" || $Part4Number ne "Null" || $Part4Number ne "NULL" || $Part4Number ne "") { $Part5Name = "$FORM{'Part5Name'}"; $Part5Number = "$FORM{'Part5Number'}"; $Part5Type = "$FORM{'Part5Type'}"; $Part5Count = "$FORM{'Part5Count'}"; }
	if ($Part5Number ne "null" || $Part5Number ne "Null" || $Part5Number ne "NULL" || $Part5Number ne "") { $Part6Name = "$FORM{'Part6Name'}"; $Part6Number = "$FORM{'Part6Number'}"; $Part6Type = "$FORM{'Part6Type'}"; $Part6Count = "$FORM{'Part6Count'}"; }
	if ($Part6Number ne "null" || $Part6Number ne "Null" || $Part6Number ne "NULL" || $Part6Number ne "") { $Part7Name = "$FORM{'Part7Name'}"; $Part7Number = "$FORM{'Part7Number'}"; $Part7Type = "$FORM{'Part7Type'}"; $Part7Count = "$FORM{'Part7Count'}"; }
	if ($Part7Number ne "null" || $Part7Number ne "Null" || $Part7Number ne "NULL" || $Part7Number ne "") { $Part8Name = "$FORM{'Part8Name'}"; $Part8Number = "$FORM{'Part8Number'}"; $Part8Type = "$FORM{'Part8Type'}"; $Part8Count = "$FORM{'Part8Count'}"; }
	if ($Part8Number ne "null" || $Part8Number ne "Null" || $Part8Number ne "NULL" || $Part8Number ne "") { $Part9Name = "$FORM{'Part9Name'}"; $Part9Number = "$FORM{'Part9Number'}"; $Part9Type = "$FORM{'Part9Type'}"; $Part9Count = "$FORM{'Part9Count'}"; }
	if ($Part9Number ne "null" || $Part9Number ne "Null" || $Part9Number ne "NULL" || $Part9Number ne "") { $Part10Name = "$FORM{'Part10Name'}"; $Part10Number = "$FORM{'Part10Number'}"; $Part10Type = "$FORM{'Part10Type'}"; $Part10Count = "$FORM{'Part10Count'}"; }
	if ($Part10Number ne "null" || $Part10Number ne "Null" || $Part10Number ne "NULL" || $Part10Number ne "") { $Part11Name = "$FORM{'Part11Name'}"; $Part11Number = "$FORM{'Part11Number'}"; $Part11Type = "$FORM{'Part11Type'}"; $Part11Count = "$FORM{'Part11Count'}"; }
	if ($Part11Number ne "null" || $Part11Number ne "Null" || $Part11Number ne "NULL" || $Part11Number ne "") { $Part12Name = "$FORM{'Part12Name'}"; $Part12Number = "$FORM{'Part12Number'}"; $Part12Type = "$FORM{'Part12Type'}"; $Part12Count = "$FORM{'Part12Count'}"; }
	if ($Part12Number ne "null" || $Part12Number ne "Null" || $Part12Number ne "NULL" || $Part12Number ne "") { $Part13Name = "$FORM{'Part13Name'}"; $Part13Number = "$FORM{'Part13Number'}"; $Part13Type = "$FORM{'Part13Type'}"; $Part13Count = "$FORM{'Part13Count'}"; }
	if ($Part13Number ne "null" || $Part13Number ne "Null" || $Part13Number ne "NULL" || $Part13Number ne "") { $Part14Name = "$FORM{'Part14Name'}"; $Part14Number = "$FORM{'Part14Number'}"; $Part14Type = "$FORM{'Part14Type'}"; $Part14Count = "$FORM{'Part14Count'}"; }
	if ($Part14Number ne "null" || $Part14Number ne "Null" || $Part14Number ne "NULL" || $Part14Number ne "") { $Part15Name = "$FORM{'Part15Name'}"; $Part15Number = "$FORM{'Part15Number'}"; $Part15Type = "$FORM{'Part15Type'}"; $Part15Count = "$FORM{'Part15Count'}"; }
	$ActionUser = "$Cookies{'Username'}";
	
{
print <<EOF

<table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update Inventory (Kit)</b></font></td>
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
	use DBI; 
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("UPDATE LOW_PRIORITY Products 
							 SET MediaCode='$MediaCode', 
							 PricingClass='$PricingClass', 
							 ItemName='$ItemName', 
							 Description='$Description', 
							 TechSpecs='$TechSpecs', 
							 Keywords='$Keywords', 
							 SmallPhoto='$SmallLogo', 
							 LargePhoto='$LargeLogo', 
							 Warranty='$Warranty', 
							 RelatedProd='$RelatedProd', 
							 Accessories='$Accessories', 
							 ModifiedBy='$ActionUser', 
							 ModifiedOn=Null 
							 WHERE CMPartNum='$CMPartNum'");
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish; 
	my $sth = $dbh->prepare("UPDATE LOW_PRIORITY Kits 
							 SET Part1Name='$Part1Name', Part1Number='$Part1Number', Part1Type='$Part1Type', Part1Count='$Part1Count', 
							 Part2Name='$Part2Name', Part2Number='$Part2Number', Part2Type='$Part2Type', Part2Count='$Part2Count', 
							 Part3Name='$Part3Name', Part3Number='$Part3Number', Part3Type='$Part3Type', Part3Count='$Part3Count', 
							 Part4Name='$Part4Name', Part4Number='$Part4Number', Part4Type='$Part4Type', Part4Count='$Part4Count', 
							 Part5Name='$Part5Name', Part5Number='$Part5Number', Part5Type='$Part5Type', Part5Count='$Part5Count', 
							 Part6Name='$Part6Name', Part6Number='$Part6Number', Part6Type='$Part6Type', Part6Count='$Part6Count', 
							 Part7Name='$Part7Name', Part7Number='$Part7Number', Part7Type='$Part7Type', Part7Count='$Part7Count', 
							 Part6Name='$Part8Name', Part8Number='$Part8Number', Part8Type='$Part8Type', Part8Count='$Part8Count', 
							 Part9Name='$Part9Name', Part9Number='$Part9Number', Part9Type='$Part9Type', Part9Count='$Part9Count', 
							 Part10Name='$Part10Name', Part10Number='$Part10Number', Part10Type='$Part10Type', Part10Count='$Part10Count', 
							 Part11Name='$Part11Name', Part11Number='$Part11Number', Part11Type='$Part11Type', Part11Count='$Part11Count', 
							 Part12Name='$Part12Name', Part12Number='$Part12Number', Part12Type='$Part12Type', Part12Count='$Part12Count', 
							 Part13Name='$Part13Name', Part13Number='$Part13Number', Part13Type='$Part13Type', Part13Count='$Part13Count', 
							 Part14Name='$Part14Name', Part14Number='$Part14Number', Part14Type='$Part14Type', Part14Count='$Part14Count', 
							 Part15Name='$Part15Name', Part15Number='$Part15Number', Part15Type='$Part15Type', Part15Count='$Part15Count', 
							 ModifiedBy='$ActionUser', 
							 ModifiedOn=Null 
							 WHERE Parent='$CMPartNum'");
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish; 
	$dbh->disconnect; 	
	print "<center><br><b>Inventory Updated</b><br><br>The the changes you have made to <b>$ItemName ($CMPartNum)</b> have been successfully saved to the system.<br><br><form><input type=\"button\" value=\"Back to Kit: $CMPartNum\" onClick=\"javascript:location.href='change_product_kit.cgi?CMPartNum=$CMPartNum'\" class=\"inputbut\"><br><br><input type=\"button\" value=\"View/Add/Update Inventory\" onClick=\"javascript:parent.location.href='change_product.cgi'\" class=\"inputbut\"><br></center><br><br></font>";
	
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
elsif (($FORM{'DELETEIT'}) && ($FORM{'CMPartNum'})) {

## TOP HTML TEMPLATE
&topper;

	## Crumble Form Input to Variables
	my $CMPartNum = "$FORM{'CMPartNum'}";
	my $ActionUser = "$Cookies{'Username'}";

{
print <<EOF

<table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update Inventory (Kit)</b></font></td>
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
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("DELETE FROM Products WHERE CMPartNum='$CMPartNum'");
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
	my $sth = $dbh->prepare("DELETE FROM Kits WHERE Parent='$CMPartNum'");
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
	
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
elsif ($FORM{'CMPartNum'}) {

	## Crumble Form Input to Variables
	my $CMPartNum = "$FORM{'CMPartNum'}";
	my $PricingClass = "$FORM{'PricingClass'}";
	my $ActionUser = "$Cookies{'Username'}";

	##----------->>> Grab DIST Account Information
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	$count=0;
	my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$CMPartNum' AND KitCode != 'NULL'");
	$sth->execute or die "Unable to execute query\n";
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$SavedProductID = $row[0];
		$SavedCMPartNum = $row[1];
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
		$SavedModifiedBy = $row[28];
		$SavedIngramPartNum = $row[29];
		$SavedTechDataPartNum = $row[30];
		$SavedSynnexPartNum = $row[31];
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
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update Inventory (Kit)</b></font></td>
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
<br><b>No Matching Records Found</b><ul><li>The Coastline Micro Part Number you specified does not seem to be a <b>Kit</b>, as you specified.</li><li>Are you sure <b>$CMPartNum</b> isn't actually a stand-alone item in the system and not a kit?</li></ul><form><center><input type="button" value="Try Again" onClick="javascript:history.go('-1')" class="inputbut"></center><br>
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

	##----------->>> Grab KIT Information
	$count=0;
	$PartCount=0;
	my $sth = $dbh->prepare("SELECT * FROM Kits WHERE Parent='$CMPartNum'");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$SavedKitID = $row[0]; $SavedParent = $row[1];
		push(@Parts,"$row[2],,,,,$row[3],,,,,$row[4],,,,,$row[5]"); $SavedPart1Number = "$row[3]"; $Numero=1;
		if (($SavedPart1Number eq "") || ($SavedPart1Number eq " ") || ($SavedPart1Number eq "Null") || ($SavedPart1Number eq "NULL")) { } else { push(@Parts,"$row[6],,,,,$row[7],,,,,$row[8],,,,,$row[9]"); $SavedPart2Number = "$row[7]"; $Numero=2; }
		if (($SavedPart2Number eq "") || ($SavedPart2Number eq " ") || ($SavedPart2Number eq "Null") || ($SavedPart2Number eq "NULL")) { } else { push(@Parts,"$row[10],,,,,$row[11],,,,,$row[12],,,,,$row[13]"); $SavedPart3Number = "$row[11]"; $Numero=3; }
		if (($SavedPart3Number eq "") || ($SavedPart3Number eq " ") || ($SavedPart3Number eq "Null") || ($SavedPart3Number eq "NULL")) { } else { push(@Parts,"$row[14],,,,,$row[15],,,,,$row[16],,,,,$row[17]"); $SavedPart4Number = "$row[15]"; $Numero=4; }
		if (($SavedPart4Number eq "") || ($SavedPart4Number eq " ") || ($SavedPart4Number eq "Null") || ($SavedPart4Number eq "NULL")) { } else { push(@Parts,"$row[18],,,,,$row[19],,,,,$row[20],,,,,$row[21]"); $SavedPart5Number = "$row[19]"; $Numero=5; }
		if (($SavedPart5Number eq "") || ($SavedPart5Number eq " ") || ($SavedPart5Number eq "Null") || ($SavedPart5Number eq "NULL")) { } else { push(@Parts,"$row[22],,,,,$row[23],,,,,$row[24],,,,,$row[25]"); $SavedPart6Number = "$row[23]"; $Numero=6; }
		if (($SavedPart6Number eq "") || ($SavedPart6Number eq " ") || ($SavedPart6Number eq "Null") || ($SavedPart6Number eq "NULL")) { } else { push(@Parts,"$row[26],,,,,$row[27],,,,,$row[28],,,,,$row[29]"); $SavedPart7Number = "$row[27]"; $Numero=7; }
		if (($SavedPart7Number eq "") || ($SavedPart7Number eq " ") || ($SavedPart7Number eq "Null") || ($SavedPart7Number eq "NULL")) { } else { push(@Parts,"$row[30],,,,,$row[31],,,,,$row[32],,,,,$row[33]"); $SavedPart8Number = "$row[31]"; $Numero=8; }
		if (($SavedPart8Number eq "") || ($SavedPart8Number eq " ") || ($SavedPart8Number eq "Null") || ($SavedPart8Number eq "NULL")) { } else { push(@Parts,"$row[34],,,,,$row[35],,,,,$row[36],,,,,$row[37]"); $SavedPart9Number = "$row[35]"; $Numero=9; }
		if (($SavedPart9Number eq "") || ($SavedPart9Number eq " ") || ($SavedPart9Number eq "Null") || ($SavedPart9Number eq "NULL")) { } else { push(@Parts,"$row[38],,,,,$row[39],,,,,$row[40],,,,,$row[41]"); $SavedPart10Number = "$row[39]"; $Numero=10; }
		if (($SavedPart10Number eq "") || ($SavedPart10Number eq " ") || ($SavedPart10Number eq "Null") || ($SavedPart10Number eq "NULL")) { } else { push(@Parts,"$row[42],,,,,$row[43],,,,,$row[44],,,,,$row[45]"); $SavedPart11Number = "$row[43]"; $Numero=11; }
		if (($SavedPart11Number eq "") || ($SavedPart11Number eq " ") || ($SavedPart11Number eq "Null") || ($SavedPart11Number eq "NULL")) { } else { push(@Parts,"$row[46],,,,,$row[47],,,,,$row[48],,,,,$row[49]"); $SavedPart12Number = "$row[47]"; $Numero=12; }
		if (($SavedPart12Number eq "") || ($SavedPart12Number eq " ") || ($SavedPart12Number eq "Null") || ($SavedPart12Number eq "NULL")) { } else { push(@Parts,"$row[50],,,,,$row[51],,,,,$row[52],,,,,$row[53]"); $SavedPart13Number = "$row[51]"; $Numero=13; }
		if (($SavedPart13Number eq "") || ($SavedPart13Number eq " ") || ($SavedPart13Number eq "Null") || ($SavedPart13Number eq "NULL")) { } else { push(@Parts,"$row[54],,,,,$row[55],,,,,$row[56],,,,,$row[57]"); $SavedPart14Number = "$row[55]"; $Numero=14; }
		if (($SavedPart14Number eq "") || ($SavedPart14Number eq " ") || ($SavedPart14Number eq "Null") || ($SavedPart14Number eq "NULL")) { } else { push(@Parts,"$row[58],,,,,$row[59],,,,,$row[60],,,,,$row[61]"); $SavedPart15Number = "$row[59]"; $Numero=15; }
		$SavedAddedBy2 = $row[62]; $SavedAddedOn2 = $row[63]; $SavedModifiedBy2 = $row[64]; $SavedModifiedOn2 = $row[65];
		## Re-Structure data as necessary
		$AddYear = substr($SavedAddedOn2, 0, 2);
		$AddMonth = substr($SavedAddedOn2, 2, 2);
		$AddDay = substr($SavedAddedOn2, 4, 2);
		$ModYear = substr($SavedModifiedOn2, 0, 2);
		$ModMonth = substr($SavedModifiedOn2, 2, 2);
		$ModDay = substr($SavedModifiedOn2, 4, 2);
		$count++;
}
$sth->execute or die "Unable to execute query\n"; 
$sth->finish;

##----------->>> IF ADDING A COMPONENT MAKE ADD ONE TO NUMERO THE TABLE MAKER
if ($FORM{'AddComponent'} eq "1") { $Numero++; }

##----------->>> START DYNAMO WINDOW STUFF
	$browser = "$ENV{'HTTP_USER_AGENT'}";
	## DYNAMIC BROWSER PLACEMENTS
	if ($browser =~ "MSIE" || $browser =~ "Netscape6" || $browser =~ "netscape6" || $browser =~ "netscape5" || $browser =~ "Netscape5") { $zindex = ""; }
	else { $zindex = "z-index:5"; }

##----------->>> PLACE WINDOW USING HOW MANY COMPONENTS THERE ARE
##----------->>> PLACE WINDOW USING HOW MANY COMPONENTS THERE ARE
$StartTop = 580;
$NumCalc=$Numero*107;
$FromTop = $StartTop + $NumCalc; 

$divcont = "#divCont{position:absolute; overflow:hidden; left:25%; top:$FromTop; clip:rect(0,300,450,0); height:450; width:300;}";
$divload = "#divLoad{position:absolute; left:25%; top:$FromTop; clip:rect(0,300,450,0); height:450; width:300; visibility:hidden;}";	
$divArrows = "#divArrows{position:absolute; left:0; top:1155; z-index:25; visibility:hidden}";
$divBground = "#bground{position:absolute; left:0; top:0; clip:rect(0,1,1,0); height:1; width:1;$zindex}";
##----------->>> END DYNAMO WINDOW STUFF


##----------->>> WHOIS IS THE MAIN DIST?
if ($SavedDISTCode =~ "Ingram") { $LeIngram="checked"; }
elsif ($SavedDISTCode =~ "TechData") { $LeTechData="checked"; }
else { $LeSynnex="checked"; }

{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - Shark Tank Admin System - Inventory ( Kits )</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="admincss.cgi" Type="text/css">
<script language="Javascript" src="js/mousetable.js"></script>
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
TheAccess = document.forms[0].TheAccess;
AllProducts = document.forms[0].AllProducts; 
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
if (thisone == "$SavedCMPartNum") { }
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
var TheAccess  = document.forms[0].TheAccess;
var sizer = TheAccess.options.length;
for(var i = (sizer-1); i >= 0; i--) {
if ((TheAccess.options[i] != null) && (TheAccess.options[i].selected == true)) {
TheAccess.options[i] = null;
      }
   }
}


function makeRelation() {
TheRelated = document.forms[0].TheRelated;
AllProducts = document.forms[0].AllProducts; 
var sizer = TheRelated.length;
for(var i = 0; i < AllProducts.length; i++) {
if ((AllProducts.options[i] != null) && (AllProducts.options[i].selected)) {
var there = false;
for(var count = 0; count < sizer; count++) {
if (TheRelated.options[count] != null) {
if (AllProducts.options[i].value == TheRelated.options[count].value) {
there = true;
break;
      }
   }
}
if (there != true) {
var thisone = AllProducts.options[i].value;
if (thisone == "$SavedCMPartNum") { }
else {
TheRelated.options[sizer] = new Option(AllProducts.options[i].text); 
TheRelated.options[sizer].value = AllProducts.options[i].value;
sizer++;
}
         }
      }
   }
}

function killRelation() {
var TheRelated  = document.forms[0].TheRelated;
var sizer = TheRelated.options.length;
for(var i = (sizer-1); i >= 0; i--) {
if ((TheRelated.options[i] != null) && (TheRelated.options[i].selected == true)) {
TheRelated.options[i] = null;
      }
   }
}

function makeKitItem(cual,cual2) {
var TheItem  = document.add[cual];
var sizer = TheItem.options.length;
for(var i = (sizer-1); i >= 0; i--) {
	if ((TheItem.options[i] != null) && (TheItem.options[i].selected == true)) {
	if ((TheItem.options[i].value == "Desktop") || (TheItem.options[i].value == "Server") || (TheItem.options[i].value == "Notebook") || (TheItem.options[i].value == "Kit") || (TheItem.options[i].value == "Monitor") || (TheItem.options[i].value == "Memory") || (TheItem.options[i].value == "HardDrive") || (TheItem.options[i].value == "VideoCard") || (TheItem.options[i].value == "Peripheral") || (TheItem.options[i].value == "Printer") || (TheItem.options[i].value == "Software")) { }
	else {
		document.add['Part'+cual2].value = TheItem.options[i].text;
		document.add['Part'+cual2+'Name'].value = TheItem.options[i].text;
		document.add['Part'+cual2+'Number'].value = TheItem.options[i].value;
	}
	}
}
}

function showKitItem(cual) {
	Name = document.add['Part'+cual+'Name'].value;
	CMNum = document.add['Part'+cual+'Number'].value;
	Quan = document.add['Part'+cual+'Count'].value;
	Cost = document.add['Part'+cual+'Cost'].value;
	alert('CM Part Number: '+CMNum+'\\n\\nName: '+Name+'\\n\\nQuantity: '+Quan+'\\n\\nCalculated Price: '+Cost+'');
}

function getProducts(mua, mue) {
var missingdrop = "";
var formindex = document.add[mua].selectedIndex;
var thisone = document.add[mua].options[formindex].value;
var me = mue;

if (thisone == "BIGNULL") {
	thefirst = mue;
    missingdrop += "\\nThat is not a valid option, please select another...";
}

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    alert(missingdrop);
 	document.add(thefirst).focus();
    return false;
} 
else {
	if ((thisone == "Desktop") || (thisone == "Server") || (thisone == "Notebook") || (thisone == "Kit") || (thisone == "Monitor") || (thisone == "Memory") || (thisone == "HardDrive") || (thisone == "VideoCard") || (thisone == "Peripheral") || (thisone == "Printer") || (thisone == "Software")) {
		var b = navigator.appName;
		if (b=="Netscape") {
			mainFrame = parent.frames.botOne;
			mainFrame.frame.loadpage('pchoose.cgi?FeedMe='+me+'&ProdType='+thisone+'');
		}

		else {
			parent.botOne.frame.loadpage('pchoose.cgi?FeedMe='+me+'&ProdType='+thisone+'');
		}
	return false;
	}
}
}

function getTypes(me) {
var b = navigator.appName;
TheType = document.forms.add[me];
TheType.style.color = "333366";
var sizer = TheType.length;

// CLEARS ALL DATA ON TheType
for(var i = (sizer-1); i >= 0; i--) {
while (TheType.options[i] != null) {
TheType.options[i] = null;
	}
}

// get length after kills
var sizer = TheType.length;

// GENERATE TheType
if (me == "ProdTypes") {
	TheType.options[sizer] = new Option('Desktop PC'); TheType.options[sizer].value = 'Desktop'; sizer++;
	TheType.options[sizer] = new Option('Notebook'); TheType.options[sizer].value = 'Notebook'; sizer++;
	TheType.options[sizer] = new Option('Server'); TheType.options[sizer].value = 'Server'; sizer++;
}
	TheType.options[sizer] = new Option('Monitor'); TheType.options[sizer].value = 'Monitor'; sizer++;
	TheType.options[sizer] = new Option('Memory'); TheType.options[sizer].value = 'Memory'; sizer++;
	TheType.options[sizer] = new Option('Hard Drive'); TheType.options[sizer].value = 'HardDrive'; sizer++;
	TheType.options[sizer] = new Option('Video Card'); TheType.options[sizer].value = 'VideoCard'; sizer++;
	TheType.options[sizer] = new Option('Peripheral'); TheType.options[sizer].value = 'Peripheral'; sizer++;
	TheType.options[sizer] = new Option('Printer'); TheType.options[sizer].value = 'Printer'; sizer++;
	TheType.options[sizer] = new Option('Software'); TheType.options[sizer].value = 'Software'; sizer++;
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
	image = document.add(me).value;
	if (document.add(me).value == null || document.add(me).value == "" || document.add(me).value == " ") {
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

function noChange(este) {
	if (este == "MultimediaBut") {
		alert('Sorry, you cannot directly edit the contents of this field. If you would like to change the multimedia object being used by this field click \\'Get Mine\\'. To Preview the multimedia obejct curretnly being used click the \\'Preview\\' button.');
		document.add(este).focus();
	}
	else {
		alert('Sorry, you cannot directly edit the contents of this field. If you would like to change the image being used by this field click \\'Get Mine\\'. To Preview the image currently being used click the \\'Preview\\' button.');
		document.add(este).focus();
	}
}


function clearUs(cual) {
// CLEARS ALL DATA DYNAMIC
ThisOne = document.add[cual];
var sizer = ThisOne.length;
	for(var i = (sizer-1); i >= 0; i--) {
		while (ThisOne.options[i] != null) {
			if (ThisOne.options[i].value == "BIGNULL") {
				ThisOne.options[i] = null;
			}
		}
	}
}

function addOne() {
if ($Numero == 15) { alert('Sorry, the system only allows a maximum of 15 components per Kit. If you would like to have more components with this Kit we suggest you use configure other Kits to use as components of this Kit. Using such a method would allow you to virtually add an unlimited quantity of components to any given Kit.'); }
else { location.href = "$script?CMPartNum=$CMPartNum&AddComponent=1"; }
}

function priceMe() {
document.add.TallyMe.value = 1;
document.add.submit();
}
</script>
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
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:ifrinit();clearUs('Warranty');clearUs('TheRelated');clearUs('TheAccess');clearUs('AllProducts');clearUs('ProdTypes');getTypes('ProdTypes');">
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
<form method="post" action="$script" name="add" onSubmit="return checkForm();">
  <table width="100%" border="0" height="100%" cellpadding="0" cellspacing="0">
    <tr valign="top"> 
      <td width="20%">$legal</td>
      <td align="center" width="80%"> 
        <table width="95%" border="0" cellspacing="0" cellpadding="0">
          <tr> 
            <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update Product (Kit - $SavedPricingClass)</b></font></td>
            <td align="right" width="50%">&nbsp;</td>
          </tr>
          <tr> 
            <td colspan="2"> 
              <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
                <tr bordercolor="#333366"> 
                  <td width="100%" align="center" valign="top" height="250"> 
                    <table width="100%" border="0" cellspacing="0" cellpadding="5">
                      <tr valign="top" align="center"> 
                        <td bordercolor="#333366" class="tableBORDER" colspan="2"> 
                          <br>
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
                  <td height="20" bgcolor="#8F8FAB" width="96%" colspan="2"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Kit 
                    Information</font></b></font></td>
                  <td width="2%" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                </tr>
                <tr> 
                  <td colspan="4" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                </tr>
                <tr> 
                  <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                  <td height="30" align="center" width="48%" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Product 
                    Name </b></font></td>
                  <td height="30" align="center" width="48%" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Indexing 
                    Keywords</b></font></td>
                  <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                </tr>
                <tr> 
                  <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                  <td height="35" align="center" width="48%" valign="middle"> 
                    <input type="text" name="ItemName" size="35" class="inputtext35" value="$SavedItemName">
                    <br>
                    <input type="hidden" name="CMPartNum" value="$CMPartNum">
                    <input type="hidden" name="PricingClass" value="$SavedPricingClass">
                    <input type="hidden" name="Numero" value="$Numero">
                    <input type="hidden" name="Description" value="NONE">
                  </td>
                  <td height="35" align="center" width="48%" valign="middle"> 
                    <input type="text" size="35" class="inputtext35" name="Keywords" value="$SavedKeywords">
                  </td>
                  <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                </tr>
                <tr> 
                  <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                  <td height="30" align="center" width="48%" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Technical 
                    Specifications</b></font></td>
                  <td height="30" align="center" width="48%" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Warranty</b></font></td>
                  <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                </tr>
                <tr> 
                  <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                  <td height="75" align="center" width="48%"> 
                    <textarea name="TechSpecs" cols="50" class="textarea2" rows="2">$SavedTechSpecs</textarea>
                  </td>
                  <td height="75" align="center" width="48%"> 
                    <textarea name="Warranty" cols="50" class="textarea2" rows="2">$SavedWarranty</textarea>
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
<table width="95%" border="0" cellspacing="0" cellpadding="0" align="center"><tr><td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td></tr><tr><td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td><td width="100%" valign="top">
<table border="0" cellspacing="0" cellpadding="0" width="100%">
<tr><td width="2%" height="15" bgcolor="#8F8FAB">&nbsp;</td><td height="20" bgcolor="#8F8FAB" width="96%" colspan="5"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Kit Configuration</font></b></font></td><td width="2%" height="15" bgcolor="#8F8FAB">&nbsp;</td></tr>
<tr><td colspan="7" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td></tr>

<!--ONE-->
EOF
}

$Counter=0;
foreach (1 .. $Numero) {
$Counter++;

if ($Numero eq $Counter) {
	$Name = "";
	$Number = "";
	$LaCuenta = "0";
	$Type = "";
	$IsShown = "checked";
	$Cost = "0.00";
}
else {
	@MyParts = split(/,,,,,/, $Parts[0]);
	shift(@Parts);
	$Name = $MyParts[0];
	$Number = $MyParts[1];
	$LaCuenta = $MyParts[2];
	$Type = $MyParts[3];
	if ($Type eq "HIDE") { $IsHidden = "checked"; $IsShown = ""; }
	else { $IsHidden = ""; $IsShown = "checked"; }
	if ($LaCuenta <= 0) { $LaCuenta=1; };
	
	my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$Number' ORDER BY ItemName ASC");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$Cost = $row[21] * $LaCuenta;
		$Cost = sprintf("%.2f", $Cost);
		push(@Totals,"$Cost");
	}
	$sth->finish;
	if ($Number eq "") { $Cost = "0.00"; $LaCuenta = "0"; }
}

##------------------->>> Calculate total for all components
$TheTotal=0;
foreach $Total (@Totals) {
	$TheTotal = $TheTotal + $Total;
	$TheTotal = sprintf("%.2f", $TheTotal);
}
	
{
print <<EOF

<tr><td width="2%" bgcolor="#F2F2F7">&nbsp;</td><td height="20" align="center" width="96%" valign="middle" colspan="5">
                                    <table border="0" cellspacing="0" cellpadding="0" width="100%">
                                      <tr align="center"> 
                                        <td height="30" width="96%" valign="middle" colspan="7" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font size="2">&nbsp;&nbsp;Component 
                                          #$Counter\ </font></b></font></td>
                                      </tr>
                                      <tr> 
                                        <td align="center" rowspan="2" valign="middle" width="18%"> 
                                          <table border="1" cellspacing="0" cellpadding="3" bordercolor="#F2F2F7" onMouseOver="runto('ebebeb')" onMouseOut="runback('white')" align="center" width="100%">
                                            <tr align="center"> 
                                              <td width="50%" height="30"><font face="verdana,arial,helvetica" size="1"><a href="javascript:getTypes('Part'+'$Counter'+'Select');"><b>Product 
                                                Types</b></a></font></td>
                                            </tr>
                                            <tr align="center"> 
                                              <td width="50%" height="30"><font face="verdana,arial,helvetica" size="1"><a href="javascript:makeKitItem('Part'+'$Counter'+'Select','$Counter')"><b>Use 
                                                Selected</b></a></font></td>
                                            </tr>
                                          </table>
                                        </td>
                                        <td height="25" align="center" width="30%" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Inventory 
                                          Reader </b></font></td>
                                        <td height="25" align="center" width="6%" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Qty.</b></font></td>
                                        <td height="25" align="center" width="12%" valign="middle" colspan="2"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Visible?</b></font></td>
                                        <td height="25" align="center" width="10%" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Cost</b></font></td>
                                        <td height="25" align="center" width="20%" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Component 
                                          View</b></font></td>
                                      </tr>
                                      <tr> 
                                        <td height="35" align="center" width="30%" valign="middle"> 
                                          <select name="Part$Counter\Select" class="inputtextSP" onChange="javascript:getProducts('Part'+'$Counter'+'Select','Part'+'$Counter'+'Select');">
                                            <option value="BIGNULL">0000000000000000</option>
                                          </select>
                                        </td>
                                        <td height="35" align="center" width="6%" valign="middle"> 
                                          <input type="text" name="Part$Counter\Count" size="3" class="inputtext3" tabindex="5" value="$LaCuenta">
                                        </td>
                                        <td height="35" align="right" width="6%" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366">Y&nbsp; 
                                          <input type="radio" name="Part$Counter\Type" value="SHOW" $IsShown>
                                          </font></td>
                                        <td height="35" align="center" width="6%" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366"> 
                                          <input type="radio" name="Part$Counter\Type" value="HIDE" $IsHidden>
                                          N</font></td>
                                        <td height="35" align="center" width="10%" valign="middle"> 
                                          <input type="text" size="7" class="inputtext7" name="Part$Counter\Cost" value="$Cost" onFocus="Javascript:showKitItem('$Counter');">
                                        </td>
                                        <td height="35" align="center" width="20%" valign="middle">
                                          <input type="text" size="15" class="inputtext15" name="Part$Counter" value="$Name" onFocus="Javascript:showKitItem('$Counter');">
                                          <input type="hidden" name="Part$Counter\Name" value="$Name">
                                          <input type="hidden" name="Part$Counter\Number" value="$Number">
                                        </td>
                                      </tr>
                                    </table>
                                  </td><td width="2%" bgcolor="#F2F2F7">&nbsp;</td></tr>
<tr><td width="2%" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td><td height="15" align="center" width="96%" valign="top" bgcolor="#F2F2F7" colspan="5"><img src="images/verticalbar.gif" width="15" height="15"><img src="images/verticalbar.gif" width="15" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td><td width="2%" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td></tr>

<!--TWO-->
EOF
}

}

{
print <<EOF
                          
<tr><td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
<td height="0" align="center" width="96%" valign="bottom" colspan="5">
<table border="1" cellspacing="0" cellpadding="3" bordercolor="#F2F2F7" align="center" width="100%">
<tr align="center">
<td height="35" width="100%">                                            <table border="1" cellspacing="0" cellpadding="3" bordercolor="#FFFFFF" onMouseOver="runto('EB0000')" onMouseOut="runback('F2F2F7')" align="center" width="500" bgcolor="#F2F2F7">
                                              <tr align="center"> 
                                                <td width="50%" height="30"> 
                                                  
                                                <input type="text" name="Cost" value="Kit Total Price = \$$TheTotal" size="15" class="prices">
                                                </td>
                                                <td width="50%" height="30"><font face="verdana,arial,helvetica" size="1"> 
                                                  <input type="submit" value="< < < Re-Calculate Total" class="pricebut">
                                                  </font></td>
                                              </tr>
                                            </table></td>
</tr>
</table>
<table border="1" cellspacing="0" cellpadding="3" bordercolor="#F2F2F7" onMouseOver="runto('ebebeb')" onMouseOut="runback('white')" align="center" width="100%">
<tr align="center">
<td width="25%" height="30"><font face="verdana,arial,helvetica" size="1"><a href="javascript:addOne();"><b>Add Another Component</b></a></font></td>
<td width="25%" height="30"><font face="verdana,arial,helvetica" size="1"><a href="javascript:prevKit();"><b>Preview as Configured</b></a></font></td>
</tr>
</table></td><td width="2%" bgcolor="#F2F2F7">&nbsp;</td></tr>
<tr><td width="2%" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td><td height="15" align="center" width="96%" valign="top" bgcolor="#F2F2F7" colspan="5"><img src="images/verticalbar.gif" width="15" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td><td width="2%" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td></tr></table></td>
<td bgcolor="#8F8FAB" width="1" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td></tr>
<tr><td width="100%" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td></tr></table>
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Small 
                                      Logo</font></b></font></td>
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
                                      <input type="text" name="SmallLogo" size="7" class="inputtext7" value="$SavedSmallLogo" onFocus="Javascript:noChange('SmallLogoBut');">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Large 
                                      Logo</font></b></font></td>
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
                                      <input type="text" name="LargeLogo" size="7" class="inputtext7" value="$SavedLargeLogo" onFocus="Javascript:noChange('LargeLogoBut');">
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
                          
                        </td>
                      </tr>
                      <tr> 
                        <td width="100%" align="center" height="27" bgcolor="#F2F2F7" class="tableBG" colspan="2"><font face="verdana,arial,helvetica" size="2" color="#333366"><b>Accessories 
                          and Related Products</b></font></td>
                      </tr>
                      <tr valign="bottom" align="center"> 
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
                                      To make a product Related to this product 
                                      choose a product from the Inventory Generator 
                                      then click <font color="#EB0000">Accessory</font> 
                                      to make the selected product an accessory. 
                                      To clear the Inventory Generator list simply 
                                      click the <font color="#EB0000">Clear List</font> 
                                      button. These same techniques apply to making 
                                      a product Relationship. </font></td>
                                    <td width="15" bgcolor="#F2F2F7" height="15">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="15" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="45" align="center"> 
                                      <table width="270" border="0" cellspacing="0" cellpadding="0" bgcolor="#FFFFFF" align="center">
                                        <tr> 
                                          <td align="center" width="100%" height="25"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Product 
                                            Types</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td align="center" width="100%" height="45"> 
                                            <select name="ProdTypes" class="inputtext" onChange="javascript:getProducts('ProdTypes','AllProducts');">
                                              <option value="BIGNULL">0000000000000000</option>
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
                                            <nobr> 
                                            <input type="Button" value="Clear List" onClick="javascript:getTypes('ProdTypes');" class="inputbut" name="All">
                                            <input type="Button" value="Related" onClick="javascript:makeRelation();" class="inputbut" name="Button33">
                                            <input type="Button" value="Accessory" onClick="javascript:makeAccessory();" class="inputbut" name="Button332">
                                            </nobr> </td>
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
                                    <td height="20" bgcolor="#8F8FAB" width="268"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Accessories 
                                      and Related Products</font></b></font></td>
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
                                      or as a related product just select the 
                                      product from the 'Accessories' or 'Related 
                                      Products' list you would like to remove 
                                      and click the <font color="#EB0000">Remove</font> 
                                      button <font color="#EB0000">BELOW</font> 
                                      the list you want to be affected.</font></td>
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
                                            <input type="button" value="Preview" onClick="javascript:alert(document.forms[0].TheAccess.value);" class="inputbut" name="button252">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="100%" valign="top" align="center" height="15" bgcolor="#F2F2F7">&nbsp;</td>
                                        </tr>
                                        <tr> 
                                          <td align="center" width="100%" height="25" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Related 
                                            Products</b></font></td>
                                        </tr>
                                        <tr> 
                                          <td width="100%" valign="top" align="center"> 
                                            <select name="TheRelated" size="8" multiple class="prodguinea">
                                              <option value="BIGNULL">0000000000000000</option>
                                            </select>
                                            <input type="hidden" name="RelatedProd">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="100%" valign="middle" height="45" align="center"> 
                                            <input type="Button" value="Remove " onClick="javascript:killRelation();" class="inputbut" name="Button32">
                                            <input type="button" value="Preview" onClick="Javascript:iPreview('Multimedia')" class="inputbut" name="button2522">
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
TheAccess = document.forms[0].TheAccess;
var sizer = TheAccess.length;
// GETTING READY TO FEED INFO

EOF
}

@Accessories = split(/,/, $SavedAccessories);
foreach $Accessory (@Accessories) {
	my $count=0;
	my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$Accessory' ORDER BY ItemName ASC");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		my $ThyCMPartNum = $row[1];
		my $ThyItemName = $row[11];
		print "TheAccess.options[sizer] = new Option('$ThyItemName');";
		print "TheAccess.options[sizer].value = '$ThyCMPartNum';";
		print "sizer++;";
		$count++;
	}
	$sth->finish;
}
print "}";
print "</script>";

##----------->>> FEED RELATIVES
{
print <<EOF

<script language="Javascript">
function feedRelatives() {
TheRelated = document.forms[0].TheRelated;
var sizer = TheRelated.length;
// GETTING READY TO FEED INFO

EOF
}

@Relatives = split(/,/, $SavedRelatedProd);
foreach $Relative (@Relatives) {
	my $count=0;
	my $sth = $dbh->prepare("SELECT * FROM Products ORDER BY ItemName ASC");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		my $ThyCMPartNum = $row[1];
		my $ThyItemName = $row[11];
		if ($Relative eq "$ThyCMPartNum") {
			print "TheRelated.options[sizer] = new Option('$ThyItemName');";
			print "TheRelated.options[sizer].value = '$ThyCMPartNum';";
			print "sizer++;";
			$count++;
		}
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
MFGCode = document.forms[0].MFGCode;
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
	if ($MFGCode eq "$ThyMFGID") {
		print "MFGCode.options[sizer] = new Option('$ThyMFGName');";
		print "MFGCode.options[sizer].value = '$ThyMFGCode';";
		print "sizer++;";
		print "MFGCode.options[sizer].selectedIndex = MFGCode.options[sizer]";
		$count++;
	}
	else {
		print "MFGCode.options[sizer] = new Option('$ThyMFGName');";
		print "MFGCode.options[sizer].value = '$ThyMFGCode';";
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
<table width="100%" background="images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0"><tr><td width="55%" align="left" height="56">&nbsp;</td></tr></table>
</body>
</html>

EOF
}
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
<table width="100%" background="images/bot_frame_bg.jpg" height="56" align="center" cellpadding="0" cellspacing="0" border="0"><tr><td width="55%" align="left" height="56">&nbsp;</td></tr></table>
</body>
</html>

EOF
}
}
exit;