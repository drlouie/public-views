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
if (b=="Netscape") { CMPartNum = parent.frames.botOne.document.change.CMPartNum; }
else { CMPartNum = parent.botOne.document.change.CMPartNum; }
var sizer = CMPartNum.length;

// CLEARS DEFAULT DATA FOR SECONDARY SELECT
for(var i = (sizer-1); i >= 0; i--) {
while (CMPartNum.options[i] != null) {
CMPartNum.options[i] = null;
	}
}

// get length after kills
var sizer = CMPartNum.length;
// GETTING READY TO FEED INFO

EOF
}

use DBI;
if ($PricingClass eq "Kit") {
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	$count=0;
	my $sth = $dbh->prepare("SELECT * FROM Kits ORDER BY Parent");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$SavedParent = $row[1];
		print "CMPartNum.options[sizer] = new Option('$SavedParent');";
		print "CMPartNum.options[sizer].value = '$SavedParent';";
		print "sizer++;";
		$count++;
	}
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
}
else {
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	$count=0;
	my $sth = $dbh->prepare("SELECT * FROM Products WHERE PricingClass='$PricingClass' ORDER BY CMPartNum");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$SavedKitCode = $row[3];
		$SavedCMPartNum = $row[1];
		if ($SavedKitCode eq "") { 
			print "CMPartNum.options[sizer] = new Option('$SavedCMPartNum');";
			print "CMPartNum.options[sizer].value = '$SavedCMPartNum';";
			print "sizer++;";
		}
		$count++;
	}
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
}

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