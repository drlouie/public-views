#!/usr/bin/perl5 -w

##########################################################################
# COPYRIGHT NOTICE:
# 
# Original Programming by FocalMedia.Net 2001
# 
# Database Interfacing by NetMediaSol.com 2002
#
##########################################################################

$muasearch = "http://www.coastlinemicro.com/admin/s_products.cgi";

$listperpage = "20";

########################################################################################
# Don't change anything below this line unless you know what you are doing.
########################################################################################

&get_env;
print "Content-type: text/html\n\n";

$fsize = (-s "s_return.nsf");
	open (RVF, "s_return.nsf");
		read(RVF,$mainlayout,$fsize);
	close (RVF);

$fsize = (-s "s_listings.nsf");
	open (RVF, "s_listings.nsf");
		read(RVF,$listings,$fsize);
	close (RVF);

if ($fields{'keywords'} eq "") {$fields{'keywords'} = "No-Keywords-Specified";}

### QUERY DB

use DBI;
my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
$dbh->{RaiseError} = 1; 
$count=0;
my $sth = $dbh->prepare("SELECT * FROM Products");
$sth->execute or die "Unable to execute query\n"; 
my @row;
while(@row = $sth->fetchrow_array) { 
	$SavedCMPartNum = $row[1];
	$SavedSYSCode = $row[2];
	$SavedKITCode = $row[3];
	$SavedMFGCode = $row[6];
	$SavedMFGPartNum = $row[7];
	$SavedItemName = $row[11];
	$SavedDescription = $row[12];
	$SavedKeywords = $row[14];
	$SavedCost = $row[21];
	$files[$count] = "$SavedCMPartNum-----$SavedMFGPartNum-----$SavedItemName------$SavedDescription------$SavedKeywords------$SavedCost" . "\t" . "$SavedCMPartNum" . "\t" . "$SavedItemName" . "\t" . "$SavedMFGCode" . "\t" . "$SavedMFGPartNum" . "\t" . "$SavedKITCode" . "\t" . "$SavedSYSCode" . "\t" . "$SavedCost";
	$tmpc = push(@sfiles,@files);
}
$sth->execute or die "Unable to execute query\n"; 
$sth->finish;
$dbh->disconnect;

### PREPARE KEYWORDS
if ($fields{'keywords'} =~ / /) { @keywords = split (/ /,$fields{'keywords'}); }
else { $keywords[0] = $fields{'keywords'}; }


### SEARCH ENTRIES
$srcntr = 0;

foreach $prod (@sfiles) {
	($item, $data, $ptitle, $mfgcode, $mfgpart, $kitcode, $syscode, $mycost) = split(/\t/,$prod);
   	$mrelevance = 0;

	### GET RELEVANCE
	  
	foreach $kw (@keywords) {
		if ($item =~ /$kw/i) {
			### RELEVANCE
			@filelines = split(/\n/,$item);
			foreach $oln (@filelines) {	
				if ($oln =~ /$kw/i){$mrelevance++;}
				if (($oln =~ /$fields{'keywords'}/i) and ($fields{'keywords'} =~ " "))
				{$mrelevance = $mrelevance + 15;}
				if ($mrelevance > $highsr) {$highsr = $mrelevance;}
			}
		
		} ### FOUND MATCH
	} ### KEYWORD LOOP
	
	if ($mrelevance > 0) {
		$mrelevance = &convertnr ($mrelevance);
		$sresults[$srcntr] = $mrelevance . "\t" . $item . "\t" . $data . "\t" . $ptitle . "\t" . $mfgcode . "\t" . $mfgpart . "\t" . $kitcode . "\t" . $syscode . "\t" . $mycost;
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

require ("date.nsp");

if ($Cuentame ne "0") { $leTable = "<table width=\"100%\" cellspacing=\"0\" cellpadding=\"0\" align=\"center\" border=\"0\"><tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"5%\" align=\"center\"><font class=\"sresults1\"><b>Rev.</b><br></font></td><td align=\"center\" width=\"40%\"><font class=\"sresults1\"><b>Name</b></font></td><td width=\"15%\" align=\"center\"><font class=\"sresults1\"><b>CLM</b></font></td><td width=\"15%\" align=\"center\"><font class=\"sresults1\"><b>MFG</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>\$</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Action</b></font></td></tr></table>"; }
else { $leTable = "<table width=\"100%\" cellspacing=\"2\" cellpadding=\"2\" align=\"center\" border=\"2\" bordercolor=\"#333366\"><tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"100%\" align=\"center\" bgcolor=\"#FFFFFF\"><font class=\"sresults1\">There were no matching products in the system, please try again...</font></td></tr></table>"; }

$mainlayout =~ s/!!LETBTR!!/$leTable/gi;
$mainlayout =~ s/!!Matches!!/$allresults/gi;
$mainlayout =~ s/!!Keywords!!/$fields{'keywords'}/gi;
$legal = `cat legal.nsf`;
$mainlayout =~ s/!!Legal!!/$legal/gi;
$mainlayout =~ s/!!Date!!/$date/gi;

foreach $item (@sresults2)	
	{
	
	if (($ippc > $fields{'st'}) and ($ippc <= $fields{'nd'}))
		{
	
		($relevance, $sp, $iurl, $ptitle, $mfgcode, $mfgpart, $kitcode, $syscode, $mycost) =split(/\t/,$item);	
		if ($ptitle eq "") {$ptitle = "Untitled";}

		if ($syscode ne "") { $myType = "change_product_system.cgi"; $myDel="change_product_system.cgi?DELETEIT=1&CMPartNum=$iurl";}
		else { $myType = "change_product_common.cgi"; $myDel="#"; }

		if ($mfgpart eq "") { $mfgpart = "<font color=\"#EB0000\">N/A</font>"; }
	
		$relevance = int($relevance / $highsr * 100);
		
		$wls = $listings;
		$wls =~ s/!!Numbers!!/$ippc\./gi;
		$wls =~ s/!!Title_With_Link!!/<a href="$myType\?CMPartNum=$iurl"><font class="slink">$ptitle<\/font><\/a>/gi;
		$wls =~ s/!!CLM!!/$iurl/gi;
		$wls =~ s/!!RPERC!!/$relevance%/gi;
		$wls =~ s/!!MFGP!!/$mfgpart/gi;
		$wls =~ s/!!MYPROG!!/$myType/gi;
		$wls =~ s/!!MYDEL!!/$myDel/gi;
		$wls =~ s/!!PRICE!!/\$$mycost/gi;
		$totalresults = $totalresults . $wls;
		}
	
	$ippc++;

}


  $kw = $fields{'keywords'};
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
		$pgstring = $pgstring . "<a href=\"$muasearch?keywords=$kw&st=$st&nd=$nd\"><font class=\"slink\">$pg</font></a> ";
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
	$nextt = "<a href=\"$muasearch?keywords=$kw&st=$st&nd=$nd\"><font class=\"slink\">Next Page >></font></a> ";
	}


 if ($fields{'st'} > 0)
	 	{
		$st = $fields{'st'} - $listperpage;
		$nd = $fields{'nd'} - $listperpage;
		$prev = "<a href=\"$muasearch?keywords=$kw&st=$st&nd=$nd\"><font class=\"slink\"><< Prev Page</font></a> ";
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

