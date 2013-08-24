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
if (($Cookies{'UserType'} eq "CMManage") || ($Cookies{'UserType'} eq "CMAdmin") || ($Cookies{'UserType'} eq "CMSales") || ($Cookies{'UserType'} eq "CMUser")) { $nextone = "1"; }
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
                            <td colspan="2" height="115">
	<table width="85%" align="center" border="1" bgcolor="#FFFFFF" cellpadding="10" cellspacing="0">
	<tr><td width="100%" valign="middle">
	<font class="sresults1"><li>To update, change or view a user's full account profile click on the '<b>Username</b>' of the person you would like to delete, or you can use the icons.</li><li>To add a new user to the system use the '<b>Add New</b>' button</li><li>The red title represents the order in which the search results are currently displayed</li><li>To Delete a user's account profile click the 'Delete' icon located on the row of the person you want to delete.</li>
	</font>
	<br><br>

	<table width="300" align="center" border="0" cellpadding="5" cellspacing="0" bgcolor="F2F2F7">
	<tr>
	<td width="100%" align="center" colspan="2"><font class="sresults1"><b>Icon Legend</b></font></td>
	</tr>
	<tr>
	<td width="50%" align="center"><nobr><img src="images/icon_change_on.gif" border="0"><font class="sresults1"><br>Change/Update Profile</font></nobr></td>
	<td width="50%" align="center"><nobr><img src="images/icon_delete_on.gif" border="0"><font class="sresults1"><br>Delete Profile</font></nobr></td>
	</tr>
	</table>
	
	</td></tr>
	</table>							
<br>
							</td>
                          </tr>
                          <tr> 
                            <td colspan="2" align="left" width="100%"> 

	<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
EOF
}

	## Crumble Form Input to DB Queries as necessary
	if ($FORM{'SearchType'} eq "Username") { 
		$Formee = "$FORM{'SearchTerms'}"; 
		$Sortee = "Username";
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" align=\"center\"><font class=\"sresultsred\"><b>Username</b><br></font></td><td align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>First Name</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>Last Name</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>Email</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Access</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Action</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	if ($FORM{'SearchType'} eq "FirstName") { 
		$Formee = "$FORM{'SearchTerms'}"; 
		$Sortee = "FirstName";
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" align=\"center\"><font class=\"sresultsred\"><b>First Name</b><br></font></td><td align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Username</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>Last Name</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>Email</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Access</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Action</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	if ($FORM{'SearchType'} eq "LastName") { 
		$Formee = "$FORM{'SearchTerms'}"; 
		$Sortee = "LastName";
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" align=\"center\"><font class=\"sresultsred\"><b>Last Name</b><br></font></td><td align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Email</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>First Name</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>Username</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Access</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Action</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	if ($FORM{'SearchType'} eq "Email") { 
		$Formee = "$FORM{'SearchTerms'}"; 
		$Sortee = "Email";
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" align=\"center\"><font class=\"sresultsred\"><b>Email</b><br></font></td><td align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Last Name</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>First Name</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>Username</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Access</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Action</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	my $SortBy = "$Sortee";
	my $FormInput = "$Formee";
	my $ActionUser = "$Cookies{'Username'}";
	## Start DB connection
	use DBI; 
	use strict; 
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $count=0;
	my $queeery = "SELECT * FROM Users WHERE $SortBy LIKE '%$FormInput%' ORDER BY $SortBy";
	my $sth = $dbh->prepare("$queeery");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$count++;
		my $SavedUsername = $row[3];
		my $SavedEmail = $row[5];
		my $SavedFirstName = $row[6];
		my $SavedLastName = $row[7];
		my $SavedPhone = $row[9];
		my $SavedPhone = $row[9];
		my $SavedUserAccess = $row[11];
		## re-format data
		my $AreaCode = substr($SavedPhone, 0, 3);
		my $PhoneNum3 = substr($SavedPhone, 3, 3);
		my $PhoneNum4 = substr($SavedPhone, 6, 4);
		if ($SortBy eq "Username") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><a href=\"https://www.coastlinemicro.com/admin/change_user.cgi?Username=$SavedUsername&LastName=$SavedLastName\" class=\"sresults1\">$SavedUsername</a></font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\">$SavedFirstName</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedLastName</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\"><a href=\"messenger.cgi?EmailAddy=$SavedEmail&FirstName=$SavedFirstName\" class=\"sresults1\">$SavedEmail</a></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedUserAccess</font></td><td width=\"10%\" align=\"center\"><a href=\"https://www.coastlinemicro.com/admin/change_user.cgi?Username=$SavedUsername&LastName=$SavedLastName\"><img src=\"images/icon_change_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'change','on');\" onMouseOut=\"javascript:iconOff(this,'change','off');\"></a>&nbsp;&nbsp;<a href=\"#\" onClick=\"javascript:deleteThis('$SavedUsername','$SavedLastName');\"><img src=\"images/icon_delete_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'delete','on');\" onMouseOut=\"javascript:iconOff(this,'delete','off');\"></a></td></tr>"; }
		if ($SortBy eq "FirstName") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\">$SavedFirstName</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><a href=\"https://www.coastlinemicro.com/admin/change_user.cgi?Username=$SavedUsername&LastName=$SavedLastName\" class=\"sresults1\">$SavedUsername</a></font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedLastName</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\"><a href=\"messenger.cgi?EmailAddy=$SavedEmail&FirstName=$SavedFirstName\" class=\"sresults1\">$SavedEmail</a></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedUserAccess</font></td><td width=\"10%\" align=\"center\"><a href=\"https://www.coastlinemicro.com/admin/change_user.cgi?Username=$SavedUsername&LastName=$SavedLastName\"><img src=\"images/icon_change_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'change','on');\" onMouseOut=\"javascript:iconOff(this,'change','off');\"></a>&nbsp;&nbsp;<a href=\"#\" onClick=\"javascript:deleteThis('$SavedUsername','$SavedLastName');\"><img src=\"images/icon_delete_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'delete','on');\" onMouseOut=\"javascript:iconOff(this,'delete','off');\"></a></td></tr>"; }
		if ($SortBy eq "LastName") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedLastName</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\"><a href=\"messenger.cgi?EmailAddy=$SavedEmail&FirstName=$SavedFirstName\" class=\"sresults1\">$SavedEmail</a></font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\">$SavedFirstName</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><a href=\"https://www.coastlinemicro.com/admin/change_user.cgi?Username=$SavedUsername&LastName=$SavedLastName\" class=\"sresults1\">$SavedUsername</a></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedUserAccess</font></td><td width=\"10%\" align=\"center\"><a href=\"https://www.coastlinemicro.com/admin/change_user.cgi?Username=$SavedUsername&LastName=$SavedLastName\"><img src=\"images/icon_change_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'change','on');\" onMouseOut=\"javascript:iconOff(this,'change','off');\"></a>&nbsp;&nbsp;<a href=\"#\" onClick=\"javascript:deleteThis('$SavedUsername','$SavedLastName');\"><img src=\"images/icon_delete_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'delete','on');\" onMouseOut=\"javascript:iconOff(this,'delete','off');\"></a></td></tr>"; }
		if ($SortBy eq "Email") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\"><a href=\"messenger.cgi?EmailAddy=$SavedEmail&FirstName=$SavedFirstName\" class=\"sresults1\">$SavedEmail</a></font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedLastName</font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\">$SavedFirstName</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><a href=\"https://www.coastlinemicro.com/admin/change_user.cgi?Username=$SavedUsername&LastName=$SavedLastName\" class=\"sresults1\">$SavedUsername</a></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedUserAccess</font></td><td width=\"10%\" align=\"center\"><a href=\"https://www.coastlinemicro.com/admin/change_user.cgi?Username=$SavedUsername&LastName=$SavedLastName\"><img src=\"images/icon_change_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'change','on');\" onMouseOut=\"javascript:iconOff(this,'change','off');\"></a>&nbsp;&nbsp;<a href=\"#\" onClick=\"javascript:deleteThis('$SavedUsername','$SavedLastName');\"><img src=\"images/icon_delete_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'delete','on');\" onMouseOut=\"javascript:iconOff(this,'delete','off');\"></a></td></tr>"; }
	}
	$sth->finish; 
	$dbh->disconnect; 
	if ($count == 0) { print "<tr><td width=\"100%\" align=\"center\"><font class=\"sresultsred\">Sorry, no users match your search criteria, <a href=\"#\" OnClick=\"Javascript:history.go(-1)\"><font class=\"sresultsred\">search again?</font></a></font></td></tr>"; }

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

## If BROWSE data present scan it...
if ($FORM{'Browse'}) { 

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
                            <td colspan="2" height="115">
	<table width="85%" align="center" border="1" bgcolor="#FFFFFF" cellpadding="10" cellspacing="0">
	<tr><td width="100%" valign="middle">
	<font class="sresults1"><li>To update, change or view a user's full account profile click on the '<b>Username</b>' of the person you would like to delete, or you can use the icons.</li><li>To add a new user to the system use the '<b>Add New</b>' button</li><li>The red title represents the order in which the search results are currently displayed</li><li>To Delete a user's account profile click the 'Delete' icon located on the row of the person you want to delete.</li>
	</font>
	<br><br>

	<table width="300" align="center" border="0" cellpadding="5" cellspacing="0" bgcolor="F2F2F7">
	<tr>
	<td width="100%" align="center" colspan="2"><font class="sresults1"><b>Icon Legend</b></font></td>
	</tr>
	<tr>
	<td width="50%" align="center"><nobr><img src="images/icon_change_on.gif" border="0"><font class="sresults1"><br>Change/Update Profile</font></nobr></td>
	<td width="50%" align="center"><nobr><img src="images/icon_delete_on.gif" border="0"><font class="sresults1"><br>Delete Profile</font></nobr></td>
	</tr>
	</table>
	
	</td></tr>
	</table>							
<br>
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
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" align=\"center\"><font class=\"sresultsred\"><b>Username</b><br></font></td><td align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>First Name</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>Last Name</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>Email</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Access</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Action</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	if ($FORM{'Browse'} eq "FirstName") { 
		$Sortee = "FirstName";
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" align=\"center\"><font class=\"sresultsred\"><b>First Name</b><br></font></td><td align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Username</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>Last Name</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>Email</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Access</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Action</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	if ($FORM{'Browse'} eq "LastName") { 
		$Sortee = "LastName";
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" align=\"center\"><font class=\"sresultsred\"><b>Last Name</b><br></font></td><td align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Email</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>First Name</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>Username</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Access</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Action</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	if ($FORM{'Browse'} eq "Email") { 
		$Sortee = "Email";
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" align=\"center\"><font class=\"sresultsred\"><b>Email</b><br></font></td><td align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Last Name</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>First Name</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>Username</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Access</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Action</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	my $SortBy = "$Sortee";
	my $ActionUser = "$Cookies{'Username'}";
	## Start DB connection
	use DBI; 
	use strict; 
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $count=0;
	my $queeery = "SELECT * FROM Users ORDER BY $SortBy";
	my $sth = $dbh->prepare("$queeery");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$count++;
		my $SavedUsername = $row[3];
		my $SavedEmail = $row[5];
		my $SavedFirstName = $row[6];
		my $SavedLastName = $row[7];
		my $SavedPhone = $row[9];
		my $SavedPhone = $row[9];
		my $SavedUserAccess = $row[11];
		## re-format data
		my $AreaCode = substr($SavedPhone, 0, 3);
		my $PhoneNum3 = substr($SavedPhone, 3, 3);
		my $PhoneNum4 = substr($SavedPhone, 6, 4);
		if ($SortBy eq "Username") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><a href=\"https://www.coastlinemicro.com/admin/change_user.cgi?Username=$SavedUsername&LastName=$SavedLastName\" class=\"sresults1\">$SavedUsername</a></font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\">$SavedFirstName</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedLastName</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\"><a href=\"messenger.cgi?EmailAddy=$SavedEmail&FirstName=$SavedFirstName\" class=\"sresults1\">$SavedEmail</a></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedUserAccess</font></td><td width=\"10%\" align=\"center\"><a href=\"https://www.coastlinemicro.com/admin/change_user.cgi?Username=$SavedUsername&LastName=$SavedLastName\"><img src=\"images/icon_change_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'change','on');\" onMouseOut=\"javascript:iconOff(this,'change','off');\"></a>&nbsp;&nbsp;<a href=\"#\" onClick=\"javascript:deleteThis('$SavedUsername','$SavedLastName');\"><img src=\"images/icon_delete_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'delete','on');\" onMouseOut=\"javascript:iconOff(this,'delete','off');\"></a></td></tr>"; }
		if ($SortBy eq "FirstName") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\">$SavedFirstName</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><a href=\"https://www.coastlinemicro.com/admin/change_user.cgi?Username=$SavedUsername&LastName=$SavedLastName\" class=\"sresults1\">$SavedUsername</a></font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedLastName</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\"><a href=\"messenger.cgi?EmailAddy=$SavedEmail&FirstName=$SavedFirstName\" class=\"sresults1\">$SavedEmail</a></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedUserAccess</font></td><td width=\"10%\" align=\"center\"><a href=\"https://www.coastlinemicro.com/admin/change_user.cgi?Username=$SavedUsername&LastName=$SavedLastName\"><img src=\"images/icon_change_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'change','on');\" onMouseOut=\"javascript:iconOff(this,'change','off');\"></a>&nbsp;&nbsp;<a href=\"#\" onClick=\"javascript:deleteThis('$SavedUsername','$SavedLastName');\"><img src=\"images/icon_delete_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'delete','on');\" onMouseOut=\"javascript:iconOff(this,'delete','off');\"></a></td></tr>"; }
		if ($SortBy eq "LastName") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedLastName</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\"><a href=\"messenger.cgi?EmailAddy=$SavedEmail&FirstName=$SavedFirstName\" class=\"sresults1\">$SavedEmail</a></font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\">$SavedFirstName</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><a href=\"https://www.coastlinemicro.com/admin/change_user.cgi?Username=$SavedUsername&LastName=$SavedLastName\" class=\"sresults1\">$SavedUsername</a></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedUserAccess</font></td><td width=\"10%\" align=\"center\"><a href=\"https://www.coastlinemicro.com/admin/change_user.cgi?Username=$SavedUsername&LastName=$SavedLastName\"><img src=\"images/icon_change_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'change','on');\" onMouseOut=\"javascript:iconOff(this,'change','off');\"></a>&nbsp;&nbsp;<a href=\"#\" onClick=\"javascript:deleteThis('$SavedUsername','$SavedLastName');\"><img src=\"images/icon_delete_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'delete','on');\" onMouseOut=\"javascript:iconOff(this,'delete','off');\"></a></td></tr>"; }
		if ($SortBy eq "Email") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\"><a href=\"messenger.cgi?EmailAddy=$SavedEmail&FirstName=$SavedFirstName\" class=\"sresults1\">$SavedEmail</a></font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedLastName</font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\">$SavedFirstName</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><a href=\"https://www.coastlinemicro.com/admin/change_user.cgi?Username=$SavedUsername&LastName=$SavedLastName\" class=\"sresults1\">$SavedUsername</a></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedUserAccess</font></td><td width=\"10%\" align=\"center\"><a href=\"https://www.coastlinemicro.com/admin/change_user.cgi?Username=$SavedUsername&LastName=$SavedLastName\"><img src=\"images/icon_change_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'change','on');\" onMouseOut=\"javascript:iconOff(this,'change','off');\"></a>&nbsp;&nbsp;<a href=\"#\" onClick=\"javascript:deleteThis('$SavedUsername','$SavedLastName');\"><img src=\"images/icon_delete_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'delete','on');\" onMouseOut=\"javascript:iconOff(this,'delete','off');\"></a></td></tr>"; }
	}
	$sth->finish; 
	$dbh->disconnect; 
	if ($count == 0) { print "<tr><td width=\"100%\" align=\"center\"><font class=\"sresultsred\">Sorry, no users match your search criteria, <a href=\"#\" OnClick=\"Javascript:history.go(-1)\"><font class=\"sresultsred\">search again?</font></a></font></td></tr>"; }

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

## if no useful calls present frameset
else {
$sorry = `cat sorry_nospec.nsf`;

{
print <<EOF

$sorry

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

$topper = `cat top_vusers.nsf`; 
$legal = `cat legal.nsf`;
$topper =~ s/%%LEGAL%%/$legal/g;
$topper =~ s/%%MENUCONFIG%%/$MenuConfig/g;
$topper =~ s/%%MENUCONSTRUCTOR%%/$MenuConstructor/g;
print $topper;

}
## bottom HTML template
sub bottom { $bottom = `cat bottom.nsf`; print $bottom; }