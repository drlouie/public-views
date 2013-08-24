#!/usr/bin/perl5 -s

###########################################################################################################
# Company: ©2001 NetMedia Solutions                                                                             #
# Date: Saturday, September 21, 2001                                                                      #
# Location: Los Angeles County, California, United States of America                                      #
# Made By: Luis Rodriguez (drlouie)                                                                       #
# Email: Drlouie@NetMediaSol.com                                                                          #
#                                                                                                         #
# Original Programming by FocalMedia.Net 2001
# 
# Database Interfacing by NetMediaSol.com 2002
##########################################################################

$muasearch = "s_prod.html";

$listperpage = "20";

########################################################################################
# Don't change anything below this line unless you know what you are doing.
########################################################################################

&get_env;
print "Content-type: text/html\n\n";

$fsize = (-s "s_prod_ret.nsf");
	open (RVF, "s_prod_ret.nsf");
		read(RVF,$mainlayout,$fsize);
	close (RVF);

$fsize = (-s "s_prod_list.nsf");
	open (RVF, "s_prod_list.nsf");
		read(RVF,$listings,$fsize);
	close (RVF);

if ($fields{'PKeywords'} eq "") {$fields{'PKeywords'} = "No&nbsp;search&nbsp;terms&nbsp;given";}

if ($fields{'ProductType'} eq "All" || $fields{'ProductType'} eq "") { $MuaPClass = ""; }
## WHAT TYPE OF PRODUCT?
else {
	if ($fields{'ProductType'} eq "Desktop" || $fields{'ProductType'} eq "Server" || $fields{'ProductType'} eq "Notebook") {
		$MuaPClass = "WHERE PricingClass='$fields{'ProductType'}'";
	}
	elsif ($fields{'ProductType'} eq "HardDrive" || $fields{'ProductType'} eq "Monitor" || $fields{'ProductType'} eq "Memory" || $fields{'ProductType'} eq "VideoCard" || $fields{'ProductType'} eq "Printer" || $fields{'ProductType'} eq "Software") {
		$MuaPClass = "WHERE PricingClass='$fields{'ProductType'}'";
	}
	else { $MuaPClass = "WHERE PricingClass='Peripheral'"; }
}

### QUERY DB

use DBI;
my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
$dbh->{RaiseError} = 1; 
$count=0;
my $sth = $dbh->prepare("SELECT * FROM Products $MuaPClass");
$sth->execute or die "Unable to execute query\n"; 
my @row;
while(@row = $sth->fetchrow_array) { 
	$SavedCMPartNum = $row[1];
	$SavedSYSCode = $row[2];
	$SavedKITCode = $row[3];
	$SavedMFGCode = $row[6];
	$SavedMFGPartNum = $row[7];
	$SavedPClass = $row[10];
	$SavedItemName = $row[11];
	$SavedDescription = $row[12];
	$SavedTechSpecs = $row[13];
	$SavedKeywords = $row[14];
	$SavedSPhoto = $row[17];
	$SavedCost = $row[21];
	$SavedProdType = $row[32];
	$Searchable = $row[33];
	if ($Searchable eq "Yes") { push(@sfiles,"$SavedCMPartNum $SavedMFGPartNum $SavedItemName $SavedDescription $SavedKeywords $SavedTechSpecs $SavedCost" . "\t" . "$SavedCMPartNum" . "\t" . "$SavedItemName" . "\t" . "$SavedMFGCode" . "\t" . "$SavedMFGPartNum" . "\t" . "$SavedKITCode" . "\t" . "$SavedSYSCode" . "\t" . "$SavedCost" . "\t" . "$SavedDescription" . "\t" . "$SavedSPhoto" . "\t" . "$SavedPClass" . "\t" . "$SavedProdType"); }
}
$sth->execute or die "Unable to execute query\n"; 
$sth->finish;

### PREPARE KEYWORDS
if ($fields{'PKeywords'} =~ / /) { @keywords = split (/ /,$fields{'PKeywords'}); }
else { $keywords[0] = $fields{'PKeywords'}; }


foreach $prod (@sfiles) {
	($item, $data, $ptitle, $mfgcode, $mfgpart, $kitcode, $syscode, $mycost, $leDesc, $lePhoto, $lePClass, $leProdType) = split(/\t/,$prod);

	if ($syscode ne "") { 
		my $sth = $dbh->prepare("SELECT * FROM Systems WHERE SystemID='$syscode'");
		$sth->execute or die "Unable to execute query\n"; 
		my @row;
		while(@row = $sth->fetchrow_array) { 
			$CMSeries = $row[2];
			if ($CMSeries eq "GreatWhite") { $CMSeries = "gw"; }
			if ($CMSeries eq "Mako") { $CMSeries = "mako"; }
			if ($CMSeries eq "Reef") { $CMSeries = "reef"; }
			if ($CMSeries eq "Thresher") { $CMSeries = "thresher"; }
			if ($CMSeries eq "Tiger") { $CMSeries = "tiger"; }
			push(@sfiles2,"$item" . "\t" . "$data" . "\t" . "$ptitle" . "\t" . "$mfgcode" . "\t" . "$mfgpart" . "\t" . "$kitcode" . "\t" . "$syscode" . "\t" . "$mycost"  . "\t" . "$leDesc" . "\t" . "$CMSeries" . "\t" . "Coastline Micro" . "\t" . "$lePhoto" . "\t" . "$lePClass" . "\t" . "$leProdType");
			
		}
		$sth->execute or die "Unable to execute query\n"; 
		$sth->finish;	
	}
	else {
		## GET MFG INFO
		my $sth = $dbh->prepare("SELECT * FROM MFGs WHERE ManufacturerID='$mfgcode'");
		$sth->execute or die "Unable to execute query\n"; 
		my @row;
		while(@row = $sth->fetchrow_array) { 
			$MFGName = $row[1];
			push(@sfiles2,"$item" . "\t" . "$data" . "\t" . "$ptitle" . "\t" . "$mfgcode" . "\t" . "$mfgpart" . "\t" . "$kitcode" . "\t" . "$syscode" . "\t" . "$mycost" . "\t" . "$leDesc" . "\t" . "NONE" . "\t" . "$MFGName" . "\t" . "$lePhoto" . "\t" . "$lePClass" . "\t" . "$leProdType");
		}
		$sth->execute or die "Unable to execute query\n"; 
		$sth->finish;
	}

}

### SEARCH ENTRIES
$srcntr = 0;

foreach $prod (@sfiles2) {
	($item, $data, $ptitle, $mfgcode, $mfgpart, $kitcode, $syscode, $mycost, $leDesc, $mycmseries, $mfgname, $lePhoto, $lePClass, $leProdType) = split(/\t/,$prod);
   	$mrelevance = 0;

	### GET RELEVANCE
	  
	foreach $kw (@keywords) {
		if ($item =~ /$kw/i) {
			### RELEVANCE
			@filelines = split(/\n/,$item);
			foreach $oln (@filelines) {	
				if ($oln =~ /$kw/i){$mrelevance++;}
				if (($oln =~ /$fields{'PKeywords'}/i) and ($fields{'PKeywords'} =~ " "))
				{$mrelevance = $mrelevance + 15;}
				if ($mrelevance > $highsr) {$highsr = $mrelevance;}
			}
		
		} ### FOUND MATCH
	} ### KEYWORD LOOP
	
	if ($mrelevance > 0) {
		$mrelevance = &convertnr ($mrelevance);
		$sresults[$srcntr] = $mrelevance . "\t" . $item . "\t" . $data . "\t" . $ptitle . "\t" . $mfgcode . "\t" . $mfgpart . "\t" . $kitcode . "\t" . $syscode . "\t" . $mycost . "\t" . $leDesc . "\t" . $mycmseries . "\t" . $mfgname . "\t" . $lePhoto . "\t" . $lePClass . "\t" . $leProdType;
		$srcntr++;
	}

} ### ENTRY LOOP

	
$Cuentame=0;
@sresults = sort (@sresults);
$allresults = push(@sresults);
$tmr = $allresults;
	foreach $item (@sresults) {
		$Cuentame++;
		$tmr = $tmr - 1;
		$sresults2[$tmr] = $item;
	}

$modp = ($allresults % $listperpage );
$pages = ($allresults - $modp) / $listperpage;
if ($modp != 0) {$pages++;}

if ($fields{'st'} eq ""){$fields{'st'} = 0;}
if ($fields{'nd'} eq ""){$fields{'nd'} = $listperpage;}

$pitem = "";
$ippc = 1;

$pow = `cat pow_products.nsf`;
## must have command to run search
$powbutton = "";	
require ("date.nsp");

$PC1 = "15"; $PC2 = "65"; $ImageTitle = "Image"; $GETIMAGES = "YES";

if ($Cuentame ne "0") { $leTable = "
<table width=\"100%\" cellspacing=\"0\" cellpadding=\"2\" align=\"center\" border=\"0\">
<tr height=\"20\" width=\"100%\">
<td align=\"left\" width=\"$PC2%\" bgcolor=\"#F2F2F7\"><font class=\"sresults1\"><b>Name</b></font></td>
<td width=\"15%\" align=\"left\"><font class=\"sresults1\"><b>CLM</b></font></td>
<td width=\"$PC1%\" align=\"center\"><font class=\"sresults1\"><b>$ImageTitle</b></font></td>
</tr></table>"; 
}
else { $leTable = "<table width=\"100%\" cellspacing=\"2\" cellpadding=\"2\" align=\"center\" border=\"2\" bordercolor=\"#333366\"><tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"100%\" align=\"center\" bgcolor=\"#FFFFFF\"><font class=\"sresults1\">There were no matching products in the system, please try again...</font></td></tr></table>"; }

$loadscript = "<script language=\"Javascript\">document.search1.PKeywords.value = '$fields{'PKeywords'}';</script>";

$mainlayout =~ s/!!LETBTR!!/$leTable/gi;
$mainlayout =~ s/!!Matches!!/$allresults/gi;
$mainlayout =~ s/!!Keywords!!/$fields{'PKeywords'}/gi;
$legal = `cat legal.nsf`;
$mainlayout =~ s/!!Legal!!/$legal/gi;
$mainlayout =~ s/!!Powbutton!!/$powbutton/gi;
$mainlayout =~ s/!!Pow!!/$pow/gi;
$mainlayout =~ s/!!Date!!/$date/gi;
$mainlayout =~ s/!!LoadScript!!/$loadscript/gi;

foreach $item (@sresults2)	
	{
	
	if (($ippc > $fields{'st'}) and ($ippc <= $fields{'nd'}))
		{
	
		($relevance, $sp, $iurl, $ptitle, $mfgcode, $mfgpart, $kitcode, $syscode, $mycost, $leDesc, $mycmseries, $mfgname, $lePhoto, $lePClass, $leProdType) =split(/\t/,$item);
		if ($ptitle eq "") {$ptitle = "Untitled Product";}
		
		if ($syscode ne "") { $myType = "products.html?title=$mycmseries&loadsys=$iurl"; $THISCOST = "<font color=\"#EB0000\">Flex Price</font>"; }
		elsif ($kitcode ne "") { $myType = "products.html?title=products&loadkit=$iurl"; $THISCOST = "View Price"; }
		else { 
			$EntireTotal = sprintf("%.2f", $mycost);
			## Snif cookie, if present test for logged in status
			require ("cookiesnif.nsp");
	
			if ($Cookies{'Echado'} eq "YES") {
				if ($lePClass eq "Monitor") { $MyTypo = "$Cookies{'MOV'}"; }
				elsif ($lePClass eq "Memory") { $MyTypo = "$Cookies{'MYV'}"; }
				elsif ($lePClass eq "HardDrive") { $MyTypo = "$Cookies{'HDV'}"; }
				elsif ($lePClass eq "VideoCard") { $MyTypo = "$Cookies{'VDV'}"; }
				elsif ($lePClass eq "Printer") { $MyTypo = "$Cookies{'PTV'}"; }
				else { $MyTypo = "$Cookies{'PHV'}"; }
				$MyTypo = 100 - $MyTypo;
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
			$mycost = sprintf("%.2f", $EntireTotal);
			$myType = "products.html?title=products&loadprod=$iurl"; $THISCOST = "\$$mycost"; 
		}

		if ($mfgpart eq "") { $mfgpart = "<font color=\"#EB0000\">CLM Product</font>"; }

		$relevance = int($relevance / $highsr * 100);

		##--->> REFORMAT DESCRIPTIONS FOR PARSING
		$DCount = "0";
		@DescCount = split(//, $leDesc);
		foreach $DescDesc (@DescCount) { 
		$DCount++; 
			if ($DCount >= "150" && ($DescDesc eq "." || $DescDesc eq "!")) { 
				$leDesc = substr($leDesc, 0, $DCount); 
			}
			elsif ($leDesc eq "test" || $leDesc eq "none" || $leDesc eq "NONE" || $leDesc eq "None") {
				$leDesc = "";
			}
		}

		if ($lePhoto ne "" && $lePhoto ne " ") {
			my $sth = $dbh->prepare("SELECT * FROM Images WHERE ImageID='$lePhoto'");
			$sth->execute or die "Unable to execute query\n";
			my @row;
			while(@row = $sth->fetchrow_array) { 
				$SavedInnerURL = $row[6];
			}
			$sth->execute or die "Unable to execute query\n"; 
			$sth->finish;
		}
		else {
			$SavedInnerURL = "images/noimage_smallsrch.gif";
		}
		$leImagen = "<a href=\"$myType\"><img src=\"/$SavedInnerURL\" width=\"83\" height=\"50\" border=\"0\"></a>";

		$wls = $listings;

		$wls =~ s/!!IMAGEN!!/$leImagen/gi;

		$wls =~ s/!!PC1!!/$PC1/gi;
		$wls =~ s/!!PC2!!/$PC2/gi;
		$wls =~ s/!!Numbers!!/$ippc\./gi;
		$wls =~ s/!!Title_With_Link!!/<a href="$myType"><font class="slink">$ptitle<\/font><\/a>/gi;
		$wls =~ s/!!CLM!!/$iurl/gi;
		$wls =~ s/!!ProdDesc!!/<br>$leDesc/gi;
		$wls =~ s/!!RPERC!!/$MiCount/gi;
		$wls =~ s/!!MYPROG!!/$myType/gi;
		$wls =~ s/!!PRICE!!/$THISCOST/gi;
		
		$totalresults = $totalresults . $wls;
		}
	
	$ippc++;

}

$dbh->disconnect;

  $kw = $fields{'PKeywords'};
  $kw =~ s/ /+/g;
  
  for ($ms = 0; $ms < $pages; $ms++) 
	{
	$pg = $ms + 1;
	if ($fields{'nd'} == ($pg * $listperpage))
		{
		$pgstring = $pgstring . " <font color=\"#FD0000\"><b>$pg</b></font> ";
		}
	  	else
		{
		$st = ($pg * $listperpage) - $listperpage;
		$nd = ($pg * $listperpage);
		$pgstring = $pgstring . "<a href=\"$muasearch?PKeywords=$kw&st=$st&nd=$nd&ProductType=$fields{'ProductType'}\"><font class=\"slink\">$pg</font></a> ";
		}
	}


if ($pages > 1)
	{
	$mainlayout =~ s/!!Pages!!/Pages: $pgstring/gi;
	}
	else
	{
	$mainlayout =~ s/!!Pages!!//gi;
	}


# PREV NEXT

$spls = $modp;
if ($spls == 0){$spls++;}

 if ($fields{'nd'} <= ($allresults - $spls))
 	{
	$st = $fields{'st'} + $listperpage;
	$nd = $fields{'nd'} + $listperpage;
	$nextt = "<a href=\"$muasearch?PKeywords=$kw&st=$st&nd=$nd&ProductType=$fields{'ProductType'}\"><font class=\"slink\">Next Page >></font></a> ";
	}


 if ($fields{'st'} > 0)
	 	{
		$st = $fields{'st'} - $listperpage;
		$nd = $fields{'nd'} - $listperpage;
		$prev = "<a href=\"$muasearch?PKeywords=$kw&st=$st&nd=$nd&ProductType=$fields{'ProductType'}\"><font class=\"slink\"><< Prev Page</font></a> ";
		}

if (($prev ne "") and ($nextt ne ""))
	{
	$spcer = " | ";
	}
	else
	{
	$spcer = " ";
	}

	$mainlayout =~ s/!!SearchResults!!/$totalresults/gi;
	$mainlayout =~ s/!!Prev_Pages!!/$prev/gi;
	$mainlayout =~ s/!!Next_Pages!!/$nextt/gi;	

print $mainlayout;

sub get_page_details
{

my ($begin_title,$end_title,$begin_title);

### TITLE
if ($rdata =~ m/<title>/gi)
	{
	$begin_title = pos($rdata);
	}

if ($rdata =~ m/<\/title>/gi)
	{
	$end_title = pos($rdata);
	$end_title = $end_title - 8;
	$end_title = $end_title - $begin_title;
	}

$title = substr($rdata, $begin_title, $end_title);

$title =~ s/<//g;
$title =~ s/>//g;
if (length($title) > 70) {$title = substr($title, 0, 70) . "...";} 

return ($title);

}



sub convertnr
{

my ($cno) = @_;

if (length($cno) == 1) {$cno = "000000000000" . $cno;}
if (length($cno) == 2) {$cno = "00000000000" . $cno;}
if (length($cno) == 3) {$cno = "0000000000" . $cno;}
if (length($cno) == 4) {$cno = "000000000" . $cno;}
if (length($cno) == 5) {$cno = "00000000" . $cno;}
if (length($cno) == 6) {$cno = "0000000" . $cno;}
if (length($cno) == 7) {$cno = "000000" . $cno;}
if (length($cno) == 8) {$cno = "00000" . $cno;}
if (length($cno) == 9) {$cno = "0000" . $cno;}
if (length($cno) == 10){$cno = "000" . $cno;}
if (length($cno) == 11){$cno = "00" . $cno;}
if (length($cno) == 12){$cno = "0" . $cno;}	

return ($cno);

}

sub get_env
{

if ($ENV{'QUERY_STRING'} ne "") {
								$temp = $ENV{'QUERY_STRING'};
								}
								else
								{
								read(STDIN, $temp, $ENV{'CONTENT_LENGTH'});
								}

@pairs=split(/&/,$temp);

foreach $item(@pairs) 
	{
	($key,$content)=split (/=/,$item,2);
	$content=~tr/+/ /;
	$content=~ s/%(..)/pack("c",hex($1))/ge;
	$fields{$key}=$content;
	}

}

