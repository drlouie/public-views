#!/usr/local/bin/perl -w


## get HSH rates

print "Content-type: text/html \n\n";


$laPaginita = ("http://rws.mortgage101.com/templateroot/Articles/MarketSnapshot.asp?PVLID=4868");

use LWP::Simple;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
my $page = get ($laPaginita);

print "$page";

##return =true
1;