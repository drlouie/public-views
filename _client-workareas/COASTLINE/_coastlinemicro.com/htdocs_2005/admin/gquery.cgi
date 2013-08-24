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
if (($Cookies{'UserType'} eq "COManage") || ($Cookies{'UserType'} eq "WEBAdmin")) { $nextone = "1"; }
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

	use DBI;
	##----------->>> Grab DIST Account Information
	my $dbh = DBI->connect("DBI:mysql:NMS-SysConfigurator","root","62Ak.fi1HdBxI") or die "Unable to connect to database: <b>NMS-SysConfigurator</b>\n"; 
	$dbh->{RaiseError} = 1; 

print "MfgCode READOUT: This Manufacturer Code readout will allow you to give each product you plan to ADD or UPDATE a specific Manufacturer Code as saved in the system. Doing so will tie your products into the system's Manufacter profile, which will display Links, Logos and other manufacturer specific information.<br><br>";
print "MFG Name - MFGCode<br>";
	my $sth = $dbh->prepare("SELECT * FROM MFGs");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$MFGID = $row[0];
		$MFGName = $row[1];
		print "$MFGName - $MFGID<br>";
	}
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;

print "<br><hr width=\"85%\" align=\"center\"><br><br>";
	
print "PRODUCT READOUT: Copy all the ROWS/LINES of data starting from the ruler below this text message. Once you copy, or before, create a new Text (.txt) document on your desktop and open it. Paste the copied data to this new document, making sure you do not have any WHITESPACE OR TABS after the last product in the list ie: THE LAST CHARACTER YOU SELECT SHOULD BE THE Double-Quote (\") surrounding the last product's last data field . Save this file and close it. Now, rename your file from the text (.txt) extension to Comma Delimited Text (.csv). Once you have done this you will notice the icon appears as an Excel document. Open the document by double-clicking it and you will have formatted data that is easy to work with when updating, adding and deleting products from the site via the admin import tool, quickly and efficiently. 
<br><br>Once you are done with your changes, you can save the file AS a Text (Tab Delimited) (*.txt) file directly from Excel. When you open this NEW text file you will have data that is ready to be imported to the site using the import tool. Keep in mind that all you will need to import back into the system are the product listings and not the first line that specifies the data's structure. If you don't know what the import tool is, you really shouldn't be using this one...<br><br><hr width=\"85%\" align=\"center\"><br>";
print "\"CmPartNum\",\"MfgPartNum\",\"MfgCode\",\"PricingClass\",\"ItemName\",\"Weight\",\"Cost\",\"IngramNum\",\"Action\",\"ProductType\",\"Searchable\"<br>";

	$count=0;
	my $sth = $dbh->prepare("SELECT * FROM Products ORDER BY CMPartNum ASC");
	$sth->execute or die "Unable to execute query\n"; 
	my @row;
	while(@row = $sth->fetchrow_array) { 
		$SavedCMPartNum = $row[1];
		$SavedSYSCode = $row[2];
		$SavedMFGCode = $row[6];
		$SavedMFGNum = $row[7];
		$SavedPricingClass = $row[10];
		$SavedItemName = $row[11];
		$SavedWeight = $row[20];
		$SavedCost = $row[21];
		$SavedIngramPartNum = $row[29];
		$SavedProductType = $row[32];
		$SavedSearchable = $row[33];
		$count++;
		if ($SavedPricingClass ne "Desktop" && $SavedPricingClass ne "Server" && $SavedPricingClass ne "Notebook") { print "\"$SavedCMPartNum\",\"$SavedMFGNum\",\"$SavedMFGCode\",\"$SavedPricingClass\",\"$SavedItemName\",\"$SavedWeight\",\"$SavedCost\",\"$SavedIngramPartNum\",\"Update\",\"$SavedProductType\",\"$SavedSearchable\"<br>"; }
	}
	$sth->execute or die "Unable to execute query\n"; 
	$sth->finish;
	$dbh->disconnect;
	
exit;