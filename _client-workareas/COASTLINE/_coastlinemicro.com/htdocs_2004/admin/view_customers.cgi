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
                            <td colspan="2" height="115">
	<table width="85%" align="center" border="1" bgcolor="#FFFFFF" cellpadding="10" cellspacing="0">
	<tr><td width="100%" valign="middle">
	<font class="sresults1"><li>To update, change or view a customer's full account profile click on the '<b>Company name</b>' of the account you would like to delete, or you can use the icons.</li><li>To add a new customer account to the system use the '<b>Add New</b>' button</li><li>The red title represents the order in which the search results are currently displayed</li><li>To Delete a customer's account click the 'Delete' icon located on the row of the company you want to delete.</li>
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
	if ($FORM{'SearchType'} eq "CMCustNum") { 
		$Formee = "$FORM{'SearchTerms'}"; 
		$Sortee = "CMCustNum"; 
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" align=\"center\"><font class=\"sresultsred\"><b>CM #</b><br></font></td><td align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Company Name</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>City</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>State</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Phone</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Action</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	if ($FORM{'SearchType'} eq "CompanyName") { 
		$Formee = "$FORM{'SearchTerms'}"; 
		$Sortee = "CompanyName"; 
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td align=\"center\" width=\"25%\"><font class=\"sresultsred\"><b>Company Name</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>CM #</b><br></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>City</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>State</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Phone</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Action</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	if ($FORM{'SearchType'} eq "MailCity") { 
		$Formee = "$FORM{'SearchTerms'}"; 
		$Sortee = "MailCity"; 
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"20%\" align=\"center\"><font class=\"sresultsred\"><b>City</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>State</b></font></td><td align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Company Name</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>CM #</b><br></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Phone</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Action</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	if ($FORM{'SearchType'} eq "MailState") { 
		$Formee = "$FORM{'SearchTerms'}"; 
		$Sortee = "MailState"; 
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"20%\" align=\"center\"><font class=\"sresultsred\"><b>State</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>City</b></font></td><td align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Company Name</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>CM #</b><br></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Phone</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Action</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
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
	my $queeery = "SELECT * FROM Customers WHERE $SortBy LIKE '%$FormInput%' ORDER BY $SortBy";
	my $sth = $dbh->prepare("$queeery");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$count++;
		my $SavedCMCustNum = $row[1];
		my $SavedCompanyName = $row[6];
		my $SavedPhone = $row[8];
		my $SavedFax = $row[9];
		my $SavedMailCity = $row[12];
		my $SavedMailState = $row[13];
		## re-format data
		my $AreaCode = substr($SavedPhone, 0, 3);
		my $PhoneNum3 = substr($SavedPhone, 3, 3);
		my $PhoneNum4 = substr($SavedPhone, 6, 4);
		my $FaxNum3 = substr($SavedFax, 3, 3);
		my $FaxNum4 = substr($SavedFax, 6, 4);
		
		if ($SortBy eq "CMCustNum") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedCMCustNum<br></font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\"><a href=\"change_customer.cgi?CMCustNum=$SavedCMCustNum&CompanyName=$SavedCompanyName\" class=\"sresults1\">$SavedCompanyName</a></font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedMailCity</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedMailState</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">($AreaCode)<br>$PhoneNum3-$PhoneNum4</font></td><td width=\"10%\" align=\"center\"><a href=\"change_customer.cgi?CMCustNum=$SavedCMCustNum&CompanyName=$SavedCompanyName\"><img src=\"images/icon_change_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'change','on');\" onMouseOut=\"javascript:iconOff(this,'change','off');\"></a>&nbsp;&nbsp;<a href=\"#\" onClick=\"javascript:deleteThis('$SavedCMCustNum','$SavedCompanyName');\"><img src=\"images/icon_delete_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'delete','on');\" onMouseOut=\"javascript:iconOff(this,'delete','off');\"></a></td></tr>"; }
		if ($SortBy eq "CompanyName") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\"><a href=\"change_customer.cgi?CMCustNum=$SavedCMCustNum&CompanyName=$SavedCompanyName\" class=\"sresults1\">$SavedCompanyName</a></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedCMCustNum<br></font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedMailCity</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedMailState</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">($AreaCode)<br>$PhoneNum3-$PhoneNum4</font></td><td width=\"10%\" valign=\"middle\" align=\"center\"><a href=\"change_customer.cgi?CMCustNum=$SavedCMCustNum&CompanyName=$SavedCompanyName\"><img src=\"images/icon_change_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'change','on');\" onMouseOut=\"javascript:iconOff(this,'change','off');\"></a>&nbsp;&nbsp;<a href=\"#\" onClick=\"javascript:deleteThis('$SavedCMCustNum','$SavedCompanyName');\"><img src=\"images/icon_delete_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'delete','on');\" onMouseOut=\"javascript:iconOff(this,'delete','off');\"></a></td></tr>"; }
		if ($SortBy eq "MailCity") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedMailCity</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedMailState</font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\"><a href=\"change_customer.cgi?CMCustNum=$SavedCMCustNum&CompanyName=$SavedCompanyName\" class=\"sresults1\">$SavedCompanyName</a></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedCMCustNum<br></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">($AreaCode)<br>$PhoneNum3-$PhoneNum4</font></td><td width=\"10%\" valign=\"middle\" align=\"center\"><a href=\"change_customer.cgi?CMCustNum=$SavedCMCustNum&CompanyName=$SavedCompanyName\"><img src=\"images/icon_change_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'change','on');\" onMouseOut=\"javascript:iconOff(this,'change','off');\"></a>&nbsp;&nbsp;<a href=\"#\" onClick=\"javascript:deleteThis('$SavedCMCustNum','$SavedCompanyName');\"><img src=\"images/icon_delete_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'delete','on');\" onMouseOut=\"javascript:iconOff(this,'delete','off');\"></a></td></tr>"; }
		if ($SortBy eq "MailState") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedMailState</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedMailCity</font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\"><a href=\"change_customer.cgi?CMCustNum=$SavedCMCustNum&CompanyName=$SavedCompanyName\" class=\"sresults1\">$SavedCompanyName</a></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedCMCustNum<br></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">($AreaCode)<br>$PhoneNum3-$PhoneNum4</font></td><td width=\"10%\" valign=\"middle\" align=\"center\"><a href=\"change_customer.cgi?CMCustNum=$SavedCMCustNum&CompanyName=$SavedCompanyName\"><img src=\"images/icon_change_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'change','on');\" onMouseOut=\"javascript:iconOff(this,'change','off');\"></a>&nbsp;&nbsp;<a href=\"#\" onClick=\"javascript:deleteThis('$SavedCMCustNum','$SavedCompanyName');\"><img src=\"images/icon_delete_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'delete','on');\" onMouseOut=\"javascript:iconOff(this,'delete','off');\"></a></td></tr>"; }
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
                            <td width="35%"><font class="stextbig"><b>Browse Results</b></font></td>
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
	<font class="sresults1"><li>To update, change or view a customer's full account profile click on the '<b>Company name</b>' of the account you would like to delete, or you can use the icons.</li><li>To add a new customer account to the system use the '<b>Add New</b>' button</li><li>The red title represents the order in which the search results are currently displayed</li><li>To Delete a customer's account click the 'Delete' icon located on the row of the company you want to delete.</li>
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
	if ($FORM{'Browse'} eq "CMCustNum") { 
		$Sortee = "CMCustNum"; 
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"10%\" align=\"center\"><font class=\"sresultsred\"><b>CM #</b><br></font></td><td align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Company Name</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>City</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>State</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Phone</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Action</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	if ($FORM{'Browse'} eq "CompanyName") { 
		$Sortee = "CompanyName"; 
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td align=\"center\" width=\"25%\"><font class=\"sresultsred\"><b>Company Name</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>CM #</b><br></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>City</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>State</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Phone</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Action</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	if ($FORM{'Browse'} eq "MailCity") { 
		$Sortee = "MailCity"; 
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"20%\" align=\"center\"><font class=\"sresultsred\"><b>City</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>State</b></font></td><td align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Company Name</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>CM #</b><br></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Phone</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Action</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}
	if ($FORM{'Browse'} eq "MailState") { 
		$Sortee = "MailState"; 
		print "<tr height=\"20\" width=\"100%\"><td height=\"20\" width=\"5%\" align=\"center\"><font class=\"sresults1\">&nbsp;</font></td><td width=\"20%\" align=\"center\"><font class=\"sresultsred\"><b>State</b></font></td><td width=\"20%\" align=\"center\"><font class=\"sresults1\"><b>City</b></font></td><td align=\"center\" width=\"25%\"><font class=\"sresults1\"><b>Company Name</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>CM #</b><br></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Phone</b></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\"><b>Action</b></font></td></tr><tr width=\"100%\"><td colspan=\"7\"><table width=\"100%\" height=\"35\" border=\"1\" bordercolor=\"#333366\" cellspacing=\"1\" cellpadding=\"3\" align=\"center\" bgcolor=\"#ffffff\">";
	}	
	## Crumble Form Input to DB Queries as necessary
	my $SortBy = "$Sortee";
	my $ActionUser = "$Cookies{'Username'}";
	## Start DB connection
	use DBI; 
	use strict; 
	my $dbh = DBI->connect("DBI:mysql:coastline","drlouie","chinga2") or die "Unable to connect to database: <b>coastline</b>\n"; 
	$dbh->{RaiseError} = 1; 
	my $queeery = "SELECT * FROM Customers ORDER BY $SortBy";
	my $sth = $dbh->prepare("$queeery");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	my $count=0;
	while(@row = $sth->fetchrow_array) { 
		$count++;
		my $SavedCMCustNum = $row[1];
		my $SavedCompanyName = $row[6];
		my $SavedPhone = $row[8];
		my $SavedFax = $row[9];
		my $SavedMailCity = $row[12];
		my $SavedMailState = $row[13];
		## re-format data
		my $AreaCode = substr($SavedPhone, 0, 3);
		my $PhoneNum3 = substr($SavedPhone, 3, 3);
		my $PhoneNum4 = substr($SavedPhone, 6, 4);
		my $FaxNum3 = substr($SavedFax, 3, 3);
		my $FaxNum4 = substr($SavedFax, 6, 4);
		
		if ($SortBy eq "CMCustNum") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedCMCustNum<br></font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\"><a href=\"change_customer.cgi?CMCustNum=$SavedCMCustNum&CompanyName=$SavedCompanyName\" class=\"sresults1\">$SavedCompanyName</a></font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedMailCity</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedMailState</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">($AreaCode)<br>$PhoneNum3-$PhoneNum4</font></td><td width=\"10%\" valign=\"middle\" align=\"center\"><a href=\"change_customer.cgi?CMCustNum=$SavedCMCustNum&CompanyName=$SavedCompanyName\"><img src=\"images/icon_change_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'change','on');\" onMouseOut=\"javascript:iconOff(this,'change','off');\"></a>&nbsp;&nbsp;<a href=\"#\" onClick=\"javascript:deleteThis('$SavedCMCustNum','$SavedCompanyName');\"><img src=\"images/icon_delete_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'delete','on');\" onMouseOut=\"javascript:iconOff(this,'delete','off');\"></a></td></tr>"; }
		if ($SortBy eq "CompanyName") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\"><a href=\"change_customer.cgi?CMCustNum=$SavedCMCustNum&CompanyName=$SavedCompanyName\" class=\"sresults1\">$SavedCompanyName</a></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedCMCustNum<br></font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedMailCity</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedMailState</font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">($AreaCode)<br>$PhoneNum3-$PhoneNum4</font></td><td width=\"10%\" valign=\"middle\" align=\"center\"><a href=\"change_customer.cgi?CMCustNum=$SavedCMCustNum&CompanyName=$SavedCompanyName\"><img src=\"images/icon_change_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'change','on');\" onMouseOut=\"javascript:iconOff(this,'change','off');\"></a>&nbsp;&nbsp;<a href=\"#\" onClick=\"javascript:deleteThis('$SavedCMCustNum','$SavedCompanyName');\"><img src=\"images/icon_delete_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'delete','on');\" onMouseOut=\"javascript:iconOff(this,'delete','off');\"></a></td></tr>"; }
		if ($SortBy eq "MailCity") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedMailCity</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedMailState</font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\"><a href=\"change_customer.cgi?CMCustNum=$SavedCMCustNum&CompanyName=$SavedCompanyName\" class=\"sresults1\">$SavedCompanyName</a></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedCMCustNum<br></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">($AreaCode)<br>$PhoneNum3-$PhoneNum4</font></td><td width=\"10%\" valign=\"middle\" align=\"center\"><a href=\"change_customer.cgi?CMCustNum=$SavedCMCustNum&CompanyName=$SavedCompanyName\"><img src=\"images/icon_change_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'change','on');\" onMouseOut=\"javascript:iconOff(this,'change','off');\"></a>&nbsp;&nbsp;<a href=\"#\" onClick=\"javascript:deleteThis('$SavedCMCustNum','$SavedCompanyName');\"><img src=\"images/icon_delete_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'delete','on');\" onMouseOut=\"javascript:iconOff(this,'delete','off');\"></a></td></tr>"; }
		if ($SortBy eq "MailState") { print "<tr><td width=\"5%\" align=\"center\"><font class=\"sresults1\">$count</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedMailState</font></td><td width=\"20%\" align=\"left\"><font class=\"sresults1\">$SavedMailCity</font></td><td align=\"left\" width=\"25%\"><font class=\"sresults1\"><a href=\"change_customer.cgi?CMCustNum=$SavedCMCustNum&CompanyName=$SavedCompanyName\" class=\"sresults1\">$SavedCompanyName</a></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">$SavedCMCustNum<br></font></td><td width=\"10%\" align=\"center\"><font class=\"sresults1\">($AreaCode)<br>$PhoneNum3-$PhoneNum4</font></td><td width=\"10%\" valign=\"middle\" align=\"center\"><a href=\"change_customer.cgi?CMCustNum=$SavedCMCustNum&CompanyName=$SavedCompanyName\"><img src=\"images/icon_change_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'change','on');\" onMouseOut=\"javascript:iconOff(this,'change','off');\"></a>&nbsp;&nbsp;<a href=\"#\" onClick=\"javascript:deleteThis('$SavedCMCustNum','$SavedCompanyName');\"><img src=\"images/icon_delete_off.gif\" border=\"0\" onMouseOver=\"javascript:iconOn(this,'delete','on');\" onMouseOut=\"javascript:iconOff(this,'delete','off');\"></a></td></tr>"; }
	}
	$sth->finish; 
	$dbh->disconnect; 
	if ($count == 0) { print "<tr><td width=\"100%\" align=\"center\"><font class=\"sresultsred\">Sorry, no users match your browsing criteria, <a href=\"#\" OnClick=\"Javascript:history.go(-1)\"><font class=\"sresultsred\">search again?</font></a></font></td></tr>"; }

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

	## bot HTML template
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

$topper = `cat top_vcustomers.nsf`; 
$legal = `cat legal.nsf`;
$topper =~ s/%%LEGAL%%/$legal/g;
$topper =~ s/%%MENUCONFIG%%/$MenuConfig/g;
$topper =~ s/%%MENUCONSTRUCTOR%%/$MenuConstructor/g;
print $topper;

}
## bottom HTML template
sub bottom { $bottom = `cat bottom.nsf`; print $bottom;}