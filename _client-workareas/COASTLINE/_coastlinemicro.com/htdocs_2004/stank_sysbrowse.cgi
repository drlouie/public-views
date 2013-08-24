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
if (($browser =~ "Mozilla/" && $browser =~ "6.") || $browser =~ "Netscape6") { $tablewidth = "100%"; $t1 = "5"; $t2 = "64%"; $t3 = "18%"; $t4 = "18%"; $t5 = "25%"; $t6 = "75%"; }	
else { $tablewidth = "470"; $t1 = "5"; $t2 = "339"; $t3 = "79"; $t4 = "42"; $t5 = "170"; $t6 = "300"; }
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


##----------->>> Grab PRODUCTS STUFF
use DBI;
my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
$dbh->{RaiseError} = 1; 
$count=0;
my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$CMPartNum'");
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
	push(@Images, "$row[17]-----SMALL");
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
if (@LargeImages ne "") { $LPhoto = "<a href=\"javascript:trigger('stank_images.html?CMPartNum=$CMPartNum&ComingFrom=sysbrowse');\" onMouseOver=\"javascript:imageOnDHTML('lphoto','ov');\" onMouseOut=\"javascript:imageOffDHTML('lphoto','off');\"><img src=\"images/tables/but_lphoto_off.gif\" width=\"75\" height=\"20\" name=\"lphoto\" border=\"0\"></a>"; $TriggerPhoto = "javascript:trigger('stank_images.html?CMPartNum=$CMPartNum&ComingFrom=sysbrowse');"; }
else { $LPhoto = "<img src=\"images/tables/but_lphoto_dn.gif\" width=\"75\" height=\"20\" name=\"lphoto\" border=\"0\">"; $TriggerPhoto = "#"; }

## MULTIMEDIA
if ($SavedMediaCode ne "") { $SysMedia = "<a href=\"javascript:trigger('stank_media.html?MyCode=$SavedMediaCode&ComingFrom=sysbrowse');\" onMouseOver=\"javascript:imageOnDHTML('multimedia','ov');\" onMouseOut=\"javascript:imageOffDHTML('multimedia','off');\"><img src=\"images/tables/but_multimedia_off.gif\" width=\"73\" height=\"20\" name=\"multimedia\" border=\"0\"></a>"; }
else { $SysMedia = "<img src=\"images/tables/but_multimedia_dn.gif\" width=\"73\" height=\"20\" name=\"multimedia\" border=\"0\">"; }

if ($FORM{'NSPRINT'}) { $NSPrinter = "onload=\"javascript:printPageNS();\""; }


$Counter = 0;
foreach (1 .. $Numero) {
$Counter++;

	@MyParts = split(/,,,,,/, $Parts[0]);
	shift(@Parts);
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
	
	if ($Character eq "All" && $Parties =~ ",") {
		$EstaCuenta=0;
		@SubParts = split(/,/, $Parties);
		foreach $SubPart (@SubParts) {
			$EstaCuenta++;
			my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$SubPart' ORDER BY ItemName ASC");
			$sth->execute or die "Unable to execute query\n"; 
			my @row;
			while(@row = $sth->fetchrow_array) {
				$MiCuesta = $row[21];
				$Emblem = $row[16];
				$Compania = $row[6];
				$MiEsteNombre = $row[11];
				$ItsDesc = $row[12];
				if ($LastCATE eq "$Category") { $CATE = "NONE"; }
				else { $CATE = "$Category"; }
				push(@SubPartes,"$CATE,,,,,$Type,,,,,$MiEsteNombre,,,,,$SubPart,,,,,$Counter,,,,,$Character,,,,,$ItsDesc,,,,,$MiCuesta");
				push(@SubTotales,"$MiCuesta,,,,,$Counter,,,,,$Character");
				if ($Compania ne "" && $Compania ne "NONE") { push(@Companias,"$Compania"); }
				$LastCATE = "$Category";
			}
			$sth->finish;
		}
	}
	else {
		@SubParts = split(/,/, $Parties);
		my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$SubParts[0]' ORDER BY ItemName ASC");
		$sth->execute or die "Unable to execute query\n"; 
		my @row;
		while(@row = $sth->fetchrow_array) {
			$SubPart = $row[1];
			$MiEsteNombre = $row[11];
			$ItsDesc = $row[12];
			$Emblem = $row[16];
			$Compania = $row[6];
			$MiCuesta = $row[21];
			push(@SubPartes,"$Category,,,,,$Type,,,,,$MiEsteNombre,,,,,$SubPart,,,,,$Counter,,,,,$Character,,,,,$ItsDesc,,,,,$MiCuesta");
			push(@SubTotales,"$MiCuesta,,,,,$Counter,,,,,$Character");
			if ($Compania ne "" && $Compania ne "NONE") { push(@Companias,"$Compania"); }
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
	elsif($tigerNAS eq "YES") {
		$EntireTotal = $EntireTotal;	
	}
	else {
		$Markup = ($EntireTotal / .65);
		$Markup = sprintf("%.2f", $Markup);
		$EntireTotal = $Markup;
	}

	if ($FORM{'TPP'} eq "1") { 
		$EntireTotal = ($firstItem + $EntireTotal);
	}

	$EntireTotal = sprintf("%.2f", $EntireTotal);
}


if ($FORM{'NMUSD'} eq "1" || $FORM{'MSP'} eq "1") { $EmailIt = "&nbsp;"; }
else {  }

## MONITOR OR NO MONITOR EXTRA? NOTEBOOK OR OTHER...
if ($SavedPricingClass eq "Notebook" || $SavedPricingClass eq "Server" || $FORM{'TPP'} eq "1") { $MonitorNOT = ""; }
else { $MonitorNOT = "<br><font class=\"stankprice2\">(monitor not included)<br>"; }


## PRICE OR NO PRICE? LOGGED OR NOT...
if ($Cookies{'Echado'} eq "YES") { $EntireTotal = "<font class=\"stankprice\"><br>Price As Shown<br><b>\$$EntireTotal</b></font>"; }
elsif ($tigerNAS eq "YES") { $EntireTotal = "<font class=\"stankprice\"><br>Price As Shown<br><b>\$$EntireTotal</b></font>"; }
else { $EntireTotal = "<font class=\"stankprice\"><br><b>Call for Proper Pricing</b></font>"; }

#### --> NMUSD
if ($FORM{'NMUSD'} eq "1") {
	$lePrecious = "<font class=\"stankprice\"><br><center>Call or request E-Quote<br>for product pricing</center></font><input type=\"hidden\" name=\"NMUSD\" value=\"1\">";
	$EmailIt = "&nbsp;";
}
#### --> MSP
elsif ($FORM{'MSP'} eq "1") {
	$lePrecious = "<font class=\"stankprice\"><br><center>Call or request E-Quote<br>for product pricing</center></font><input type=\"hidden\" name=\"MSP\" value=\"1\">";
	$EmailIt = "&nbsp;";
}
#### --> TPP
elsif ($FORM{'TPP'} eq "1") { 
	$lePrecious = "<br><center>$EntireTotal</center>"; 
	$EmailIt = "&nbsp;";
}
#### --> COMMON
else { 
	$lePrecious = "<br><center>$EntireTotal</center>"; 
	$EmailIt = "<a href=\"javascript:void(0);\" onClick=\"toggleEmailer('https://www.coastlinemicro.com/stank_emailit.html?MySubject=$SavedCMSeries&MyTitle=$SavedCMSeries&MyLoad=loadsys&MyData=$CMPartNum&EmailSubject=$MainTitle');\" onMouseOver=\"javascript:imageOnDHTML('emailit','ov');\" onMouseOut=\"javascript:imageOffDHTML('emailit','off');\"><img src=\"images/tables/but_emailit_off.gif\" width=\"62\" height=\"21\" name=\"emailit\" border=\"0\"></a>";
}


### --> TPP
if ($FORM{'TPP'} eq "1") { 
	$leTS = "<img src=\"images/tables/but_techspecs_dn.gif\" width=\"77\" height=\"20\" name=\"techspecs\" border=\"0\">";
	$leDRIVER = "<img src=\"images/tables/but_sysdrivers_dn.gif\" width=\"78\" height=\"20\" name=\"sysdrivers\" border=\"0\">";
	$lePrinter = "&nbsp;";
}
else {
	$leTS = "<a href=\"javascript:trigger('products.html?title=$FORM{'title'}&specIt=$CMPartNum$MSP$NMUSD$TPP');\" onMouseOver=\"javascript:imageOnDHTML('techspecs','ov');\" onMouseOut=\"javascript:imageOffDHTML('techspecs','off');\"><img src=\"images/tables/but_techspecs_off.gif\" width=\"77\" height=\"20\" name=\"techspecs\" border=\"0\"></a>";
	$leDRIVER = "<a href=\"javascript:trigger('products.html?title=$FORM{'title'}&sysdrivers=$CMPartNum$MSP$NMUSD$TPP');\" onMouseOver=\"javascript:imageOnDHTML('sysdrivers','ov');\" onMouseOut=\"javascript:imageOffDHTML('sysdrivers','off');\"><img src=\"images/tables/but_sysdrivers_off.gif\" width=\"78\" height=\"20\" name=\"sysdrivers\" border=\"0\"></a>";
	$lePrinter = "<a href=\"javascript:void(0);\" onClick=\"javascript:runTemplate('stank_sysbrowse.html','CMPartNum','$CMPartNum');\" onMouseOver=\"javascript:imageOnDHTML('printit','ov');\" onMouseOut=\"javascript:imageOffDHTML('printit','off');\"><img src=\"images/tables/but_printit_off.gif\" width=\"67\" height=\"21\" name=\"printit\" border=\"0\"></a>";
}

## RECONFIGURABLE?
if ($SavedReconfig eq "Y") { $ConfigIT = "<a href=\"#\" onClick=\"trigger('products.html?reconfigIt=$CMPartNum&title=$FORM{'title'}$MSP$NMUSD$TPP');\" onMouseOver=\"javascript:imageOnDHTML('configureit','ov');\" onMouseOut=\"javascript:imageOffDHTML('configureit','off');\"><img src=\"images/tables/but_configureit_off.gif\" width=\"81\" height=\"20\" name=\"configureit\" border=\"0\"></a>"; }
else { $ConfigIT = "<img src=\"images/tables/but_configureit_dn.gif\" width=\"81\" height=\"20\" name=\"configureit\" border=\"0\">"; }


print "Content-type: text/html\n\n";
{
print <<EOF

<html>
<head>
<title>Coastline Micro Inc.</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<LINK REL="STYLESHEET" HREF="common_css.html?anchor=333366&anchorov=EB0000&weight=normal&weightov=normal&decor=underline&decorov=underline" Type="text/css">
<STYLE TYPE="text/css">
body { background-color:#ffffff; scrollbar-face-color:#F2F2F7; scrollbar-highlight-color:#F2F2F7; scrollbar-shadow-color:#8f8fab; scrollbar-3dlight-color: #333366; scrollbar-arrow-color:#333366; scrollbar-track-color:#F2F2F7; scrollbar-darkshadow-color:#8f8fab; }
</STYLE>
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
    window.open('stank_sysbrowse.html?CMPartNum=$CMPartNum&NSPRINT=1','PRINT','width=485,height=590');
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
<body bgcolor="#ffffff" text="#8F8FAB" leftmargin="0" topmargin="0" marginwidth="0" scroll="yes" marginheight="0" $NSPrinter>



<table width="$tablewidth" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td align="center" valign="middle" width="$tablewidth" height="25"> 
      <table width="$tablewidth" border="0" cellspacing="0" cellpadding="0" background="images/tables/topbar.jpg" height="24">
        <tr> 
          <td width="$t1"><img src="images/tables/topbar_left.jpg" width="5" height="24"></td>
          <td width="$t2"><nobr><font class="btext">&nbsp;&nbsp;<b>$MainTitle</b></font></nobr></td>
          <td width="$t3" align="center" valign="top">$EmailIt</td>
          <td width="$t4" align="center" valign="top"><a href="javascript:void(0);" onClick="javascript:printPage('stank_sysbrowse.html','CMPartNum','$CMPartNum');" onMouseOver="javascript:imageOnDHTML('printit','ov');" onMouseOut="javascript:imageOffDHTML('printit','off');"><img src="images/tables/but_printit_off.gif" width="67" height="21" name="printit" border="0"></a></td>
          <td width="$t1" align="right" valign="top"><img src="images/tables/topbar_right.jpg" width="5" height="24"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr> 
    <td align="center"> 
      <table width="$tablewidth" border="0" cellspacing="0" cellpadding="0" height="30">
        <tr align="center"> 
          <td width="20%" align="left"><img src="images/tables/icon_back_off.gif" width="60" height="20" name="back" border="0"></td>
          <td width="16%">$ConfigIT</td>
          <td width="16%"><a href="javascript:trigger('stank_techspecs.html?CMPartNum=$CMPartNum&ComingFrom=sysbrowse');" onMouseOver="javascript:imageOnDHTML('techspecs','ov');" onMouseOut="javascript:imageOffDHTML('techspecs','off');"><img src="images/tables/but_techspecs_off.gif" width="77" height="20" name="techspecs" border="0"></a></td>
          <td width="16%"><a href="javascript:trigger('stank_sysdrivers.html?CMPartNum=$CMPartNum&ComingFrom=sysbrowse');" onMouseOver="javascript:imageOnDHTML('sysdrivers','ov');" onMouseOut="javascript:imageOffDHTML('sysdrivers','off');"><img src="images/tables/but_sysdrivers_off.gif" width="78" height="20" name="sysdrivers" border="0"></a></td>
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
          <td align="center" valign="top" height="150" width="$t5">$lePrecious<a href="$TriggerPhoto"><img src="/dbimages/prod_common/$SmallImageN" width="165" height="100" vspace="20" border="0" alt="Click to view large photo(s) of this product."></a>$MonitorNOT<br></font>

          </td>
          <td valign="top" width="$t6"> 
            <table width="100%" cellspacing="1" cellpadding="0" bgcolor="#FFFFFF">
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="0" bgcolor="#F2F2F7" class="stankth" height="18" $border>
                    <tr> 
                      <td align="center"><font class="btext"><b>System Specifications</b></font></td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr> 
                <td> 
                  <table width="100%" cellspacing="0" cellpadding="2" class="stankth" $border>
                    <tr> 
                      <td> 

EOF
}

$SCuenta=0;
foreach $EstaParte (@SubPartes) {
	@EsteMio = split(/,,,,,/, $EstaParte);

	$Category = $EsteMio[0];
	$Type = $EsteMio[1];
	$MiEsteNombre = $EsteMio[2];
	$SubPart = $EsteMio[3];
	$Counter = $EsteMio[4];
	$Character = $EsteMio[5];
	$ItsDesc = $EsteMio[6];
	
	##--->> REFORMAT INCOMING DATA FOR PARSING
	$DCount = "0";
	@DescCount = split(//, $ItsDesc);
	foreach $DescDesc (@DescCount) { 
	$DCount++; 
		if ($DCount >= "50" && ($DescDesc eq "." || $DescDesc eq "!")) { 
			$ItsDesc = substr($ItsDesc, 0, $DCount); 
		} 
	}
	##--->> REFORMAT INCOMING DATA FOR PARSING
	$NCount = "0";
	@NameCount = split(//, $MiEsteNombre);
	foreach $NameName (@NameCount) { 
	$NCount++; 
		if ($NCount >= "35" && $NameName eq " ") { 
			$MiEsteNombre = substr($MiEsteNombre, 0, $NCount); 
		} 
	}

	if ($MiEsteNombre ne "none" && $MiEsteNombre ne "NONE") { 
		if ($SCuenta ne "0" && $Category ne "NONE") { print "<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" bgcolor=\"#F2F2F7\"><tr><tr><td width=\"100%\" height=\"10\"><font size=\"-4\" face=\"verdana,arial,helvetica\">&nbsp;</font></td></tr></table><hr width=\"65%\" align=\"center\" size=\"1\" color=\"#333366\">"; }
		print "<table width=\"100%\" border=\"0\" bordercolor=\"#FFFFFF\" cellspacing=\"0\" cellpadding=\"0\" bgcolor=\"#F2F2F7\">";
		print "<tr>";
		if ($Category eq "NONE") { print "<td colspan=\"2\" height=\"5\"><font face=\"verdana,arial,helvetica\" size=\"-4\">&nbsp;</font></td>"; }
		else { print "<td height=\"20\" width=\"90%\" ><font class=\"btext4\">&nbsp;<b>$Category</b></font></td>"; }


		if ($tigerNAS eq "YES") {
			print "<td rowspan=\"2\" width=\"10%\" align=\"center\" valign=\"top\">&nbsp;</td>";
			print "</tr><tr><td width=\"90%\" align=\"right\">";
			print "<table width=\"95%\" border=\"0\" cellspacing=\"0\" cellpadding=\"3\" bgcolor=\"#FFFFFF\"><tr><td colspan=\"2\" width=\"100%\" height=\"15\"><font class=\"btext3\" style=\"color:#333366;font-weight:normal;\">$MiEsteNombre</font></td></tr>";
			print "</table>";
			print "</td></tr></table>";
		}
		else {
			print "<td rowspan=\"2\" width=\"10%\" align=\"center\" valign=\"top\"><a href=\"javascript:trigger('stank_viewprod.html?CMPartNum=$SubPart&ComingFrom=sysbrowse&OGPart=$CMPartNum');\" onMouseOver=\"javascript:imageOnDHTML2('I_$SCuenta','info','ov');\" onMouseOut=\"javascript:imageOffDHTML2('I_$SCuenta','info','off');\"><img src=\"images/db/but_info_off.gif\" width=\"12\" height=\"12\" vspace=\"5\" border=\"0\" name=\"I_$SCuenta\"></a></td>";
			print "</tr><tr><td width=\"90%\" align=\"right\">";
			print "<table width=\"95%\" border=\"0\" cellspacing=\"0\" cellpadding=\"3\" bgcolor=\"#FFFFFF\"><tr><td colspan=\"2\" width=\"100%\" height=\"15\"><font class=\"btext3\"><a href=\"javascript:trigger('stank_viewprod.html?CMPartNum=$SubPart&ComingFrom=sysbrowse&OGPart=$CMPartNum');\" onMouseOver=\"javascript:imageOnDHTML2('I_$SCuenta','info','ov');\" onMouseOut=\"javascript:imageOffDHTML2('I_$SCuenta','info','off');\">$MiEsteNombre</a></font></td></tr>";
			print "<tr><td width=\"4%\">&nbsp;</td><td width=\"86%\"><font class=\"btext3\">$ItsDesc</font></td></tr></table>";
			print "</td></tr></table>";		
		}

		
	}
$SCuenta++;
}

{
print <<EOF
<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" bgcolor=\"#F2F2F7\"><tr><tr><td width=\"100%\" height=\"10\"><font size=\"-4\" face=\"verdana,arial,helvetica\">&nbsp;</font></td></tr></table>
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