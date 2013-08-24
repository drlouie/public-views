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

## Check to see if the logged user is granted rights to this action script
if (($Cookies{'UserType'} eq "CMManage") || ($Cookies{'UserType'} eq "CMAdmin") || ($Cookies{'UserType'} eq "CMSales")) { $nextone = "1"; }
else {
	$noaccess = `cat noaccess.nsf`;
	print "$noaccess";	
	exit;
}

## Grab User Input
require ("parse_query.nsp");

## script's name
$script = "$ENV{'SCRIPT_NAME'}";
## grab admin date format
require ("date.nsp");

## get CM legal piece
$legal = `cat legal.nsf`;

## If SEARCH data present scan it...
if (($FORM{'SearchType'}) && ($FORM{'SearchTerms'})) { 

## top HTML template
&topper;

## top INFO TABLE template
{
print <<EOF
<br>
<table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr>
    <td>
                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                          <tr> 
                            <td width="35%"><font class="stextbig"><b>Search Results</b></font></td>
                            <td align="right" width="65%"><font class="stext2"><b><font color="#FD0000">&nbsp;</font></b></font></td>
                          </tr>
                          <tr bgcolor="#333366"> 
                            <td colspan="2" height="1"><img src="images/spacer.gif" width="1" height="1"></td>
                          </tr>
                          <tr> 
                            <td colspan="2" height="10"><img src="images/spacer.gif" width="1" height="10"></td>
                          </tr>
                          <tr> 
                            <td colspan="2" height="75">
	<table width="85%" align="center" border="1" bgcolor="#FFFFFF" cellpadding="2" cellspacing="0">
	<tr><td width="100%" valign="middle">
	<font class="sresults1"><li>To view a message click on the '<b>Subject</b>' of choice</li><li>The red title represents the order in which the search results are currently displayed</li></font>
	</td></tr>
	</table>							
							</td>
                          </tr>
                          <tr> 
                            <td colspan="2" align="left" width="100%"> 

	<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
EOF
}

	## Crumble Form Input to DB Queries as necessary
	$Formee = "$FORM{'SearchTerms'}"; 
	if ($FORM{'SearchType'} eq "Username") { 
		$Searchee = "Username"; 
		$Sortee = "Username"; 
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" valign=\"top\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresultsred\"><b>Username</b><br></font></td><td valign=\"top\" align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Reply Email</b></font></td><td width=\"20%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Recipients</b></font></td><td width=\"20%\"valign=\"top\"  align=\"center\"><font class=\"sresults1\"><b>Subject</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Date</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>File(s)</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	if ($FORM{'SearchType'} eq "ReplyAdd") { 
		$Searchee = "ReplyAdd"; 
		$Sortee = "ReplyAdd"; 
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" valign=\"top\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresultsred\"><b>Reply Email</b><br></font></td><td valign=\"top\" align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Reply Email</b></font></td><td width=\"20%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Recipients</b></font></td><td width=\"20%\"valign=\"top\"  align=\"center\"><font class=\"sresults1\"><b>Subject</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Date</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>File(s)</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	if ($FORM{'SearchType'} eq "Recipients") { 
		$Searchee = "Recipients"; 
		$Sortee = "Recipients"; 
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" valign=\"top\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresultsred\"><b>Recipient(s)</b><br></font></td><td valign=\"top\" align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Subject</b></font></td><td width=\"20%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Reply Email</b></font></td><td width=\"20%\"valign=\"top\"  align=\"center\"><font class=\"sresults1\"><b>Username</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Date</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>File(s)</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	if ($FORM{'SearchType'} eq "Subject") { 
		$Searchee = "Subject"; 
		$Sortee = "Subject"; 
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" valign=\"top\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresultsred\"><b>Subject</b><br></font></td><td valign=\"top\" align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Recipients</b></font></td><td width=\"20%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Reply Email</b></font></td><td width=\"20%\"valign=\"top\"  align=\"center\"><font class=\"sresults1\"><b>Username</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Date</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>File(s)</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	if ($FORM{'SearchType'} eq "Attachments") { 
		$Searchee = "Attachment1, Attachment2, Attachment3"; 
		$Sortee = "Attachment1"; 
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" valign=\"top\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresultsred\"><b>File(s)</b><br></font></td><td valign=\"top\" align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Recipients</b></font></td><td width=\"20%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Reply Email</b></font></td><td width=\"20%\"valign=\"top\"  align=\"center\"><font class=\"sresults1\"><b>Username</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Date</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Subject</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	my $SearchBy = "$Searchee";
	my $SortBy = "$Sortee";
	my $FormInput = "$Formee";
	my $ActionUser = "$Cookies{'Username'}";
	## Start DB connection
	use DBI; 
	use strict; 
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $count=0;
	my $queeery = "SELECT * FROM Messages WHERE $SortBy LIKE '%$FormInput%' ORDER BY $SearchBy";
	my $sth = $dbh->prepare("$queeery");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$count++;
		my $SavedUsername = $row[1];
		my $SavedReplyAdd = $row[5];
		my $SavedRecipients = $row[6];
		my $SavedSubject = $row[7];
		my $SavedAttachments = "$row[9] &nbsp; $row[10] &nbsp; $row[11]";
		my $SavedAddedOn = $row[12];
		my $TheYear = substr($SavedAddedOn, 0, 2);
		my $TheMonth = substr($SavedAddedOn, 2, 2);
		my $TheDay = substr($SavedAddedOn, 4, 2);
		if ($SortBy eq "Username") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedUsername<br></font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\">$SavedReplyAdd</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedRecipients</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\"><u>$SavedSubject</u></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$TheMonth/$TheDay/$TheYear</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedAttachments</font></td></tr>"; }
		if ($SortBy eq "ReplyAdd") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\">$SavedReplyAdd</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedUsername<br></font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedRecipients</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\"><u>$SavedSubject</u></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$TheMonth/$TheDay/$TheYear</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedAttachments</font></td></tr>"; }
		if ($SortBy eq "Recipients") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedRecipients</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\"><u>$SavedSubject</u></font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\">$SavedReplyAdd</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedUsername<br></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$TheMonth/$TheDay/$TheYear</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedAttachments</font></td></tr>"; }
		if ($SortBy eq "Subject") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\"><u>$SavedSubject</u></font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedRecipients</font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\">$SavedReplyAdd</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedUsername<br></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$TheMonth/$TheDay/$TheYear</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedAttachments</font></td></tr>"; }
		if ($SortBy eq "Attachment1") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedAttachments</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedRecipients</font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\">$SavedReplyAdd</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedUsername<br></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$TheMonth/$TheDay/$TheYear</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><u>$SavedSubject</u></font></td></tr>"; }
	}
	$sth->finish; 
	$dbh->disconnect; 
	if ($count == 0) { print "<tr><td width=\"100%\" align=\"center\"><font class=\"sresultsred\">Sorry, no users match your search, criteria, <a href=\"#\" OnClick=\"Javascript:history.go(-1)\"><font class=\"sresultsred\">search again?</font></a></font></td></tr>"; }

## bottom INFO TABLE template
{
print <<EOF
                              		</table>
								</td></tr>
                              </table>
                            </td>
                          </tr>
                          <tr> 
                            <td colspan="2" height="15"><img src="images/spacer.gif" width="1" height="15"></td>
                          </tr>
                        </table>
          </td>
        </tr>
      </table>
EOF
}
	
## bottom HTML template
&bottom;
	
exit;
}

## Else If BROWSE data present scan it...
elsif ($FORM{'Browse'}) {

## top HTML template
&topper;

## top INFO TABLE template
{
print <<EOF
<br>
<table width="95%" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr>
    <td>
                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                          <tr> 
                            <td width="35%"><font class="stextbig"><b>Search Results</b></font></td>
                            <td align="right" width="65%"><font class="stext2"><b><font color="#FD0000">&nbsp;</font></b></font></td>
                          </tr>
                          <tr bgcolor="#333366"> 
                            <td colspan="2" height="1"><img src="images/spacer.gif" width="1" height="1"></td>
                          </tr>
                          <tr> 
                            <td colspan="2" height="10"><img src="images/spacer.gif" width="1" height="10"></td>
                          </tr>
                          <tr> 
                            <td colspan="2" height="75">
	<table width="85%" align="center" border="1" bgcolor="#FFFFFF" cellpadding="2" cellspacing="0">
	<tr><td width="100%" valign="middle">
	<font class="sresults1"><li>To view a message click on the '<b>Subject</b>' of choice</li><li>The red title represents the order in which the search results are currently displayed</li></font>
	</td></tr>
	</table>							
							</td>
                          </tr>
                          <tr> 
                            <td colspan="2" align="left" width="100%"> 

	<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
EOF
}

	## Crumble Form Input to DB Queries as necessary
	if ($FORM{'Browse'} eq "Username") { 
		$Sortee = "Username"; 
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" valign=\"top\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresultsred\"><b>Username</b><br></font></td><td valign=\"top\" align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Reply Email</b></font></td><td width=\"20%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Recipients</b></font></td><td width=\"20%\"valign=\"top\"  align=\"center\"><font class=\"sresults1\"><b>Subject</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Date</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>File(s)</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";	
	}
	if ($FORM{'Browse'} eq "ReplyAdd") { 
		$Sortee = "ReplyAdd";
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" valign=\"top\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresultsred\"><b>Reply Email</b><br></font></td><td valign=\"top\" align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Reply Email</b></font></td><td width=\"20%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Recipients</b></font></td><td width=\"20%\"valign=\"top\"  align=\"center\"><font class=\"sresults1\"><b>Subject</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Date</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>File(s)</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";		
	}
	if ($FORM{'Browse'} eq "Recipients") { 
		$Sortee = "Recipients"; 
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" valign=\"top\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresultsred\"><b>Recipient(s)</b><br></font></td><td valign=\"top\" align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Subject</b></font></td><td width=\"20%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Reply Email</b></font></td><td width=\"20%\"valign=\"top\"  align=\"center\"><font class=\"sresults1\"><b>Username</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Date</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>File(s)</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";		
	}
	if ($FORM{'Browse'} eq "Subject") { 
		$Sortee = "Subject"; 
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" valign=\"top\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresultsred\"><b>Subject</b><br></font></td><td valign=\"top\" align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Recipients</b></font></td><td width=\"20%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Reply Email</b></font></td><td width=\"20%\"valign=\"top\"  align=\"center\"><font class=\"sresults1\"><b>Username</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Date</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>File(s)</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";		
	}
	if ($FORM{'Browse'} eq "Attachments") { 
		$Sortee = "Attachment1"; 
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" valign=\"top\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresultsred\"><b>File(s)</b><br></font></td><td valign=\"top\" align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Recipients</b></font></td><td width=\"20%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Reply Email</b></font></td><td width=\"20%\"valign=\"top\"  align=\"center\"><font class=\"sresults1\"><b>Username</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Date</b></font></td><td width=\"10%\" valign=\"top\" align=\"center\"><font class=\"sresults1\"><b>Subject</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";	
	}
	my $SortBy = "$Sortee";
	my $ActionUser = "$Cookies{'Username'}";
	## Start DB connection
	use DBI; 
	use strict; 
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $count=0;
	my $queeery = "SELECT * FROM Messages ORDER BY $SortBy";
	my $sth = $dbh->prepare("$queeery");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$count++;
		my $SavedUsername = $row[1];
		my $SavedReplyAdd = $row[5];
		my $SavedRecipients = $row[6];
		my $SavedSubject = $row[7];
		my $SavedAttachments = "$row[9] &nbsp; $row[10] &nbsp; $row[11]";
		my $SavedAddedOn = $row[12];
		my $TheYear = substr($SavedAddedOn, 0, 2);
		my $TheMonth = substr($SavedAddedOn, 2, 2);
		my $TheDay = substr($SavedAddedOn, 4, 2);
		if ($SortBy eq "Username") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedUsername<br></font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\">$SavedReplyAdd</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedRecipients</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\"><u>$SavedSubject</u></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$TheMonth/$TheDay/$TheYear</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedAttachments</font></td></tr>"; }
		if ($SortBy eq "ReplyAdd") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\">$SavedReplyAdd</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedUsername<br></font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedRecipients</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\"><u>$SavedSubject</u></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$TheMonth/$TheDay/$TheYear</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedAttachments</font></td></tr>"; }
		if ($SortBy eq "Recipients") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedRecipients</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\"><u>$SavedSubject</u></font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\">$SavedReplyAdd</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedUsername<br></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$TheMonth/$TheDay/$TheYear</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedAttachments</font></td></tr>"; }
		if ($SortBy eq "Subject") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\"><u>$SavedSubject</u></font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedRecipients</font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\">$SavedReplyAdd</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedUsername<br></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$TheMonth/$TheDay/$TheYear</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedAttachments</font></td></tr>"; }
		if ($SortBy eq "Attachment1") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedAttachments</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedRecipients</font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\">$SavedReplyAdd</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedUsername<br></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$TheMonth/$TheDay/$TheYear</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><u>$SavedSubject</u></font></td></tr>"; }
	}
	$sth->finish; 
	$dbh->disconnect; 
	if ($count == 0) { print "<tr><td width=\"100%\" align=\"center\"><font class=\"sresultsred\">Sorry, no users match your search, criteria, <a href=\"#\" OnClick=\"Javascript:history.go(-1)\"><font class=\"sresultsred\">search again?</font></a></font></td></tr>"; }

## bottom INFO TABLE template
{
print <<EOF
                              		</table>
								</td></tr>
                              </table>
                            </td>
                          </tr>
                          <tr> 
                            <td colspan="2" height="15"><img src="images/spacer.gif" width="1" height="15"></td>
                          </tr>
                        </table>
          </td>
        </tr>
      </table>
EOF
}

## bottom HTML template
&bottom;

exit;
}

## Else If no data present drop default frameset...
elsif ($FORM{'enformthee'}) {

## top HTML template
&topper;

## bottom HTML template
&bottom;

exit;
}

## if no useful calls present frameset
else {

{
print <<EOF

<html>
<head>
<title>Coastline Micro, Inc. - Shark Tank Admin System - Message Depot</title>
</head>
<frameset rows="64,*" rows="*" border="0" framespacing="0"> 
<frame name="topOne" scrolling="NO" noresize src="topper.cgi" marginwidth="0" marginheight="0" frameborder="NO">
<frame name="botOne" src="$script?enformthee=1" frameborder="NO" marginheight="0" marginwidth="0" scrolling="AUTO">
</frameset>
<noframes><body bgcolor="#FFFFFF">
</body></noframes>
</html>

EOF
}
exit;
}

## top HTML template
sub topper { 

## get perl built dynamic DHTML menu js
$MenuConfig = `cat js/menu_config.js`;
$MenuConstructor = `cat js/menu_constructor.js`;
$MenuConfig = "<script langauage=\"Javascript\">\n$MenuConfig\n</script>";
$MenuConstructor = "<script langauage=\"Javascript\">\n$MenuConstructor\n</script>";

$topper = `cat top_vmessages.nsf`; 
$legal = `cat legal.nsf`;
$topper =~ s/%%LEGAL%%/$legal/g;
$topper =~ s/%%MENUCONFIG%%/$MenuConfig/g;
$topper =~ s/%%MENUCONSTRUCTOR%%/$MenuConstructor/g;
print $topper;

}
## bottom HTML template
sub bottom { $bottom = `cat bottom.nsf`; print $bottom; }