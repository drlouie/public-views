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

require ("referer.nsp"); 
require ("parse_query.nsp");
require ("date.nsp");

$browser = "$ENV{'HTTP_USER_AGENT'}";
if (($browser =~ "Mozilla/" && $browser =~ "6.") || $browser =~ "Netscape6") { $tablewidth = "100%"; $t1 = "5"; $t2 = "64%"; $t3 = "18%"; $t4 = "18%"; $t5 = "100%"; }	
else { $tablewidth = "470"; $t1 = "5"; $t2 = "339"; $t3 = "79"; $t4 = "42"; $t5 = "470"; }
if ($browser =~ "Mozilla/4.7") { $border = "border=\"1\" bordercolor=\"#333366\""; }

if ($browser =~ "MSIE 5.0" || $browser =~ "MSIE 5.5" || $browser =~ "Mozilla/4.7" || $browser =~ "MSIE 4.0") { $StartURLer="javascript:void(0);\" onClick=\"javascript:window.open"; $EndURLer=",'EMAILIT','width=485,height=590');";}
else { $StartURLer="javascript:trigger"; $EndURLer=");";}

$STANKLEGAL = `cat stank_legal.nsf`;

## ----------------->>> Must Have CMPartNum!
if ($FORM{'CMPartNum'}) {
$CMPartNum = "$FORM{'CMPartNum'}";


############################
#### TEST FOR TIGER NAS ####
############################
if ($FORM{'CMPartNum'} eq "M14P" || $FORM{'CMPartNum'} eq "M14S" || $FORM{'CMPartNum'} eq "M14SS" || $FORM{'CMPartNum'} eq "M212S" || $FORM{'CMPartNum'} eq "M212SS" || $FORM{'CMPartNum'} eq "M316S" || $FORM{'CMPartNum'} eq "M316SS") {
	$tigerNAS = "YES";
}


## ----------------->>> BACK BUTTON OR NO BACK BUTTON?
$ComingFrom = $FORM{'ComingFrom'};
if ($FORM{'ComingFrom'}) { $GoBack = "<a href=\"javascript:trigger('stank_$ComingFrom\.html?CMPartNum=$CMPartNum');\"><img src=\"images/tables/icon_back_on.gif\" width=\"60\" height=\"20\" name=\"back\" border=\"0\"></a>"; }
else { $GoBack = "<img src=\"images/tables/icon_back_off.gif\" width=\"60\" height=\"20\" name=\"back\" border=\"0\">"; }

##----------->>> Grab PRODUCTS STUFF
use DBI;
my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
$dbh->{RaiseError} = 1; 
$count=0;
my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$CMPartNum'");
$sth->execute or die "Unable to execute query\n";
my @row;
while(@row = $sth->fetchrow_array) {
	$SavedSYSCode = $row[2];
	$SavedMediaCode = $row[4];
	$SavedPricingClass = $row[10];
	$SavedItemName = $row[11];
	$SavedEmblem = $row[16];
	push(@Images, "$row[17]-----SMALL");
	$SavedLargeLogo = $row[18];
	$SavedWarranty = $row[19];
	$SavedAccessories = $row[24];
	$count++;
}
$sth->execute or die "Unable to execute query\n"; 
$sth->finish;

##----------->>> Grab system IMAGE information
foreach $Image (@Images) {
	@Estos = split(/-----/, $Image);
	$count=0;
	my $sth = $dbh->prepare("SELECT * FROM Images WHERE ImageID='$Estos[0]'");
	$sth->execute or die "Unable to execute query\n";
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$SavedFileName = $row[3];
		$SavedDesc = $row[8];
		if ($Estos[1] eq "LARGE") { push(@LargeImages, "$SavedFileName-----$SavedDesc"); }
		else { $SmallImageN = "$SavedFileName"; $SmallImageD= "$SavedDesc";  }
		$count++;
	}
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
}

##----------->>> Grab system ACCESSORY information
	@MyAccessory = split(/,/, $SavedAccessories);
	$count=0;
	foreach $Accessory (@MyAccessory) {
		my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$Accessory'");
		$sth->execute or die "Unable to execute query\n";
		my @row;
		while(@row = $sth->fetchrow_array) { 
			$AccCMNum = $row[1];
			$AccItemName = $row[11];
			push(@ProdAccessories, "$AccItemName,,,,,$AccCMNum");
			$count++;
		}
		$sth->execute or die "Unable to execute query\n"; 
		$sth->finish;
	}

##----------->>> Grab SYSTEMS STUFF
$count=0;
$PartCount=0;
my $sth = $dbh->prepare("SELECT * FROM Systems WHERE SystemID='$SavedSYSCode'");
$sth->execute or die "Unable to execute query\n"; 
my @row;
while(@row = $sth->fetchrow_array) { 
	$SavedSystemID = $row[0]; $SavedParent = $row[1]; $SavedCMSeries = $row[2]; $SavedReconfig = $row[3];
	push(@Parts,"$row[4],,,,,$row[5],,,,,$row[6],,,,,$row[7]"); $SavedMainNumbers = $row[7]; $Numero=1;
	if (($SavedMainNumbers eq "") || ($SavedMainNumbers eq " ") || ($SavedMainNumbers eq "Null") || ($SavedMainNumbers eq "NULL")) { } else { push(@Parts,"$row[8],,,,,$row[9],,,,,$row[10],,,,,$row[11]"); $SavedSub1Numbers = $row[11]; $Numero=2; }
	if (($SavedSub1Numbers eq "") || ($SavedSub1Numbers eq " ") || ($SavedSub1Numbers eq "Null") || ($SavedSub1Numbers eq "NULL")) { } else { push(@Parts,"$row[12],,,,,$row[13],,,,,$row[14],,,,,$row[15]"); $SavedSub2Numbers = $row[15]; $Numero=3; }
	if (($SavedSub2Numbers eq "") || ($SavedSub2Numbers eq " ") || ($SavedSub2Numbers eq "Null") || ($SavedSub2Numbers eq "NULL")) { } else { push(@Parts,"$row[16],,,,,$row[17],,,,,$row[18],,,,,$row[19]"); $SavedSub3Numbers = $row[19]; $Numero=4; }
	if (($SavedSub3Numbers eq "") || ($SavedSub3Numbers eq " ") || ($SavedSub3Numbers eq "Null") || ($SavedSub3Numbers eq "NULL")) { } else { push(@Parts,"$row[20],,,,,$row[21],,,,,$row[22],,,,,$row[23]"); $SavedSub4Numbers = $row[23]; $Numero=5; }
	if (($SavedSub4Numbers eq "") || ($SavedSub4Numbers eq " ") || ($SavedSub4Numbers eq "Null") || ($SavedSub4Numbers eq "NULL")) { } else { push(@Parts,"$row[24],,,,,$row[25],,,,,$row[26],,,,,$row[27]"); $SavedSub5Numbers = $row[27]; $Numero=6; }
	if (($SavedSub5Numbers eq "") || ($SavedSub5Numbers eq " ") || ($SavedSub5Numbers eq "Null") || ($SavedSub5Numbers eq "NULL")) { } else { push(@Parts,"$row[28],,,,,$row[29],,,,,$row[30],,,,,$row[31]"); $SavedSub6Numbers = $row[31]; $Numero=7; }
	if (($SavedSub6Numbers eq "") || ($SavedSub6Numbers eq " ") || ($SavedSub6Numbers eq "Null") || ($SavedSub6Numbers eq "NULL")) { } else { push(@Parts,"$row[32],,,,,$row[33],,,,,$row[34],,,,,$row[35]"); $SavedSub7Numbers = $row[35]; $Numero=8; }
	if (($SavedSub7Numbers eq "") || ($SavedSub7Numbers eq " ") || ($SavedSub7Numbers eq "Null") || ($SavedSub7Numbers eq "NULL")) { } else { push(@Parts,"$row[36],,,,,$row[37],,,,,$row[38],,,,,$row[39]"); $SavedSub8Numbers = $row[39]; $Numero=9; }
	if (($SavedSub8Numbers eq "") || ($SavedSub8Numbers eq " ") || ($SavedSub8Numbers eq "Null") || ($SavedSub8Numbers eq "NULL")) { } else { push(@Parts,"$row[40],,,,,$row[41],,,,,$row[42],,,,,$row[43]"); $SavedSub9Numbers = $row[43]; $Numero=10; }
	if (($SavedSub9Numbers eq "") || ($SavedSub9Numbers eq " ") || ($SavedSub9Numbers eq "Null") || ($SavedSub9Numbers eq "NULL")) { } else { push(@Parts,"$row[44],,,,,$row[45],,,,,$row[46],,,,,$row[47]"); $SavedSub10Numbers = $row[47]; $Numero=11; }
	if (($SavedSub10Numbers eq "") || ($SavedSub10Numbers eq " ") || ($SavedSub10Numbers eq "Null") || ($SavedSub10Numbers eq "NULL")) { } else { push(@Parts,"$row[48],,,,,$row[49],,,,,$row[50],,,,,$row[51]"); $SavedSub11Numbers = $row[51]; $Numero=12; }
	if (($SavedSub11Numbers eq "") || ($SavedSub11Numbers eq " ") || ($SavedSub11Numbers eq "Null") || ($SavedSub11Numbers eq "NULL")) { } else { push(@Parts,"$row[52],,,,,$row[53],,,,,$row[54],,,,,$row[55]"); $SavedSub12Numbers = $row[55]; $Numero=13; }
	if (($SavedSub12Numbers eq "") || ($SavedSub12Numbers eq " ") || ($SavedSub12Numbers eq "Null") || ($SavedSub12Numbers eq "NULL")) { } else { push(@Parts,"$row[56],,,,,$row[57],,,,,$row[58],,,,,$row[59]"); $SavedSub13Numbers = $row[59]; $Numero=14; }
	if (($SavedSub13Numbers eq "") || ($SavedSub13Numbers eq " ") || ($SavedSub13Numbers eq "Null") || ($SavedSub13Numbers eq "NULL")) { } else { push(@Parts,"$row[60],,,,,$row[61],,,,,$row[62],,,,,$row[63]"); $SavedSub14Numbers = $row[63]; $Numero=15; }
	if (($SavedSub14Numbers eq "") || ($SavedSub14Numbers eq " ") || ($SavedSub14Numbers eq "Null") || ($SavedSub14Numbers eq "NULL")) { } else { push(@Parts,"$row[64],,,,,$row[65],,,,,$row[66],,,,,$row[67]"); $SavedSub15Numbers = $row[67]; $Numero=16; }
	if (($SavedSub15Numbers eq "") || ($SavedSub15Numbers eq " ") || ($SavedSub15Numbers eq "Null") || ($SavedSub15Numbers eq "NULL")) { } else { push(@Parts,"$row[68],,,,,$row[69],,,,,$row[70],,,,,$row[71]"); $SavedSub16Numbers = $row[71]; $Numero=17; }
	if (($SavedSub16Numbers eq "") || ($SavedSub16Numbers eq " ") || ($SavedSub16Numbers eq "Null") || ($SavedSub16Numbers eq "NULL")) { } else { push(@Parts,"$row[72],,,,,$row[73],,,,,$row[74],,,,,$row[75]"); $SavedSub17Numbers = $row[75]; $Numero=18; }
	if (($SavedSub17Numbers eq "") || ($SavedSub17Numbers eq " ") || ($SavedSub17Numbers eq "Null") || ($SavedSub17Numbers eq "NULL")) { } else { push(@Parts,"$row[76],,,,,$row[77],,,,,$row[78],,,,,$row[79]"); $SavedSub18Numbers = $row[79]; $Numero=19; }
	if (($SavedSub18Numbers eq "") || ($SavedSub18Numbers eq " ") || ($SavedSub18Numbers eq "Null") || ($SavedSub18Numbers eq "NULL")) { } else { push(@Parts,"$row[80],,,,,$row[81],,,,,$row[82],,,,,$row[83]"); $SavedSub19Numbers = $row[83]; $Numero=20; }
	if (($SavedSub19Numbers eq "") || ($SavedSub19Numbers eq " ") || ($SavedSub19Numbers eq "Null") || ($SavedSub19Numbers eq "NULL")) { } else { push(@Parts,"$row[84],,,,,$row[85],,,,,$row[86],,,,,$row[87]"); $SavedSub20Numbers = $row[87]; $Numero=21; }
	if (($SavedSub20Numbers eq "") || ($SavedSub20Numbers eq " ") || ($SavedSub20Numbers eq "Null") || ($SavedSub20Numbers eq "NULL")) { } else { push(@Parts,"$row[88],,,,,$row[89],,,,,$row[90],,,,,$row[91]"); $SavedSub21Numbers = $row[91]; $Numero=22; }
	if (($SavedSub21Numbers eq "") || ($SavedSub21Numbers eq " ") || ($SavedSub21Numbers eq "Null") || ($SavedSub21Numbers eq "NULL")) { } else { push(@Parts,"$row[92],,,,,$row[93],,,,,$row[94],,,,,$row[95]"); $SavedSub22Numbers = $row[95]; $Numero=23; }
	if (($SavedSub22Numbers eq "") || ($SavedSub22Numbers eq " ") || ($SavedSub22Numbers eq "Null") || ($SavedSub22Numbers eq "NULL")) { } else { push(@Parts,"$row[96],,,,,$row[97],,,,,$row[98],,,,,$row[99]"); $SavedSub23Numbers = $row[99]; $Numero=24; }
	if (($SavedSub23Numbers eq "") || ($SavedSub23Numbers eq " ") || ($SavedSub23Numbers eq "Null") || ($SavedSub23Numbers eq "NULL")) { } else { push(@Parts,"$row[100],,,,,$row[101],,,,,$row[102],,,,,$row[103]"); $SavedSub24Numbers = $row[103]; $Numero=25; }
	if (($SavedSub24Numbers eq "") || ($SavedSub24Numbers eq " ") || ($SavedSub24Numbers eq "Null") || ($SavedSub24Numbers eq "NULL")) { } else { push(@Parts,"$row[104],,,,,$row[105],,,,,$row[106],,,,,$row[107]"); $SavedSub25Numbers = $row[107]; $Numero=26; }
	$SavedAddedBy2 = $row[64]; $SavedAddedOn2 = $row[65]; $SavedModifiedBy2 = $row[66]; $SavedModifiedOn2 = $row[67];
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

## to show the true amount of components
$Numero--;

##---------------------------->>> CONFIGURE SYSTEM INFORMATION AND IMAGERY FOR OUTPUT
$MainTitle = "$SavedItemName";

##--->> REFORMAT MAINTITLE
$NCount = "0";
@NameCount = split(//, $MainTitle);
foreach $NameName (@NameCount) { 
$NCount++; 
	if ($NCount >= "30" && $NameName eq " ") { 
		$MainTitle = substr($MainTitle, 0, $NCount); 
	}
}

## LARGE PHOTO
if (@LargeImages ne "") { $LPhoto = "<a href=\"javascript:trigger('stank_images.html?CMPartNum=$CMPartNum&ComingFrom=reconfig');\" onMouseOver=\"javascript:imageOnDHTML('lphoto','ov');\" onMouseOut=\"javascript:imageOffDHTML('lphoto','off');\"><img src=\"images/tables/but_lphoto_off.gif\" width=\"75\" height=\"20\" name=\"lphoto\" border=\"0\"></a>"; $TriggerPhoto = "javascript:trigger('stank_images.html?CMPartNum=$CMPartNum&ComingFrom=reconfig');"; }
else { $LPhoto = "<img src=\"images/tables/but_lphoto_dn.gif\" width=\"75\" height=\"20\" name=\"lphoto\" border=\"0\">"; $TriggerPhoto = "#"; }

## MULTIMEDIA
if ($SavedMediaCode ne "") { $SysMedia = "<a href=\"javascript:trigger('stank_media.html?MyCode=$SavedMediaCode&ComingFrom=reconfig');\" onMouseOver=\"javascript:imageOnDHTML('multimedia','ov');\" onMouseOut=\"javascript:imageOffDHTML('multimedia','off');\"><img src=\"images/tables/but_multimedia_off.gif\" width=\"73\" height=\"20\" name=\"multimedia\" border=\"0\"></a>"; }
else { $SysMedia = "<img src=\"images/tables/but_multimedia_dn.gif\" width=\"73\" height=\"20\" name=\"multimedia\" border=\"0\">"; }

## RECONFIGURABLE?
$ConfigIT = "<img src=\"images/tables/but_configureit_dn.gif\" width=\"81\" height=\"20\" name=\"configureit\" border=\"0\">";

if ($FORM{'NSPRINT'}) { $NSPrinter = "onload=\"javascript:printPageNS();feedAllParts()\""; }
else { $NSPrinter = "onload=\"javascript:feedAllParts()\""; }

## ---------->>> GET PRODUCT INFO
$Counter = 0;
foreach (1 .. $Numero) {
$Counter++;

	@MyParts = split(/,,,,,/, $Parts[0]);
	shift(@Parts);
	push(@Parts2,"$MyParts[0],,,,,$MyParts[1],,,,,$MyParts[2],,,,,$MyParts[3]");
	$Category = $MyParts[0];
	$Type = $MyParts[1];
	$Character = $MyParts[2];
	$Parties = $MyParts[3];
	## WHICH TYPE?
	if ($Type eq "HIDE") { $IsHidden = "selected"; $IsShown = ""; }
	else { $IsHidden = ""; $IsShown = "selected"; }
	## WHICH CHARACTERISTIC?
	if ($Character eq "All") { $IsSingle = ""; $IsMultiple = ""; $IsAll = "selected"; }
	elsif ($Character eq "Multiple") { $IsSingle = ""; $IsMultiple = "selected"; $IsAll = ""; }
	else { $IsSingle = "selected"; $IsMultiple = ""; $IsAll = ""; }
	
	@SubParts = split(/,/, $Parties);
	foreach $SubPart (@SubParts) {
		my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$SubPart' ORDER BY ItemName ASC");
		$sth->execute or die "Unable to execute query\n"; 
		my @row;
		while(@row = $sth->fetchrow_array) {
			$MuaCMNum = $row[1];
			$MFGPartNum = $row[7];
			$MuaName = $row[11];
			$MuaEmblem = $row[16];
			$MuaPhoto = $row[17];
			$MuaWarr = $row[19];
			$MuaLbs = $row[20];
			$MuaCost = $row[21];
			$MuaRelated = $row[23];
			$MuaAccessories = $row[24];
			if ($MuaName =~ "&reg;") { $MuaName =~ s/&reg;//g; }
			if ($MuaName =~ "&#153;") { $MuaName =~ s/&#153;//g; }
			if ($MuaName =~ "&copy;") { $MuaName =~ s/&copy;//g; }
			push(@MuaBits,"$Category,,,,,$MuaCMNum,,,,,$MFGPartNum,,,,,$MuaName,,,,,$MuaPhoto,,,,,$MuaWarr,,,,,$MuaLbs,,,,,$MuaCost,,,,,$MuaRelated,,,,,$MuaAccessories,,,,,$Character");
			if ($MuaEmblem ne "" && $MuaEmblem ne $LastMuaEmblem) { push(@Emblems,"$MuaCMNum,,,,,$MuaName,,,,,$MuaEmblem"); $LastMuaEmblem = $MuaEmblem; }
		}
		$sth->finish;
	}
}

## ---------->>> GET TOTAL PRICE
$Counter = 0;
$MuaCatCount=0; 
foreach (1 .. $Numero) {
$Counter++;

	@MuaParts = split(/,,,,,/, $Parts2[0]);
	shift(@Parts2);
	$Category = $MuaParts[0];
	$Type = $MuaParts[1];
	$Character = $MuaParts[2];
	$Parties = $MuaParts[3];
	## WHICH TYPE?
	if ($Type eq "HIDE") { $IsHidden = "selected"; $IsShown = ""; }
	else { $IsHidden = ""; $IsShown = "selected"; }
	## WHICH CHARACTERISTIC?
	if ($Character eq "All") { $IsSingle = ""; $IsMultiple = ""; $IsAll = "selected"; }
	elsif ($Character eq "Multiple") { $IsSingle = ""; $IsMultiple = "selected"; $IsAll = ""; }
	else { $IsSingle = "selected"; $IsMultiple = ""; $IsAll = ""; }
	
	@SubParts = split(/,/, $Parties);
	foreach $SubPart (@SubParts) {
		my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$SubPart' ORDER BY ItemName ASC");
		$sth->execute or die "Unable to execute query\n"; 
		my @row;
		while(@row = $sth->fetchrow_array) { 
			$MiEsteNombre = $row[11];
			if ($MiEsteNombre =~ "&reg;") { $MiEsteNombre =~ s/&reg;//g; }
			if ($MiEsteNombre =~ "&#153;") { $MiEsteNombre =~ s/&#153;//g; }
			if ($MiEsteNombre =~ "&copy;") { $MiEsteNombre =~ s/&copy;//g; }
			$MiCuesta = $row[21];
			if ($Counter eq "1" || $ThisSec eq $Category) { $ThisSec = $Category; push(@MainPartes,"$MiEsteNombre,,,,,$SubPart,,,,,$Counter,,,,,$Character,,,,,$Category"); }
			elsif ($ThisLast2 eq $Category) { push(@SubPartes,"$MiEsteNombre,,,,,$SubPart,,,,,$MuaCatCount,,,,,$Character,,,,,$Category"); }
			else { $MuaCatCount++; $ThisLast2 = $Category; push(@SubPartes,"$MiEsteNombre,,,,,$SubPart,,,,,$MuaCatCount,,,,,$Character,,,,,$Category"); }
			push(@SubTotales,"$MiCuesta,,,,,$Counter,,,,,$Character,,,,,$MiEsteNombre");
		}
		$sth->finish;
	}
	
##------------------->>> Calculate total for all SUB components
$ComponentTotal=0;
$TCCount=0;
if ($Character eq "All") {
	foreach $Total (@SubTotales) {
		@ThisPrice = split(/,,,,,/, $Total);
		if ($ThisPrice[1] eq $Counter) {
			$TCCount++;
			$ComponentTotal = $ThisPrice[0] + $ComponentTotal;
		}
	}
}

else {
	foreach $Total (@SubTotales) {
		@ThisPrice = split(/,,,,,/, $Total);
		if ($ThisPrice[1] eq $Counter && $TCCount eq "0") {
			$TCCount++;
			$DaFirstObj = "$ThisPrice[3]";
			$ComponentTotal = $ThisPrice[0] + $ComponentTotal;
		}
		elsif ($ThisPrice[1] eq $Counter && $ThisPrice[3] eq $DaFirstObj) {
			$TCCount++;
			$ComponentTotal = $ThisPrice[0] + $ComponentTotal;			
		}
	}
}

$ComponentTotal = sprintf("%.2f", $ComponentTotal);
push(@LeTotalistico, $ComponentTotal);

##------------------>>> CALCULATE TOTAL FOR ALL ITEMS IN SYSTEM
$AllCompTotal=0;
foreach $Totalistico (@LeTotalistico) {
	$AllCompTotal = $AllCompTotal + $Totalistico;
}

$EntireTotal = sprintf("%.2f", $AllCompTotal);

	## Snif cookie, if present test for logged in status
	require ("cookiesnif.nsp");

	if ($SavedItemName =~ "mdlschool" || $SavedItemName =~ "MDLSCHOOL") {
		$Markup = ($EntireTotal / .85);
		$Markup = sprintf("%.2f", $Markup);
		$EntireTotal = $Markup;
	}
	elsif (($SavedPricingClass eq "Desktop") && ($Cookies{'DTV'})) {
		$MyTypo = 100 - $Cookies{'DTV'};
		if ($MyTypo < 10) { $MyTypo = "." . "0" . "$MyTypo"; }
		else { $MyTypo = ".$MyTypo"; }
		$Markup = ($EntireTotal / $MyTypo);
		$Markup = sprintf("%.2f", $Markup);
		$EntireTotal = $Markup;
	}
	elsif (($SavedPricingClass eq "Server") && ($Cookies{'SRV'})) {
		$MyTypo = 100 - $Cookies{'SRV'};
		if ($MyTypo < 10) { $MyTypo = "." . "0" . "$MyTypo"; }
		else { $MyTypo = ".$MyTypo"; }
		$Markup = ($EntireTotal / $MyTypo);
		$Markup = sprintf("%.2f", $Markup);
		$EntireTotal = $Markup;
	}
	elsif (($SavedPricingClass eq "Notebook") && ($Cookies{'NBV'})) {
		$MyTypo = 100 - $Cookies{'NBV'};
		if ($MyTypo < 10) { $MyTypo = "." . "0" . "$MyTypo"; }
		else { $MyTypo = ".$MyTypo"; }
		$Markup = ($EntireTotal / $MyTypo);
		$Markup = sprintf("%.2f", $Markup);
		$EntireTotal = $Markup;
	}
	elsif ($Cookies{'UserType'} eq "CMManage" || $Cookies{'UserType'} eq "CMAdmin" || $Cookies{'UserType'} eq "CMSales" || $Cookies{'UserType'} eq "CMUser") {
		$EntireTotal = $EntireTotal;
	}
	elsif($tigerNAS eq "YES") {
		$EntireTotal = $EntireTotal;	
	}
	else {
		$Markup = ($EntireTotal / .65);
		$Markup = sprintf("%.2f", $Markup);
		$EntireTotal = $Markup;
	}
	$EntireTotal = sprintf("%.2f", $EntireTotal);

}

if ($SavedCMSeries eq "GreatWhite") { $MuaSeries = "Great White"; }
else { $MuaSeries = "$SavedCMSeries"; }

if ($SavedPricingClass eq "Notebook" || $SavedPricingClass eq "Server") { $MonitorNOT = ""; }
else { $MonitorNOT = "<br><font class=\"stankprice2\">(monitor not included)<br>"; }


## PRICE OR NO PRICE? LOGGED OR NOT...
if ($Cookies{'Echado'} eq "YES") { $EntireTotal = "<font class=\"stankprice\"><br>System's Current Price<br><b>\$$EntireTotal</b></font>"; }
elsif ($tigerNAS eq "YES") { $EntireTotal = "<font class=\"stankprice\"><br>System's Current Price<br><b>\$$EntireTotal</b><br><br></font>"; $priceButton="Price It!"; $sysPhraseEnd = "Price It!"; }
else { $EntireTotal = "<font class=\"stankprice\"><br><b>Call for Proper Pricing</b></font>"; }

##### --> NMUSD
if ($FORM{'NMUSD'} eq "1") {
	$lePrecious = "<font class=\"stankprice\"><br><center>Call or request E-Quote<br>for product pricing</center><br><br></font><input type=\"hidden\" name=\"NMUSD\" value=\"1\">";
	$leTexter = "Once you are done configuring your <b>$MuaSeries Series&#153;</b> system, click on the 'View Config!' button to view your personalized <b>$MuaSeries Series&#153;</b> system's layout.";
	$lebuttext = "View Config!";
	$EmailIt = "&nbsp;";
}
elsif ($FORM{'MSP'} eq "1") {
	$lePrecious = "<font class=\"stankprice\"><br><center>Call or request E-Quote<br>for product pricing</center><br><br></font><input type=\"hidden\" name=\"MSP\" value=\"1\">";
	$leTexter = "Once you are done configuring your <b>$MuaSeries Series&#153;</b> system, click on the 'View Config!' button to view your personalized <b>$MuaSeries Series&#153;</b> system's layout.";
	$lebuttext = "View Config!";
	$EmailIt="&nbsp;";
}
else {
	$lePrecious = "<center>$EntireTotal<br><br></center>";
	$leTexter = "Once you are done configuring your <b>$MuaSeries Series&#153;</b> system, click on the 'Price It!' button to get your personalized <b>$MuaSeries Series&#153;</b> system's price.";
	$lebuttext = "Price It!";
	$EmailIt = "<a href=\"$StartURLer('https://www.coastlinemicro.com/stank_emailit.html?MySubject=$SavedCMSeries&MyTitle=$SavedCMSeries&MyLoad=loadsys&MyData=$CMPartNum&EmailSubject=$MainTitle'$EndURLer\" onMouseOver=\"javascript:imageOnDHTML('emailit','ov');\" onMouseOut=\"javascript:imageOffDHTML('emailit','off');\"><img src=\"images/tables/but_emailit_off.gif\" width=\"62\" height=\"21\" name=\"emailit\" border=\"0\"></a>";
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
<script language="Javascript" src="js/mousetable.js"></script>
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

function printPage() {
  if (ns4) // NS4
    window.open('stank_techspecs.html?CMPartNum=$CMPartNum&NSPRINT=1','PRINT','width=485,height=590');
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

function addSystemItem(cual,DaValue) {
acual = document.Reconfig[cual];
itsValue = acual.value;
	if (itsValue == "") { acual.value = DaValue; }
	else { 
		NewValue = itsValue+','+DaValue;
		acual.value = NewValue;
	}
}

function makeSystemItem2(cual,DaText,DaValue) {
acual = document.Reconfig[cual];
sizer = acual.length;
there = false;
for(var count = 0; count < sizer; count++) {
	if (acual.options[count] != null) {
		if (acual.options[count].value.indexOf(DaValue) != -1) {
			there = true;
				if (acual.options[count].value.indexOf('-----') == -1) { 
					acual.options[count].text = '(2) '+DaText; 
					acual.options[count].value = DaValue+'-----'+2+'';
					count++;
				}
				else { 
					OldCount=0;
					Este2 = acual.options[count].value;
					var MyCount = Este2.split(/-----/);
					MyCounter = MyCount[1];
					MyCounter++;
					acual.options[count].text = '('+MyCounter+') '+DaText; 
					acual.options[count].value = DaValue+'-----'+MyCounter+'';
					count++;
				}
    		}
   		}
	}
	if (there != true) {
		var thisone = DaValue;
		if (thisone != "$SavedCMPartNum") {
			acual.options[sizer] = new Option(DaText); 
			acual.options[sizer].value = DaValue;
			if (cual != "TheAccess") { acual.selectedIndex = 0; }
			sizer++;
		}
    }
}

function killSystemItem(cual) {
var cual  = document.Reconfig[cual];
var sizer = cual.options.length;
for(var i = (sizer-1); i >= 0; i--) {
if ((cual.options[i] != null) && (cual.options[i].selected == true)) {
cual.options[i] = null;
      }
   }
}

function clearUs(cual) {
// CLEARS ALL DATA DYNAMIC
ThisOne = document.Reconfig[cual];
var sizer = ThisOne.length;
	for(var i = (sizer-1); i >= 0; i--) {
		while (ThisOne.options[i] != null) {
			if (ThisOne.options[i].value == "BIGNULL") {
				ThisOne.options[i] = null;
			}
		}
	}
}
</script>
<script language="Javascript">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

// FORM CHECKER FUNCTIONS
// By Drlouie \@ NetMedia Solutions
// info\@NetMediaSol.com for help
// Copyright 2001 NetMedia Solutions

function checkForm() {
var missingdrop = "";
var thefirst = "";

EOF
}

## MAIN PARTS
	@EsteSplits2 = split(/,,,,,/, $MainPartes[0]);
	if ($EsteSplits2[3] ne "All") {
		print " if (document.Reconfig.MainNumbers.selectedIndex > -1) {\n";
		print "// Check Main Components\n";
		print "var strValues = \"\"; var boxLength = document.Reconfig.MainNumbers.length; var count = 0;\n";
		print "if (boxLength != 0) {\n";
		print "	for (i = 0; i < boxLength; i++) {\n";
		print "		var LeValue = document.Reconfig.MainNumbers.options[i].value;\n";
		print "		if (LeValue.indexOf('-----') == -1) {\n";
		print "			MyNumber=LeValue;\n";
		print "			if (count == 0) { strValues = MyNumber; }\n";
		print "			else { strValues = strValues + \",\" + MyNumber; }\n";
		print "		}\n";
		print "		else {\n";
		print "			OldCount=0;\n";
		print " 		var MyCount = LeValue.split(/-----/);\n";
		print "			MyCounter=0;\n";
		print "			MyCounter = MyCount[1];\n";
		print "			MyNumber = MyCount[0];\n";
		print "			for(var cuenta = 0; cuenta < MyCounter; cuenta++) {\n";
		print "				if (strValues == \"\") { strValues = MyNumber; }\n";
		print "				else { strValues = strValues + \",\" + MyNumber; }\n";
		print "			}\n";
		print "		}\n";
		print "	count++;\n";
		print "   }\n";
		print "}\n";
		print "else { }\n";
		print "if (strValues.length == 0) { }\n";
		print "else { document.Reconfig.MainNumeros.value = strValues; }\n";
		print "}\n";
		print "else {\n";
		print "    missingdrop += \"\\n     - $EsteSplits[4]\";\n";
		print "	   if (thefirst == \"\") { thefirst = \"Sub$EsteSplits[2]\Numbers\"; }\n";
		print "}\n";
		$MyKills = "clearUs('MainNumeros');";
	}

## SUB PARTS
## Make as many as are in system
foreach $SubParte (@SubPartes) {
	@EsteSplits = split(/,,,,,/, $SubParte);
	if ($EsteSplits[3] ne "All" && $LastCount ne $EsteSplits[2]) {
		$LastCount = $EsteSplits[2];
		print " if (document.Reconfig.Sub$EsteSplits[2]\Numbers.selectedIndex  > -1) {\n";
		print "// Check Sub$EsteSplits[2]\Numbers Components\n";
		print "var strValues = \"\"; var leSelected= document.Reconfig.Sub$EsteSplits[2]\Numbers.selectedIndex; var boxLength = document.Reconfig.Sub$EsteSplits[2]\Numbers.length; var count = 0;\n";
		print "if (boxLength != 0) {\n";
		print "	for (i = 0; i < boxLength; i++) {\n";
		print " if (document.Reconfig.Sub$EsteSplits[2]\Numbers.options[i].selected) {\n";
		print "		var LeValue = document.Reconfig.Sub$EsteSplits[2]\Numbers.options[i].value;\n";
		print "		if (LeValue.indexOf('-----') == -1) {\n";
		print "			MyNumber=LeValue;\n";
		print "			if (count == 0) { strValues = MyNumber; }\n";
		print "			else { strValues = strValues + \",\" + MyNumber; }\n";
		print "		}\n";
		print "		else {\n";
		print "			OldCount=0;\n";
		print " 		var MyCount = LeValue.split(/-----/);\n";
		print "			MyCounter=0;\n";
		print "			MyCounter = MyCount[1];\n";
		print "			MyNumber = MyCount[0];\n";
		print "			for(var cuenta = 0; cuenta < MyCounter; cuenta++) {\n";
		print "				if (strValues == \"\") { strValues = MyNumber; }\n";
		print "				else { strValues = strValues + \",\" + MyNumber; }\n";
		print "			}\n";
		print "		}\n";
		print "	count++;\n";
		print "}\n";
		print "   }\n";
		print "}\n";
		print "if (strValues.length == 0) { }\n";
		print "else { document.Reconfig.Sub$EsteSplits[2]\Numeros.value = strValues; }\n";
		print "}\n";
		print "else {\n";
		print "    missingdrop += \"\\n     - $EsteSplits[4]\";\n";
		print "	   if (thefirst == \"\") { thefirst = \"Sub$EsteSplits[2]\Numbers\"; }\n";
		print "}\n";
		$AllKills = "$MyKills" . "clearUs('Sub$EsteSplits[2]\Numeros');";
	}
}


##FINALIZE NSPrint with extra start commands;
$NSPrinter = "$NSPrinter" . "$AllKills";

## START THE IF STATEMENT FOR ACCESSORIES
if (@ProdAccessories) {

{
print <<EOF

// Check Product Accessories
if (document.Reconfig.TheAccess.selectedIndex  > -1) {
var strValues = "";
	var boxLength = document.Reconfig.TheAccess.length;
	var count = 0;
if (boxLength != 0) {
	for (i = 0; i < boxLength; i++) {
		if (document.Reconfig.TheAccess.options[i].selected) {
			if (count == 0) { strValues = document.Reconfig.TheAccess.options[i].value; }
			else { strValues = strValues + "," + document.Reconfig.TheAccess.options[i].value; }
			count++;
		}
   }
}
else { }
if (strValues.length == 0) { }
else {
	// Grab selected fields from TheAccess and make Accessories form field for processing
	document.Reconfig.Accessories.value = strValues;
}
}

EOF
}

## END THE IF STATEMENT FOR ACCESSORIES
}


{
print <<EOF

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    missingdrop ="___________________________________________                   \\n\\n" + "  Sorry, there is a problem with your system\\'s configuration.\\n  Please review the following errors to continue:\\n" + "___________________________________________                   \\n\\n" +
    missingdrop + "\\n___________________________________________                   " + "\\n\\n   To continue, fix the listed errors and retry your request!" + "\\n___________________________________________";
    alert(missingdrop);
	document.Reconfig(thefirst).focus();
    return false;
} 
else {
return true;
}
}
</SCRIPT>
<base href="http://www.coastlinemicro.com/">
</head>
<body bgcolor="#ffffff" text="#8F8FAB" leftmargin="0" topmargin="0" marginwidth="0" scroll="yes" marginheight="0" $NSPrinter>
<form action="stank_newconfig.html" name="Reconfig" method="post" onSubmit="return checkForm();">
<input type="hidden" name="CMPartNum" value="$CMPartNum">
<input type="hidden" name="Warranty" value="$SavedWarranty">
<input type="hidden" name="PricingClass" value="$SavedPricingClass">
<input type="hidden" name="ItemName" value="$SavedItemName">
<input type="hidden" name="CMSeries" value="$SavedCMSeries">
<table width="$tablewidth" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td align="center" valign="middle" width="$tablewidth" height="25"> 
      <table width="$tablewidth" border="0" cellspacing="0" cellpadding="0" background="images/tables/topbar.jpg" height="24">
        <tr> 
          <td width="$t1"><img src="images/tables/topbar_left.jpg" width="5" height="24"></td>
          <td width="$t2"><nobr><font class="btext">&nbsp;&nbsp;<b>$MainTitle</b></font></nobr></td>
          <td width="$t3" align="center" valign="top">$EmailIt</td>
          <td width="$t4" align="center" valign="top"><a href="javascript:void(0);" onClick="javascript:printPage('stank_techspecs.html','CMPartNum','$CMPartNum');" onMouseOver="javascript:imageOnDHTML('printit','ov');" onMouseOut="javascript:imageOffDHTML('printit','off');"><img src="images/tables/but_printit_off.gif" width="67" height="21" name="printit" border="0"></a></td>
          <td width="$t1" align="left" valign="top"><img src="images/tables/topbar_right.jpg" width="5" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr> 
    <td align="center"> 
      <table width="$tablewidth" border="0" cellspacing="0" cellpadding="0" height="30">
        <tr align="center"> 
          <td width="20%" align="left">$GoBack</td>
          <td width="16%">$ConfigIT</td>
          <td width="16%"><a href="javascript:trigger('stank_techspecs.html?CMPartNum=$CMPartNum&ComingFrom=reconfig');" onMouseOver="javascript:imageOnDHTML('techspecs','ov');" onMouseOut="javascript:imageOffDHTML('techspecs','off');"><img src="images/tables/but_techspecs_off.gif" width="77" height="20" name="techspecs" border="0"></a></td>
          <td width="16%"><a href="javascript:trigger('stank_sysdrivers.html?CMPartNum=$CMPartNum&ComingFrom=reconfig');" onMouseOver="javascript:imageOnDHTML('sysdrivers','ov');" onMouseOut="javascript:imageOffDHTML('sysdrivers','off');"><img src="images/tables/but_sysdrivers_off.gif" width="78" height="20" name="sysdrivers" border="0"></a></td>
          <td width="16%">$LPhoto</td>
          <td width="16%">$SysMedia</td>
        </tr>
      </table>
    </td>
  </tr>
  <tr> 
    <td valign="top"> 
      <table width="$tablewidth" border="0" cellspacing="1" cellpadding="0" align="center">
        <tr> 
          <td valign="top" width="$t5"> 
            <table width="100%" cellspacing="1" cellpadding="0" bgcolor="#FFFFFF">
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="0" bgcolor="#F2F2F7" class="stankth" height="18" $border>
                    <tr> 
                      <td align="center"><font class="btext"><b>Customize Your $MuaSeries!</b></font></td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="2" class="stankth" $border>
                    <tr> 
                      <td valign="top">
<table width="100%" align="center" cellpadding="0" cellspacing="0" border="0">
<tr> 
<td width="40%" valign="middle" align="center"><a href="$TriggerPhoto"><img src="/dbimages/prod_common/$SmallImageN" width="165" height="100" vspace="20" border="0" alt="Click to view large photo(s) of this product."></a>$MonitorNOT<br></td>
<td width="55%" valign="top">$lePrecious<font class="btext"><b>Configurator Instructions</b><br>To re-configure this <b>$MuaSeries Series&#153;</b> system, simply select the option(s) for every component you would like to have in your system. You can either select 'One', 'All' or 'None' of the listed components depending on the type of component it is. Components that do not give you a selection/option are static, and are included by default for this <b>$MuaSeries Series&#153;</b> system. $leTexter<br><br><br></font></td>
<td width="5%">&nbsp;</td>
</tr>

</table>
<table width="100%" align="center" cellpadding="0" cellspacing="5" border="0">
<tr><td width="100%" align="left" valign="top">

EOF
}

$MuaCount=0;
$CatCount=1;
foreach $TS (@MuaBits) {
	@MyTS = split(/,,,,,/, $TS);
	$ThyCategory = $MyTS[0];
	$ThyCMNum = $MyTS[1];
	$ThyMFGNum = $MyTS[2];
	$ThyName = $MyTS[3];
	$ThyPhoto = $MyTS[4];
	$ThyWarr = $MyTS[5];
	$ThyLbs = $MyTS[6];
	$ThyCost = $MyTS[7];
	$ThyRelated = $MyTS[8];
	$ThyAccessories = $MyTS[9];
	$ThyChar = $MyTS[10];

	if ($ThyChar eq "Single" && $MuaCount eq "0") { $CatCount--; }
	
	if ($MuaCount eq "0") { $CualC = "MainCategory"; $CualN = "MainNumbers"; $CualChar = "MainCharacter"; $CualN2 = "MainNumeros"; }
	else { $CualC = "Sub$CatCount\Category"; $CualN = "Sub$CatCount\Numbers"; $CualChar = "Sub$CatCount\Character"; $CualN2 = "Sub$CatCount\Numeros"; }

	if ($ThyChar eq "All")	{
		if ($LastMuaCate eq "$ThyCategory") { 
			$MuaCategory = ""; 
			print "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src=\"images/checkbox_blue.gif\" border=\"0\"><font class=\"btext\" style=\"line-height:10px\">&nbsp;$ThyName<br><br></font>";
		}
		elsif ($LastMuaCate ne "$ThyCategory") { 
			$MuaCategory = "<b>$ThyCategory</b>"; 
			print "<font class=\"btext3\"><b>&nbsp;&nbsp;$MuaCategory</b>&nbsp;<font color=\"#eb0000\"><i>(Static)</i></font><br><br></font>";
			print "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src=\"images/checkbox_blue.gif\" border=\"0\"><font class=\"btext\" style=\"line-height:10px\">&nbsp;$ThyName<br><br></font>";
			print "<input type=\"hidden\" name=\"$CualC\" value=\"$ThyCategory\">";
			print "<input type=\"hidden\" name=\"$CualN2\" value=\"\">";
			print "<input type=\"hidden\" name=\"$CualChar\" value=\"$ThyChar\">";
			if ($MuaCount ne "0") { $CatCount++; }
		}
		$LastMuaCate = "$ThyCategory";
		push(@AllPartes,"$ThyCategory,,,,,$ThyCMNum,,,,,$ThyLbs,,,,,$ThyCost");
	}
	elsif ($ThyChar eq "Multiple") {
		if ($LastMuaCate eq "$ThyCategory") { }
		elsif ($LastMuaCate ne "$ThyCategory") {
			$MuaCategory = "<b>$ThyCategory</b>"; 
			print "<font class=\"btext3\"><b>&nbsp;&nbsp;$MuaCategory</b>&nbsp;<font color=\"#eb0000\"><i>(Multiple)</i></font>";
			print "<input type=\"hidden\" name=\"$CualC\" value=\"$ThyCategory\">";
			print "<input type=\"hidden\" name=\"$CualChar\" value=\"$ThyChar\">";
			print "<input type=\"hidden\" name=\"$CualN2\" value=\"\">";
			print "<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<select size=\"2\" class=\"prodguinea\" multiple name=\"$CualN\"></select><br><br></font>";
			if ($MuaCount ne "0") { $CatCount++; }
		}
		$LastMuaCate = "$ThyCategory";
		push(@AllPartes,"$ThyCategory,,,,,$ThyCMNum,,,,,$ThyLbs,,,,,$ThyCost");
	}
	else {
		if ($LastMuaCate eq "$ThyCategory") {
			$MuaCategory = "";
		}
		elsif ($LastMuaCate ne "$ThyCategory") {
			$MuaCategory = "<b>$ThyCategory</b>"; 
			print "<font class=\"btext3\"><b>&nbsp;&nbsp;$MuaCategory</b>&nbsp;<font color=\"#eb0000\"><i>(Select ONE)</i></font>";
			print "<input type=\"hidden\" name=\"$CualC\" value=\"$ThyCategory\">";
			print "<input type=\"hidden\" name=\"$CualChar\" value=\"$ThyChar\">";
			print "<input type=\"hidden\" name=\"$CualN2\" value=\"\">";
			print "<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<select class=\"prodguinea2\" name=\"$CualN\"></select><br><br></font>";
			$CatCount++;
		}
		$LastMuaCate = "$ThyCategory";
		push(@AllPartes,"$ThyCategory,,,,,$ThyCMNum,,,,,$ThyLbs,,,,,$ThyCost");
	}

	$MuaCount++;
}


if ($MuaCount eq "0") { print "<center><font class=\"btext3\"><br>Sorry, no results found...<br></font></center>"; }

## ---------->>> END WITH WARRANTY
if ($SavedWarranty ne "") {
	print "<font class=\"btext3\"><b>&nbsp;&nbsp;$SavedPricingClass Warranty</b><br><br></font>";
	print "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font class=\"btext\" style=\"line-height:10px\">$SavedWarranty<br><br></font>";
}

## ---------->>> IF ACCESSORIES AVAILABLE
if (@ProdAccessories) {
	print "<font class=\"btext3\"><b>&nbsp;&nbsp;Accessories</b>&nbsp;<font color=\"#eb0000\"><i>(Multiple)</i></font><br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<select size=\"2\" class=\"prodguinea\" multiple name=\"TheAccess\"></select><input type=\"hidden\" name=\"Accessories\" value=\"\"><br><br></font>";
}


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
			  <tr>
			  	<td>

<table width="100%" cellspacing="0" cellpadding="0" bgcolor="#F2F2F7" class="stankth" height="30" $border align="center" width="500" bgcolor="#F2F2F7">
	<tr>
    	<td align="center" width="50%" align="center"><input type="reset" value="Reset It!" class="pricebut"></td>
    	<td align="center" width="50%" align="center"><input type="submit" value="$lebuttext" class="pricebut"></td>
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

EOF
}

##----------->>> FEED INVENTORY

{
print <<EOF

<script language="Javascript">

///////////////////////////////////////////////////////////////////
// This script and its counterparts are ©2001 NetMedia Solutions //
// For use ONLY with CoastlineMicro.com                          //
// To re-use or have this script re-interfaced for your specific //
// needs please contact SServices\@NetMediaSolutions.com         //
// Prices are cheap for re-interfacing of current scripts and    //
// programs, so email us today to get you own LEGAL programming  //
// licensed for use only on YOUR site(s) or for YOUR purpose(s). //
///////////////////////////////////////////////////////////////////

function feedAllParts() {

EOF
}

## MAIN PARTS
foreach $Parte (@MainPartes) {
	@LosSplits = split(/,,,,,/, $Parte);
	if ($LosSplits[3] ne "All") {
	}
	else {
		print "addSystemItem('MainNumeros','$LosSplits[1]');\n";
	}
}

## SUB PARTS
foreach $SubParte (@SubPartes) {
	@LeSplits = split(/,,,,,/, $SubParte);
	if ($LeSplits[3] ne "All") {
		print "makeSystemItem2('Sub$LeSplits[2]\Numbers','$LeSplits[0]','$LeSplits[1]');\n";
	}
	else {
		print "addSystemItem('Sub$LeSplits[2]\Numeros','$LeSplits[1]');\n";
	}
}

## ACCESSORIES
if (@ProdAccessories) {
	## SUB PARTS
	foreach $ProdAccessory (@ProdAccessories) {
		@ThySplits = split(/,,,,,/, $ProdAccessory);
		print "makeSystemItem2('TheAccess','$ThySplits[0]','$ThySplits[1]');\n";
	}
}

print "}";
print "</script>";


{
print <<EOF

</form>

<table width="$tablewidth" border="0" cellspacing="0" cellpadding="0"><tr><td align="center" width="$tablewidth"> 
$STANKLEGAL
</td></tr></table>

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