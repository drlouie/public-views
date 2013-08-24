#!/usr/bin/perl5 -s

###########################################################################################################
# Company: ©2001 NetMedia Solutions                                                                       #
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

## ----------------->>> Must Have MainNumbers and MainCategory!
if ($FORM{'MainNumeros'} && $FORM{'MainCategory'} && $FORM{'MainCharacter'}) {

	## Crumble Form Input to Variables
	$CMPartNum = "$FORM{'CMPartNum'}";
	$PricingClass = "$FORM{'PricingClass'}";
	$ItemName = "$FORM{'ItemName'}";
	$Warranty = "$FORM{'Warranty'}";
	$Accessories = "$FORM{'Accessories'}";
	$SavedCMSeries = $FORM{'CMSeries'};
	push(@Parts,"$FORM{'MainCategory'},,,,,$FORM{'MainNumeros'},,,,,$FORM{'MainType'},,,,,$FORM{'MainCharacter'}"); $MainNumbers = $FORM{'MainNumeros'}; $Numero=1; 
	if ($FORM{'MainNumbers'} ne "null" || $FORM{'MainNumbers'} ne "Null" || $FORM{'MainNumbers'} ne "NULL" || $FORM{'MainNumbers'} ne "") { push(@Parts,"$FORM{'Sub1Category'},,,,,$FORM{'Sub1Numeros'},,,,,$FORM{'Sub1Type'},,,,,$FORM{'Sub1Character'}"); $Sub1Numbers = $FORM{'Sub1Numeros'}; $Numero=2; }
	if ($FORM{'Sub1Numbers'} ne "null" || $FORM{'Sub1Numbers'} ne "Null" || $FORM{'Sub1Numbers'} ne "NULL" || $FORM{'Sub1Numbers'} ne "") { push(@Parts,"$FORM{'Sub2Category'},,,,,$FORM{'Sub2Numeros'},,,,,$FORM{'Sub2Type'},,,,,$FORM{'Sub2Character'}"); $Sub2Numbers = $FORM{'Sub2Numeros'}; $Numero=3; }
	if ($FORM{'Sub2Numbers'} ne "null" || $FORM{'Sub2Numbers'} ne "Null" || $FORM{'Sub2Numbers'} ne "NULL" || $FORM{'Sub2Numbers'} ne "") { push(@Parts,"$FORM{'Sub3Category'},,,,,$FORM{'Sub3Numeros'},,,,,$FORM{'Sub3Type'},,,,,$FORM{'Sub3Character'}"); $Sub3Numbers = $FORM{'Sub3Numeros'}; $Numero=4; }
	if ($FORM{'Sub3Numbers'} ne "null" || $FORM{'Sub3Numbers'} ne "Null" || $FORM{'Sub3Numbers'} ne "NULL" || $FORM{'Sub3Numbers'} ne "") { push(@Parts,"$FORM{'Sub4Category'},,,,,$FORM{'Sub4Numeros'},,,,,$FORM{'Sub4Type'},,,,,$FORM{'Sub4Character'}"); $Sub4Numbers = $FORM{'Sub4Numeros'}; $Numero=5; }
	if ($FORM{'Sub4Numbers'} ne "null" || $FORM{'Sub4Numbers'} ne "Null" || $FORM{'Sub4Numbers'} ne "NULL" || $FORM{'Sub4Numbers'} ne "") { push(@Parts,"$FORM{'Sub5Category'},,,,,$FORM{'Sub5Numeros'},,,,,$FORM{'Sub5Type'},,,,,$FORM{'Sub5Character'}"); $Sub5Numbers = $FORM{'Sub5Numeros'}; $Numero=6; }
	if ($FORM{'Sub5Numbers'} ne "null" || $FORM{'Sub5Numbers'} ne "Null" || $FORM{'Sub5Numbers'} ne "NULL" || $FORM{'Sub5Numbers'} ne "") { push(@Parts,"$FORM{'Sub6Category'},,,,,$FORM{'Sub6Numeros'},,,,,$FORM{'Sub6Type'},,,,,$FORM{'Sub6Character'}"); $Sub6Numbers = $FORM{'Sub6Numeros'}; $Numero=7; }
	if ($FORM{'Sub6Numbers'} ne "null" || $FORM{'Sub6Numbers'} ne "Null" || $FORM{'Sub6Numbers'} ne "NULL" || $FORM{'Sub6Numbers'} ne "") { push(@Parts,"$FORM{'Sub7Category'},,,,,$FORM{'Sub7Numeros'},,,,,$FORM{'Sub7Type'},,,,,$FORM{'Sub7Character'}"); $Sub7Numbers = $FORM{'Sub7Numeros'}; $Numero=8; }
	if ($FORM{'Sub7Numbers'} ne "null" || $FORM{'Sub7Numbers'} ne "Null" || $FORM{'Sub7Numbers'} ne "NULL" || $FORM{'Sub7Numbers'} ne "") { push(@Parts,"$FORM{'Sub8Category'},,,,,$FORM{'Sub8Numeros'},,,,,$FORM{'Sub8Type'},,,,,$FORM{'Sub8Character'}"); $Sub8Numbers = $FORM{'Sub8Numeros'}; $Numero=9; }
	if ($FORM{'Sub8Numbers'} ne "null" || $FORM{'Sub8Numbers'} ne "Null" || $FORM{'Sub8Numbers'} ne "NULL" || $FORM{'Sub8Numbers'} ne "") { push(@Parts,"$FORM{'Sub9Category'},,,,,$FORM{'Sub9Numeros'},,,,,$FORM{'Sub9Type'},,,,,$FORM{'Sub9Character'}"); $Sub9Numbers = $FORM{'Sub9Numeros'}; $Numero=10; }
	if ($FORM{'Sub9Numbers'} ne "null" || $FORM{'Sub9Numbers'} ne "Null" || $FORM{'Sub9Numbers'} ne "NULL" || $FORM{'Sub9Numbers'} ne "") { push(@Parts,"$FORM{'Sub10Category'},,,,,$FORM{'Sub10Numeros'},,,,,$FORM{'Sub10Type'},,,,,$FORM{'Sub10Character'}"); $Sub10Numbers = $FORM{'Sub10Numeros'}; $Numero=11; }
	if ($FORM{'Sub10Numbers'} ne "null" || $FORM{'Sub10Numbers'} ne "Null" || $FORM{'Sub10Numbers'} ne "NULL" || $FORM{'Sub10Numbers'} ne "") { push(@Parts,"$FORM{'Sub11Category'},,,,,$FORM{'Sub11Numeros'},,,,,$FORM{'Sub11Type'},,,,,$FORM{'Sub11Character'}"); $Sub11Numbers = $FORM{'Sub11Numeros'}; $Numero=12; }
	if ($FORM{'Sub11Numbers'} ne "null" || $FORM{'Sub11Numbers'} ne "Null" || $FORM{'Sub11Numbers'} ne "NULL" || $FORM{'Sub11Numbers'} ne "") { push(@Parts,"$FORM{'Sub12Category'},,,,,$FORM{'Sub12Numeros'},,,,,$FORM{'Sub12Type'},,,,,$FORM{'Sub12Character'}"); $Sub12Numbers = $FORM{'Sub12Numeros'}; $Numero=13; }
	if ($FORM{'Sub12Numbers'} ne "null" || $FORM{'Sub12Numbers'} ne "Null" || $FORM{'Sub12Numbers'} ne "NULL" || $FORM{'Sub12Numbers'} ne "") { push(@Parts,"$FORM{'Sub13Category'},,,,,$FORM{'Sub13Numeros'},,,,,$FORM{'Sub13Type'},,,,,$FORM{'Sub13Character'}"); $Sub13Numbers = $FORM{'Sub13Numeros'}; $Numero=14; }
	if ($FORM{'Sub13Numbers'} ne "null" || $FORM{'Sub13Numbers'} ne "Null" || $FORM{'Sub13Numbers'} ne "NULL" || $FORM{'Sub13Numbers'} ne "") { push(@Parts,"$FORM{'Sub14Category'},,,,,$FORM{'Sub14Numeros'},,,,,$FORM{'Sub14Type'},,,,,$FORM{'Sub14Character'}"); $Sub14Numbers = $FORM{'Sub14Numeros'}; $Numero=15; }
	if ($FORM{'Sub14Numbers'} ne "null" || $FORM{'Sub14Numbers'} ne "Null" || $FORM{'Sub14Numbers'} ne "NULL" || $FORM{'Sub14Numbers'} ne "") { push(@Parts,"$FORM{'Sub15Category'},,,,,$FORM{'Sub15Numeros'},,,,,$FORM{'Sub15Type'},,,,,$FORM{'Sub15Character'}"); $Sub15Numbers = $FORM{'Sub15Numeros'}; $Numero=16; }
	if ($FORM{'Sub15Numbers'} ne "null" || $FORM{'Sub15Numbers'} ne "Null" || $FORM{'Sub15Numbers'} ne "NULL" || $FORM{'Sub15Numbers'} ne "") { push(@Parts,"$FORM{'Sub16Category'},,,,,$FORM{'Sub16Numeros'},,,,,$FORM{'Sub16Type'},,,,,$FORM{'Sub16Character'}"); $Sub16Numbers = $FORM{'Sub16Numeros'}; $Numero=17; }
	if ($FORM{'Sub16Numbers'} ne "null" || $FORM{'Sub16Numbers'} ne "Null" || $FORM{'Sub16Numbers'} ne "NULL" || $FORM{'Sub16Numbers'} ne "") { push(@Parts,"$FORM{'Sub17Category'},,,,,$FORM{'Sub17Numeros'},,,,,$FORM{'Sub17Type'},,,,,$FORM{'Sub17Character'}"); $Sub17Numbers = $FORM{'Sub17Numeros'}; $Numero=18; }
	if ($FORM{'Sub17Numbers'} ne "null" || $FORM{'Sub17Numbers'} ne "Null" || $FORM{'Sub17Numbers'} ne "NULL" || $FORM{'Sub17Numbers'} ne "") { push(@Parts,"$FORM{'Sub18Category'},,,,,$FORM{'Sub18Numeros'},,,,,$FORM{'Sub18Type'},,,,,$FORM{'Sub18Character'}"); $Sub18Numbers = $FORM{'Sub18Numeros'}; $Numero=19; }
	if ($FORM{'Sub18Numbers'} ne "null" || $FORM{'Sub18Numbers'} ne "Null" || $FORM{'Sub18Numbers'} ne "NULL" || $FORM{'Sub18Numbers'} ne "") { push(@Parts,"$FORM{'Sub19Category'},,,,,$FORM{'Sub19Numeros'},,,,,$FORM{'Sub19Type'},,,,,$FORM{'Sub19Character'}"); $Sub19Numbers = $FORM{'Sub19Numeros'}; $Numero=20; }
	if ($FORM{'Sub19Numbers'} ne "null" || $FORM{'Sub19Numbers'} ne "Null" || $FORM{'Sub19Numbers'} ne "NULL" || $FORM{'Sub19Numbers'} ne "") { push(@Parts,"$FORM{'Sub20Category'},,,,,$FORM{'Sub20Numeros'},,,,,$FORM{'Sub20Type'},,,,,$FORM{'Sub20Character'}"); $Sub20Numbers = $FORM{'Sub20Numeros'}; $Numero=21; }
	if ($FORM{'Sub20Numbers'} ne "null" || $FORM{'Sub20Numbers'} ne "Null" || $FORM{'Sub20Numbers'} ne "NULL" || $FORM{'Sub20Numbers'} ne "") { push(@Parts,"$FORM{'Sub21Category'},,,,,$FORM{'Sub21Numeros'},,,,,$FORM{'Sub21Type'},,,,,$FORM{'Sub21Character'}"); $Sub21Numbers = $FORM{'Sub21Numeros'}; $Numero=22; }
	if ($FORM{'Sub21Numbers'} ne "null" || $FORM{'Sub21Numbers'} ne "Null" || $FORM{'Sub21Numbers'} ne "NULL" || $FORM{'Sub21Numbers'} ne "") { push(@Parts,"$FORM{'Sub22Category'},,,,,$FORM{'Sub22Numeros'},,,,,$FORM{'Sub22Type'},,,,,$FORM{'Sub22Character'}"); $Sub22Numbers = $FORM{'Sub22Numeros'}; $Numero=23; }
	if ($FORM{'Sub22Numbers'} ne "null" || $FORM{'Sub22Numbers'} ne "Null" || $FORM{'Sub22Numbers'} ne "NULL" || $FORM{'Sub22Numbers'} ne "") { push(@Parts,"$FORM{'Sub23Category'},,,,,$FORM{'Sub23Numeros'},,,,,$FORM{'Sub23Type'},,,,,$FORM{'Sub23Character'}"); $Sub23Numbers = $FORM{'Sub23Numeros'}; $Numero=24; }
	if ($FORM{'Sub23Numbers'} ne "null" || $FORM{'Sub23Numbers'} ne "Null" || $FORM{'Sub23Numbers'} ne "NULL" || $FORM{'Sub23Numbers'} ne "") { push(@Parts,"$FORM{'Sub24Category'},,,,,$FORM{'Sub24Numeros'},,,,,$FORM{'Sub24Type'},,,,,$FORM{'Sub24Character'}"); $Sub24Numbers = $FORM{'Sub24Numeros'}; $Numero=25; }
	if ($FORM{'Sub24Numbers'} ne "null" || $FORM{'Sub24Numbers'} ne "Null" || $FORM{'Sub24Numbers'} ne "NULL" || $FORM{'Sub24Numbers'} ne "") { push(@Parts,"$FORM{'Sub25Category'},,,,,$FORM{'Sub25Numeros'},,,,,$FORM{'Sub25Type'},,,,,$FORM{'Sub25Character'}"); $Sub25Numbers = $FORM{'Sub25Numeros'}; $Numero=26; }
	
## ----------------->>> BACK BUTTON OR NO BACK BUTTON?
$ComingFrom = $FORM{'ComingFrom'};
if ($FORM{'ComingFrom'}) { $GoBack = "<a href=\"javascript:trigger('stank_$ComingFrom\.html?CMPartNum=$CMPartNum');\"><img src=\"images/tables/icon_back_on.gif\" width=\"60\" height=\"20\" name=\"back\" border=\"0\"></a>"; }
else { $GoBack = "<img src=\"images/tables/icon_back_off.gif\" width=\"60\" height=\"20\" name=\"back\" border=\"0\">"; }

##----------->>> Grab PRODUCTS STUFF
use DBI;
my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>coastline</b>\n"; 
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

##----------->>> Grab system ACCESSORY information
if ($FORM{'Accessories'} > 0) {
	@MyAccessory = split(/,/, $FORM{'Accessories'});
	$count=0;
	foreach $Accessory (@MyAccessory) {
		my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$Accessory'");
		$sth->execute or die "Unable to execute query\n";
		my @row;
		while(@row = $sth->fetchrow_array) { 
			$AccCMNum = $row[1];
			$AccItemName = $row[11];
			$AccWeight = $row[20];
			$AccPrice = $row[21];
			push(@ProdAccessories, "$AccCMNum,,,,,$AccItemName,,,,,$AccWeight,,,,,$AccCost");
			push(@AccTotales, "$AccPrice");
			$count++;
		}
		$sth->execute or die "Unable to execute query\n"; 
		$sth->finish;
	}
}

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

if ($FORM{'NSPRINT'}) { $NSPrinter = "onload=\"javascript:printPageNS();\""; }


## ---------->>> GET PRODUCT INFO
$Counter = 0;
foreach (1 .. $Numero) {
$Counter++;

	@MyParts = split(/,,,,,/, $Parts[0]);
	shift(@Parts);
	push(@Parts2,"$MyParts[0],,,,,$MyParts[1],,,,,$MyParts[2],,,,,$MyParts[3]");
	$Category = $MyParts[0];
	$Parties = $MyParts[1];
	$Type = $MyParts[2];
	$Character = $MyParts[3];
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
			$MuaPhoto = $row[17];
			$MuaWarr = $row[19];
			$MuaLbs = $row[20];
			$MuaCost = $row[21];
			$MuaRelated = $row[23];
			$MuaAccessories = $row[24];
			push(@MuaBits,"$Category,,,,,$MuaCMNum,,,,,$MFGPartNum,,,,,$MuaName,,,,,$MuaPhoto,,,,,$MuaWarr,,,,,$MuaLbs,,,,,$MuaCost,,,,,$MuaRelated,,,,,$MuaAccessories,,,,,$Character");
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
	$Parties = $MuaParts[1];
	$Type = $MuaParts[2];
	$Character = $MuaParts[3];
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
	foreach $Total (@SubTotales) {
		@ThisPrice = split(/,,,,,/, $Total);
		if ($ThisPrice[1] eq $Counter) {
			$TCCount++;
			$ComponentTotal = $ThisPrice[0] + $ComponentTotal;
		}
	}

$ComponentTotal = sprintf("%.2f", $ComponentTotal);
push(@LeTotalistico, $ComponentTotal);

##------------------->>> Calculate total for all ACCESSORIES
if (@AccTotales) {
	$ACCTotal=0;
	$ACCount=0;
	foreach $ACCMine (@AccTotales) {
		$ACCount++;
		$ACCTotal = $ACCMine + $ACCTotal;
		$ACCTotal = sprintf("%.2f", $ACCTotal);
	}
}

##------------------>>> CALCULATE TOTAL FOR ALL ITEMS IN SYSTEM
$AllCompTotal=0;
foreach $Totalistico (@LeTotalistico) {
	$AllCompTotal = $AllCompTotal + $Totalistico;
}

$AllCompTotal = $AllCompTotal + $ACCTotal;

$EntireTotal = sprintf("%.2f", $AllCompTotal);

	## Snif cookie, if present test for logged in status
	require ("cookiesnif.nsp");

	if ($SavedItemName =~ "mdlschool" || $SavedItemName =~ "MDLSCHOOL") {
		$Markup = ($EntireTotal / .85);
		$Markup = sprintf("%.2f", $Markup);
		$EntireTotal = $Markup;
	}
	elsif ($SavedPricingClass eq "Desktop" && $Cookies{'DTV'} > 0) {
		$MyTypo = 100 - $Cookies{'DTV'};
		if ($MyTypo < 10) { $MyTypo = "." . "0" . "$MyTypo"; }
		else { $MyTypo = ".$MyTypo"; }
		$Markup = ($EntireTotal / $MyTypo);
		$Markup = sprintf("%.2f", $Markup);
		$EntireTotal = $Markup;
	}
	elsif ($SavedPricingClass eq "Server" && $Cookies{'SRV'} > 0) {
		$MyTypo = 100 - $Cookies{'SRV'};
		if ($MyTypo < 10) { $MyTypo = "." . "0" . "$MyTypo"; }
		else { $MyTypo = ".$MyTypo"; }
		$Markup = ($EntireTotal / $MyTypo);
		$Markup = sprintf("%.2f", $Markup);
		$EntireTotal = $Markup;
	}
	elsif ($SavedPricingClass eq "Notebook" && $Cookies{'NBV'} > 0) {
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
	else {
		$Markup = ($EntireTotal / .65);
		$Markup = sprintf("%.2f", $Markup);
		$EntireTotal = $Markup;
	}
	$EntireTotal = sprintf("%.2f", $EntireTotal);

}

if ($Cookies{'Echado'} eq "YES" && $FORM{'MSP'} != "1" && $FORM{'NMUSD'} != "1") {
	$EQuoteIt = "<tr><td width=\"100%\" colspan=\"3\" align=\"center\" valign=\"middle\"><a href=\"javascript:EQuoteIt();document.leConfig.submit();\" onMouseOver=\"javascript:imageOnDHTML3('equoteit','ov');\" onMouseOut=\"javascript:imageOffDHTML3('equoteit','off');\"><img src=\"images/newones/equoteit_off.gif\" border=\"0\" name=\"equoteit\"></a></td></tr>";
	$CartOrSave = "<tr><td width=\"33%\" align=\"center\" valign=\"middle\"><a href=\"javascript:CartIt();document.leConfig.submit();\" onMouseOver=\"javascript:imageOnDHTML3('cartit','ov');\" onMouseOut=\"javascript:imageOffDHTML3('cartit','off');\"><img src=\"images/newones/cartit_off.gif\" border=\"0\" name=\"cartit\"></a></td><td width=\"33%\" align=\"center\" valign=\"middle\">&nbsp;</td><td width=\"34%\" align=\"center\" valign=\"middle\"><a href=\"javascript:SaveIt();document.leConfig.submit();\" onMouseOver=\"javascript:imageOnDHTML3('saveit','ov');\" onMouseOut=\"javascript:imageOffDHTML3('saveit','off');\"><img src=\"images/newones/saveit_off.gif\" border=\"0\" name=\"saveit\"></a></td></tr>";
	$TrashIt = "<tr><td width=\"100%\" colspan=\"3\" align=\"center\" valign=\"middle\"><a href=\"javascript:trigger('stank_reconfig.html?CMPartNum=$CMPartNum');\" onMouseOver=\"javascript:imageOnDHTML3('trashit','ov');\" onMouseOut=\"javascript:imageOffDHTML3('trashit','off');\"><img src=\"images/newones/trashit_off.gif\" border=\"0\" name=\"trashit\"></a></td></tr>";
	$SaveCartText = "To Save this configuration for later review click 'Save It!'. To put this configuration in your shopping-cart click 'Cart It!'.";
	$EmailIt = "<a href=\"$StartURLer('stank_emailit.cgi?MySubject=$SavedCMSeries&MyTitle=$SavedCMSeries&MyLoad=loadsys&MyData=$CMPartNum&EmailSubject=$MainTitle'$EndURLer\" onMouseOver=\"javascript:imageOnDHTML('emailit','ov');\" onMouseOut=\"javascript:imageOffDHTML('emailit','off');\"><img src=\"images/tables/but_emailit_off.gif\" width=\"62\" height=\"21\" name=\"emailit\" border=\"0\"></a>";
}
else {
	if ($Cookies{'Echado'} eq "YES") { 	$EQuoteIt = "<tr><td width=\"100%\" colspan=\"3\" align=\"center\" valign=\"middle\"><a href=\"javascript:EQuoteIt();document.leConfig.submit();\" onMouseOver=\"javascript:imageOnDHTML3('equoteit','ov');\" onMouseOut=\"javascript:imageOffDHTML3('equoteit','off');\"><img src=\"images/newones/equoteit_off.gif\" border=\"0\" name=\"equoteit\"></a></td></tr>"; }
	else { $EQuoteIt = "<tr><td width=\"100%\" colspan=\"3\" align=\"center\" valign=\"middle\"><input type=\"image\" name=\"submit\" onMouseOver=\"javascript:imageOnDHTML2(this,'equoteit','ov');\" onMouseOut=\"javascript:imageOffDHTML2(this,'equoteit','off');\" src=\"images/newones/equoteit_off.gif\" width=\"60\" height=\"48\" border=\"0\"></a></td></tr>"; }
	$CartOrSave = "";
	$TrashIt = "<tr><td width=\"100%\" colspan=\"3\" align=\"center\" valign=\"middle\"><a href=\"javascript:trigger('stank_reconfig.html?CMPartNum=$CMPartNum');\" onMouseOver=\"javascript:imageOnDHTML3('trashit','ov');\" onMouseOut=\"javascript:imageOffDHTML3('trashit','off');\"><img src=\"images/newones/trashit_off.gif\" border=\"0\" name=\"trashit\"></a></td></tr>";
	$EmailIt = "&nbsp;";
}

if ($SavedCMSeries eq "GreatWhite") { $MuaSeries = "Great White"; }
else { $MuaSeries = "$SavedCMSeries"; }

##### --> NMUSD
if ($FORM{'NMUSD'} eq "1") {
	$lePrecious = "<font class=\"stankprice\"><br><center>Call or request E-Quote<br>for product pricing</center></font><input type=\"hidden\" name=\"NMUSD\" value=\"1\">";
	$orPricingtxt = " or pricing";
}
elsif ($FORM{'MSP'} eq "1") {
	$lePrecious = "<font class=\"stankprice\"><br><center>Call or request E-Quote<br>for product pricing</center></font><input type=\"hidden\" name=\"MSP\" value=\"1\">";
	$orPricingtxt = " or pricing";
}
else {
	$lePrecious = "<font class=\"stankprice\"><br><center>System's New Price<br><b>\$$EntireTotal</b></center></font>";
	$orPricingtxt = "";	
}

print "Content-type: text/html\n\n";

{
print <<EOF

<html>
<head>
<title>Company Name</title>
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

function imageOffDHTML2(daobject,which,thisone) {
	var cual = 	"images/newones/"+which+"_"+thisone+".gif";
	daobject.src = cual;
}
function imageOnDHTML2(daobject,which,thisone) {
	var cual = 	"images/newones/"+which+"_"+thisone+".gif";
	daobject.src = cual;
}

function imageOffDHTML3(which,thisone) {
	var cual = 	"images/newones/"+which+"_"+thisone+".gif";
	document.images[which].src = cual;
}
function imageOnDHTML3(which,thisone) {
	var cual = 	"images/newones/"+which+"_"+thisone+".gif";
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

function SaveIt() {
	document.leConfig.CartSaveEQuote.value = "SAVE";
}
function CartIt() {
	document.leConfig.CartSaveEQuote.value = "CART";
}
function EQuoteIt() {
	document.leConfig.CartSaveEQuote.value = "EQUOTE";
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
<base href="http://www.rhomberg.com/systemConfigurator/">
</head>
<body bgcolor="#ffffff" text="#8F8FAB" leftmargin="0" topmargin="0" marginwidth="0" scroll="yes" marginheight="0" $NSPrinter>

EOF
}

if ($Cookies{'Echado'} ne "YES") { print "<form action=\"stank_cse.html\" name=\"leConfig\" method=\"post\" onSubmit=\"return checkForm();\">"; }
else { print "<form action=\"stank_cse.html\" name=\"leConfig\" method=\"post\">"; }
{
print <<EOF

<input type="hidden" name="CMPartNum" value="$CMPartNum">
<input type="hidden" name="Warranty" value="$Warranty">
<input type="hidden" name="PricingClass" value="$PricingClass">
<input type="hidden" name="ItemName" value="$ItemName">
<input type="hidden" name="CMSeries" value="$SavedCMSeries">
<input type="hidden" name="CartSaveEQuote" value="">


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
                      <td align="center"><font class="btext"><b>Customize Your $MuaSeries&#153; $SavedPricingClass</b></font></td>
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
<td width="40%" valign="middle" align="center"><img src="/dbimages/prod_common/$SmallImageN" width="165" height="100" vspace="20" border="0"></td>
<td width="55%" valign="top">$lePrecious<font class="btext"><br><b>System Re-Configuration Successful!</b><br>Your customized <b>$MuaSeries Series&#153;</b> system configuration is listed below. Your new $MuaSeries&#153; system is color-coded to help you locate the components you chose for your system. Follow the 'Component Legend' located directly below these instructions to see what the different colors mean. $SaveCartText To Re-Configure this system just click 'Trash It! ', to start over. To inquire about buying$orPricingtxt this system click 'E-Quote It!'.
<br><br></font></td>
<td width="5%">&nbsp;</td>
</tr>
</table>

           <table width="100%" cellspacing="1" cellpadding="0" bgcolor="#FFFFFF">
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="0" bgcolor="#F2F2F7" class="stankth" height="18" $border>
                    <tr> 
                      <td align="center"><font class="btext"><b>Component Legend</b></font></td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="0" class="stankth" $border>
                    <tr> 
                      <td width="5%">&nbsp;</td><td align="left" width="90%"><font class="btext"><nobr><font class="btext3_blue"><<img src="images/checkbox_blue.gif" border="0">> <b>Default Components</b></font>&nbsp;&nbsp;&nbsp;<font class="btext3_green"><<img src="images/checkbox_green.gif" border="0">> <b>Single Choice</b></font>&nbsp;&nbsp;&nbsp;<font class="btext3_red"><<img src="images/checkbox_red.gif" border="0">> <b>Multiple Choice</b></font></nobr></font></td><td width="5%">&nbsp;</td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
<br>

<table width="100%" align="center" cellpadding="2" cellspacing="0" border="0">
<tr> 
<td width="65%" valign="top">


<table width="100%" align="center" cellpadding="0" cellspacing="0" border="0">
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

	if ($ThyChar eq "Single") { $MuaCheckBox = "checkbox_green"; $leColor = "green"; }
	elsif ($ThyChar eq "Multiple") { $MuaCheckBox = "checkbox_red"; $leColor = "red"; }
	else { $MuaCheckBox = "checkbox_blue"; $leColor = "blue"; }

	if ($ThyChar eq "Single" && $MuaCount eq "0") { $CatCount--; }
	
	if ($MuaCount eq "0") { $CualC = "MainCategory"; $CualN = "MainName"; $CualC2 = "MainNumeros"; }
	else { $CualC = "Sub$CatCount\Category"; $CualN = "Sub$CatCount\Name"; $CualC2 = "Sub$CatCount\Numeros"; }

	if ($ThyCMNum ne "NONE") {
		if ($LastMuaCate eq "$ThyCategory") { 
			$MuaCategory = "";
			print "<tr height=\"12\"><td valign=\"top\"  width=\"8%\" align=\"center\"><img src=\"images/$MuaCheckBox.gif\" border=\"0\"></td><td valign=\"top\"  width=\"92%\"><font class=\"btext_$leColor\" style=\"line-height:10px\">$ThyName</font></td></tr>";
			push(@theParts,"$ThyCategory,,,,,$ThyName,,,,,$ThyCMNum");
		}
		else {
			$MuaCategory = "<b>$ThyCategory</b>"; 
			print "<tr height=\"20\"><td valign=\"middle\"  width=\"100%\" colspan=\"2\"><font class=\"btext3_$leColor\"><b>&nbsp;&nbsp;$MuaCategory</b></font></td></tr>";
			print "<tr height=\"12\"><td valign=\"top\"  width=\"8%\" align=\"center\"><img src=\"images/$MuaCheckBox.gif\" border=\"0\"></td><td valign=\"top\"  width=\"92%\"><font class=\"btext_$leColor\" style=\"line-height:10px\">$ThyName</font></td></tr>";
			if ($MuaCount ne "0") { $CatCount++; }
		}
		$LastMuaCate = "$ThyCategory";
		push(@AllPartes,"$ThyCategory,,,,,$ThyCMNum,,,,,$ThyLbs,,,,,$ThyCost");
	$MuaCount++;

		if ($CualC eq "MainCategory") {
			## ---------->>> END WITH WARRANTY
			if ($SavedWarranty ne "") {
				print "<tr height=\"20\"><td valign=\"middle\" width=\"100%\" colspan=\"2\"><font class=\"btext3_blue\"><b>&nbsp;&nbsp;$SavedPricingClass Warranty</b></font>";
				print "<tr height=\"12\"><td valign=\"top\" width=\"8%\" align=\"center\">&nbsp;</td><td valign=\"top\"  width=\"92%\"><font class=\"btext_blue\" style=\"line-height:10px\">$SavedWarranty</font></td></tr>";
			}
		}
	}
}


if ($MuaCount eq "0") { print "<tr><td valign=\"top\"  width=\"100%\"><center><font class=\"btext3\">Sorry, no results found...</font></center></td></tr>"; }

## ---------->>> IF ACCESSORIES AVAILABLE
if (@AccTotales) {
	print "<tr height=\"20\"><td valign=\"top\" width=\"100%\" colspan=\"2\"><font class=\"btext3_red\"><b>&nbsp;&nbsp;Accessories</b></font></td></tr>";
	foreach $MuaAccess (@ProdAccessories) {
		@MuaAA = split(/,,,,,/, $MuaAccess);
		push(@AllPartes,"Accessory,,,,,$MuaAA[0],,,,,$MuaAA[2],,,,,$MuaAA[3]");
		print "<tr height=\"12\"><td valign=\"top\"  width=\"8%\" align=\"center\"><img src=\"images/checkbox_red.gif\" border=\"0\"></td><td width=\"92%\"><font class=\"btext_red\" style=\"line-height:10px\">$MuaAA[0]</font></td></tr>";
	}
}

## ALL PARTS NUMBERS, WEIGHT AND PRICE FIELDS
$MuaCounter=0;
foreach $daParte (@AllPartes) {
	$MuaCounter++;
	@splitParte = split(/,,,,,/, $daParte);
	## PARTS
	if ($MuaCounter eq "1") { $PartsListing = "$splitParte[0]-----$splitParte[1]"; }
	else { $PartsListing = "$PartsListing" . ",,,,," . "$splitParte[0]-----$splitParte[1]"; }
	## POUNDS
	if ($MuaCounter eq "1") { $ElWeight = "$splitParte[2]"; }
	else { $ElWeight = $ElWeight + $splitParte[2]; }
}

print "<input type=\"hidden\" name=\"LasPartes\" value=\"$PartsListing\">";
print "<input type=\"hidden\" name=\"ElPeso\" value=\"$ElWeight\">";
print "<input type=\"hidden\" name=\"ElPrecio\" value=\"$EntireTotal\">";
print "<input type=\"hidden\" name=\"Image\" value=\"$SmallImageN\">";

print "</table></td><td width=\"35%\" valign=\"top\">";

if ($Cookies{'Echado'} ne "YES") {
{
print <<EOF

<table width="90%" cellspacing="0" cellpadding="2" border="0"><font class="btext3red">*Since you are currently NOT logged into the system you must complete the form below to be able to request an E-Quote on this system configuration. Please fill in all the fields correctly, then click the 'E-Quote' icon below.<br><br></font></table>
<font class="btext3"><b>Company Name</b><br></font>
<input type="text" name="CoNo" value="" size="15" class="inputtext15">
<font class="btext3"><br><br><b>First Name</b><br></font>
<input type="text" name="FirstName" value="" size="15" class="inputtext15">
<font class="btext3"><br><br><b>Last name</b><br></font>
<input type="text" name="LastName" value="" size="15" class="inputtext15">
<font class="btext3"><br><br><b>Email Address</b><br></font>
<input type="text" name="Email" value="" size="15" class="inputtext15">
<font class="btext3"><br><br><b>Area Code - Phone Number</b><br></font>
<input type="text" name="Area" value="" size="3" class="inputtext3"><font class="btext3"> - </font><input type="text" name="Phone" value="" size="7" class="inputtext7"><font class="btext3red"><br><i>(*only numbers)</i><br><br><br></font>

<script language="Javascript">
function checkForm() {
EQuoteIt();
var missingdrop = "";
var thefirst = "";

if (document.leConfig.CoNo.value == "" || document.leConfig.CoNo.value == " ") {
    missingdrop += "\\n     - Company Name";
	thefirst = "CoNo";
}

if (document.leConfig.FirstName.value == "" || document.leConfig.FirstName.value == " ") {
    missingdrop += "\\n     - First Name";
	if (thefirst == "") { thefirst = "FirstName"; }
}

if (document.leConfig.LastName.value == "" || document.leConfig.LastName.value == " ") {
    missingdrop += "\\n     - Last Name";
	if (thefirst == "") { thefirst = "LastName"; }
}

// CHECK EMAIL
  if (document.leConfig.Email.value == "")	{
    missingdrop += "\\n     - Email";
	if (thefirst == "") { thefirst = "Email"; }
  } else if ((document.leConfig.Email.value.indexOf('\@') == -1) || 
        (document.leConfig.Email.value.indexOf('.') == -1)) {
    missingdrop += "\\n     - Email Format should be: username\@mycompany.com";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.leConfig.Email.value.indexOf(',') != -1)) {
    missingdrop += "\\n     - Commas are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.leConfig.Email.value.indexOf(';') != -1)) {
    missingdrop += "\\n     - Semicolons are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.leConfig.Email.value.indexOf(':') != -1)) {
    missingdrop += "\\n     - Colons are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.leConfig.Email.value.indexOf('&') != -1)) {
    missingdrop += "\\n     - Ampersands are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }
  if ((document.leConfig.Email.value.indexOf(' ') != -1)) {
    missingdrop += "\\n     - Spaces are not allowed in email addresses";
	if (thefirst == "") { thefirst = "Email"; }
  }


// Check Phone number and format if it is there get the area code and num and feed the Phone field
if (isNaN(document.leConfig.Area.value) || (document.leConfig.Area.value == "") || (document.leConfig.Area.value == " ") || (document.leConfig.Area.value.length != 3)) {
    missingdrop += "\\n     - Area Code must be a 3 digit number";
	if (thefirst == "") { thefirst = "Area"; }
}
else if (isNaN(document.leConfig.Phone.value) || (document.leConfig.Phone.value == "") || (document.leConfig.Phone.value == " ") || (document.leConfig.Phone.value.indexOf('-') != -1) || (document.leConfig.Phone.value.length != 7)) {
    missingdrop += "\\n     - Phone Number must be a 7 digit number\\n        *No hyphen (-) necessary";
	if (thefirst == "") { thefirst = "Phone"; }
}



// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    missingdrop ="___________________________________________                   \\n\\n" + "  Sorry, I cannot process your request because the\\n  following fields are either blank or filled incorrectly:\\n" + "___________________________________________                   \\n\\n" +
    missingdrop + "\\n\\n___________________________________________                   " + "\\n\\n   To continue, check fields and submit form again!" + "\\n___________________________________________";
    alert(missingdrop);
	document.leConfig[thefirst].focus();
    return false;
} 
else {
return true;
}
}
</script>

EOF
}

}

print "<table width=\"100%\" cellspacing=\"0\" cellpadding=\"2\" border=\"0\">$EQuoteIt $CartOrSave $TrashIt</table>";


{
print <<EOF




</td></tr>
</table>

<br>
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