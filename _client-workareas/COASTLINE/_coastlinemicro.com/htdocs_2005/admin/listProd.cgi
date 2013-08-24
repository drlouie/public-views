#!/usr/bin/perl5 -w

## Test location of request
require ("referer.nsp");

print "Content-type: text/html\n\n";

## Grab User Input
require ("parse_query.nsp");

## If data present scan it...
if ($FORM{'PricingClass'}) {

$PricingClass = "$FORM{'PricingClass'}";

{
print <<EOF

<html>
<head>
<title>Product Sniffer</title>
<script language="javascript">
function feedProducts() {
var b = navigator.appName;
if (b=="Netscape") { InternalPartNum = parent.frames.botOne.document.change.InternalPartNum; }
else { InternalPartNum = parent.botOne.document.change.InternalPartNum; }
var sizer = InternalPartNum.length;

// CLEARS DEFAULT DATA FOR SECONDARY SELECT
for(var i = (sizer-1); i >= 0; i--) {
while (InternalPartNum.options[i] != null) {
InternalPartNum.options[i] = null;
	}
}

// get length after kills
var sizer = InternalPartNum.length;
// GETTING READY TO FEED INFO

EOF
}

use DBI;
my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
$dbh->{RaiseError} = 1; 
$count=0;

if ($PricingClass eq "Kit") {
	my $sth = $dbh->prepare("SELECT * FROM Kits ORDER BY Parent");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$SavedParent = $row[1];
		print "InternalPartNum.options[sizer] = new Option('$SavedParent');";
		print "InternalPartNum.options[sizer].value = '$SavedParent';";
		print "sizer++;";
		$count++;
	}
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
}
else {
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 
	$count=0;
	my $sth = $dbh->prepare("SELECT * FROM Products WHERE PricingClass='$PricingClass' ORDER BY InternalPartNum");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$SavedKitCode = $row[3];
		$SavedInternalPartNum = $row[1];
		if ($SavedKitCode eq "") { 
			print "InternalPartNum.options[sizer] = new Option('$SavedInternalPartNum');";
			print "InternalPartNum.options[sizer].value = '$SavedInternalPartNum';";
			print "sizer++;";
		}
		$count++;
	}
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
}
$dbh->disconnect; 
{
print <<EOF

}
</script>
</head>
<body onLoad="javascript:feedProducts();"></body>
</html>

EOF
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