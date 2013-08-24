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
	$PricingClass = "$FORM{'PricingClass'}";
	$ItemName = "$FORM{'ItemName'}";
	$Description = "$FORM{'Description'}";	
	$TechSpecs = "$FORM{'TechSpecs'}";
	$Keywords = "$FORM{'Keywords'}";
	$SmallLogo = "$FORM{'SmallLogo'}";
	$LargeLogo = "$FORM{'LargeLogo'}";
	$SneakPeak = "$FORM{'SneakPeak'}";
	$MediaCode = "$FORM{'Multimedia'}";
	$Warranty = "$FORM{'Warranty'}";
	$RelatedProd = "";
	$Accessories = "$FORM{'Accessories'}";
	$ProductType = "$FORM{'ProductType'}";
	$Searchable = "$FORM{'Searchable'}";
	$MainCategory = "$FORM{'MainCategory'}"; $MainNumbers = "$FORM{'MainNumeros'}";	$MainType = "$FORM{'MainType'}"; $MainCharacter = "$FORM{'MainCharacter'}";
	$Sub1Category = "$FORM{'Sub1Category'}"; $Sub1Numbers = "$FORM{'Sub1Numeros'}"; $Sub1Type = "$FORM{'Sub1Type'}"; $Sub1Character = "$FORM{'Sub1Character'}"; $EstaCuenta = 1;
	if ($Sub1Numbers ne "null" || $Sub1Numbers ne "Null" || $Sub1Numbers ne "NULL" || $Sub1Numbers ne "") { $Sub2Category = "$FORM{'Sub2Category'}"; $Sub2Numbers = "$FORM{'Sub2Numeros'}"; $Sub2Type = "$FORM{'Sub2Type'}"; $Sub2Character = "$FORM{'Sub2Character'}"; $EstaCuenta = 2; }
	if ($Sub2Numbers ne "null" || $Sub2Numbers ne "Null" || $Sub2Numbers ne "NULL" || $Sub2Numbers ne "") { $Sub3Category = "$FORM{'Sub3Category'}"; $Sub3Numbers = "$FORM{'Sub3Numeros'}"; $Sub3Type = "$FORM{'Sub3Type'}"; $Sub3Character = "$FORM{'Sub3Character'}"; $EstaCuenta = 3; }
	if ($Sub3Numbers ne "null" || $Sub3Numbers ne "Null" || $Sub3Numbers ne "NULL" || $Sub3Numbers ne "") { $Sub4Category = "$FORM{'Sub4Category'}"; $Sub4Numbers = "$FORM{'Sub4Numeros'}"; $Sub4Type = "$FORM{'Sub4Type'}"; $Sub4Character = "$FORM{'Sub4Character'}"; $EstaCuenta = 4; }
	if ($Sub4Numbers ne "null" || $Sub4Numbers ne "Null" || $Sub4Numbers ne "NULL" || $Sub4Numbers ne "") { $Sub5Category = "$FORM{'Sub5Category'}"; $Sub5Numbers = "$FORM{'Sub5Numeros'}"; $Sub5Type = "$FORM{'Sub5Type'}"; $Sub5Character = "$FORM{'Sub5Character'}"; $EstaCuenta = 5; }
	if ($Sub5Numbers ne "null" || $Sub5Numbers ne "Null" || $Sub5Numbers ne "NULL" || $Sub5Numbers ne "") { $Sub6Category = "$FORM{'Sub6Category'}"; $Sub6Numbers = "$FORM{'Sub6Numeros'}"; $Sub6Type = "$FORM{'Sub6Type'}"; $Sub6Character = "$FORM{'Sub6Character'}"; $EstaCuenta = 6; }
	if ($Sub6Numbers ne "null" || $Sub6Numbers ne "Null" || $Sub6Numbers ne "NULL" || $Sub6Numbers ne "") { $Sub7Category = "$FORM{'Sub7Category'}"; $Sub7Numbers = "$FORM{'Sub7Numeros'}"; $Sub7Type = "$FORM{'Sub7Type'}"; $Sub7Character = "$FORM{'Sub7Character'}"; $EstaCuenta = 7; }
	if ($Sub7Numbers ne "null" || $Sub7Numbers ne "Null" || $Sub7Numbers ne "NULL" || $Sub7Numbers ne "") { $Sub8Category = "$FORM{'Sub8Category'}"; $Sub8Numbers = "$FORM{'Sub8Numeros'}"; $Sub8Type = "$FORM{'Sub8Type'}"; $Sub8Character = "$FORM{'Sub8Character'}"; $EstaCuenta = 8; }
	if ($Sub8Numbers ne "null" || $Sub8Numbers ne "Null" || $Sub8Numbers ne "NULL" || $Sub8Numbers ne "") { $Sub9Category = "$FORM{'Sub9Category'}"; $Sub9Numbers = "$FORM{'Sub9Numeros'}"; $Sub9Type = "$FORM{'Sub9Type'}"; $Sub9Character = "$FORM{'Sub9Character'}"; $EstaCuenta = 9; }
	if ($Sub9Numbers ne "null" || $Sub9Numbers ne "Null" || $Sub9Numbers ne "NULL" || $Sub9Numbers ne "") { $Sub10Category = "$FORM{'Sub10Category'}"; $Sub10Numbers = "$FORM{'Sub10Numeros'}"; $Sub10Type = "$FORM{'Sub10Type'}"; $Sub10Character = "$FORM{'Sub10Character'}"; $EstaCuenta = 10; }
	if ($Sub10Numbers ne "null" || $Sub10Numbers ne "Null" || $Sub10Numbers ne "NULL" || $Sub10Numbers ne "") { $Sub11Category = "$FORM{'Sub11Category'}"; $Sub11Numbers = "$FORM{'Sub11Numeros'}"; $Sub11Type = "$FORM{'Sub11Type'}"; $Sub11Character = "$FORM{'Sub11Character'}"; $EstaCuenta = 11; }
	if ($Sub11Numbers ne "null" || $Sub11Numbers ne "Null" || $Sub11Numbers ne "NULL" || $Sub11Numbers ne "") { $Sub12Category = "$FORM{'Sub12Category'}"; $Sub12Numbers = "$FORM{'Sub12Numeros'}"; $Sub12Type = "$FORM{'Sub12Type'}"; $Sub12Character = "$FORM{'Sub12Character'}"; $EstaCuenta = 12; }
	if ($Sub12Numbers ne "null" || $Sub12Numbers ne "Null" || $Sub12Numbers ne "NULL" || $Sub12Numbers ne "") { $Sub13Category = "$FORM{'Sub13Category'}"; $Sub13Numbers = "$FORM{'Sub13Numeros'}"; $Sub13Type = "$FORM{'Sub13Type'}"; $Sub13Character = "$FORM{'Sub13Character'}"; $EstaCuenta = 13; }
	if ($Sub13Numbers ne "null" || $Sub13Numbers ne "Null" || $Sub13Numbers ne "NULL" || $Sub13Numbers ne "") { $Sub14Category = "$FORM{'Sub14Category'}"; $Sub14Numbers = "$FORM{'Sub14Numeros'}"; $Sub14Type = "$FORM{'Sub14Type'}"; $Sub14Character = "$FORM{'Sub14Character'}"; $EstaCuenta = 14; }
	if ($Sub14Numbers ne "null" || $Sub14Numbers ne "Null" || $Sub14Numbers ne "NULL" || $Sub14Numbers ne "") { $Sub15Category = "$FORM{'Sub15Category'}"; $Sub15Numbers = "$FORM{'Sub15Numeros'}"; $Sub15Type = "$FORM{'Sub15Type'}"; $Sub15Character = "$FORM{'Sub15Character'}"; $EstaCuenta = 15; }
	if ($Sub15Numbers ne "null" || $Sub15Numbers ne "Null" || $Sub15Numbers ne "NULL" || $Sub15Numbers ne "") { $Sub16Category = "$FORM{'Sub16Category'}"; $Sub16Numbers = "$FORM{'Sub16Numeros'}"; $Sub16Type = "$FORM{'Sub16Type'}"; $Sub16Character = "$FORM{'Sub16Character'}"; $EstaCuenta = 16; }
	if ($Sub16Numbers ne "null" || $Sub16Numbers ne "Null" || $Sub16Numbers ne "NULL" || $Sub16Numbers ne "") { $Sub17Category = "$FORM{'Sub17Category'}"; $Sub17Numbers = "$FORM{'Sub17Numeros'}"; $Sub17Type = "$FORM{'Sub17Type'}"; $Sub17Character = "$FORM{'Sub17Character'}"; $EstaCuenta = 17; }
	if ($Sub17Numbers ne "null" || $Sub17Numbers ne "Null" || $Sub17Numbers ne "NULL" || $Sub17Numbers ne "") { $Sub18Category = "$FORM{'Sub18Category'}"; $Sub18Numbers = "$FORM{'Sub18Numeros'}"; $Sub18Type = "$FORM{'Sub18Type'}"; $Sub18Character = "$FORM{'Sub18Character'}"; $EstaCuenta = 18; }
	if ($Sub18Numbers ne "null" || $Sub18Numbers ne "Null" || $Sub18Numbers ne "NULL" || $Sub18Numbers ne "") { $Sub19Category = "$FORM{'Sub19Category'}"; $Sub19Numbers = "$FORM{'Sub19Numeros'}"; $Sub19Type = "$FORM{'Sub19Type'}"; $Sub19Character = "$FORM{'Sub19Character'}"; $EstaCuenta = 19; }
	if ($Sub19Numbers ne "null" || $Sub19Numbers ne "Null" || $Sub19Numbers ne "NULL" || $Sub19Numbers ne "") { $Sub20Category = "$FORM{'Sub20Category'}"; $Sub20Numbers = "$FORM{'Sub20Numeros'}"; $Sub20Type = "$FORM{'Sub20Type'}"; $Sub20Character = "$FORM{'Sub20Character'}"; $EstaCuenta = 20; }
	if ($Sub20Numbers ne "null" || $Sub20Numbers ne "Null" || $Sub20Numbers ne "NULL" || $Sub20Numbers ne "") { $Sub21Category = "$FORM{'Sub21Category'}"; $Sub21Numbers = "$FORM{'Sub21Numeros'}"; $Sub21Type = "$FORM{'Sub21Type'}"; $Sub21Character = "$FORM{'Sub21Character'}"; $EstaCuenta = 21; }
	if ($Sub21Numbers ne "null" || $Sub21Numbers ne "Null" || $Sub21Numbers ne "NULL" || $Sub21Numbers ne "") { $Sub22Category = "$FORM{'Sub22Category'}"; $Sub22Numbers = "$FORM{'Sub22Numeros'}"; $Sub22Type = "$FORM{'Sub22Type'}"; $Sub22Character = "$FORM{'Sub22Character'}"; $EstaCuenta = 22; }
	if ($Sub22Numbers ne "null" || $Sub22Numbers ne "Null" || $Sub22Numbers ne "NULL" || $Sub22Numbers ne "") { $Sub23Category = "$FORM{'Sub23Category'}"; $Sub23Numbers = "$FORM{'Sub23Numeros'}"; $Sub23Type = "$FORM{'Sub23Type'}"; $Sub23Character = "$FORM{'Sub23Character'}"; $EstaCuenta = 23; }
	if ($Sub23Numbers ne "null" || $Sub23Numbers ne "Null" || $Sub23Numbers ne "NULL" || $Sub23Numbers ne "") { $Sub24Category = "$FORM{'Sub24Category'}"; $Sub24Numbers = "$FORM{'Sub24Numeros'}"; $Sub24Type = "$FORM{'Sub24Type'}"; $Sub24Character = "$FORM{'Sub24Character'}"; $EstaCuenta = 24; }
	if ($Sub24Numbers ne "null" || $Sub24Numbers ne "Null" || $Sub24Numbers ne "NULL" || $Sub24Numbers ne "") { $Sub25Category = "$FORM{'Sub25Category'}"; $Sub25Numbers = "$FORM{'Sub25Numeros'}"; $Sub25Type = "$FORM{'Sub25Type'}"; $Sub25Character = "$FORM{'Sub25Character'}"; $EstaCuenta = 25; }
	$ActionUser = "$Cookies{'Username'}";
	
{
print <<EOF

<table width="95%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update Inventory (System)</b></font></td>
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
							 SneakPeak='$SneakPeak', 
							 Warranty='$Warranty', 
							 RelatedProd='$RelatedProd', 
							 Accessories='$Accessories', 
							 ModifiedBy='$ActionUser', 
							 ModifiedOn=Null, 
							 ProductType='$ProductType', 
							 Searchable='$Searchable' 
							 WHERE CMPartNum='$CMPartNum'");
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish; 

	if ($EstaCuenta >= 1) { $SubCat1 = "Sub1Category='$Sub1Category', Sub1Type='$Sub1Type', Sub1Character='$Sub1Character', Sub1Parts='$Sub1Numbers', "; } else { $SubCat1 = ""; }
	if ($EstaCuenta >= 2) { $SubCat2 = "Sub2Category='$Sub2Category', Sub2Type='$Sub2Type', Sub2Character='$Sub2Character', Sub2Parts='$Sub2Numbers', "; } else { $SubCat2 = ""; }
	if ($EstaCuenta >= 3) { $SubCat3 = "Sub3Category='$Sub3Category', Sub3Type='$Sub3Type', Sub3Character='$Sub3Character', Sub3Parts='$Sub3Numbers', "; } else { $SubCat3 = ""; }
	if ($EstaCuenta >= 4) { $SubCat4 = "Sub4Category='$Sub4Category', Sub4Type='$Sub4Type', Sub4Character='$Sub4Character', Sub4Parts='$Sub4Numbers', "; } else { $SubCat4 = ""; }
	if ($EstaCuenta >= 5) { $SubCat5 = "Sub5Category='$Sub5Category', Sub5Type='$Sub5Type', Sub5Character='$Sub5Character', Sub5Parts='$Sub5Numbers', "; } else { $SubCat5 = ""; }
	if ($EstaCuenta >= 6) { $SubCat6 = "Sub6Category='$Sub6Category', Sub6Type='$Sub6Type', Sub6Character='$Sub6Character', Sub6Parts='$Sub6Numbers', "; } else { $SubCat6 = ""; }
	if ($EstaCuenta >= 7) { $SubCat7 = "Sub7Category='$Sub7Category', Sub7Type='$Sub7Type', Sub7Character='$Sub7Character', Sub7Parts='$Sub7Numbers', "; } else { $SubCat7 = ""; }
	if ($EstaCuenta >= 8) { $SubCat8 = "Sub8Category='$Sub8Category', Sub8Type='$Sub8Type', Sub8Character='$Sub8Character', Sub8Parts='$Sub8Numbers', "; } else { $SubCat8 = ""; }
	if ($EstaCuenta >= 9) { $SubCat9 = "Sub9Category='$Sub9Category', Sub9Type='$Sub9Type', Sub9Character='$Sub9Character', Sub9Parts='$Sub9Numbers', "; } else { $SubCat9 = ""; }
	if ($EstaCuenta >= 10) { $SubCat10 = "Sub10Category='$Sub10Category', Sub10Type='$Sub10Type', Sub10Character='$Sub10Character', Sub10Parts='$Sub10Numbers', "; } else { $SubCat10 = ""; }
	if ($EstaCuenta >= 11) { $SubCat11 = "Sub11Category='$Sub11Category', Sub11Type='$Sub11Type', Sub11Character='$Sub11Character', Sub11Parts='$Sub11Numbers', "; } else { $SubCat11 = ""; }
	if ($EstaCuenta >= 12) { $SubCat12 = "Sub12Category='$Sub12Category', Sub12Type='$Sub12Type', Sub12Character='$Sub12Character', Sub12Parts='$Sub12Numbers', "; } else { $SubCat12 = ""; }	
	if ($EstaCuenta >= 13) { $SubCat13 = "Sub13Category='$Sub13Category', Sub13Type='$Sub13Type', Sub13Character='$Sub13Character', Sub13Parts='$Sub13Numbers', "; } else { $SubCat13 = ""; }	
	if ($EstaCuenta >= 14) { $SubCat14 = "Sub14Category='$Sub14Category', Sub14Type='$Sub14Type', Sub14Character='$Sub14Character', Sub14Parts='$Sub14Numbers', "; } else { $SubCat14 = ""; }	
	if ($EstaCuenta >= 15) { $SubCat15 = "Sub15Category='$Sub15Category', Sub15Type='$Sub15Type', Sub15Character='$Sub15Character', Sub15Parts='$Sub15Numbers', "; } else { $SubCat15 = ""; }	
	if ($EstaCuenta >= 16) { $SubCat16 = "Sub16Category='$Sub16Category', Sub16Type='$Sub16Type', Sub16Character='$Sub16Character', Sub16Parts='$Sub16Numbers', "; } else { $SubCat16 = ""; }	
	if ($EstaCuenta >= 17) { $SubCat17 = "Sub17Category='$Sub17Category', Sub17Type='$Sub17Type', Sub17Character='$Sub17Character', Sub17Parts='$Sub17Numbers', "; } else { $SubCat17 = ""; }	
	if ($EstaCuenta >= 18) { $SubCat18 = "Sub18Category='$Sub18Category', Sub18Type='$Sub18Type', Sub18Character='$Sub18Character', Sub18Parts='$Sub18Numbers', "; } else { $SubCat18 = ""; }	
	if ($EstaCuenta >= 19) { $SubCat19 = "Sub19Category='$Sub19Category', Sub19Type='$Sub19Type', Sub19Character='$Sub19Character', Sub19Parts='$Sub19Numbers', "; } else { $SubCat19 = ""; }	
	if ($EstaCuenta >= 20) { $SubCat20 = "Sub20Category='$Sub20Category', Sub20Type='$Sub20Type', Sub20Character='$Sub20Character', Sub20Parts='$Sub20Numbers', "; } else { $SubCat20 = ""; }	
	if ($EstaCuenta >= 21) { $SubCat21 = "Sub21Category='$Sub21Category', Sub21Type='$Sub21Type', Sub21Character='$Sub21Character', Sub21Parts='$Sub21Numbers', "; } else { $SubCat21 = ""; }	
	if ($EstaCuenta >= 22) { $SubCat22 = "Sub22Category='$Sub22Category', Sub22Type='$Sub22Type', Sub22Character='$Sub22Character', Sub22Parts='$Sub22Numbers', "; } else { $SubCat22 = ""; }	
	if ($EstaCuenta >= 23) { $SubCat23 = "Sub23Category='$Sub23Category', Sub23Type='$Sub23Type', Sub23Character='$Sub23Character', Sub23Parts='$Sub23Numbers', "; } else { $SubCat23 = ""; }	
	if ($EstaCuenta >= 24) { $SubCat24 = "Sub24Category='$Sub24Category', Sub24Type='$Sub24Type', Sub24Character='$Sub24Character', Sub24Parts='$Sub24Numbers', "; } else { $SubCat24 = ""; }	
	if ($EstaCuenta >= 25) { $SubCat25 = "Sub25Category='$Sub25Category', Sub25Type='$Sub25Type', Sub25Character='$Sub25Character', Sub25Parts='$Sub25Numbers', "; } else { $SubCat25 = ""; }	
		
	my $sth = $dbh->prepare("UPDATE LOW_PRIORITY Systems 
							 SET MainCategory='$MainCategory', MainType='$MainType', MainCharacter='$MainCharacter', MainParts='$MainNumbers', 
							 $SubCat1
							 $SubCat2
							 $SubCat3
							 $SubCat4
							 $SubCat5
							 $SubCat6
							 $SubCat7
							 $SubCat8
							 $SubCat9
							 $SubCat10
							 $SubCat11
							 $SubCat12
							 $SubCat13
							 $SubCat14
							 $SubCat15
							 $SubCat16
							 $SubCat17
							 $SubCat18
							 $SubCat19
							 $SubCat20
							 $SubCat21
							 $SubCat22
							 $SubCat23
							 $SubCat24
							 $SubCat25
							 ModifiedBy='$ActionUser', 
							 ModifiedOn=Null 
							 WHERE Parent='$CMPartNum'");
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish; 
	$dbh->disconnect; 	
	print "<center><br><b>Inventory Updated</b><br><br>The the changes you have made to <b>$ItemName ($CMPartNum)</b> have been successfully saved to the system.<br><br><form><input type=\"button\" value=\"Back to System: $CMPartNum\" onClick=\"javascript:location.href='change_product_system.cgi?CMPartNum=$CMPartNum'\" class=\"inputbut\"><br><br><input type=\"button\" value=\"Inventory Main\" onClick=\"javascript:parent.location.href='change_product.cgi'\" class=\"inputbut\"></form><br></center><br><br></font>";
	
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
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update Inventory (System)</b></font></td>
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
	my $sth = $dbh->prepare("DELETE FROM Systems WHERE Parent='$CMPartNum'");
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
	my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$CMPartNum' AND SYSCode != 'NULL'");
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
		$SavedProductType = $row[32];
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
          <td width="50%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update Inventory (System)</b></font></td>
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
<br><b>No Matching Records Found</b><ul><li>The Coastline Micro Part Number you specified does not seem to be a <b>System</b>, as you specified.</li><li>Are you sure <b>$CMPartNum</b> isn't actually a stand-alone item in the system and not a system?</li></ul><form><center><input type="button" value="Try Again" onClick="javascript:history.go('-1')" class="inputbut"></center><br>
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
	my $sth = $dbh->prepare("SELECT * FROM Systems WHERE Parent='$CMPartNum'");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$SavedSystemID = $row[0]; $SavedParent = $row[1]; $SavedCMSeries = $row[2]; $SavedReconfig = $row[3];
		$SavedMainCategory = $row[4]; $SavedMainType = $row[5]; $SavedMainCharacter = $row[6]; $SavedMainNumbers = $row[7];
		push(@Parts,"$row[8],,,,,$row[9],,,,,$row[10],,,,,$row[11]"); $SavedSub1Numbers = $row[11]; $Numero=1;
		if (($SavedSub1Numbers eq "") || ($SavedSub1Numbers eq " ") || ($SavedSub1Numbers eq "Null") || ($SavedSub1Numbers eq "NULL")) { } else { push(@Parts,"$row[12],,,,,$row[13],,,,,$row[14],,,,,$row[15]"); $SavedSub2Numbers = $row[15]; $Numero=2; }
		if (($SavedSub2Numbers eq "") || ($SavedSub2Numbers eq " ") || ($SavedSub2Numbers eq "Null") || ($SavedSub2Numbers eq "NULL")) { } else { push(@Parts,"$row[16],,,,,$row[17],,,,,$row[18],,,,,$row[19]"); $SavedSub3Numbers = $row[19]; $Numero=3; }
		if (($SavedSub3Numbers eq "") || ($SavedSub3Numbers eq " ") || ($SavedSub3Numbers eq "Null") || ($SavedSub3Numbers eq "NULL")) { } else { push(@Parts,"$row[20],,,,,$row[21],,,,,$row[22],,,,,$row[23]"); $SavedSub4Numbers = $row[23]; $Numero=4; }
		if (($SavedSub4Numbers eq "") || ($SavedSub4Numbers eq " ") || ($SavedSub4Numbers eq "Null") || ($SavedSub4Numbers eq "NULL")) { } else { push(@Parts,"$row[24],,,,,$row[25],,,,,$row[26],,,,,$row[27]"); $SavedSub5Numbers = $row[27]; $Numero=5; }
		if (($SavedSub5Numbers eq "") || ($SavedSub5Numbers eq " ") || ($SavedSub5Numbers eq "Null") || ($SavedSub5Numbers eq "NULL")) { } else { push(@Parts,"$row[28],,,,,$row[29],,,,,$row[30],,,,,$row[31]"); $SavedSub6Numbers = $row[31]; $Numero=6; }
		if (($SavedSub6Numbers eq "") || ($SavedSub6Numbers eq " ") || ($SavedSub6Numbers eq "Null") || ($SavedSub6Numbers eq "NULL")) { } else { push(@Parts,"$row[32],,,,,$row[33],,,,,$row[34],,,,,$row[35]"); $SavedSub7Numbers = $row[35]; $Numero=7; }
		if (($SavedSub7Numbers eq "") || ($SavedSub7Numbers eq " ") || ($SavedSub7Numbers eq "Null") || ($SavedSub7Numbers eq "NULL")) { } else { push(@Parts,"$row[36],,,,,$row[37],,,,,$row[38],,,,,$row[39]"); $SavedSub8Numbers = $row[39]; $Numero=8; }
		if (($SavedSub8Numbers eq "") || ($SavedSub8Numbers eq " ") || ($SavedSub8Numbers eq "Null") || ($SavedSub8Numbers eq "NULL")) { } else { push(@Parts,"$row[40],,,,,$row[41],,,,,$row[42],,,,,$row[43]"); $SavedSub9Numbers = $row[43]; $Numero=9; }
		if (($SavedSub9Numbers eq "") || ($SavedSub9Numbers eq " ") || ($SavedSub9Numbers eq "Null") || ($SavedSub9Numbers eq "NULL")) { } else { push(@Parts,"$row[44],,,,,$row[45],,,,,$row[46],,,,,$row[47]"); $SavedSub10Numbers = $row[47]; $Numero=10; }
		if (($SavedSub10Numbers eq "") || ($SavedSub10Numbers eq " ") || ($SavedSub10Numbers eq "Null") || ($SavedSub10Numbers eq "NULL")) { } else { push(@Parts,"$row[48],,,,,$row[49],,,,,$row[50],,,,,$row[51]"); $SavedSub11Numbers = $row[51]; $Numero=11; }
		if (($SavedSub11Numbers eq "") || ($SavedSub11Numbers eq " ") || ($SavedSub11Numbers eq "Null") || ($SavedSub11Numbers eq "NULL")) { } else { push(@Parts,"$row[52],,,,,$row[53],,,,,$row[54],,,,,$row[55]"); $SavedSub12Numbers = $row[55]; $Numero=12; }
		if (($SavedSub12Numbers eq "") || ($SavedSub12Numbers eq " ") || ($SavedSub12Numbers eq "Null") || ($SavedSub12Numbers eq "NULL")) { } else { push(@Parts,"$row[56],,,,,$row[57],,,,,$row[58],,,,,$row[59]"); $SavedSub13Numbers = $row[59]; $Numero=13; }
		if (($SavedSub13Numbers eq "") || ($SavedSub13Numbers eq " ") || ($SavedSub13Numbers eq "Null") || ($SavedSub13Numbers eq "NULL")) { } else { push(@Parts,"$row[60],,,,,$row[61],,,,,$row[62],,,,,$row[63]"); $SavedSub14Numbers = $row[63]; $Numero=14; }
		if (($SavedSub14Numbers eq "") || ($SavedSub14Numbers eq " ") || ($SavedSub14Numbers eq "Null") || ($SavedSub14Numbers eq "NULL")) { } else { push(@Parts,"$row[64],,,,,$row[65],,,,,$row[66],,,,,$row[67]"); $SavedSub15Numbers = $row[67]; $Numero=15; }
		if (($SavedSub15Numbers eq "") || ($SavedSub15Numbers eq " ") || ($SavedSub15Numbers eq "Null") || ($SavedSub15Numbers eq "NULL")) { } else { push(@Parts,"$row[68],,,,,$row[69],,,,,$row[70],,,,,$row[71]"); $SavedSub16Numbers = $row[71]; $Numero=16; }
		if (($SavedSub16Numbers eq "") || ($SavedSub16Numbers eq " ") || ($SavedSub16Numbers eq "Null") || ($SavedSub16Numbers eq "NULL")) { } else { push(@Parts,"$row[72],,,,,$row[73],,,,,$row[74],,,,,$row[75]"); $SavedSub17Numbers = $row[75]; $Numero=17; }
		if (($SavedSub17Numbers eq "") || ($SavedSub17Numbers eq " ") || ($SavedSub17Numbers eq "Null") || ($SavedSub17Numbers eq "NULL")) { } else { push(@Parts,"$row[76],,,,,$row[77],,,,,$row[78],,,,,$row[79]"); $SavedSub18Numbers = $row[79]; $Numero=18; }
		if (($SavedSub18Numbers eq "") || ($SavedSub18Numbers eq " ") || ($SavedSub18Numbers eq "Null") || ($SavedSub18Numbers eq "NULL")) { } else { push(@Parts,"$row[80],,,,,$row[81],,,,,$row[82],,,,,$row[83]"); $SavedSub19Numbers = $row[83]; $Numero=19; }
		if (($SavedSub19Numbers eq "") || ($SavedSub19Numbers eq " ") || ($SavedSub19Numbers eq "Null") || ($SavedSub19Numbers eq "NULL")) { } else { push(@Parts,"$row[84],,,,,$row[85],,,,,$row[86],,,,,$row[87]"); $SavedSub20Numbers = $row[87]; $Numero=20; }
		if (($SavedSub20Numbers eq "") || ($SavedSub20Numbers eq " ") || ($SavedSub20Numbers eq "Null") || ($SavedSub20Numbers eq "NULL")) { } else { push(@Parts,"$row[88],,,,,$row[89],,,,,$row[90],,,,,$row[91]"); $SavedSub21Numbers = $row[91]; $Numero=21; }
		if (($SavedSub21Numbers eq "") || ($SavedSub21Numbers eq " ") || ($SavedSub21Numbers eq "Null") || ($SavedSub21Numbers eq "NULL")) { } else { push(@Parts,"$row[92],,,,,$row[93],,,,,$row[94],,,,,$row[95]"); $SavedSub22Numbers = $row[95]; $Numero=22; }
		if (($SavedSub22Numbers eq "") || ($SavedSub22Numbers eq " ") || ($SavedSub22Numbers eq "Null") || ($SavedSub22Numbers eq "NULL")) { } else { push(@Parts,"$row[96],,,,,$row[97],,,,,$row[98],,,,,$row[99]"); $SavedSub23Numbers = $row[99]; $Numero=23; }
		if (($SavedSub23Numbers eq "") || ($SavedSub23Numbers eq " ") || ($SavedSub23Numbers eq "Null") || ($SavedSub23Numbers eq "NULL")) { } else { push(@Parts,"$row[100],,,,,$row[101],,,,,$row[102],,,,,$row[103]"); $SavedSub24Numbers = $row[103]; $Numero=24; }
		if (($SavedSub24Numbers eq "") || ($SavedSub24Numbers eq " ") || ($SavedSub24Numbers eq "Null") || ($SavedSub24Numbers eq "NULL")) { } else { push(@Parts,"$row[104],,,,,$row[105],,,,,$row[106],,,,,$row[107]"); $SavedSub25Numbers = $row[107]; $Numero=25; }
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

##----------->>> IF ADDING A COMPONENT MAKE ADD ONE TO NUMERO THE TABLE MAKER
if ($FORM{'AddComponent'} eq "1") { $Numero++; }

##----------->>> START DYNAMO WINDOW STUFF
	$browser = "$ENV{'HTTP_USER_AGENT'}";
	## DYNAMIC BROWSER PLACEMENTS
	if ($browser =~ "MSIE" || $browser =~ "Netscape6" || $browser =~ "netscape6" || $browser =~ "netscape5" || $browser =~ "Netscape5") { $zindex = ""; }
	else { $zindex = "z-index:5"; }

##----------->>> PLACE WINDOW USING HOW MANY COMPONENTS THERE ARE
$StartTop = 925;
$NumCalc=$Numero*309;
$FromTop = $StartTop + $NumCalc; 
$divcont = "#divCont{position:absolute; overflow:hidden; left:25%; top:$FromTop; clip:rect(0,300,450,0); height:450; width:300;}";
$divload = "#divLoad{position:absolute; left:25%; top:$FromTop; clip:rect(0,300,450,0); height:450; width:300; visibility:hidden;}";	
$divArrows = "#divArrows{position:absolute; left:0; top:1155; z-index:25; visibility:hidden}";
$divBground = "#bground{position:absolute; left:0; top:0; clip:rect(0,1,1,0); height:1; width:1;$zindex}";
##----------->>> END DYNAMO WINDOW STUFF

## ------------>> IS PRODUCT SEARCHABLE?
if ($SavedSearchable eq "No") { $Syes = ""; $Sno = "selected"; }
else { $Syes = "selected"; $Sno = ""; }

{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - Shark Tank Admin System - Inventory ( Systems )</title>
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
var TheAccess  = document.change.TheAccess;
var sizer = TheAccess.options.length;
for(var i = (sizer-1); i >= 0; i--) {
if ((TheAccess.options[i] != null) && (TheAccess.options[i].selected == true)) {
TheAccess.options[i] = null;
      }
   }
}

function makeSystemItem(cual,cual2) {
acual = document.change[cual]; 
acual2 = document.change[cual2];
var sizer = acual2.length;
for(var i = 0; i < acual.length; i++) {
	thisone = acual.options[i].value;
	if ((acual.options[i] != null) && (acual.options[i].selected) && (thisone != "Desktop") && (thisone != "Server") && (thisone != "Notebook") && (thisone != "Kit") && (thisone != "Monitor") && (thisone != "Memory") && (thisone != "HardDrive") && (thisone != "VideoCard") && (thisone != "Peripheral") && (thisone != "Printer") && (thisone != "Software")) {
	var there = false;
	for(var count = 0; count < sizer; count++) {
		if (acual2.options[count] != null) {
			if (acual2.options[count].value.indexOf(acual.options[i].value) != -1) {
				there = true;
					if (acual2.options[count].value.indexOf('-----') == -1) { 
						acual2.options[count].text = '(2) '+acual.options[i].text; 
						acual2.options[count].value = acual.options[i].value+'-----'+2+'';
						count++;
					}
					else { 
						OldCount=0;
						Este2 = acual2.options[count].value;
						var MyCount = Este2.split(/-----/);
						MyCounter = MyCount[1];
						MyCounter++;
						acual2.options[count].text = '('+MyCounter+') '+acual.options[i].text; 
						acual2.options[count].value = acual.options[i].value+'-----'+MyCounter+'';
						count++;
					}
      			}
   			}
		}
		if (there != true) {
			var thisone = acual.options[i].value;
			if (thisone != "$SavedCMPartNum") {
				acual2.options[sizer] = new Option(acual.options[i].text); 
				acual2.options[sizer].value = acual.options[i].value;
				sizer++;
			}
         }
      }
   }
}

function makeSystemItem2(cual,DaText,DaValue) {
acual = document.change[cual];
var sizer = acual.length;
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
			sizer++;
		}
    }
}

function killSystemItem(cual) {
var cual  = document.change[cual];
var sizer = cual.options.length;
for(var i = (sizer-1); i >= 0; i--) {
if ((cual.options[i] != null) && (cual.options[i].selected == true)) {
cual.options[i] = null;
      }
   }
}

function editSystemItem(cual) {
	var CMPartNum = document.change[cual].value;
	var esteURL = 'change_product_common.cgi?CMPartNum='+CMPartNum+'';
	if (CMPartNum != "" && CMPartNum != "null") {
		location.href = esteURL;
	}
}

function getProducts(mua, mue) {
var missingdrop = "";
var formindex = document.change[mua].selectedIndex;
var thisone = document.change[mua].options[formindex].value;
var thisone2 = document.change[mua].options[formindex].text;
var me = mue;

if (thisone == "BIGNULL") {
	thefirst = mue;
    missingdrop += "\\nThat is not a valid option, please select another...";
}

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    alert(missingdrop);
 	document.change(thefirst).focus();
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
	else {
	if (thisone.indexOf('-----') == -1) { no=1; Quantity = ""; }
	else {
		var MyOne = thisone.split(/-----/);
		thisone = MyOne[0];
	}
    alertmessage = "___________________________________________                   \\n\\n                             Inventory Reader\\n___________________________________________\\n\\nCoastline Micro Part Number\\n     "+thisone+"\\n\\nProduct Name\\n     "+thisone2+"\\n___________________________________________                   \\n\\n                    Click 'OK' to close this window...\\n___________________________________________";
	alert(alertmessage);
	}
}
}

function getTypes(me) {
var b = navigator.appName;
TheType = document.forms.change[me];
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


function clearUs(cual) {
// CLEARS ALL DATA DYNAMIC
ThisOne = document.change[cual];
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
if ($Numero == 25) { alert('Sorry, the system only allows a maximum of 25 components per System. If you would like to have more components with this System we suggest you use configure other Kits to use as components of this System. Using such a method would allow you to virtually add an unlimited quantity of components to any given System.'); }
else { location.href = "$script?CMPartNum=$CMPartNum&AddComponent=1"; }
}

function priceMe(me, me2, me3) {
var Charindex = document.change[me3].selectedIndex;
var Char = document.change[me3].options[Charindex].value;

var strValues = "";
var boxLength = document.change[me].length;
var count = 0;
if (boxLength != 0) {
	for (i = 0; i < boxLength; i++) {
		var LeValue = document.change[me].options[i].value;
		var LeText = document.change[me].options[i].text;
		if (LeValue.indexOf('-----') == -1) { 
			MyNumber=LeValue;
			if (count == 0) { strValues = MyNumber + "-----" + LeText; }
			else { strValues = strValues + "," + MyNumber + "-----" + LeText; }
		}
		else {
			OldCount=0;
			var MyCount = LeValue.split(/-----/);
			MyCounter=0;
			MyCounter = MyCount[1];
			MyNumber = MyCount[0];
			for(var cuenta = 0; cuenta < MyCounter; cuenta++) {
				if (strValues == "") { strValues = MyNumber + "-----" + LeText; }
				else { strValues = strValues + "," + MyNumber + "-----" + LeText; }
			}
		}
	count++;
   }
}
else { vete=1; }
if (strValues.length == 0) { vete=1; }
else {
	var b = navigator.appName;
	if (b=="Netscape") { mainFrame = parent.frames.botOne; mainFrame.frame.loadpage('calc_components.cgi?FeedMe='+me2+'&LosNumbers='+strValues+'&Character='+Char+'');	}
	else { parent.botOne.frame.loadpage('calc_components.cgi?FeedMe='+me2+'&LosNumbers='+strValues+'&Character='+Char+''); }
	}
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
if (document.change.Keywords.value == "" || document.change.Keywords.value == " ") {
    missingdrop += "\\n     - Indexing Keywords";
	thefirst = "Keywords";
}

if (document.change.MainCategory.value == "" || document.change.MainCategory.value == " ") {
    missingdrop += "\\n     - Main Category Title/Name";
	if (thefirst == "") { thefirst = "MainCategory"; }
}

// Check Main Product Numbers
var strValues = ""; var boxLength = document.change.MainNumbers.length; var count = 0;
if (boxLength != 0) {
	for (i = 0; i < boxLength; i++) {
		var LeValue = document.change.MainNumbers.options[i].value;
		if (LeValue.indexOf('-----') == -1) { 
			MyNumber=LeValue;
			if (count == 0) { strValues = MyNumber; }
			else { strValues = strValues + "," + MyNumber; }
		}
		else {
			OldCount=0; var MyCount = LeValue.split(/-----/); MyCounter=0; MyCounter = MyCount[1]; MyNumber = MyCount[0];
			for(var cuenta = 0; cuenta < MyCounter; cuenta++) {
				if (strValues == "") { strValues = MyNumber; }
				else { strValues = strValues + "," + MyNumber; }
			}
		}
	count++;
   }
}
else {
    missingdrop += "\\n     - Main Category - Selected Items\\n        *Select at least one product as a base for your system";
	if (thefirst == "") { thefirst = "MainNumbers"; }
}
if (strValues.length == 0) { }
else { document.change.MainNumeros.value = strValues; }

EOF
}

## Make as many as are in system
$Counter = 0;
foreach (1 .. $Numero) {
$Counter++;
	print "// Check Sub $Counter\Components\n";
	print "var strValues = \"\"; var boxLength = document.change.Sub$Counter\Numbers.length; var count = 0;\n";
	print "if (boxLength != 0) {\n";
	print "	for (i = 0; i < boxLength; i++) {\n";
	print "		var LeValue = document.change.Sub$Counter\Numbers.options[i].value;\n";
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
	print "else { document.change.Sub$Counter\Numeros.value = strValues; }\n";
}

{
print <<EOF

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
	document.change(thefirst).focus();
    return false;
} 
else {
return true;
}

// If anything comes back wrong alert and detain form, else submit info
if (missingdrop != "") {
    missingdrop ="___________________________________________                   \\n\\n" + "  Sorry, I cannot process your request because the\\n  following fields are either blank or filled incorrectly:\\n" + "___________________________________________                   \\n\\n" +
    missingdrop + "\\n\\n___________________________________________                   " + "\\n\\n   To continue, check fields and submit form again!" + "\\n___________________________________________";
    alert(missingdrop);
	document.change(thefirst).focus();
    return false;
} 
else {
return true;
}
}
</SCRIPT>
<BODY TEXT="#333366" LINK="#8F8FAB" VLINK="#8F8FAB" ALINK="#8F8FAB" BGCOLOR="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="javascript:ifrinit();clearUs('Warranty');clearUs('TheAccess');clearUs('AllProducts');clearUs('ProdTypes');clearUs('MainSelect');clearUs('MainNumbers');getTypes('MainSelect');getTypes('ProdTypes');feedAccessories();feedMainParts();">
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
            <td width="95%"> <font face="verdana,arial,helvetica" size="2" color="#333366"><b>View/Update 
              Product ($SavedPricingClass - $CMPartNum)</b></font></td>
            <td align="right" width="5%">&nbsp;</td>
          </tr>
          <tr> 
            <td colspan="2"> 
              <table width="100%" border="1" cellspacing="0" cellpadding="0" class="tableBORDER">
                <tr bordercolor="#333366"> 
                  <td width="100%" align="center" valign="top" height="250"> 
                    <table width="100%" border="0" cellspacing="0" cellpadding="5">
                      <tr> 
                        <td width="100%" align="center" height="27" bgcolor="#F2F2F7" class="tableBG" colspan="2"><font face="verdana,arial,helvetica" size="2" color="#333366"><b>System Configuration and Information</b></font></td>
                      </tr>
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
                <td height="20" bgcolor="#8F8FAB" width="96%" colspan="2"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">$SavedPricingClass 
                  Information</font></b></font></td>
                <td width="2%" height="15" bgcolor="#8F8FAB">&nbsp;</td>
              </tr>
              <tr> 
                <td colspan="4" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
              </tr>
              <tr> 
                <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                <td height="20" align="center" width="48%" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Product 
                  Name </b></font></td>
                <td height="20" align="center" width="48%" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Indexing 
                  Keywords</b></font></td>
                <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
              </tr>
              <tr> 
                <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                <td height="25" align="center" width="48%" valign="middle"> 
                  <input type="text" name="ItemName" size="35" class="inputtext35" value="$SavedItemName">
                  <br>
                  <input type="hidden" name="CMPartNum" value="$CMPartNum">
                  <input type="hidden" name="PricingClass" value="$SavedPricingClass">
                  <input type="hidden" name="Numero" value="$Numero">
                </td>
                <td height="25" align="center" width="48%" valign="middle"> 
                  <input type="text" size="35" class="inputtext35" name="Keywords" value="$SavedKeywords">
                  <input type="hidden" name="Description" value="NONE">
                  <input type="hidden" name="TechSpecs" value="NONE">
                </td>
                <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
              </tr>
              <tr> 
                <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                <td height="30" align="center" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"></font><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Warranty</b></font></td>
                <td height="30" align="center" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Searchable?</b></font></td>
                <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
              </tr>
              <tr> 
                <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                <td height="75" align="center"> 
                  <textarea name="Warranty" cols="50" class="textarea2" rows="2">$SavedWarranty</textarea>
                </td>
                <td height="75" align="center">
                  <select name="Searchable" class="inputtext">
                    <option value="Yes" $Syes>Yes</option>
                    <option value="No" $Sno>No</option>
                  </select>
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

EOF
}

## ----------------->>> PREPARE MAIN COMPONENT STUFF
if ($SavedMainType eq "HIDE") { $Hide = "selected"; $Show = ""; }
else { $Hide = ""; $Show = "selected"; }

if ($SavedMainCharacter eq "All") { $All = "selected"; $Multiple = ""; $Single = ""; }
elsif ($SavedMainCharacter eq "Multiple") { $All = ""; $Multiple = "selected"; $Single = ""; }
else { $All = ""; $Multiple = ""; $Single = "selected"; }

	@MainParts = split(/,/, $SavedMainNumbers);
	foreach $MainPart (@MainParts) {
		my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$MainPart' ORDER BY ItemName ASC");
		$sth->execute or die "Unable to execute query\n"; 
		my @row;
		while(@row = $sth->fetchrow_array) { 
			$EsteNombre = $row[11];
			$Cuesta = $row[21];
			push(@Partes,"$EsteNombre,,,,,$MainPart");
			push(@Totales,"$Cuesta,,,,,$Counter,,,,,$SavedMainCharacter,,,,,$EsteNombre");
		}
		$sth->finish;
	}

##------------------->>> Calculate total for all MAIN components
$MainTotal=0;
$TCount=0;
if ($SavedMainCharacter eq "All") {
	foreach $Totalo (@Totales) {
		@MainPrice = split(/,,,,,/, $Totalo);
		$MainTotal = $MainPrice[0] + $MainTotal;
	}
}

else {
	foreach $Totalo (@Totales) {
		@MainPrice = split(/,,,,,/, $Totalo);
		if ($TCount eq "0") {
			$TCount++;
			$DaFoistObj = "$MainPrice[3]";
			$MainTotal = $MainPrice[0] + $MainTotal;
		}
		elsif ($MainPrice[3] eq $DaFoistObj) {
			$TCount++;
			$MainTotal = $MainPrice[0] + $MainTotal;			
		}
	}
}

$MainTotal = sprintf("%.2f", $MainTotal);
push(@LeTotalistico, $MainTotal);

{
print <<EOF
						  
<table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr> 
                              <td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td>
                            </tr>
                            <tr> 
                              <td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td>
                              <td width="100%" valign="top"> 
                                <table border="0" cellspacing="0" cellpadding="0" width="100%">
                                  <tr> 
                                    <td colspan="7" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <!--UNO-->
                                  <tr> 
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="20" align="center" width="96%" valign="middle" colspan="5"> 
                                      <table border="0" cellspacing="0" cellpadding="0" width="100%">
                                        <tr align="left" bgcolor="#F2F2F7"> 
                                          <td height="20" width="100%" valign="middle" colspan="2" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font size="2">Main/Default 
                                            Component(s)</font></b></font></td>
                                        </tr>
                                        <tr> 
                                          <td align="center" valign="bottom" colspan="2"> 
                                            <table border="0" cellspacing="0" cellpadding="0" width="100%">
                                              <tr bgcolor="#F2F2F7"> 
                                                <td height="0" align="center" width="50%" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Category 
                                                  Title/Name</b></font></td>
                                                <td height="20" align="center" width="20%" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Hide 
                                                  Price?</b></font></td>
                                                <td height="20" align="center" width="30%" valign="middle" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Characteristics</b></font></td>
                                              </tr>
                                              <tr> 
                                                <td height="25" align="center" width="50%" valign="middle"> 
                                                  <input type="text" size="15" class="inputtext15" name="MainCategory" value="$SavedMainCategory">
                                                </td>
                                                <td height="25" align="center" valign="middle" width="20%"><font face="verdana,arial,helvetica" size="1" color="#333366"> 
                                                  <select name="MainType" class="inputtext">
                                                    <option value="HIDE" $Hide>Yes</option>
                                                    <option value="SHOW" $Show>No</option>
                                                  </select>
                                                  </font></td>
                                                <td height="25" align="center" valign="middle" width="30%"><font face="verdana,arial,helvetica" size="1" color="#333366"> 
                                                  <select name="MainCharacter" class="inputtext">
                                                    <option value="Single" $Single>Single</option>
                                                    <option value="Multiple" $Multiple>Multiple</option>
                                                    <option value="All" $All>All</option>
                                                  </select>
                                                  </font></td>
                                              </tr>
                                            </table>
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="0%" align="left" valign="middle"> 
                                            <table border="0" cellspacing="0" cellpadding="0" width="100%">
                                              <tr> 
                                                <td height="20" align="center" width="50%" valign="middle" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Inventory 
                                                  Reader </b></font></td>
                                                <td height="20" align="center" width="50%" valign="middle" colspan="2" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Selected 
                                                  Items</b></font></td>
                                              </tr>
                                              <tr valign="middle"> 
                                                <td height="120" align="center" width="50%"> 
                                                  <font face="verdana,arial,helvetica" size="1" color="#333366">Product 
                                                  Name<br>
                                                  </font> 
                                                  <select name="MainSelect" multiple class="prodguinea2" size="4" onDblClick="javascript:getProducts('MainSelect','MainSelect');">
                                                    <option value="BIGNULL">0000000000000000</option>
                                                  </select>
                                                </td>
                                                <td height="120" align="center" width="50%" colspan="2"><font face="verdana,arial,helvetica" size="1" color="#333366">(Count 
                                                  if 2+) Product Name<br>
                                                  </font> 
                                                  <select size="4" multiple class="prodguinea2Grey" name="MainNumbers" value="$MainParts" onDblClick="javascript:getProducts('MainNumbers','MainNumbers');">
                                                    <option value="BIGNULL">0000000000000000</option>
                                                  </select>
                                                  <input type="hidden" name="MainNumeros" value="">
                                                </td>
                                              </tr>
                                              <tr valign="middle"> 
                                                <td height="20" align="center" width="50%"> 
                                                  <table border="1" cellspacing="0" cellpadding="3" bordercolor="#FFFFFF" onMouseOver="runto('ebebeb')" onMouseOut="runback('F2F2F7')" align="center" width="90%" bgcolor="#F2F2F7">
                                                    <tr align="center"> 
                                                      <td width="50%" height="20"><font face="verdana,arial,helvetica" size="1"><a href="javascript:getTypes('MainSelect');"><b>Product 
                                                        Types</b></a></font></td>
                                                      <td width="50%" height="20"><font face="verdana,arial,helvetica" size="1"><a href="javascript:makeSystemItem('MainSelect','MainNumbers')"><b>Use 
                                                        Selected</b></a></font></td>
                                                    </tr>
                                                  </table>
                                                </td>
                                                <td height="20" align="center" width="50%" colspan="2"> 
                                                  <table border="1" cellspacing="0" cellpadding="3" bordercolor="#FFFFFF" onMouseOver="runto('F2F2F7')" onMouseOut="runback('EBEBEB')" align="center" width="90%" bgcolor="#EBEBEB">
                                                    <tr align="center"> 
                                                      <td width="50%" height="20"><font face="verdana,arial,helvetica" size="1"><a href="javascript:editSystemItem('MainNumbers');"><b>Edit/Update Selected</b></a></font></td>
                                                      <td width="50%" height="20"><font face="verdana,arial,helvetica" size="1"><a href="javascript:killSystemItem('MainNumbers')"><b>Remove 
                                                        Selected</b></a></font></td>
                                                    </tr>
                                                  </table>
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                        </tr>
                                      </table>
                                    </td>
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <!--DOS-->
                                  <tr> 
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td align="center" width="96%" valign="bottom" colspan="5"> 
                                      <table border="1" cellspacing="0" cellpadding="3" bordercolor="#F2F2F7" align="center" width="100%">
                                        <tr align="center"> 
                                          <td height="37" width="100%"> 
                                            <table border="1" cellspacing="0" cellpadding="3" bordercolor="#FFFFFF" onMouseOver="runto('EB0000')" onMouseOut="runback('F2F2F7')" align="center" width="500" bgcolor="#F2F2F7">
                                              <tr align="center"> 
                                                <td width="50%" height="30"> 
                                                  <input type="text" name="MainCost" value="Section Total = \$$MainTotal" size="15" class="prices">
                                                </td>
                                                <td width="50%" height="30"><font face="verdana,arial,helvetica" size="1"> 
                                                  <input type="button" value="< < < Re-Calculate Total" class="pricebut" onClick="javascript:priceMe('MainNumbers','MainCost','MainCharacter');">
                                                  </font></td>
                                              </tr>
                                            </table>
                                          </td>
                                        </tr>
                                      </table>
                                    </td>
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="2%" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="96%" valign="top" bgcolor="#F2F2F7" colspan="5"><img src="images/verticalbar.gif" width="15" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
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

EOF
}

$Counter = 0;
foreach (1 .. $Numero) {
$Counter++;

if (($Numero eq $Counter) && ($FORM{'AddComponent'} eq "1")) {
	$Name = "";
	$Number = "";
	$LaCuenta = "1";
	$Type = "";
	$IsShown = "checked";
	$Cost = "";
}
else {
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
			push(@SubPartes,"$MiEsteNombre,,,,,$SubPart,,,,,$Counter");
			push(@SubTotales,"$MiCuesta,,,,,$Counter,,,,,$Character,,,,,$MiEsteNombre");
		}
		$sth->finish;
	}
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

{
print <<EOF

<table width="95%" border="0" cellspacing="0" cellpadding="0" align="center"><tr><td width="348" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td></tr>
<tr><td bgcolor="#8F8FAB" width="1" height="80"><img src="images/verticalbar.gif" width="1" height="25"></td><td width="100%" valign="top">
                                <table border="0" cellspacing="0" cellpadding="0" width="100%">
                                  <tr>
                                    <td colspan="7" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <tr>
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td align="center" width="96%" valign="middle" colspan="5"> 
                                      <table border="0" cellspacing="0" cellpadding="0" width="100%">
                                        <tr align="left" bgcolor="#F2F2F7">
                                          <td height="20" width="100%" valign="middle" colspan="2" align="center"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font size="2">Sub-Component $Counter</font></b></font></td>
                                        </tr>
                                        <tr>
                                          <td align="center" valign="bottom" colspan="2">
                                            <table border="0" cellspacing="0" cellpadding="0" width="100%">
                                              <tr bgcolor="#F2F2F7">
                                                <td height="20" align="center" width="50%" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Category Title/Name</b></font></td>
                                                <td height="20" align="center" width="20%" valign="middle"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Hide Component?</b></font></td>
                                                <td height="20" align="center" width="30%" valign="middle" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Characteristics</b></font></td>
                                              </tr>
                                              <tr>
                                                <td height="25" align="center" width="50%" valign="middle"> 
                                                  <input type="text" size="15" class="inputtext15" name="Sub$Counter\Category" value="$Category">
                                                </td>
                                                <td height="25" align="center" valign="middle" width="20%"><font face="verdana,arial,helvetica" size="1" color="#333366"> 
                                                  <select name="Sub$Counter\Type" class="inputtext">
                                                    <option value="HIDE" $IsHidden>Yes</option>
                                                    <option value="SHOW" $IsShown>No</option>
                                                  </select>
                                                  </font></td>
                                                <td height="25" align="center" valign="middle" width="30%"><font face="verdana,arial,helvetica" size="1" color="#333366"> 
                                                  <select name="Sub$Counter\Character" class="inputtext">
                                                    <option value="Single" $IsSingle>Single</option>
                                                    <option value="Multiple" $IsMultiple>Multiple</option>
                                                    <option value="All" $IsAll>All</option>
                                                  </select>
                                                  </font></td>
                                              </tr>
                                            </table>
                                          </td>
                                        </tr>
                                        <tr>
                                          <td width="0%" align="left" valign="middle"> 
                                            <table border="0" cellspacing="0" cellpadding="0" width="100%">
                                              <tr>
                                                <td height="20" align="center" width="50%" valign="middle" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Inventory Reader </b></font></td>
                                                <td height="20" align="center" width="50%" valign="middle" colspan="2" bgcolor="#F2F2F7"><font face="verdana,arial,helvetica" size="1" color="#333366"><b>Selected Items</b></font></td>
                                              </tr>
                                              <tr valign="middle">
                                                <td height="0" align="center" width="50%"><font face="verdana,arial,helvetica" size="1" color="#333366">Product Name</font><br>
                                                  <select name="Sub$Counter\Select" multiple class="prodguinea2" size="4" onDblClick="javascript:getProducts('Sub$Counter\Select','Sub$Counter\Select');">
                                                    <option value="BIGNULL">0000000000000000</option>
                                                  </select>
                                                </td>
                                                <td height="120" align="center" width="50%" colspan="2"><font face="verdana,arial,helvetica" size="1" color="#333366">(Count if 2+) Product Name</font><br>
                                                  <select size="4" class="prodguinea2Grey" multiple name="Sub$Counter\Numbers" onDblClick="javascript:getProducts('Sub$Counter\Numbers','Sub$Counter\Numbers');">
                                                    <option value="BIGNULL">0000000000000000</option>
                                                  </select>
                                                  <input type="hidden" name="Sub$Counter\Numeros" value="">
                                                </td>
                                              </tr>
                                              <tr valign="middle">
                                                <td height="0" align="center" width="50%"> 
                                                  <table border="1" cellspacing="0" cellpadding="3" bordercolor="#FFFFFF" onMouseOver="runto('ebebeb')" onMouseOut="runback('F2F2F7')" align="center" width="90%" bgcolor="#F2F2F7">
                                                    <tr align="center">
                                                      <td width="50%" height="0"><font face="verdana,arial,helvetica" size="1"><a href="javascript:getTypes('Sub$Counter\Select');"><b>Product Types</b></a></font></td>
                                                      <td width="50%" height="0"><font face="verdana,arial,helvetica" size="1"><a href="javascript:makeSystemItem('Sub$Counter\Select','Sub$Counter\Numbers')"><b>Use Selected</b></a></font></td>
                                                    </tr>
                                                  </table>
                                                </td>
                                                <td height="0" align="center" width="50%" colspan="2"> 
                                                  <table border="1" cellspacing="0" cellpadding="3" bordercolor="#FFFFFF" onMouseOver="runto('F2F2F7')" onMouseOut="runback('EBEBEB')" align="center" width="90%" bgcolor="#EBEBEB">
                                                    <tr align="center">
                                                      <td width="50%" height="0"><font face="verdana,arial,helvetica" size="1"><a href="javascript:editSystemItem('Sub$Counter\Numbers');"><b>Edit/Update Selected</b></a></font></td>
                                                      <td width="50%" height="0"><font face="verdana,arial,helvetica" size="1"><a href="javascript:killSystemItem('Sub$Counter\Numbers')"><b>Remove Selected</b></a></font></td>
                                                    </tr>
                                                  </table>
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                        </tr>
                                      </table>
                                      <font face="verdana,arial,helvetica" size="1" color="#333366"></font></td>
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr>
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="0" align="center" width="96%" valign="bottom" colspan="5">
                                      <table border="1" cellspacing="0" cellpadding="3" bordercolor="#F2F2F7" align="center" width="100%">
                                        <tr align="center">
                                          <td height="32" width="100%"> 
                                            <table border="1" cellspacing="0" cellpadding="3" bordercolor="#FFFFFF" onMouseOver="runto('EB0000')" onMouseOut="runback('F2F2F7')" align="center" width="500" bgcolor="#F2F2F7">
                                              <tr align="center">
                                                <td width="50%" height="30"><input type="text" name="Sub$Counter\Cost" value="Section Total = \$$ComponentTotal" size="15" class="prices"></td>
                                                <td width="50%" height="30"><font face="verdana,arial,helvetica" size="1"><input type="button" value="< < < Re-Calculate Total" class="pricebut" onClick="javascript:priceMe('Sub$Counter\Numbers','Sub$Counter\Cost','Sub$Counter\Character');"></font></td>
                                              </tr>
                                            </table>
                                          </td>
                                        </tr>
                                      </table>
                                    </td>
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr>
                                    <td width="2%" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="96%" valign="top" bgcolor="#F2F2F7" colspan="5"><img src="images/verticalbar.gif" width="15" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td width="2%" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                </table>
                              </td><td bgcolor="#8F8FAB" width="1" height="70"><img src="images/verticalbar.gif" width="1" height="25"></td></tr>
<tr><td width="100%" colspan="3" bgcolor="#8F8FAB"><img src="images/spacer.gif" width="25" height="1"></td></tr></table><br>
<script language="Javascript">javascript:clearUs('Sub$Counter\Numbers');javascript:getTypes('Sub$Counter\Select');</script>

EOF
}

}

##------------------>>> CALCULATE TOTAL FOR ALL ITEMS IN SYSTEM
$AllCompTotal=0;
foreach $Totalistico (@LeTotalistico) {
	$AllCompTotal = $AllCompTotal + $Totalistico;
}

$EntireTotal = sprintf("%.2f", $AllCompTotal);

{
print <<EOF
						  
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
                                    <td height="20" bgcolor="#8F8FAB" width="96%" colspan="5"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Total 
                                      System Price and Associated Actions</font></b></font></td>
                                    <td width="2%" height="15" bgcolor="#8F8FAB">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td colspan="7" height="1"><img src="images/verticalbar.gif" width="15" height="1"></td>
                                  </tr>
                                  <!--UNO-->
                                  <tr> 
                                    <td width="2%" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="96%" valign="middle" colspan="5" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"> 
                                    </td>
                                    <td width="2%" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                  </tr>
                                  <!--DOS-->
                                  <tr> 
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                    <td height="0" align="center" width="96%" valign="bottom" colspan="5"> 
                                      <table border="1" cellspacing="0" cellpadding="3" bordercolor="#F2F2F7" align="center" width="100%">
                                        <tr align="center"> 
                                          <td height="55" width="100%"> 
                                            <table border="1" cellspacing="0" cellpadding="3" bordercolor="#FFFFFF" onMouseOver="runto('EB0000')" onMouseOut="runback('F2F2F7')" align="center" width="500" bgcolor="#F2F2F7">
                                              <tr align="center"> 
                                                <td width="50%" height="35"> 
                                                  <input type="text" name="AllCost" value="Config's Total Price = \$$EntireTotal" size="15" class="prices">
                                                </td>
                                                <td width="50%" height="35"><font face="verdana,arial,helvetica" size="1"> 
                                                  <input type="submit" value="< < < Re-Calculate Total" class="pricebut">
                                                  </font></td>
                                              </tr>
                                            </table>
                                            <table border="1" cellspacing="0" cellpadding="3" bordercolor="#FFFFFF" onMouseOver="runto('ebebeb')" onMouseOut="runback('F2F2F7')" align="center" width="500" bgcolor="#F2F2F7" height="20">
                                              <tr align="center"> 
                                                <td width="50%" height="0"><font face="verdana,arial,helvetica" size="1">
<script language="Javascript">
function addComponent() {
var agree=confirm("You requested to add another component, to do so this page must REFRESH itself, in turn NOT saving the changes you have made to it in this session. To save changes click \'Cancel\' on this window and save the changes to the system. Otherwise click \'OK\' to continue adding a new component to this system.");
if (agree)
location.href = "change_product_system.cgi?AddComponent=1&CMPartNum=$CMPartNum";
else
nogo=1;
}
</script>
<input type="button" value="Add Another Component" class="inputbut" onClick="javascript:addComponent();">
                                                  </font></td>
                                                <td width="50%" height="35"><font face="verdana,arial,helvetica" size="1">
                                                  <input type="button" value="Preview As Configured" class="inputbut" name="button3" onClick="Javascript:window.open('../stank_sysbrowse.cgi?CMPartNum=$CMPartNum','Preview','width=470,height=590');">
                                                  </font></td>
                                              </tr>
                                            </table>
                                          </td>
                                        </tr>
                                      </table>
                                    </td>
                                    <td width="2%" bgcolor="#F2F2F7">&nbsp;</td>
                                  </tr>
                                  <tr> 
                                    <td width="2%" bgcolor="#F2F2F7"><img src="images/verticalbar.gif" width="15" height="15"></td>
                                    <td height="15" align="center" width="96%" valign="top" bgcolor="#F2F2F7" colspan="5"><img src="images/verticalbar.gif" width="15" height="15"><img src="images/verticalbar.gif" width="15" height="15"></td>
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
                <tr bordercolor="#333366"> 
                  <td width="100%" align="center" valign="top" bordercolor="#333366"> 
                    <table width="100%" border="0" cellspacing="0" cellpadding="5">
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
                                      <input type="button" value="Preview" onClick="Javascript:iPreview('SmallLogo')" class="inputbut" name="button2">
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
                                      <input type="button" value="Preview" onClick="Javascript:iPreview('LargeLogo')" class="inputbut" name="button2">
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
                                    <td height="20" bgcolor="#8F8FAB"><font face="verdana,arial,helvetica" size="1" color="#333366"><b><font color="#FFFFFF">Sneak Peek</font></b></font></td>
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
                                      <input type="text" name="SneakPeak" size="7" class="inputtext7" value="$SavedSneakPeak" onFocus="Javascript:noChange('SneakPeakBut');">
                                      <input type="button" value="Get Mine!" onClick="Javascript:theHungry('SneakPeak','sneak')" class="inputbut" name="SneakPeakBut">
                                      <input type="button" value="Preview" onClick="Javascript:iPreview('SneakPeak')" class="inputbut">
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
                    </table>
                  </td>
                </tr>
                <tr bordercolor="#333366"> 
                  <td width="100%" align="center" valign="top" bordercolor="#333366"> 
                    <table width="100%" border="0" cellspacing="0" cellpadding="5">
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
                                            <select name="AllProducts" size="20" multiple width="20" class="prodselect" onDblClick="javascript:getProducts('AllProducts','AllProducts');">
                                              <option value="BIGNULL">00000000000000000000000000000000</option>
                                            </select>
                                            <nobr> 
                                            <input type="Button" value="Clear List" onClick="javascript:getTypes('ProdTypes');" class="inputbut" name="All">
                                            <input type="Button" value="Accessory" onClick="javascript:makeAccessory();" class="inputbut" name="Button">
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
                                      To remove a product being used as an accessory, just select the 
                                      product from the 'Accessories' list you would like to remove 
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
                                            <select name="TheAccess" size="8" multiple class="prodguinea" onDblClick="javascript:getProducts('TheAccess','TheAccess');">
                                              <option value="BIGNULL">0000000000000000</option>
                                            </select>
                                            <input type="hidden" name="Accessories">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="100%" valign="middle" align="center" height="45"> 
                                            <input type="Button" value=" Remove" onClick="javascript:killAccessory();" class="inputbut" name="Button">
                                            <input type="button" value="Preview" onClick="javascript:getProducts('TheAccess','TheAccess');" class="inputbut" name="button">
                                          </td>
                                        </tr>
                                        <tr> 
                                          <td width="100%" valign="top" align="center" height="15" bgcolor="#F2F2F7">&nbsp;</td>
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
                  </td>
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
	my $sth = $dbh->prepare("SELECT * FROM Products WHERE CMPartNum='$Accessory' ORDER BY ItemName ASC");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		my $ThyCMPartNum = $row[1];
		my $ThyItemName = $row[11];
		if ($ThyItemName =~ "&reg;") { $ThyItemName =~ s/&reg;//g; }
		if ($ThyItemName =~ "&#153;") { $ThyItemName =~ s/&#153;//g; }
		if ($ThyItemName =~ "&copy;") { $ThyItemName =~ s/&copy;//g; }
		print "TheAccess.options[sizer] = new Option('$ThyItemName');";
		print "TheAccess.options[sizer].value = '$ThyCMPartNum';";
		print "sizer++;";
		$count++;
	}
	$sth->finish;
}
print "}";
print "</script>";

##----------->>> FEED Main Components
{
print <<EOF

<script language="Javascript">
function feedMainParts() {

EOF
}

## MAIN PARTS
foreach $Parte (@Partes) {
	@LosSplits = split(/,,,,,/, $Parte);
	print "makeSystemItem2('MainNumbers','$LosSplits[0]','$LosSplits[1]');\n";
}

## SUB PARTS
foreach $SubParte (@SubPartes) {
	@LeSplits = split(/,,,,,/, $SubParte);
	print "		makeSystemItem2('Sub$LeSplits[2]\Numbers','$LeSplits[0]','$LeSplits[1]');\n";
}

print "}";
print "</script>";

{
print <<EOF

<input type="hidden" name="ProductType" value="$SavedPricingClass">
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
<title>Coastline Micro, Inc. - Shark Tank Admin System - Inventory ( Systems )</title>
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