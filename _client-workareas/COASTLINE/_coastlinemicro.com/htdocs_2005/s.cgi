#!/usr/bin/perl5 -s

###########################################################################################################
# Company: �2001 NetMedia Solutions                                                                             #
# Date: Saturday, September 21, 2001                                                                      #
# Location: Los Angeles County, California, United States of America                                      #
# Made By: Luis Rodriguez (drlouie)                                                                       #
# Email: Drlouie@NetMediaSol.com                                                                          #
#                                                                                                         #
# Original Programming by FocalMedia.Net 2001
# 
# Database Interfacing by NetMediaSol.com 2002
##########################################################################

$fmsearch = "http://www.rhomberg.com/systemConfigurator/s.html";

## What directories on your server/hosting account would you like to search, If there is more than one directory, seperate them with a comma
@searchcrit = ("/usr/local/www/vhosts/coastlinemicro.com/htdocs/pointers/");

## Please specify the url paths below for the directories you would like to search. Enter the URLS in the same order as above. The first url path has to match the first server path that you specified above
@weburls = ("http://www.rhomberg.com/systemConfigurator/pointers");

## What is the extensions of the files to be searched If you want to use more than one extension seperate them via comma
@searchext = (".html", ".htm");

## How many items to list per page
$listperpage = "20";

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

### GET FILES

$itec = 0;

foreach $item (@searchcrit)
   {

     if (-e "$item")
        {
        opendir(DIR,"$item");
     	  @files = readdir(DIR);
        closedir (DIR);
        
        $fnc = 0;
        foreach $fn (@files)
           {
           $files[$fnc] = "$item/$fn" . "\t" . "$weburls[$itec]/$fn";
           $fnc++;
           }
        
        }
        else
        {
        print "Error - $item does not exist.";
        }

	 $itec++;
    $tmpc = push(@allfiles,@files);
   }


### SORT FILES

$sc = 0;

foreach $item (@allfiles)
   {
   foreach $ext (@searchext)
      {
   	if ($ext eq substr($item, length($item) - length($ext), length($ext)))
   	  {
   	  $sfiles[$sc] = $item;
   	  $sc++;
   	  }
      }
   }
  



### PREPARE KEYWORDS

   if ($fields{'keywords'} =~ / /)
   	{
    	@keywords = split (/ /,$fields{'keywords'});
    	}
    	else
    	{
    	$keywords[0] = $fields{'keywords'};
    	}


### SEARCH FILES
$srcntr = 0;

foreach $item (@sfiles)
   {

	($item, $iurl) = split(/\t/,$item);
   
   $mrelevance = 0;
   
	$fsize = (-s "$item");
   	open (RVF, "$item");
			read(RVF,$rdata,$fsize);
		close (RVF);

	 
	 ### GET RELEVANCE
	  
	  foreach $kw (@keywords)
	   {
	
	   if ($rdata =~ /$kw/i)
		  {
		
			### RELEVANCE
		
			@filelines = split(/\n/,$rdata);
			foreach $oln (@filelines)
					{
					if ($oln =~ /$kw/i){$mrelevance++;}
					if (($oln =~ /$fields{'keywords'}/i) and ($fields{'keywords'} =~ " "))
							{$mrelevance = $mrelevance + 15;}
							
							if ($mrelevance > $highsr) {$highsr = $mrelevance;}
							
					}
		
		   } ### FOUND MATCH
		 
		 } ### KEYWORD LOOP
	
	if ($mrelevance > 0) 
				{
				
				($ptitle) = &get_page_details($item);
				
				#print "FOUND MATCH IN $item - Relevance = $mrelevance -> $ptitle <br><b></b><br><br>";
				
				$mrelevance = &convertnr ($mrelevance);
				
				$sresults[$srcntr] = $mrelevance . "\t" . 
										   $item . "\t" . 
										   $iurl . "\t" . 
										   $ptitle;
				$srcntr++;
				}
	
   } ### FILE LOOP

	
	@sresults = sort (@sresults);
	$allresults = push(@sresults);
	$tmr = $allresults;
	
	foreach $item (@sresults)
		{
		$tmr = $tmr - 1;
		$sresults2[$tmr] = $item;
		}

##########################################################



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

$loadscript = "<script language=\"Javascript\">document.search2.keywords.value = '$fields{'keywords'}';</script>";

$mainlayout =~ s/!!Matches!!/$allresults/gi;
$mainlayout =~ s/!!Keywords!!/$fields{'keywords'}/gi;
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
	
		($relevance, $sp, $iurl, $ptitle) =split(/\t/,$item);	
		if ($ptitle eq "") {$ptitle = "Untitled";}
	
		$relevance = int($relevance / $highsr * 100);
		
		$wls = $listings;
		$wls =~ s/!!Numbers!!/$ippc\./gi;
		$wls =~ s/!!Title_With_Link!!/<a href="$iurl"><font class="slink">$ptitle<\/font><\/a>/gi;
		$wls =~ s/!!URL!!/$iurl/gi;
		$wls =~ s/!!RPERC!!/$relevance%/gi;
		
		$totalresults = $totalresults . $wls;
		
		#print "<p>$ippc. <a href=\"$iurl\">$ptitle</a><br>$iurl<br>Relevance: $relevance%</p>";

		}
	
	$ippc++;

}


  $kw = $fields{'keywords'};
  $kw =~ s/ /+/g;
  
  #$rplc = "<p align=\"center\"><font face=\"Verdana\" size=\"1\">"."P"."o".
  #"w"."e"."r"."e"."d". 
  #" by <a href=\"http://www.focalmedia.net/cgi-bin/fmsitesearch.html\" target=\"_blank\">"."F"."M"." S"."i"."t"."e"."S"."e"."a"."r"."c"."h</a></font></p><br></body>";
  #$mainlayout =~ s/<\/body>/$rplc/gi; 

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
		$pgstring = $pgstring . "<a href=\"$fmsearch?keywords=$kw&st=$st&nd=$nd\"><font class=\"slink\">$pg</font></a> ";
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
	$nextt = "<a href=\"$fmsearch?keywords=$kw&st=$st&nd=$nd\"><font class=\"slink\">Next Page >></font></a> ";
	}


 if ($fields{'st'} > 0)
	 	{
		$st = $fields{'st'} - $listperpage;
		$nd = $fields{'nd'} - $listperpage;
		$prev = "<a href=\"$fmsearch?keywords=$kw&st=$st&nd=$nd\"><font class=\"slink\"><< Prev Page</font></a> ";
		}

if (($prev ne "") and ($nextt ne ""))
	{
	$spcer = " | ";
	}
	else
	{
	$spcer = " ";
	}

	#if ($icnt < 1){$pitem = $configitems[16];}
	
	$mainlayout =~ s/!!SearchResults!!/$totalresults/gi;
	$mainlayout =~ s/!!Prev_Pages!!/$prev/gi;
	$mainlayout =~ s/!!Next_Pages!!/$nextt/gi;	

print $mainlayout;





######################################################################################

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



########################################################################################################################

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

