#!/usr/local/bin/perl -w


## create marketRates.html file

 print "Content-type: text/html \n\n";


$laPaginita = ("http://rws.mortgage101.com/templateroot/Articles/MarketSnapshot.asp?PVLID=4868");

use LWP::Simple;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
my $page = get ($laPaginita);

@splitPage = split(/\n/,$page);


$theC = 0;

$finder = "<!--content-->";

foreach $sp (@splitPage) {

	$scriptI = "this.src='http://rws.mortgage101.com/images";
	$scriptIb = "this.src='/images";
	$sp =~ s/$scriptIb/$scriptI/gi;

	$iURL = '"http://rws.mortgage101.com/images/';
	$iURLb = '"/images/';
	$sp =~ s/$iURLb/$iURL/gi;	

	$iBR = '<td vAlign="top"><font class="pagetitle" style="padding-top:5px;">Stock Market Status</font>';
	$iBRb = '<td vAlign="top"><br>';
	$sp =~ s/$iBRb/$iBR/gi;	
	

	$leTR = '</tr>';
	if ($sp =~ "$finder" && $theC eq "0") {
		$theC = 1;
		push(@theContent,"$sp");
	}
	elsif ($sp =~ "$finder") { 
		$theC = 0;
		$sp =~ s/$leTR//gi;	
		push(@theContent,"$sp");
	}
	elsif ($theC eq "1") {
		push(@theContent,"$sp");
	}

}

  	open(FILE,">/u179/lend24/marketRates.html") || &error('can not write log file');
	print FILE "@theContent\n";
	close(FILE);


	print "okay written: <a href='http://www.americorlending.com/marketRates.html'>http://www.americorlending.com/marketRates.html</a>";


#print "okay";
### <!--RWSBEGINHEADER-->
### <!--RWSENDHEADER-->

##return =true
1;