#!/usr/bin/perl5 -w

## Test location of request
require ("referer.nsp");

print "Content-type: text/html\n\n";

## Grab User Input
require ("parse_query.nsp");

## If data present scan it...
if ($FORM{'Courier'} eq "UPS") {

{
print <<EOF

<html>
<head>
<title>Shipping Scripter</title>
<script language="javascript">
function shipPrice() {
var b = navigator.appName;
if (b=="Netscape") { ShipPrice = parent.frames.botOne.document.forms[0].ShipPrice; }
else { ShipPrice = parent.botOne.document.forms[0].ShipPrice; }

EOF
}

## get dynamic shipping price per pound
use lib '.';
use Business::UPS;
my $type = "$FORM{'Package'}";
my $to = "$FORM{'ShipZip'}";
my $wgt = "1";
my ($from,$co) = qw/92618/;
my ($shipping,$ups_zone,$error) = getUPS($type,$from,$to,$wgt,$co,'', '', '', '', '');
$error and die "ERROR: $error\n";
print "ShipPrice.value = \"$shipping\";";

{
print <<EOF

}
</script>
</head>
<body onLoad="javascript:shipPrice();"></body>
</html>

EOF
}
exit;
}

else {

{
print <<EOF

<html>
<head>
<title>Shipping Scripter</title>
<script language="javascript">
function shipPrice() {
var b = navigator.appName;
if (b=="Netscape") { ShipPrice = parent.frames.botOne.document.forms[0].ShipPrice; }
else { ShipPrice = parent.botOne.document.forms[0].ShipPrice; }
}
</script>
</head>
<body onLoad="javascript:shipPrice();"></body>
</html>

EOF
}
exit;
}