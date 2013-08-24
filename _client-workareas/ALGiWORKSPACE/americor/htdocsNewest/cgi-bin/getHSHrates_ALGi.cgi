#!/usr/bin/perl5 -s

print "Content-type: text/html \n\n";

use Finance::HSHrates;
@rates = getrates;

print @rates;
  
exit;