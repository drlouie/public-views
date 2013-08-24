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

## Grab User Input
require ("parse_query.nsp");

## script's name
$script = "$ENV{'SCRIPT_NAME'}";
## grab admin date format
require ("date.nsp");

	my $drop = "$FORM{'drop'}";
	my $date = $date;
	use DBI; 
	use strict; 
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $sth = $dbh->prepare("DROP DATABASE $drop");
	$sth->execute or die "Sorry, that Username/Password combination is incorrect, please try again.\n"; 
	my $row = $sth->fetchrow_arrayref; 
	$sth->finish;
	$dbh->disconnect; 
	
{
print <<EOF

<html>
<head>
<title>Press Release Article Administration System - $date</title>
</head>
<body bgcolor="#FFFFFF">
Table <strong>$drop</strong> deleted
</body></noframes>
</html>

EOF
}
exit;