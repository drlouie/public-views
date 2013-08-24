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
function feedPackages() {
var b = navigator.appName;
if (b=="Netscape") { Package = parent.frames.botOne.document.forms[0].Package; }
else { Package = parent.botOne.document.forms[0].Package; }
var sizer = Package.length;

// CLEARS DEFAULT DATA FOR SECONDARY SELECT
for(var i = (sizer-1); i >= 0; i--) {
while (Package.options[i] != null) {
Package.options[i] = null;
	}
}

// get length after kills
var sizer = Package.length;
// GETTING READY TO FEED INFO

EOF
}

## FEED ALL UPS PACKAGES
$count=0;
@Packages = ("1DM,Next Day Air Early AM","1DA,Next Day Air","2DA,2nd Day Air","3DS,3 Day Select","GNDCOM,Ground Commercial","GNDRES,Ground Residential");
foreach $Package (@Packages) {
	$count++;
   	# Split each pair into individual variables.
   	local($value, $name) = split(/,/, $Package);
	print "Package.options[sizer] = new Option('$name');";
	print "Package.options[sizer].value = '$value';";
	print "sizer++;";
}


{
print <<EOF

}
</script>
</head>
<body onLoad="javascript:feedPackages();"></body>
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
function feedPackages() {
var b = navigator.appName;
if (b=="Netscape") { Package = parent.frames.botOne.document.forms[0].Package; }
else { Package = parent.botOne.document.forms[0].Package; }
var sizer = Package.length;

// CLEARS DEFAULT DATA FOR SECONDARY SELECT
for(var i = (sizer-1); i >= 0; i--) {
while (Package.options[i] != null) {
Package.options[i] = null;
	}
}

// get length after kills
var sizer = Package.length;
// GETTING READY TO FEED INFO


}
</script>
</head>
<body onLoad="javascript:feedPackages();"></body>
</html>

EOF
}
exit;
}