#!/usr/local/bin/perl -w


## create mortgageRates.html file

print "Content-type: text/html \n\n";


$laPaginita = ("http://www.mortgage101.com/Articles/DailyRateSurvey.asp?state=california");

use LWP::Simple;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
my $page = get ($laPaginita);

@splitPage = split(/\n/,$page);


$theC = 0;
$startCapture =0;
$greenRates = 0;
$redRates = 0;

foreach $sp (@splitPage) {

		$part1 = '<table id="DailyRateSurvey_Table1"';
		$part2 = '<P><br>';
		$part3 = '<td class="gybg" style="width:160px;"><SPAN CLASS="bt">';
		$rem1 = '<td colSpan="2">';
		$URLpart1 = '<td class="bt" nowrap="nowrap" style="width:160px;">';
		$URLpart2 = '</a>';
		
		$iURL = '"http://rws.mortgage101.com/images/';
		$iURLb = '"/images/';
		$sp =~ s/$iURLb/$iURL/gi;

		$sp =~ s/TREND//gi;
		$sp =~ s/Trend//gi;
		
		if ($sp =~ $part1) {
			$sp =~ s/$rem1//gi;
			push(@theContent,"$sp");
			$startCapture = "1"
		}
		elsif ($sp =~ $part2) {
			$startCapture = "0"
		}
		elsif ($startCapture eq "1") {

			if ($sp =~ $URLpart1) {
				$sp1 = substr($sp,0,53);
				$sp2 = substr($sp,150);
				$sp2 =~ s/$URLpart2//gi;
				push(@theContent,"$sp1 $sp2");

					$sp1 =~ s/dlt/none/gi;
					$sp1 =~ s/ 00//gi;
					$sp2 =~ s/dlt/none/gi;
					$sp2 =~ s/ 00//gi;
					
				if ($sp =~ "grnuparrow" && $sp =~ "green") { 
					$greenRates++;
					push(@theGreen,"$sp1 $sp2");
				}
				if ($sp =~ "reddwnarrow") { 
					$redRates++;
					push(@theRed,"$sp1 $sp2");
				}

			}
			else {
			
				push(@theContent,"$sp");
				if ($sp =~ $part3) { 
					$sp =~ s/PRODUCT/<b>Loan Type<\/b>/gi;
					$sp =~ s/POINTS/<b>Points<\/b>/gi;
					$sp =~ s/RATE/<b>Rate<\/b>/gi;
					$sp =~ s/CHANGE/<b>Change<\/b>/gi;
					$sp =~ s/APR/<b>APR<\/b>/gi;
					$sp =~ s/dlt/none/gi;
					$sp =~ s/ 00//gi;
					push(@theRateTitle,"<tr class=\"rateTitle\">$sp</tr>"); 
				}


			}
		}

		


}




#	print "okay written: <a href='http://www.americorlending.com/mortgageRates.html'>http://www.americorlending.com/mortgageRates.html</a> and <a href='http://www.americorlending.com/mortgageRates5.html'>http://www.americorlending.com/mortgageRates5.html</a><br><br>";
	$totalParse = 0;



  	open(FILE,">/u179/lend24/mortgageRates.html") || &error('can not write log file');

	print FILE "<div class=\"theRateTitleB\">Current Mortgage Rates</div><table class=\"theRateSheetB\">";
	foreach $thisG (@theContent) {
		print FILE "<tr class=\"rateItemsB\">$thisG</tr>";
	}
	print FILE "</table>";

	close(FILE);
	
	$totalParse = 0;	
	print "<div class=\"theRateTitle\">Current Mortgage Rates</div><table class=\"theRateSheet\">@theRateTitle";
	foreach $thisG (@theGreen) {
		if ($totalParse ne "3") {  
			print "<tr class=\"rateItems\">$thisG</tr>";
			$totalParse++;
		}
	}
	foreach $thisR (@theRed) {
		if ($totalParse ne "3") {  
			print "<tr class=\"rateItems\">$thisR</tr>";
			$totalParse++;
		}
	}
	print "</table><div class=\"theRateLink\"><a href=\"Mortgage_Rates.shtml\" class=\"theRateLink\">view all rates</a></div>";



##return =true
1;