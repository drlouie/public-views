#!/usr/local/bin/perl

require ("referer.hs"); 

require ("parse_query.hs");

require ("date.hs");

if ($FORM{'new_url'}) { 

$new_url = "$FORM{'new_url'}";

&new_url;

}

elsif ($FORM{'shot'}) { 

$shot = "$FORM{'shot'}";

&shot;

}

elsif ($FORM{'internal'}) { 

$internal = "$FORM{'internal'}";

&internal;

}

else {
print "Content-type: text/html\n\n";
{
print <<EOF
<HTML>
<HEAD>
<TITLE>Coastline Micro Inc - ERROR: Location Unspecified</title>
<META HTTP-EUIV="Refresh" CONTENT="5; URL=index.cgi">
</head>
</html>

Sorry, you are coming from an unspecified location out of Coastline Micro. This portion of the site only can be accessed from within the site. We will forward you to our Home Page in approximately 5 seconds. Sorry for the inconvenience this may have caused.

EOF
}
}

sub new_url {

print "Content-type: text/html\n\n";

{
print <<EOF

<html>
<head>
<title>Coastline Micro Inc. - $date</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>

<frameset rows="30, *" frameborder="NO" border="0" framespacing="0" cols="*">
  <frame name="topOut" noresize scrolling=no src="topout.cgi">
  <frame name="botOut" noresize src="$new_url">
</frameset>
<noframes>
<body bgcolor="#FFFFFF">
Sorry
</body>
</noframes>
</html>

EOF
}
}

sub shot {
print "Content-type: text/html\n\n";
{
print <<EOF

<html>
<head>
<title>Coastline Micro inc. - $date </title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body bgcolor="#ffffff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<center>
<font color="#8f8fab" face="verdana,arial,helvetica" size="2"><b>Click image to close window.<br>
<a href="javascript:window.close()"><img src="/images/shots/$shot.jpg" border="0"></a>
<br>
Click image to close window.</b></font>
</center>
</body>
</noframes>
</html>

EOF
}
}

sub internal {
print "Location: $internal\n\n";
}