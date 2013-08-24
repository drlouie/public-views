#!/usr/bin/perl5

$buffer = $ENV{'QUERY_STRING'};
@pairs = split(/&/, $buffer);

foreach $pair (@pairs)
{
        local ($name, $value) = split(/=/, $pair);
        $value =~ tr/+/ /;
        $value =~
s/%([a-fA-F0-9][a-fA-F0-9])/pack("C",hex($1))/eg;
	$value =~ s/~!/ ~!/g;
	$FORM{$name} = $value;
}

##return =true
1;
